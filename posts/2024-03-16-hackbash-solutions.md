# Crypto solutions for Hackbash 2024


### Mahjong Cipher

A pictoral substitution cipher followed by another substitution cipher.

### My First Encryption

Let $h(X)$ denote the SHA1 hash of the character $X$. Given the flag **flag{??$\ldots$??}**, the code computes the hash of each character and stores it in a list $L$, setting the key to be the first 4 elements $(h(\text{f})\ h(\text{l})\ h(\text{a})\ h(\text{g}))$. Then there is a loop where each element of $L$ is replaced by its XOR with every element of the key. Represented pictorially:

$$\begin{matrix}
L & = & h(\text{f}) & h(\text l) & h(\text a) & h(\text g) & h(\text \{) & h(\text?) & h(\text?) & \ldots \\[5pt]
  &   &      &      &      & \Big\downarrow \\[5pt]
C & = & h(\text{f})\oplus S & h(\text l)\oplus S & h(\text a)\oplus S & h(\text g)\oplus S & h(\text\{)\oplus S & h(\text ?)\oplus S & h(\text ?)\oplus S & \ldots
\end{matrix}$$

where $S=h(\text f)\oplus h(\text l)\oplus h(\text a)\oplus h(\text g)$. We are given $C$, so the solution is rather straightforward:

1. Compute a table of $h(X)\oplus S$ for all possible characters $X$ (at most 256 of them)
2. For each character $h(\text ?)\oplus S$ in $C$, match it against the table to find $\text ?$.

### Anti-Fermat

An RSA decryption challenge.

1. The prime generation algorithm makes use of Dirichlet's theorem on primes in arithmetic progression, thus we know the primes have the form $p$ and $q=p+kd$, where $d$ is known and $k>0$ is likely small.
2. I found both primes by setting up a quadratic $x(x+kd)=x^2+xkd=n$ (where $n=pq$), and then incrementing $k$ until the discriminant is a perfect square, indicating that the solution $x$ is very likely integral (and hopefully a prime, which it did turn out to be).
3. Usually decryption would proceed trivially by finding some inverse $d=e\inv$ mod $(p-1)(q-1)$ and then computing $c^d$ mod $n$, where $c$ is the encrypted message. But this is not possible because of the sly choice of exponent $e=22$, causing $e$ and $(p-1)(q-1)$ to have gcd $>1$.
4. It turns out that 11 is invertible mod $(p-1)(q-1)$ though. So the next best thing is to compute its inverse $d'$, and note that

    $$c^{d'}\equiv m^{22d'}\equiv (m^{11d'})^2\equiv m^2 \mod{n}.$$

    So the problem reduces to finding $m$ given $m^2$ mod $n$, i.e. finding a modular square root. (Because $m^2\gg n$, simply square rooting doesn't work!) Searching up online, I saw it can be done by some math magic involving Tonelli-Shanks algorithm and CRT which I don't yet fully understand, but I copy-pasted an implementation and ran it, yielding the message with the flag inside!

    (Remark: there are many possible modular square roots $r$ mod $n$ which would solve the equation

    $$(r-m)(r+m)\equiv 0 \mod{n}.$$

    Thus there are technically many possibilities for $m$ given a computed modular square root $r'$: for instance we could have (1) $r'-m=cp$ and $r'+m=dq$ for some $c,d$, or (2) $r'-m=cq$ and $r'+m=dp$ for some $c,d$, or (3) $r'-m\equiv 0$ mod $n$ or (4) $r'+m\equiv0$ mod $n$. Fortunately the solution turned out to fall under either case 3 or 4, I don't remember exactly which.)

### XOR key

We are given a 10000-byte long ciphertext $C_1\ldots C_{10000}$, which was encrypted by XORing a random byte sequence $B_1\ldots B_{10000}$ containing the flag with a 30-byte key $K_1\ldots K_{30}$ repeated cyclically. (Note the $B$'s and $K$'s are unknown.) So for instance, $C_1=B_1\oplus K_1$, $C_2=B_2\oplus K_2$ and $C_{31}=B_{31}\oplus K_1$. Rearranging, we get 10000 equations of the form

$$K_{k\ \text{mod}\ 30} = B_k\oplus C_k.$$

Now, we use the fact that each $B_k$ is within a small range of printable characters (let's say there are $n$ of them). Thus in the above equation, $K_{k\ \text{mod}\ 30}$ is actually narrowed down to $n$ possibilities. Then, we use the fact that each $K_i$ appears in at least $\floor{10000/30}=333$ equations; taking all of them into consideration at once, we see that the set of possiblities for $K_i$ is the intersection of 333 $n$-element sets. Computing the intersection for each byte of the key, we happily find that all of them have exactly one element, meaning the key is determined exactly. The flag is then obtained by XORing the ciphertext with the key repeated (since XOR is symmetric).

### Bleichenbacher's attack

I'm just going to re-explain Jules' write-up in my own words. Recall the set of valid RSA decrypts is a range of integers $[0,n)$, because we are exponentiating the ciphered message $c$, and then taking *mod $n$*. The set of decrypts with *valid padding* (which I'll just call valid) is a subrange $[0,k)$ where $0<k<n$---in this case these correspond to the messages starting with a zero byte. We are also given an oracle that takes in any integer $x$, and tells us if $mx$ mod $n$ is valid (this is done by sending the encrypted message $cx^e$ mod $n$, which is decrypted to $(cx^e)^d\equiv mx$ mod $n$).

Now suppose $m<n$. If $x>0$ is the smallest integer such that $mx$ mod $n$ is invalid and $m(x+1)$ mod $n$ is valid, then we can pretty easily conclude that $mx<n\le m(x+1)$, therefore $t=n/m$ lies in $(x,x+1]$. Thus we have determined the integral part of $t$, and we shall find its decimal part via binary search.

Doubling the inequality we have $m(2x)<2n\le m(2x+2)$, and we can split into two cases $m(2x)<2n\le m(2x+1)$ and $m(2x+1)<2n\le m(2x+2)$, which can be rewritten as

$$t\in(x,x+1/2] \quad\text{or}\quad t\in(x+1/2,x+1].$$

(Remark: I believe we need to assume that $m$ is small enough relative to $n$, so that $m(2x)$ mod $n$ doesn't veer off too far left into valid territory, and $m(2x+1)$ mod $n$ right into invalid territory.) We can find out which case it is by checking which of the two conditions holds true:
1. $m(2x)$ invalid, $m(2x+1)$ valid
2. $m(2x+1)$ invalid, $m(2x+2)$ valid

Assuming it is the first case, we can determine whether $t\in(x,x+1/4]$ or $(x+1/4,x+1/2]$ by checking which one of the conditions is valid:
1. $m(4x)$ invalid, $m(4x+1)$ valid
2. $m(4x+1)$ invalid, $m(4x+2)$ valid

In the second case, we instead find out whether $t\in(x+1/2,x+3/4]$ or $(x+3/4,x+1]$ by the conditions
1. $m(4x+2)$ invalid, $m(4x+3)$ valid
2. $m(4x+3)$ invalid, $m(4x+4)$ valid

Then we keep performing the binary search until $t$ is sufficiently precise that $m$ can be recovered by rounding off $n/t$. Some remarks about the practical implementation:
1. Many iterations of the binary search are required. Thus one should use pwntools to script the interaction with the oracle. (Also debugging on a local version is always helpful!)
2. Don't use standard floats to represent the current approximation to $t$, it does not afford enough precision. And we absolutely need the precision because the flag occurs among the least significant digits of $m$. I used gmpy2 multi-precision floats (with precision 10000) and it worked fine.

### Easier Padding Oracle

This is straightforward once one understands the theory behind AES-CBC padding oracle. Recall the following equation governing AES-CBC decryption:

$$T_{i+16} = C_i\oplus f(C_{i+16}),$$

where $C$ and $T$ are ciphertext and plaintext respectively, $f$ is the block cipher encryption, and 16 is the block size. If we change $C_i$ to $C_i'$ such that the plaintext $T'$ has valid padding, then most likely $T_{i+16}'=(17-i)\ \text{mod}\ 16$. For instance, if setting $C_{14}$ to $C_{14}'$ gives valid padding, then most likely the block containing $T_{30}'$ has the form

$$\underbrace{?????????????}_{13\ \text{bytes}}\ \text{0x03}\ \text{0x03}\ \text{0x03},$$

thus $T_{30}'=3$. We have the equation

$$T_{i+16}' = C_i'\oplus f(C_{i+16}) \implies f(C_{i+16}) = T_{i+16}'\oplus C_i' = \bigl((17-i)\ \text{mod}\ 16\bigr) \oplus C_i',$$

and subbing it into the previous equation allows us to recover $T_{i+16}$:

$$T_{i+16} = C_i\oplus C_i'\oplus \bigl((17-i)\ \text{mod}\ 16\bigr).$$

The flag is obtained simply by applying this formula to each line of the attached text file.

### AES-CBC

Didn't solve this lol