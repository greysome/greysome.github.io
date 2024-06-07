# Characterising quotients of finitely generated torsion modules over a PID


Let $M$ be a finitely generated torsion module over a PID $D$. Then by
the structure theorem we have

$$M\cong \bigoplus_{i=1}^n D/(d_i),\quad\text{$d_i$ prime and $d_i\mid d_{i+1}$.}$$

**Proposition.** Any quotient of $M$ has the form $\bigoplus_i D_i$,
  where each $D_i$ is a submodule of $D/(d_i)$.

*Proof.* The bulk of the proof happens in the case where $M$ is
primary, which I'll first deal with. Then the $d_i$'s are all powers
$p^{e_i}$ of some fixed prime $p$, and $e_i\le e_{i+1}$. We can view
$M$ as a tuple $(e_1,\ldots,e_n)$.

Let $N\cong M/M'$ be any quotient. Then $N$ is also a $p$-primary
module, and admits a similar decomposition $N\cong \bigoplus_{j=1}^m
D/(p^{f_j})$, where $f_j\le f_{j+1}$. We can also treat $N$ as a
tuple $(f_1,\ldots,f_m)$. Now, the argument would be greatly
expedited if $m=n$; so if for instance $n>m$, then I will instead
consider the decomposition

$$N\cong \bigoplus_{j=1}^n D/(p^{f_j}),\quad\text{$f_j=0$ for $m<j\le n$.}$$

Likewise if $m>n$[^1], then I consider the decomposition

$$M\cong \bigoplus_{i=1}^m D/(p^{e_i}),\quad\text{$e_i=0$ for $n<i\le m$.}$$

Identifying $M$ and $N$ with their respective tuples, this corresponds
to padding the shorter tuple with 0s to make them equal length. I
would like to reiterate that identifying $p$-primary modules with
tuples is possible because of the uniqueness of the decomposition
(modulo the extra 0s).

From now I'll assume that $m=n$. Then what we want to prove is that

$$(f_1,\ldots,f_n)\le(e_1,\ldots,e_n),\quad\text{i.e. $f_i\le e_i$ for all $i$.}$$

For example, if $M=\Z/(p)\oplus\Z/(p^2)$, then the only nontrivial
possibilities for $N$ are

$$\Z/(p)\oplus\Z/(p),\quad \Z/(p^2)\cong\Z/(1)\oplus\Z/(p^2),\quad \Z/(p)\cong\Z/(p)\oplus\Z/(1).$$

Let us proceed with the proof. The idea is that certain operations on
$p$-primary modules can be interpreted in terms of tuples:

1. $p^kM$ is the module $\bigoplus_i D/(p^{e_i-k})$. Thus it is
represented by the tuple $(e_1-k,\ldots,e_n-k)$[^2].

2. $p^kM/p^{k+1}M$ is the module

   $$\bigoplus_i D/(p^{(e_i-k)-(e_i-k-1)}) = \bigoplus_i D/(p^{[e_i>k]}),$$

   where the latter expression uses Iverson bracket notation. Note
   that it is always $\le(1,1,\ldots,1)$, and this implies that
   $p^kM/p^{k+1}M$ is a direct sum of $D/(p)$'s, and the number of
   nonzero summands is the dimension (as a vector space) over the
   field $D/(p)$.

We can go a step further. By identifying modules with tuples, we have
the identity $p^kM = p^kM/p^{k+1}M + p^{k+1}M$. By induction we thus
have the wonderful expression

$$M = M/pM + pM/p^2M + \ldots + p^{l-1}M/p^lM,\quad l=\max\,\{e_i\}.$$

Now let $l'=\max\,\\{f_j\\}$; there exists $x\in M$ with
$\ann(x+M')=(p^{l'})$. Then

$$\ann(x+M')\supseteq \ann x\ge (p^l),$$

and thus $l'\le l$[^3]. The rest of the proof boils down to the
calculation

$$\begin{align*}
N &= N/pN + \ldots + p^{l'-1}N/p^{l'}N \\
&\le M/pM + \ldots + p^{l'-1}M/p^{l'}M + \ldots + p^{l-1}M/p^lM \\
&= M.
\end{align*}$$

We just need to show the

**Lemma.** $p^kN/p^{k+1}N$ is a quotient of $p^kM/p^{k+1}M$. Thus

$$\dim_{D/(p)} p^kN/p^{k+1}N \le \dim_{D/(p)} p^kM/p^{k+1}M,$$

and so

$$p^kN/p^{k+1}N \le p^kM/p^{k+1}M\ \ \text{as tuples.}$$

*Proof.* Suppose $N\cong M/M'$. We have the isomorphism $p^kN\cong
p^kM/(p^kM\cap M')$ by applying the 1st iso theorem to the map

$$\begin{matrix}
p^kM & \to & p^kN \\
m & \mapsto & \overline{m}.
\end{matrix}$$ 

The rest is just spamming the isomorphism theorems:

$$\begin{align*}
p^kN/p^{k+1}N &\cong {p^kM/(p^kM\cap M') \over p^{k+1}M/(p^{k+1}M\cap M')} \\
&\cong {p^kM/(p^kM\cap M') \over [p^{k+1}M+(p^kM\cap M')]/(p^kM\cap M')}
\quad\text{(2nd iso theorem on $p^{k+1}M$ and $p^kM\cap M'$)}\\
&\cong {p^kM \over [p^{k+1}M+(p^kM\cap M')]} \\
&\cong {p^kM/p^{k+1}M \over [p^{k+1}M+(p^kM\cap M')]/p^{k+1}M}.\quad\qed \\
\end{align*}$$

This completes the proof for primary modules. In the general case,
consider the decomposition of $M$ into primary components, $M\cong
\bigoplus_i M_{p_i}$. Let $l_1,\ldots,l_n$ be the maximum
multiplicities of each prime. For each $M'$, we have that

$${p_2}^{l_2}\cdots{p_n}^{l_n}(M/M') \cong (M/M')_{p_1}$$

but this is also isomorphic to the quotient

$${p_2}^{l_2}\cdots{p_n}^{l_n}M / ({p_2}^{l_2}\cdots{p_n}^{l_n}M\cap M') \cong M_{p_1}/(M_{p_1}\cap M').$$

Thus we can apply the previous part of the proof to conclude
$(M/M')\_{p_1}\le M\_{p\_1}$ as tuples. Similarly, $(M/M')\_{p\_k}\le
M\_{p\_k}$ for each $k$, and a moment's reflection should convince the
reader that this implies the original proposition. $\qed$

[^1]: It turns out that $m\le n$ always, but we don't know that at this juncture.
[^2]: Here $a-b$ is defined as 0 if $a<b$, and the usual difference otherwise.
[^3]: This is obvious in the case $D=\Z$: here $l$ denotes the maximum order of an element, and clearly passage to the quotient cannot increase the order.