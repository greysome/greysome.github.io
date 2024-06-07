# Real Jordan form and complexification

First, a recap of the usual Jordan form. Consider a complex vector
space $V$ and a linear map $\l$ on it, such that $V$ is a
$\C[\l]$-module in the obvious way. Since $\C$ is algebraically
closed, the elementary factors of $V$ have the form $(\l-\a)^k$, so

$$V \cong \bigoplus_i \C[\l]/(\l-\a_i)^{k_i}.$$

The point of Jordan form is that each $\l$-span
$\C[\l]/(\l-\a_i)^{k_i}$ admits a basis

$$\{1,\ \l-\a_i\,, \ldots,\ (\l-\a_i)^{k_i-1}\}$$

that satisfies the simple relations

$$\l(\l-\a_i)^k = \a_i(\l-\a_i)^k+(\l-\a_i)^{k+1}.$$

Thus the action of $\l$ on this $\l$-span can be represented by the
matrix

$$\begin{pmatrix}
1 & \a_i & & & \\
& 1 & \a_i & & \\
& & \ddots & & \\
& & & 1 & \a_i \\
& & & & 1
\end{pmatrix}$$

As a whole, the matrix of $\l$ can be represented as a direct sum of
these Jordan blocks.

It turns out that we can get something close to Jordan form when
working purely in $\R$. So now suppose $V$ is a real vector space and
the linear map $\l$ induces an $\R[\l]$-module structure. The key fact
is that all irreducibles in $\R[\l]$ are either linears or
quadratics. Therefore, in the elementary factor decomposition of $V$,
each direct summand is either

$$\R[\l]/(\l-\a)^k \quad\text{or}\quad \R[\l]/(\l^2-\a\l-\b)^k,
\quad\text{$\l^2-\a\l-\b$ irreducible.}$$

If the former, we already know from the above discussion that there is
a nice matrix form on that $\l$-span. So it is the latter case that is
new.

This is where the magic of complexification comes in. Suppose $V$ is
the $\l$-span $\R[\l]/(\l^2-\a\l-\b)^k$. The idea is that we make $V$
into a complex vector space

$$V^\C \cong \C[\l]/(\l^2-\a\l-\b)^k,$$

and by CRT $V^\C$ splits into two 'nice' $\l$-spans $\C[\l]/(\l-\g)^k$
and $\C[\l]/(\l-\ol\g)^k$, where $\g,\ol\gamma$ are the roots to
$\l^2-\a\l-\b$. By the above discussion we have two nice sets of
*complex* bases $\\{\v_1,\ldots,\v_k\\}$ and $\\{\w_1,\ldots,\w_k\\}$
for each of the summands, which we then use to obtain a *real* basis
$\\{v_1',\ldots,v_{2k}'\\}$ under which $\l$ has a nice matrix form.

Usually $V^\C$ is straightaway defined as the scalar extension
$\C\otimes_\R V$, but it might be more illuminating to list out the
properties that we want $V^\C$ to satisfy, and then prove
$\C\otimes_\R V$ is indeed a model (which I'll leave as an
exercise). So, $V^\C$ should satisfy these very reasonable properties:

1. Elements of $V^\C$ can be written in the form $v+wi$ where $v,w\in
   V$. There is an embedding $V\hookrightarrow V^\C$ mapping $v\mapsto
   v+0i$.

2. Addition is defined in the obious way. Scalar multiplication is
   defined by the formula

   $$(a+bi)(v+wi) = (av-bw)+(aw+bv)i, \quad a,b\in\R.$$

3. A linear map $\l$ on $V$ extends to a map on $V^\C$ by the formula

   $$\l(v+wi) = \l v + (\l w)i.$$

Now we establish some basic facts about $V^\C$.

**Proposition 1.** A basis $\\{v_1,\ldots,v_n\\}$ is also a basis for
  $V^\C$.

*Proof.* If $\sum_k (a_k+b_ki)(v_k+0i) = 0$ then $(\sum_k a_kv_k) +
 (\sum_k b_kv_k)i = 0$, so $\sum_k a_kv_k=\sum_k b_kv_k=0$ and thus
 $a_k=b_k=0$ for all $k$. Thus linear independence is preserved.

 If $v,w\in V$ then $v=\sum_k a_kv_k$ and $w=\sum_k b_kv_k$, so

 $$\begin{align*}
 v+wi &= \sum_k a_kv_k + \left(\sum_k b_kv_k\right)i \\
 &= \sum_k a_kv_k + \left(\sum_k b_ki\cdot v_k\right) \\
 &= \sum_k (a_k+b_ki)v_k,
 \end{align*}$$

so $v_1,\ldots,v_n$ span $V^\C$ as well. $\qed$

**Proposition 2.** The extension of $\l:V\to V$ to $V^\C$ as defined
  above is automatically $\C$-linear. Furthermore it satisfies

  $$\ol{\l(v+wi)} = \l(\ol{v+wi}) = \l(v-wi).$$

*Proof.* Additivity is trivial. And we have

$$\begin{align*}
(a+bi)\l(v+wi) &= (a+bi)\bigl(\l(v)+\l(w)i\bigr) \\
&= \bigl(a\l(v)-b\l(w)\bigr)+\bigl(a\l(w)+b\l(v)\bigr)i \\
&= \l(av-bw)+\l(aw+bv)i \\
&= \l\bigl((av-bw)+(aw+bv)i\bigr) \\
&= \l\bigl((a+bi)(v+wi)\bigr).
\end{align*}$$

As for the second claim, let $v_1,\ldots,v_n$ be a basis for
$V$. Since elements of $V$ are self-conjugate we have

$$\ol{\l v_i} = \l v_i = \l\ol{v_i}.$$

By proposition 1, the $v_i$'s also form a basis of $V^\C$, so it
suffices to prove that linear combinations preserve the equality
between the first and third terms. This is pure calculation:

$$\begin{align*}
\ol{\l\left(\sum_k (a_k+b_ki)v_k\right)}
&= \ol{\sum_k (a_k+b_ki)\l v_i} \\
&= \sum_k \ol{a_k+b_ki}\cdot\ol{\l v_i} \\
&= \sum_k \ol{a_k+b_ki}\ \l\ol{v_i} \\
&= \l\left(\ol{\sum_k (a_k+b_ki)v_k}\right).\ \qed
\end{align*}$$


Proposition 1 is very important, because if $M$ is the matrix
representing $\l$ in $V$, then we can also use $M$ to represent $\l$
in $V^\C$! Thus, the characteristic polynomial of $\l$ in $V^\C$ is
also $(\l^2-\a\l-\b)^k$, but this time it splits into linear
factors. Therefore,

$$V^\C \cong \C[\l]/(\l^2-\a\l-\b)^k \cong \C[\l]/(\l-\g)^k \oplus
\C[\l]/(\l-\ol\g)^k.$$

Put in words, the complexification of the real $\l$-span splits into
two 'nice' complex $\l$-spans. Thus we have two separate (complex) bases
$\\{\v_1,\ldots,\v_n\\}$ and $\\{\w_1,\ldots,\w_n\\}$ such that

$$\begin{align*}
\l \v_k &= \g\,\v_k + \v_{k+1}, \\
\l \w_k &= \ol\g\,\w_k + \w_{k+1}.
\end{align*}$$

But conjugating the first equation yields

$$\l\ol{\v_k} = \ol\gamma\,\ol{\v_k} + \ol{\v_{k+1}},$$

meaning that given the basis $\\{\v_k\\}$, we can in fact choose
$\w_k=\ol{\v_k}$! Now define the real vectors

$$v_k' = {1\over2}(\v_k+\ol{\v_k}),\quad w_k' = {1\over2}(\v_k-\ol{\v_k}).$$

Note that $v_k'$ and $w_k'$ are simply the real and imaginary parts of
$\v_k$. The corresponding relations matrix has the block form

$$\begin{pmatrix}
1/2 & 1/2 & & \\
1/2 & -1/2 & & \\
& & 1/2 & 1/2 & \\
& & 1/2 & -1/2 & \\
&&&& \ddots
\end{pmatrix},$$

which has nonzero determinant and is hence invertible. Thus the
$v_k'$'s and $w_k'$'s together form a real basis for $V^\C$. Now let
$\g=a+bi$. Since $\v_k = v_k'+w_k'i$, we can deduce the relations

$$\begin{align*}
\l v_k' &= \Re \l \v_k \\
&= \Re(\g\v_i + \v_{k+1}) \\
&= \Re\bigl((a+bi)(v_k'+w_k'i)\bigr) + v_{k+1}' \\
&= av_k'-bw_k'+v_{k+1}'.
\end{align*}$$

Similarly,

$$\l w_k' = bv_k'+aw_k'+w_{k+1}'.$$

Thus the matrix of $\l$ wrt the $v_k'$'s and $w_k'$'s has the block
form

$$\begin{pmatrix}
a & -b & 1 & &&&&&& \\
b & a & & 1 &&&&&& \\
&& a & -b & 1 &&&&& \\
&& b & a & & 1 &&&& \\
&&&& \ddots &&&&& \\
&&&&&& a & -b & 1 & \\
&&&&&& b & a & & 1 \\
&&&&&&&& a & -b \\
&&&&&&&& b & a
\end{pmatrix}$$

I'll call this a *real Jordan block*. Thus, any linear map on a real
vector space can be represented by a diagonal block matrix, where each
block is either a usual Jordan block or a real Jordan block.

### Addendum

I discovered a matrix form slightly different from the real Jordan
block. This form is obtained by considering the basis

$$\{p(\l), \l p(\l), p(\l)^2, \l p(\l)^2, \ldots\}$$

of $\R[\l]/p(\l)^k$, where $p(\l)=\l^2-\a\l-\b$ is an irreducible
quadratic. Since

$$\l^2 p(\l)^i = -\b\ p(\l)^i - \a\l p(\l)^i + p(\l)^{i+1},$$

the matrix of $\l$ on this $\l$-span, wrt this basis, has the form

$$\begin{pmatrix}
0 & 1 & 0 & 0 &&&&&& \\
-\b & -\a & 1 & 0 &&&&&& \\
&& 0 & 1 & 0 & 0 &&&& \\
&& -\b & -\a & 1 & 0 &&&& \\
&&&& \ddots &&&&& \\
&&&&&& 0 & 1 & 0 & 0 \\
&&&&&& -\b & -\a & 1 & 0 \\
&&&&&&&& 0 & 1 \\
&&&&&&&& -\b & -\a
\end{pmatrix},$$

composed of the subblocks

$$\begin{pmatrix} 0 & 1 \\ -\b & -\a\end{pmatrix}
\quad\text{and}\quad
\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}.$$