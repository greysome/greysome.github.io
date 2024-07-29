# Microcorruption solutions: Hollywood

This challenge is of a different flavor from the rest: the assembly code has been obfuscated in a myriad of different ways, so a significant difficulty comes from understanding what the code even does. After we peel away the layers of deception, we will see that the real meat of the challenge is to reverse a hash-like function.

At first, the sheer number of `jmp` and `dadd.b` instructions popped out to me. This is the `main` function:

```text
4400 <main>
4400:  013c           jmp	$+0x4 <main+0x4>
4402:  d1a1 3140 0044 dadd.b	0x4031(sp), 0x4400(sp)
4408:  013c           jmp	$+0x4 <main+0xc>
440a:  d1a1 1542 5c01 dadd.b	0x4215(sp), 0x15c(sp)
4410:  013c           jmp	$+0x4 <main+0x14>
4412:  d1a1 75f3 013c dadd.b	-0xc8b(sp), 0x3c01(sp)
4418:  d1a1 35d0 085a dadd.b	-0x2fcb(sp), 0x5a08(sp)
441e:  013c           jmp	$+0x4 <main+0x22>
4420:  d1a1 3f40 0011 dadd.b	0x403f(sp), 0x1100(sp)
4426:  013c           jmp	$+0x4 <main+0x2a>
4428:  d1a1 0f93 0724 dadd.b	-0x6cf1(sp), 0x2407(sp)
442e:  013c           jmp	$+0x4 <main+0x32>
4430:  d1a1 8245 5c01 dadd.b	0x4582(sp), 0x15c(sp)
4436:  013c           jmp	$+0x4 <
4438:  d1a1 2f83 0343 dadd.b	-0x7cd1(sp), 0x4303(sp)
443e:  013c           jmp	$+0x4 <main+0x42>
4440:  d1a1 1e4f 3446 dadd.b	0x4f1e(sp), 0x4634(sp)
4446:  013c           jmp	$+0x4 <main+0x4a>
4448:  d1a1 8f4e 0024 dadd.b	0x4e8f(sp), 0x2400(sp)
444e:  013c           jmp	$+0x4 <main+0x52>
4450:  d1a1 ef23 013c dadd.b	0x23ef(sp), 0x3c01(sp)
4456:  d1a1 0f43 0f93 dadd.b	0x430f(sp), -0x6cf1(sp)
445c:  013c           jmp	$+0x4 <main+0x60>
445e:  d1a1 0e24 013c dadd.b	0x240e(sp), 0x3c01(sp)
4464:  d1a1 8245 5c01 dadd.b	0x4582(sp), 0x15c(sp)
446a:  013c           jmp	$+0x4 <main+0x6e>
446c:  d1a1 1f83 013c dadd.b	-0x7ce1(sp), 0x3c01(sp)
4472:  d1a1 cf43 0035 dadd.b	0x43cf(sp), 0x3500(sp)
4478:  013c           jmp	$+0x4 <main+0x7c>
447a:  d1a1 f923 013c dadd.b	0x23f9(sp), 0x3c01(sp)
4480:  d1a1 3e40 0012 dadd.b	0x403e(sp), 0x1200(sp)
4486:  013c           jmp	$+0x4 <main+0x8a>
4488:  d1a1 3f40 0024 dadd.b	0x403f(sp), 0x2400(sp)
448e:  013c           jmp	$+0x4 <main+0x92>
4490:  d1a1 bf4f feef dadd.b	0x4fbf(sp), -0x1002(sp)
4496:  013c           jmp	$+0x4 <main+0x9a>
4498:  d1a1 3e53 fa23 dadd.b	0x533e(sp), 0x23fa(sp)
449e:  013c           jmp	$+0x4 <main+0xa2>
44a0:  d1a1 3b40 0c16 dadd.b	0x403b(sp), 0x160c(sp)
44a6:  013c           jmp	$+0x4 <main+0xaa
44a8:  d1a1 0212 013c dadd.b	0x1202(sp), 0x3c01(sp)
44ae:  d1a1 3040 be44 dadd.b	0x4030(sp), 0x44be(sp)
```

On closer inspection, the CPU isn't actually executing the `dadd.b`s, because the preceding `jmp` instructions will always direct the CPU to the 4 (or sometimes 2) bytes hidden *inside*. Since the bytes `d1a1` are always jumped over, they don't serve any purpose other than to confuse the program that prints out assembly instructions. This was not hard to get around: I copied the assembly into Ghidra and replaced the byte sequence `013c d1a1` (and other sequences `013c XXXX` which appear later in the program) with no-ops; Ghidra then parses the assembly in the desired manner and reveals the hidden instructions.

![viewing the real instructions in Ghidra](mc-hollywood/1.png "")

I won't go through these instructions in detail, other than noting that it does some setup and promptly jumps to `<insn_start>`, which is presumably the main body of the program. It seemed like a very strange function, because there were absolutely no signs of interrupt calls, which is the only way to unlock the door. Yet we know the door must be unlockable somehow (otherwise this is just an impossible challenge) -- the only possibility is that the code for the interrupt call `0x7e` or `0x7f` is generated during runtime.

The first part of `<insn_start>` reads some encrypted bytes from the address in `r10`, decodes them using `<my_decrypt_one_byte>`, and then moves it to the address in `r12`.

```text
44be <insn_start>
// Call the RNG and store result in r15
44be:  3240 00a0      mov	#0xa000, sr
44c2:  b012 1000      call	#0x10
// r12 is computed based on r15
44c6:  0c4f           mov	r15, r12
44c8:  3cf0 fe0f      and	#0xffe, r12
44cc:  3c50 00e0      add	#0xe000, r12
44d0:  0a4b           mov	r11, r10
// Decrypt one byte at r10 and write to 0x0(r12)
44d2:  3f4a           mov	@r10+, r15
44d4:  0012           push	pc
44d6:  733c           jmp	$+0xe8 <my_decrypt_one_byte+0x0>
44d8:  8c4f 0000      mov	r15, 0x0(r12)
... a few more times...
// Decrypt one byte at r10 and write to 0xc(r12)
4516:  3f4a           mov	@r10+, r15
4518:  0012           push	pc
451a:  513c           jmp	$+0xa4 <my_decrypt_one_byte+0x0>
451c:  8c4f 0c00      mov	r15, 0xc(r12)
... rest of procedure ...
```

(Note that `push pc` then `jmp` is equivalent to `call`.) The encrypted bytes reside in the range `0x1400` to `0x2500`, and the decoded bytes are located far down in memory (the exact address being random). The next part of `<insn_start>` (after unobfuscating the `dadd.b`'s and `jmp`'s) goes like this:

```text
...
4520:  0e4c           mov	r12, r14
// 013c 9f4f
4526:  0e4c           mov       r12, r14
4528:  0d40           mov       pc, r13
452a:  3d50 0c00      add	#0xc, r13  // r13 = return address after the br
// 013c 9d4e
4532:  3241           pop       sr
4534:  004c           br        r12
...
```

`r12` stores the address of the decrypted bytes, so they are executed as code. For example, this is the first set of decrypted bytes:

```text
e300:  3182           sub      #0x8, sp
e302:  3c40 ea49      mov      #0x49ea, r12  // affects the new load address
e306:  004d           br       r13        // return to <insn_start>
// the rest are not executed
```

The rest of `<insn_start>` moves the entire program code to a new, random location in memory, and then jumps back to the start of `<insn_start>` (at its new address). At the new iteration, `r10` is different and so another batch of instructions is decrypted and executed. The value of `r10` can be traced back to the value of `r12` (I did not give the exact code here), which was set in line `0xe302` above. Also, in every batch the first instruction is the 'interesting' one, and the last two sets `r12` and returns control to `<insn_start>`.

By running `<my_decrypt_one_byte>` on each encrypted byte, we can piece together the 'interesting' instructions to recover the true program lying beneath the obfuscation. In fact the decryption is relatively straightforward: it just xors the input byte with another byte computed from `r10`. However, I didn't get this approach to work, because somehow the decrypted bytes I got didn't match up with the actual execution. Luckily, there is another method, which is to step through the program and read off the instructions directly from the Microcorruption debugger. I couldn't use breakpoints normally (remember the program code keeps changing address), so I resorted to defining macros that will step through all the unimportant parts of `<insn_start>`, since I just want to see the interesting instructions. Just for fun, they looked like this:

```text
// Jump to the next batch of instructions
#define z n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;s;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;
// Same, but for some reason every other iteration requires an extra step
#define zz n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;s;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;n;
// Skip through the loaded instructions also, useful if I already know them and I have to accidentally start over
#define y z;s;s;s;s
#define yy zz;s;s;s;s
```

To save time, I only recorded the instructions after receiving the user input which is stored in `0x2600`.

```text
sub      #0x8, sp
// Input address
mov      #0x2000, r5
clr      r6
// (*)
add      @r5, r4
swpb     r4
xor      @r5+, r6
xor      r4, r6
xor      r6, r4
xor      r4, r6
tst      0x0(r5)
mov      sr, r7
and      #0x2, r7
rra      r7
xor      #0x1, r7
swpb     r7
rra      r7
sxt      r7
swpb     r7
sxt      r7
// r8 is the address of (*)
mov      #0x4b18, r8
and      r7, r8
xor      #-0x1, r7
and      #0x47aa, r7
add      r7, r8

// Next two lines are executed only if @r5 != 0, forgot what the exact instruction was
// Jump back to (*)
clr      r7
mov      r8, r12

cmp      #0xfeb1, r4
mov      sr, r7
clr      r4
// (1)
cmp      #0xfeb1, r4
mov      sr, r7
clr      r4
// (2)
cmp      #0x9298, r6
and      sr, r7
clr      r6
rra      r7
xor      #0x1, r7
swpb     r7
rra      r7
rra      r7
rra      r7
rra      r7
// Stops here if the CPUOFF bit is set, which occurs if either (1) or (2) is false
bis      r7, sr
// Freedom!
mov      #0xff00, sr
call     #0x10
```

Translated into C:

```C
unsigned short r4 = 0, r6 = 0;
for (int i = 0; i < input_len; i++) {
  r4 += input[i];
  r4 = swpb(r4);
  r6 ^= input[i];
  // Swap r4 and r6
  r6 ^= r4;
  r4 ^= r6;
  r6 ^= r4;
}
if (r4 == 0xfeb1 && r6 == 0x9298)
  unlock_door();
else
  exit();
```

In other words we have a recurrence

```text
r4' = r6 ^ input[i]
r6' = swpb(r4 + input[i])
```

and we want to find a suitable input that gives the desired final value for `r4` and `r6`.

TODO TODO TODO