# The extension $\C(t^n,u^n)/\C(t,u)$, where $t^2+u^2=1$


This is one of my favourite exercises from Jacobson so far. Let $t$ be
transcendental over $\C$, and $u$ be an element such that $t^2+u^2=1$.

**Theorem.** $\C(t^n,u^n)/\C(t,u)$ is normal. The Galois group is
  trivial if $n$ is odd and $V_4$ if $n$ is even.

*Proof.* The extension is the splitting field of the polynomial
 $(x^n-t^n)(x^n-u^n)$ since $\C$ contains all $n$th roots of unity,
 thus it is normal. For $n$ odd, consider the following lattice:

$$\xymatrix{
& \C(t,u) & \\
& \C(t,u^n)\ar@{-}[u] & \\
\C(t^n,u^n)\ar@{-}[ur] & & \C(t)\ar@{-}[ul] \\
\C(t^n,u^{2n})\ar@{-}[u]\ar@{-}[urr] & & \\
& & \C(t^n)\ar@{-}[ull]\ar@{-}[uu]
}$$

We have $\C(t,u^n)=\C(t,u)$ since $u^n/u$ is a power of
$u^2\in\C(t)$. And $[\C(t,u):\C(t)]=2$, since $u$ satisfies the
quadratic $x^2+(t^2-1)$ which has no roots in $\C(t)$ and is hence
irreducible. Thus $[\C(t,u^n):\C(t)]=2$ as well.

Next, I show that $[\C(t):\C(t^n)]=n$, which implies
$[\C(t,u^n):\C(t^n)]=2n$. Clearly the degree is at most $n$. Suppose
$p(x)\in\C(t^n)[x]$ has degree $<n$ and $p(t)=0$. Multiplying common
denominators, we obtain $q(t)=0$ for some
$q(x)\in\C[t^n][x]$. Expanding this out gives

$$q_{n-1}(t^n)t^{n-1} + q_{n-2}(t^n)t^{n-2} + \ldots + q_0(t^n) =
0,\quad q_i(x)\in\C[x].$$

The reader can convince himself that all the $q_i(x)$'s are forced to
be 0, so $p(x)=q(x)=0$.

Alternatively, we can factor the extension into a tower of
subextensions with prime degrees
$\C(t)/\C(t^{p_1})/\C(t^{p_1p_2})/\ldots$, where $n=\prod_{i=1}^n
p_i$. The degree $[\C(t):\C(t^{p_1})]$ is $p_1$, since
$x^{p_1}-t^{p_1}$ either has a root in $\C(t^{p_1})$ or is
irreducible, and the former cannot be true. Likewise for
$[\C(t^{p_1}):\C(t^{p_1p_2})]$ and so on.

For the reader's sake, here is the lattice with the aforementioned
degrees filled in:

$$\xymatrix{
& \C(t,u) & \\
& \C(t,u^n)\ar@{-}[u]_1 & \\
\C(t^n,u^n)\ar@{-}[ur] & & \C(t)\ar@{-}[ul]_2 \\
\C(t^n,u^{2n})\ar@{-}[u]\ar@{-}[urr] & & \\
& & \C(t^n)\ar@{-}[ull]\ar@{-}[uu]_n
}$$

It remains to determine $[\C(t^n,u^n):\C(t^n,u^{2n})]$ and
$[\C(t^n,u^{2n}):\C(t^n)]$, which will allow us to determine the
desired degree $[\C(t,u^n):\C(t^n,u^n)]=[\C(t,u):\C(t^n,u^n)]$. The
first degree is obviously $\le2$, and it is $>1$ since
$\C(t^n,u^{2n})\subset\C(t)$ whereas $\C(t^n,u^n)$ isn't. Thus it is
2.

As for the second degree, observe that $\C(t)/\C(t^n)$ is Galois with
automorphisms generated by $t\mapsto \zeta t$, where $\zeta$ is a
primitive $n$th root of unity. And $\C(t^n,u^{2n})/\C(t^n)$ is a
subextension since $u^{2n}=(1-t^2)^n\subset \C(t^n,t^2)=\C(t)$.
Observe that $(1-\zeta^2 t^2)^n \neq (1-t^2)^n$, since by virtue of
$\C[t]$ being a UFD this implies $1-\zeta^2t^2 = 1-t^2$, a
contradiction. Therefore, $u^{2n}$ is fixed only by the trivial
automorphism, and so $[\C(t^n,u^{2n}):\C(t^n)]=n$.

Here is the completed lattice diagram:

$$\xymatrix{
& \C(t,u) & \\
& \C(t,u^n)\ar@{-}[u]_1 & \\
\C(t^n,u^n)\ar@{-}[ur]^1 & & \C(t)\ar@{-}[ul]_2 \\
\C(t^n,u^{2n})\ar@{-}[u]_2 \ar@{-}[urr]_1 & & \\
& & \C(t^n)\ar@{-}[ull]_n \ar@{-}[uu]_n
}$$

The arguments for the even case are quite similar so I won't go
through them. The lattice is

$$\xymatrix{
& \C(t,u) \\
& \C(t,u^n)\ar@{-}[u]_2 \\
& \C(t)\ar@{-}[u]_1 \\
& \C(t^2)\ar@{-}[u]_2 \\
\C(t^n,u^n)\ar@{-}[ur]^1 & \\
& \C(t^2)\ar@{-}[ul]_{n/2}\ar@{-}[uu]_{n/2} \\
}$$

Thus $[\C(t,u):\C(t^n,u^n)]=4$. There are degree 2 subextensions of
$\C(t,u)/\C(t^n,u^n)$, namely $\C(t)$ and $\C(u)$, so the Galois group
is $V_4$. The proof is done. $\qed$

As a corollary, the element

$${(t+iu)^n+(t-iu)^n\over 2}$$

lies in $\C(t^n,u^n)$ for all $n$. If $n$ is odd, this is trivial. If
$n$ is even, it is fixed by the automorphisms $t\mapsto -t, u\mapsto
u$ and $t\mapsto t, u\mapsto -u$ of $\C(t,u)/\C(t^n,u^n)$. In
particular,

$$\cos nx = {(\cos x+i\sin x)^n+(\cos x-i\sin x)^n\over 2}$$

can be expressed in terms of $\cos^n x$ and $\sin^n x$. A little bit
of experimentation shows this is not obvious at all! Courtesy of
Ariana, here's an expression for $n=3$:

$$\cos3x={\cos^3x\left(-2+5\cos^6x-7\sin^6x\right) \over
1+2\cos^6x-\sin^6x}.$$