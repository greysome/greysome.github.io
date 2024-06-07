# An alternative discriminant


Recall that if $f(x)\in F[x]$ has distinct roots $r_1,\ldots,r_n$ in a
splitting field, then the *discriminant* is defined to be

$$d = \prod_{i<j}\ (r_i-r_j)^2.$$

Since $d$ is fixed by all permutations of the roots, we have $d\in
F$. Furthermore, in characteristic $\neq2$[^1] we have

$$\sqrt d\in F \iff G_f\subset A_n.$$

There is an alternative definition that works for all
characteristics, namely

$$D' = \sum_{\pi\in A_n} r_{\pi(1)}{}^0 r_{\pi(2)}{}^1 \cdots
r_{\pi(n)}{}^{n-1}.$$

For $n=2$ and 3, the values of $D'$ are

$$r_2 \quad\text{and}\quad r_2r_3{}^2 + r_3r_1{}^2 + r_1r_2{}^2.$$

It is clear from the definition that $D'$ is fixed by all permutations
in $G_f\cap A_n$. It remains to show that these are precisely the
permutations fixing $D'$. To do that I'll introduce another number:

$$D'' = \sum_{\pi\in S_n\setminus A_n} r_{\pi(1)}{}^0 r_{\pi(2)}{}^1 \cdots
r_{\pi(n)}{}^{n-1}.$$

If $\sigma$ is an odd permutation, then clearly

$$\sum_{\pi\in A_n} r_{\sigma\pi(1)}{}^0 r_{\sigma\pi(2)}{}^1 \cdots
r_{\sigma\pi(n)}{}^{n-1} = D''.$$

Now, there are two different ways to evaluate the determinant of the
Vandermonde matrix

$$\begin{pmatrix}
1 & r_1 & r_1{}^2 & \cdots & r_1{}^{n-1} \\
1 & r_2 & r_2{}^2 & \cdots & r_2{}^{n-1} \\
& & & \vdots & \\
1 & r_n & r_n{}^2 & \cdots & r_n{}^{n-1} \\
\end{pmatrix}.$$

One is via a sum over all permutations and another is via the
well-known formula $\prod_{i<j}\ (r_i-r_j)$. Thus we have the identity

$$D'-D'' = \sqrt d.$$

But the RHS is $\neq0$ since the roots are distinct, and this implies
that odd permutations do not fix $D'$. Therefore, the permutations
fixing $D'$ are precisely $G_f\cap A_n$. So we can conclude that if
$D'\in F$, then $G_f\subset A_n$ since $G_f$ fixes $D'$. Otherwise
$G_f\not\subset A_n$.

How do we determine whether $D'\in F$? It is a root of the quadratic
$(x-D')(x-D'')$, which lies in $F[x]$ because its coefficients
$-D'-D''$ and $D'D''$ are fixed under all permutations. The roots lie
in $F$ only if the discriminant

$$(D'+D'')^2-4D'D'' = (D'-D'')^2$$

has square roots in $F$. But the RHS is simply $d$, which is the usual
discriminant. Thus, determining whether $D'\in F$ is just as hard as
determining whether $\sqrt d\in F$, so $D'$ doesn't have much
practical value. However, it is of theoretical interest as a
characteristic-agnostic alternative to $\sqrt d$.

[^1]: In characteristic 2 we always have $\sqrt d\in F$ since $d=\prod_{i<j}\ (r_i+r_j)$ is clearly fixed by every permutation.