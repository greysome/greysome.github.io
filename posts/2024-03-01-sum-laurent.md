# A summation identity, via Laurent expansion


**Claim.** Given $n$ variables $x_1,\ldots,x_n$, the following identity holds:

$$\sum_{j=1}^n{x_j^r\over\prod_{\substack{1\le k\le n\\ k\neq j}}(x_j-x_k)} =
\begin{cases}
0,& 0\le r<n-1\\
1,& r=n-1\\
\sum x_j,& r=n.
\end{cases}$$

For example, when $n=3$ and the variables $a,b,c$ are used in place of $x_1,x_2,x_3$, we have the following identities

$$\begin{align*}
{1\over(a-b)(a-c)} + {1\over(b-a)(b-c)} + {1\over(c-a)(c-b)} &= 0, \\[5pt]
{a\over(a-b)(a-c)} + {b\over(b-a)(b-c)} + {c\over(c-a)(c-b)} &= 0, \\[5pt]
{a^2\over(a-b)(a-c)} + {b^2\over(b-a)(b-c)} + {c^2\over(c-a)(c-b)} &= 1, \\[5pt]
{a^3\over(a-b)(a-c)} + {b^3\over(b-a)(b-c)} + {c^3\over(c-a)(c-b)} &= a+b+c.
\end{align*}$$

This appears as problem 1.2.3.33 of TAOCP, and it can be used as a lemma. For instance, one way to evaluate the Vandermonde determinant

$$\begin{vmatrix}
1 & x_1 & \cdots & x_1^{n-1} \\
1 & x_2 & \cdots & x_2^{n-1} \\
\vdots & \vdots & \ddots & \vdots \\
1 & x_n & \cdots & x_n^{n-1}
\end{vmatrix}$$

is via cofactor expansion along the last column, which yields the sum in the claim with $r=n-1$, times a factor of $\prod_{i<j}(x_i-x_j)$.

### The proof

Let $M=\max\\{\|x_1\|,\ldots,\|x_n\|\\}$ and $R>M$. The function

$$f(z)={1\over(z-x_1)\cdots(z-x_n)}$$

has a Laurent expansion $\sum_{m=-\infty}^\infty a_mz^m$ on the
annulus $M<|z|<\infty$. There are two ways of computing the Laurent
expansion: the first is to directly find each coefficient $a_m$ via
the expression

$$a_m = {1\over2\pi i}\oint_{|z|=R} {f(z)\over z^{m+1}}\,dz = {1\over2\pi i}\oint_{|z|=R}{1\over z^{m+1}(z-x_1)\cdots(z-x_n)}\,dz.$$

Actually, for our purposes it suffices to compute $a_m$ for $m\le -1$;
by the residue theorem this is equal to

$$\begin{equation}\label{eq1}\sum_{j=1}^n{x_j^{-m-1}\over\prod_{\substack{1\le k\le n\\ k\neq j}}(x_j-x_k)}\end{equation}$$

The other way is to rewrite

$$\begin{align*}
f(z) &= z^{-n}\left(1\over 1-x_1/z\right)\cdots\left(1\over 1-x_n/z\right) \\
&= z^{-n}\left(1+{x_1\over z}+{x_1^2\over z^2}+\cdots\right) \cdots \left(1+{x_n\over z}+{x_n^2\over z^2}+\cdots\right) \\
&= z^{-n} + z^{-n-1} \sum x_j + z^{-n-2} \sum(\text{degree 2 monomials}) + \cdots
\end{align*}$$

Since Laurent expansions are unique, we see that $a_{-n-k}$ is also
equal to the sum of the degree $k$ monomials (true for both positive
and negative $k$). The range $-n-1\le k\le 1$ for $k$ corresponds to
the range $0\le -m-1\le n$ for the exponent in \eqref{eq1}, from which
the result follows. By letting $k>1$ we obtain the value of the sum
for higher exponents for free. $\qed$

<br>

The above proof was what I came up with; Knuth's one is slightly
different. He instead works with the function

$$f(z)={z^r\over(z-x_1)\cdots(z-x_n)};$$

by the residue theorem, the integral

$${1\over2\pi i}\oint_{|z|=R}f(z)\,dz$$

is equal to the original sum with exponent $r$. The Laurent expansion
of the integrand is derived as above, except now the coefficient of
$z^{r-n-k}$ is the sum of the degree $k$ monomials. It converges
uniformly on the circle $|z|=R$, so we can integrate the Laurent
expansion term-by-term. Using the fact that the integral of $z^m$ is
$2\pi i$ for $m=-1$ and 0 otherwise, the integral evaluates to

$$z^{-1}\sum(\text{degree $r-n+1$ monomials}),$$

and we are done. This proof is not that much
different, because to show that Laurent expansions are unique also
involves this term-by-term integration argument.