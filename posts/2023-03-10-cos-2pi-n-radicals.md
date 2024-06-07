# Expressing $\cos(2\pi/n)$ in radicals


The problem of expressing $\cos(2\pi/n)$ in radicals (or in the terms
of [this other entry]({% post_url 2023-03-10-radicals-principal-roots
%}), expressing it in principal roots) is an interesting one. Actually
it is easily seen to be possible for all $n$: $e^{2\pi i/n}$ is
obviously expressible in radicals hence by the previous entry is
expressible in principal roots. Thus

$$\cos(2\pi/n)={e^{2\pi i/n}+(e^{2\pi i/n})^{-1} \over 2}$$

is as well. One can find online the following table of radical
expressions for small $n$:

$$\begin{matrix}
n & \cos(2\pi/n) \\
\hline
5 & (\sqrt5-1)/4 \\
6 & 1/2 \\
7 & {1\over6}\left(\sqrt[3]{7-21i\sqrt3\over2}+\sqrt[3]{7+21i\sqrt3\over2}-1\right) \\
8 & \sqrt2/2 \\
9 & {1\over2}\left(\sqrt[3]{-1-i\sqrt3\over2}+\sqrt[3]{-1+i\sqrt3\over2}\right) \\
10 & (\sqrt5+1)/4 \\
11 & \text{too long to show here} \\
12 & \sqrt3/2 \\
13 & {1\over12}\left(\sqrt[3]{104-20\sqrt{13}-12i\sqrt{39}}+\sqrt[3]{104-20\sqrt{13}+12i\sqrt{39}}+\sqrt{13}-1\right) \\
14 & {1\over12}\left(\sqrt{3\left(20+2\sqrt[3]{28-84i\sqrt3}+2\sqrt[3]{28+84i\sqrt3}\right)}\right) \\
15 & {1\over8}\left(1+\sqrt5+\sqrt{30-6\sqrt5}\right) \\
16 & \left(\sqrt{2+\sqrt2}\right)/2 \\
17 & {1\over16}\left(\sqrt{17}+\sqrt{34-2\sqrt{17}}+2\sqrt{17+3\sqrt{17}-\sqrt{170+38\sqrt{17}}}-1\right)
\end{matrix}$$

Note that there are two types of expressions: those involving complex
radicals ($n=7,9,13,14,\ldots$) and those where the radicands are
positive real (all other $n$). If $\cos(2\pi/n)$ falls into the latter
type, we say $n$ is expressible in real radicals. A curious
observation is that all the real radicals involved are square
roots---I'll explain this phenomenon later. I'll also provide a
concrete test on $n$ to determine whether $\cos(2\pi/n)$ is
expressible in real radicals.

The results I prove in this entry come in two sets. Think of them as
lying in different 'realms', but linked by a bridge---the notion of
constructability.

#### Set 1

**Theorem 1A.** A real algebraic element is *totally real* if all its
  conjugates over $\Q$ are real, or equivalently its minpoly splits
  over $\R$. An element that is totally real and expressible in real
  radicals is constructible.

**Theorem 1B.** $\cos(2\pi/n)$ is totally real.

**Theorem 1C.** A real, constructible element is expressible in
  *positive* square roots, thus is expressible in real radicals.

#### Set 2

**Theorem 2A.** $\cos(2\pi/n)$ constructible $\iff$ $e^{2\pi i/n}$
  constructible.

**Theorem 2B.** $e^{2\pi i/n}$ constructible $\iff$ $\[\Q(e^{2\pi
  i/n}):\Q]$ is a power of 2.

**Theorem 2C.** $\[\Q(e^{2\pi i/n}):\Q]$ is a power of 2 $\iff$
  $n=2^ep_2\cdots p_k$ for distinct Fermat primes $p_i$.

Combining the results give us the following chains of implications:

$$n=2^ep_2\cdots p_k \overset{\small\text{2C,2B,2A}}\implies \cos(2\pi/n)\ \text{constructible}
\overset{\small\text{1C}}\implies \cos(2\pi/n)\ \text{can be expressed with +ve sqrts}$$

$$n\neq2^ep_2\cdots p_k \overset{\small\text{2C,2B,2A}}\implies \cos(2\pi/n)\ \text{not constructible}
\overset{\small\text{1A,1B}}\implies \cos(2\pi/n)\ \text{not expressible in real radicals}.$$

## The proofs

*Proof of 1A.* If $\a$ is expressible in real radicals then $\a$ lies
 in a tower

 $$\eq{\label{eq:tower}\Q\s F_1\s F_2\s \cdots\s F_k,}$$

 where $F_{i+1}=F_i(a_i)$ and $a_i{}^{n_i}\in F$ for some $n_i$. I'll
 additionally assume WLOG that $a_i\nin F_i$ and $n_i$ is prime. Now,
 the conjugates of $\a$ are the images of $\a$ under maps
 $F_k\to\ol\Q$, and such maps can be constructed by building up
 through the tower \eqref{eq:tower}. That is to say, if we have a map
 $F_i\to\ol\Q$, then a map $F_{i+1}\to\ol\Q$ can be constructed by
 sending $a_i$ to one of its conjugates over $F_i$, which has the form
 $za_i$, $z$ an $n_i$th root of unity.

 Since $F_k=\Q(a_1,\ldots,a_{k-1})$, we have
 $\a=f(a_1,\ldots,a_{k-1})$ where $f$ is a rational function. Given
 $\psi:F_k\to\ol\Q$, we have

 $$\eq{\label{eq:f}\psi(\a)=f(z{}^{l_1}\,a_1,\ldots,z{}^{l_{k-1}}\,a_{k-1}),
 \quad z\;\text{a large enough root of unity}.}$$

 The rest of the proof is handwavy. If the expression for $\a$
 involves other radicals besides square roots, that means some $n_i$
 is odd, and so there is some $\psi$ sending $a_i$ to a conjugate
 $z{}^{l_i}\,a_i$ not of the form $\pm a_i$, and so this conjugate is
 complex. Furthermore if it is *necessary* that the radical expression
 contains a non-square-root radical, then intuitively the variable
 $x_i$ should play a nontrivial role in $f$. Then, it would be pretty
 unlikely that with one of the inputs to the RHS of \eqref{eq:f}
 complex, the LHS remains a real number. There would have to be some
 miraculous cancelling out for that to happen. This contradicts the
 hypothesis that $\a$ is totally real. $\qed$

<br>

*Proof of 1B.* Let $K=\Q(\cos(2\pi/n))\s\R$. It is a subfield of the
 abelian extension $\Q(e^{2\pi i/n})/\Q$, so $\Gal(\Q(e^{2\pi
 i/n})/K)$ is a normal subgroup, so $K$ is fixed by the conjugation
 action of $\Gal(\Q(e^{2\pi i/n})/\Q)$. In particular this means that
 all the conjugates of $\cos(2\pi/n)$ lie in $K$ and are thus
 real. $\qed$

<br>

*Proof of 1C.* If $F$ is a subfield of $\R$ and $K/F$ is a real
 quadratic extension, then $K=F(\sqrt d)$ where $d>0$. Now, given any
 real constructible element $\a$ and some square root tower, we can
 intersect the tower with $\R$ to obtain a real square root tower
 containing $\a$. By repeatedly applying the aforementioned fact
 starting from $F=\Q$, we can see the intersected tower is built out
 of positive square roots. $\qed$

<br>

*Proof of 2A.*

$$\cos(2\pi/n) = {e^{2\pi i/n}+(e^{2\pi i/n})^{-1} \over 2} \and
e^{2\pi i/n} = {\cos(2\pi/n) + i\sqrt{1-\cos(2\pi/n)^2}},$$ 

and it is clear that one is constructible iff the other is. $\qed$

<br>

*Proof of 2B.* More generally, we can prove that $\a\in\C$ is
constructible iff the splitting field $K$ of its minpoly has a power 2
degree over $\Q$.

($\imp$) $\a$ lies in a field $L$ with a square root tower over
$\Q$. Let $L_1$ be its normal closure; then by applying each
$\eta\in\Gal(L_1/K)$ to the square root tower, we obtain a square root
tower for $\eta(L)$. And since $L_1$ is generated by the conjugates of
$L$, we can concatenate the square root towers for the $\eta(L)$'s to
obtain a large square root tower for $L_1$ (note that some factors may
become trivial along the way since they happen over a larger field,
but that doesn't matter). Thus $[L_1:\Q]$ is a power of 2, and since
$K$ is isomorphic to a subfield of $L_1$ we also have $[K:\Q]$ a power
of 2.

($\impd$) By the Galois correspondence, $\Gal(K/\Q)$ is a
2-group. 2-groups are solvable, so the factors of its composition
series are all $C_2$. This corresponds to a tower of quadratic
extensions from $\Q$ up to $K$, and so every element of $K$, in
particular $\a$, is constructible. $\qed$

<br>

*Proof of 2C.* Since $[\Q(e^{2\pi i/n}):\Q]=\varphi(n)$ this reduces
to the number-theoretic problem of finding all $n$ with $\varphi(n)$ a
power of 2. If $n=2^{e_1}\,p_2{}^{e_2}\cdots p_s{}^{e_s}$ with $e_i\ge0$
then

$$\varphi(n) = \begin{cases}
2^{e_1-1}\,p_2{}^{e_2-1}(p_2-1)\cdots p_s{}^{e_s-1}(p_s-1), &e_1 > 0 \\
p_2{}^{e_2-1}(p_2-1)\cdots p_s{}^{e_s-1}(p_s-1), &e_1 = 0.
\end{cases}$$

So $\varphi(n)$ can only be a power of 2 if and only if the odd primes
$p$ in its factorization have multiplicity 1, and have the form
$2^{2^k}+1$.[^1] $\qed$

[^1]: If $p=2^k+1$ is a prime, then $k$ is a necessarily a power of 2, otherwise an odd number divides $k$ and this induces a factorisation of $p$.
