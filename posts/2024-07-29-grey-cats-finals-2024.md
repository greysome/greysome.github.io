# Grey Cat The Flags 2024 Finals, Crypto writeups

1. [BabyRSA](#babyrsa)
2. [HMAC-CRC](#hmac-crc)
3. [Learning With Mistakes](#learning-with-mistakes)
4. [RC4 Signing Scheme](#rc4-signing-scheme-upsolve)

### BabyRSA

*lol* [(code)](/resource/babyrsa.py)

The code generates primes $$p,q,r,\ 2p+1,\ 2q+1,\ 2r+1$$ and then uses the public moduli $$N_1=p(2q+1),\;N_2=q(2r+1),\;N_3=r(2p+1)$$ to RSA encrypt the three parts of the flag. We know the values of $N_1,N_2,N_3$, so the problem is to solve for $p,q,r$ and then decrypting would be a piece of cake. The easiest method is to plug the equations into a Gr&ouml;bner basis algorithm, but unfortunately I haven't learnt about them yet. So I resorted to a more elementary solution as follows.

Expanding out, we get

$$(2p+1)(2q+1)(2r+1) = 8pqr+4pq+4pr+4qr+2p+2q+2r+1 = 8pqr+2(N_1+N_2+N_3)+1,$$

thus

$$N_1N_2N_3 = pqr(2p+1)(2q+1)(2r+1) = pqr\bigl(8pqr + 2(N_1+N_2+N_3) + 1\bigr).$$

We know the values of $N_1N_2N_3$ and $2(N_1+N_2+N_3)+1$, so we can actually solve for $pqr$ via the quadratic formula. Then we can recover $p,q,r$ by taking the GCD of $pqr$ with each of the $N_i$'s, and the rest is easy peasy.

`grey{3_equations_3_unknowns_just_use_groebnerXD}`

### HMAC-CRC

*I came up with a new HMAC algorithm. How has no one thought of this before?* [(code)](/resource/dist-hmac-crc/hmac-crc.py)

The program encrypts messages using a custom algorithm; the challenge is to correctly encrypt 10 test messages by ourselves, without the program's help. The custom algorithm appends to the plaintext `pt` a special 4-byte HMAC, defined as `CRC32(key+pt+key)` where the 16-byte `key` is unknown, and then AES-CTR encrypts the padded `pt+HMAC`.

Recall that AES-CTR works by generating a continuous keystream based on the IV and then xoring with the plaintext to produce the ciphertext. Since the IV is fixed in the program, the keystream can be derived by asking the program to encrypt a block of 0s (32 bytes turn out to be sufficient) and then taking the first 32 bytes of the output (the last 16 bytes corresponds to the padded HMAC).

Thus to replicate the encryption of `pt` ourselves, we just need to know the value `HMAC = CRC32(key pt key)`, and then we can xor `pt+HMAC` with the known keystream. (I mentioned 32 bytes earlier because the test plaintexts are 16 bytes, so `pt+HMAC` padded is 32 bytes.) At this point I spent many hours trying to pin down the details of how CRC32 worked; in theory it just involves polynomial division, but in practice there were many extra steps which I never figured out. I got seriously frustrated, especially after seeing how many other teams solved the challenge at that point.

But it turns out I didn't need to know the details. All I needed is the following special property which is easily found in the CRC32 wiki page:

$$\text{CRC32}(x\oplus y\oplus z) = \text{CRC32}(x)\oplus \text{CRC32}(y)\oplus \text{CRC32}(z),\quad \text{len}(x)=\text{len}(y)=\text{len}(z).$$

Here we sub `x = key 0 0`, `y = 0 pt 0`, `z = 0 0 key`, where `0` denotes a 16-byte block of zeroes and `pt` is 16 bytes long. Thus if we know `k = CRC32(key 0 0) xor CRC(0 0 key)`, then we can derive the HMAC for any 16-byte plaintext since we can compute `CRC(0 pt 0)` ourselves. And `k` is derived by asking the program to encrypt a 16-byte block `pt` (I chose `pt = 0`), then xoring the result (minus the last 16 bytes) with `CRC32(0 pt 0)`.

```python
from pwn import *
from binascii import crc32

def CRC32(x):
    return int.to_bytes(crc32(x), 4, 'big')

def encrypt(s):
    r.clean()
    r.sendline(b'1')
    r.clean()
    r.sendline(s.encode())
    l = r.recvline().decode()[:-1]
    return bytes.fromhex(l)

r = remote('challs.nusgreyhats.org', 32000)
context.log_level = 'debug'
actual_key = r.recvline().decode()[:-1]

# Derive keystream
raw = encrypt('00'*32)[:-16]
assert len(raw) == 32
keystream = []
for i in range(0, len(raw), 16):
    keystream.append(raw[i:i+16])
assert keystream[0] == raw[:16]

crc_key_zero_key = xor(encrypt('00'*16), keystream[1])[16:16+4]
crc_zeroes = CRC32(b'\x00'*48)
# This is our desired k
crc_key_key = xor(crc_zeroes, crc_key_zero_key)

r.clean()
r.sendline(b'2')

for i in range(10):
    qn = bytes.fromhex(r.recvline().decode()[8:])
    r.clean()
    hmac = xor(CRC32(b'\x00'*16 + qn + b'\x00'*16), crc_key_key)

    b1 = xor(qn, keystream[0])
    b2 = xor(hmac + b'\x0c'*12, keystream[1])
    r.sendline((b1 + b2).hex().encode())

r.interactive()
```

`grey{everything_is_linear_algebra_a0945v832q}`

### Learning With Mistakes

*Original LWE use field GF(prime). TFHE use Mod(2^n). I use GF(2^n) so that it's still a field so obviously mine is gna be more secure lmao.* [(code)](/resource/dist-learning-with-mistakes/lwe.sage) [(log)](/resource/dist-learning-with-mistakes/log)

The goal is to retrieve the secret key $S$ (an element of $\F_2^{500}$), with which the flag can be easily recovered. The ciphertext given in the log file is a list of 132 pairs $(A,c)$ where $A$ is a length-500 vector of integers and $c$ is an integer. Actually, the integers represent elements of $F=\text{GF}(2^{32})$, so $A$ and $c$ should be thought of as elements of $F^{500}$ and $F$ respectively. Specifically, from the bit representation $b_0b_1\cdots b_{31}$ of the integer we form the element

$$y = b_0 x^{31} + b_1 x^{30} + \cdots + b_{31},$$

where $x$ is chosen via `GF(2^32).gen()`. In fact, $\text{GF}(2^{32})$ is a vector space over $\F_2$ and $\{1,x,\ldots,x^{31}\}$ is a basis, so $y$ can also be thought of as the vector $(b_0,\ldots,b_{31})$.

Now, $A$ is randomly sampled, whereas $c$ is computed as

$$c = A\cdot S + m + \text{noise}.$$

Taken as integers, $m$ is 4 bits from the original message followed by 28 zero bits, whereas $\text{noise}$ is 4 zero bits followed by 28 random bits. But taken as vectors, $m$ and $\text{noise}$ are independent of each other -- and that is the crux of the challenge! (If we worked in $\ZZ{2^{32}}$ instead, then $m$ and $\text{noise}$ cannot be viewed as vectors.)

Let $A=(A_1\ A_2\ \cdots\ A_{500})$. If we take the first to the fourth coordinate of the above equation, we can eliminate the noise term:

$$c_i = (A_{1i}\ A_{2i}\ \cdots\ A_{500,i})\cdot S + m_i,\quad 1\le i\le 4.$$

Note that since the entries of $S$ are bits, $A\cdot S$ is just a sum over certain entries of $A$, so this can be rewritten as a system of four equations over $\F_2$ with 500 unknowns (the elements of $S$):

$$b_1 A_{1i} + b_2 A_{2i} + \cdots + b_{500}A_{500,i} = c_i-m_i,\quad 1\le i\le 4.$$

Since there are 132 pairs of $(A,c)$, we have $132\cdot4=528$ equations in total, which is enough to completely determine the solutions $b_i$ and recover $S$. (Yet another challenge that involves solving a large linear system, lol.)

```python
from sage.all import *
from Crypto.Util.number import getPrime, inverse, bytes_to_long as b2l, long_to_bytes as l2b
from hashlib import sha512
import numpy as np

n = 500
qbits = 32
mbits = 4
q = 2**qbits
F = GF(q)
x = F.gen()

def int_to_F(n):
    return sum(b*x**i for i,b in enumerate(map(int, bin(n)[2:][::-1])))

L = [copied from log file]
assert len(L) == 132

message = b"Original LWE use field GF(prime). TFHE use Mod(2^n). I use GF(2^n)"
msgL = bytes_to_long(message)

def project(n):
    return list(int_to_F(n))[-4:][::-1]

M = []  # matrix of A's
X = []  # vector of ci-mi's
for i in range(132):
    msg_fourbits = msgL & 0b1111
    msgL >>= 4
    m0, m1, m2, m3 = [(msg_fourbits >> (3-j)) & 1 for j in range(4)]
    c0, c1, c2, c3 = project(L[i][1])
    As = [project(j) for j in L[i][0]]
    A0s = [A[0] for A in As]
    A1s = [A[1] for A in As]
    A2s = [A[2] for A in As]
    A3s = [A[3] for A in As]
    M.append(A0s)
    M.append(A1s)
    M.append(A2s)
    M.append(A3s)
    X.append((c0-m0)%2)
    X.append((c1-m1)%2)
    X.append((c2-m2)%2)
    X.append((c3-m3)%2)

assert len(M) == 132*4
assert len(M[0]) == 500
assert len(X) == 132*4

M = matrix(GF(2), M)
X = vector(GF(2), X)
S = M.solve_right(X)

flag_xored = bytes.fromhex('b70262bb880763fe7f3ce2b67e130ed866330acae6f38fb7e4ded75afa12e02036b8c8bbb2b9672e7739fa162cad5ca289ed4c7d70915e5152b6d6e5ec763f8a')
keyhash = sha512(long_to_bytes(int(''.join(map(str, list(S))), 2))).digest()
flag = bytes([a^b for a,b in zip(flag_xored, keyhash)])
print(flag)
```

`grey{I'm_flyin_soon_I'm-_rushing-this-challenge-rn-ajsdadsdasks}`

### RC4 Signing Scheme (upsolve)

*1024-bit (secure!) signing algorithm with RC4 (fast!)* [(code)](/resource/dist-rc4-signing-scheme/rc4-signing-scheme.py)

This challenge is similar to HMAC-CRC in that the program encrypts a message for us and we have to somehow recreate that encryption ourselves. In this case, the program provides RC4 signatures of a fixed secret message, along with the IV used. The challenge is to produce our own valid signature, except the IVs already used by the program are not allowed.

RC4 works by initializing an array $S$ (which is a permutation of 0 to 255) via a key-scheduling algorithm, and then generating a keystream from $S$ to xor with the message. The key passed into the scheduler is the IV concatenated with a private key that we do not know, and the main loop of the scheduler swaps two elements of $S$ for each character in the key. Thus, the scheduler processes the IV first, producing a 'partial' array $S'$, and then processes the private key which yields the final $S$ for the keystream.

```python
def keyschedule(key):
    S = list(range(256))
    j = 0
    for i in range(256):
         j = (j + S[i] + key[i % len(key)]) % 256
	 S[i], S[j] = S[j], S[i]
    return S
```

If we could find a different IV that produced the same partial $S'$, then the final $S$ would also be the same (since the private key is fixed), thus the signature is the same. This means we can pass in our new IV along with the old signature to pass the challenge.

How to find this special IV? We know that $S'$ is obtained by applying a sequence of swaps to the list `[0,1,...,255]` -- `S[0]` swaps with some `S[a0]`, `S[1]` swaps with some `S[a1]`, ..., `S[127]` swaps with some `S[a127]` (since IV is 128 bytes long). Note the `ai`'s are the successive values of `j` in the loop above. In left-to-right cycle notation this can be written

$$(0\ a_0)(1\ a_1)\cdots(127\ a_{127}).$$

The problem is to find a different set of swapping indices $a_0',\ldots,a_{127}'$ which will achieve the same permutation. Then the special IV can be computed as follows:

```python
# swaps is a list of swapping indices a_i'
def derive_iv(swaps):
    S = list(range(256))
    iv = []
    j = 0
    for i in range(128):
        k = swaps[i] # the value we want j to update to
        iv.append((k - j - S[i]) % 256)
        j = (j + S[i] + iv[i]) % 256
	assert j == k
        S[i], S[k] = S[k], S[i]
    return bytes(iv)
```

We can find a set of $a_i'$ by only changing a few $a_i$. Suppose $x=a_0$, $y=a_x$, $z=a_y$, which means 0 is swapped with $x$, $x$ is swapped with $y$, and $y$ is swapped with $z$. I need to assume that $x,y<128$, because otherwise the swaps $(x\ y)$ and $(y\ z)$ only occur *after* the partial $S'$, and we can only influence the swaps that happen before. Furthermore, assume that no other swaps touch $0$, $x$, $y$ or $z$, so these four values are permuted among themselves (as a consequence I also require $z\ge128$). These assumptions mean that I need the program to generate multiple signatures until a one with 'good' swaps is found.

If $x<y$, then in (left-to-right) cycle notation the permutation of $\{0,x,y,z\}$ is

$$(0\ x)(x\ y)(y\ z) = (0\ z\ y\ x).$$

Now note that $(0\ z\ y\ x)$ is also equal to $(0\ x)(x\ z)(y\ x)$, which means we can set $a_0'=x$, $a_x'=z$ and $a_y'=x$ (and all other $a_i'$ to $a_i$). On the other hand if $x\ge y$ then the permutation is

$$(0\ x)(y\ z)(x\ y) = (0\ y\ z\ x)$$

which is equal to $(0\ x)(y\ x)(x\ z)$, so the assignment of $a_i's$ is actually the same.


```python
from pwn import *
from copy import deepcopy
  
def get_partial_swaps_list(iv):
    swaps = []
    S = list(range(256))
    j = 0
    for i in range(len(iv)):
        j = (j + S[i] + iv[i]) % 256
        S[i], S[j] = S[j], S[i]
        swaps.append(j)
    return swaps, S

def derive_iv(swaps):
    S = list(range(256))
    iv = []
    j = 0
    for i in range(128):
        k = swaps[i]
        iv.append((k - j - S[i]) % 256)
        j = (j + S[i] + iv[i]) % 256
        assert j == k
        S[i], S[k] = S[k], S[i]
    return bytes(iv)

def apply_swaps(swaps):
    S = list(range(256))
    for i, j in enumerate(swaps):
        S[i], S[j] = S[j], S[i]
    return S

def get_equivalent_swaps_list(swaps):
    swaps = deepcopy(swaps)
    a = swaps[0]
    if a >= 128:
        print('a >= 128')
        return None
        
    b = swaps[a]
    if b >= 128:
        print('b >= 128')
        return None

    c = swaps[b]
    if c < 128:
        print('c < 128')
        return None

    for i in range(128):
        if i in (0,a,b): continue
        if swaps[i] in (0,a,b,c):
            print(f'swaps[{i}] = {swaps[i]}')
            return None

    swaps[0], swaps[a], swaps[b] = a, c, a
    print(a,b,c)
    return swaps

def list_equal(L1, L2):
    return len(L1) == len(L2) and all(L1[i] == L2[i] for i in range(len(L1)))

while True:
    r = remote('challs.nusgreyhats.org', 32001)
    r.clean()
    r.sendline(b'1')
    ivct = r.recvline().decode()[:-1]
    iv, ct = bytes.fromhex(ivct[:128*2]), bytes.fromhex(ivct[128*2:])
    assert len(iv) == 128

    swaps, partial_S = get_partial_swaps_list(iv)

    new_swaps = get_equivalent_swaps_list(swaps)
    if new_swaps is None:
        r.clean()
        r.sendline(b'3')
        continue

    new_partial_S = apply_swaps(new_swaps)
    new_iv = derive_iv(new_swaps)
    assert list_equal(partial_S, new_partial_S)

    assert list_equal(get_partial_swaps_list(iv)[0], swaps)
    assert list_equal(get_partial_swaps_list(new_iv)[0], new_swaps)
    assert list_equal(get_partial_swaps_list(iv)[1], get_partial_swaps_list(new_iv)[1])

    r.clean()
    r.sendline(b'2')
    r.clean()
    r.sendline((new_iv.hex() + ct.hex()).encode())
    print(r.recvline())
    break
```

`grey{rc4_more_like_rcgone_amirite_q20v498n20}`