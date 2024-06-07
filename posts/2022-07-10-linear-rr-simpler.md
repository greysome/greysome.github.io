# A simpler way of solving linear recurrences


The standard method involves diagonalisation and Jordan normal form
(in the separable and non-separable case respectively). However a
problem sent by a friend in Discord prompted me to figure out a less
sophisticated but frankly more elegant and illuminating method.

Let

$$a_{n+k}=c_{k-1}a_{n+k-1}+c_{k-2}a_{n+k-2}+\ldots+c_0a_n$$

be our $k$th order homogeneous linear recurrence with complex
coefficients. A *solution* is simply taken to be a sequence $\{a_n\}$
satisfying the recurrence, and its first $k$ terms are the *initial
conditions*. Clearly every choice of initial conditions induces a
unique solution, and so we have an isomorphism of vector spaces

$$\begin{matrix}
T & : & \{\text{initial conditions}\} & \to & \{\text{solutions}\} \\
&& \cong & & \cong \\
&& \C^k & & \text{a subspace of $\C^\omega$}
\end{matrix}$$

(Crucially, the solutions form a vector space because the recurrence
is linear.) To solve the recurrence, we will find a convenient basis
$B$ of initial conditions whose solutions have a nice closed form, so
that by passage through $T$, every solution is a linear combination of
these closed forms.

### Separable case

Let $\lambda_1,\ldots,\lambda_k$ be the $k$ distinct roots of the charpoly

$$p(\lambda)=\lambda^k-c_{k-1}\lambda^{k-1}-\ldots-c_0.$$

For each $\lambda_i$ we can generate the initial condition
$(1,\lambda_i,\cdots,\lambda_i^{k-1})$, whose image under $T$ is the
sequence $\{\lambda_i^n\}$ (since successive powers of $\lambda_i$
always satisfy the recurrence). Furthermore these $k$ initial
conditions form a basis since the determinant of the corresponding
Vandermonde matrix

$$\begin{pmatrix}
1 & \lambda_1 & \cdots & \lambda_1^{k-1} \\
1 & \lambda_2 & \cdots & \lambda_2^{k-1} \\
& & \vdots & \\
1 & \lambda_k & \cdots & \lambda_k^{k-1} \\
\end{pmatrix}$$

is nonzero. Thus every solution $\{a_n\}$ has the form

$$a_n = A_1\lambda_1^n+\ldots+A_k\lambda_k^n.$$

I love this proof more than the diagonalisation proof because it makes
the role of the charpoly transparent: their roots just happen to
provide the simplest closed-form solutions.

### Non-separable case

Let $\lambda_1,\ldots,\lambda_l$ be the roots with multiplicities
$m_1,\ldots,m_l$. Unfortunately the $l$ initial conditions
$(1,\lambda_i,\ldots,\lambda_i^{k-1})$ are not enough to form a basis,
so we need to find more initial conditions with easy-to-express
solutions. This is done by considering successive derivatives of
$p(\lambda)$, courtesy of the following result which is given without
proof.

**Lemma.** If $\lambda$ is a root of $p$ with multiplicity $m$, then
  $\lambda$ is also a root of
  $p'(\lambda)$, $p''(\lambda)$, $\ldots$ , $p^{(m-1)}(\lambda)$.

So for each root $\lambda_i$, we can generate $m_i-1$ more initial
conditions by multiplying the equation
$\lambda_i^k=c_{k-1}\lambda_i^{k-1}+\ldots+c_0$ by powers of
$\lambda_i$ and then differentiating up to $m-1$ times:

$$\begin{align*}
\lambda_i^{k+n}&=c_{k-1}\lambda_i^{k+n-1}+c_{k-2}\lambda_i^{k+n-2}+\ldots+c_1\lambda_i^{n+1}+c_0\lambda_i^n, \\
(k+n)\lambda_i^{k+n-1}&=c_{k-1}\bigl((k+n-1)\lambda_i^{k+n-2}\bigr)+c_{k-2}\bigl((k+n-2)\lambda_i^{k+n-3}\bigr)+\ldots \\
&\qquad+c_1\bigr((n+1)\lambda_i^n\bigr)+c_0(n\lambda_i^{n-1}), \\
(k+n)(k+n-1)\lambda_i^{k+n-2}&=c_{k-1}\bigl((k+n-1)(k+n-2)\lambda_i^{k+n-3}\bigr)+c_{k-2}\bigl((k+n-2)(k+n-3)\lambda_i^{k+n-4}\bigr)+\ldots \\
&\qquad+c_1\bigr((n+1)n\lambda_i^{n-1}\bigr)+c_0(n(n-1)\lambda_i^{n-2}), \\
&\vdots
\end{align*}$$

Thus we see that the initial conditions

$$\begin{align*}
&(1,\ \lambda_i,\ \lambda_i^2,\ \ldots,\  \lambda_i^{k-1}), \\
&(1,\ 2\lambda_i,\ 3\lambda_i^2,\ \ldots,\  k\lambda_i^{k-1}), \\
&(2,\ 6\lambda_i,\ 12\lambda_i^2,\ \ldots,\ k(k+1)\lambda_i^{k-1}), \\
&(6,\ 24\lambda_i,\ 60\lambda_i^2,\ \ldots,\ k(k+1)(k+2)\lambda_i^{k-1}), \\
&\qquad\vdots \\
&\bigl((m_i-1)!,\ {m_i!\over1!}\lambda_i,\ {(m_i+1)!\over2!}\lambda_i^2,\ \ldots,\ {(m_i+k-2)!\over(k-1)!}\lambda_i^{k-1}\bigr)
\end{align*}$$

correspond to the solutions

$$\bigl\{\lambda_i^n\bigr\},\;\bigl\{(n+1)\lambda_i^n\bigr\},\;\bigl\{(n+1)(n+2)\lambda_i^n\bigr\},\;\ldots,\;\bigl\{(n+1)(n+2)\cdots(n+m_i-1)\lambda_i^n\bigr\}.$$

So each root $\lambda_i$ generates $m_i$ initial conditions, and we have a tentative basis of $k$ elements. We just need to show that it is linearly independent to conclude that every solution has the form

$$\begin{matrix}
a_n & = & A_{1,1}\lambda_1^n & + & A_{1,2}(n+1)\lambda_1^n & + & \cdots & + & A_{1,m_1}(n+1)\cdots(n+m_1-1)\lambda_1^n \\
& + & A_{2,1}\lambda_2^n & + & A_{2,2}(n+1)\lambda_2^n & + & \cdots & + & A_{2,m_2}(n+1)\cdots(n+m_2-1)\lambda_2^n \\
& + & \cdots \\
& + & A_{l,1}\lambda_l^n & + & A_{l,2}(n+1)\lambda_l^n & + & \cdots & + & A_{l,m_l}(n+1)\cdots(n+m_l-1)\lambda_l^n
\end{matrix}$$

So far I have been unable to prove linear independence in full
generality; the main difficulty comes from handling roots with the
same argument. In certain special cases however the proof is not too
hard[^1]:

**Proposition.** If $P_1,\ldots,P_l$ are polys and
  $|\lambda_1|<|\lambda_2|<\ldots<|\lambda_l|$ are complex numbers,
  then the sequences $\{P_i(n)\lambda_i^n\}$ are linearly
  independent. (Since the polys $1,\ n+1,\ (n+1)(n+2),\ \ldots$ are
  linearly independent, this implies the $k$ initial conditions form a
  basis.)

*Proof.* Since polynomials are closed under multiplication by constants, it suffices to prove that the sum $\sum_i P_i(n)\lambda_i^n$ is always a nonzero sequence. WLOG we can assume $P_l(n)\neq0$; for sufficiently large $n$ we have

$$\begin{align*}
|P_l(n)\lambda_l^n|&> c(l-1)|\lambda_l^n|\quad\text{for some constant $c>0$} \\
&=c|\lambda_1|^n\left|\lambda_l\over\lambda_1\right|^n+\ldots+c|\lambda_{l-1}|^n\left|\lambda_l\over\lambda_{l-1}\right|^n \\
&>c|\lambda_1|^n\left|P_1(n)\over c\right|+\ldots+c|\lambda_{l-1}|^n\left|P_{l-1}(n)\over c\right|\quad\text{since $\lambda_i/\lambda_1>1$ for $1\le i<l$} \\
&=|P_1(n)\lambda_1^n|+\ldots+|P_{l-1}(n)\lambda_{l-1}^n| \\
&\ge|P_1(n)\lambda_1^n+\ldots+P_{l-1}(n)\lambda_{l-1}^n|.
\end{align*}$$

Therefore, $-P_l(n)\lambda_l^n\neq
P_1(n)\lambda_1^n+\ldots+P_{l-1}(n)\lambda_{l-1}^n$ for sufficiently
large $n$. $\qed$

[^1]: The proof is highly reminiscent about a result I proved back in January about my so-called "strongly dominating chains" while finding the transcendence degree of $\hR/\R$.