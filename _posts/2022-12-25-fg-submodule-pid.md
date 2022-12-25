---
layout: post
title: Characterising submodules of finitely generated torsion modules over a PID
---

A previous post characterised the quotient modules. It turns out that
submodules admit the exact same characterisation---the proof is
different but it still shares some elements. I'll refer to the other
post as QUOT.

**Proposition.** Any submodule of $M\cong \bigoplus_i D/(d_i)$ has the
  form $\bigoplus_i D_i$, where each $D_i$ is a submodule of
  $D/(d_i)$.

*Proof.* I handle the primary case first. Then

$$M\cong \bigoplus_{i=1}^n D/(p^{e_i}).$$

If $N$ is a submodule then it is also $p$-primary and

$$N\cong \bigoplus_{j=1}^m D/(p^{f_j}).$$

Using the padding trick in QUOT, we can assume that $m=n$. Let

$$l=\max\,\{e_i\},\quad l'=\max\,\{f_j\}.$$

I showed in QUOT that $l'\le l$, and thus $p^{l-l'}M$ is
well-defined. The annihilator of $N$ is $(p^{l'})$, and $p^{l-l'}M$ is
the largest submodule of $M$ whose annihilator is $(p^{l'})$.[^1] Thus
$N$ is a submodule of $p^{l-l'}M$, whose largest invariant factor is
$p^{l'}$. In other words, the maximum components of the tuples
corresponding to $N$ and $p^{l-l'}M$ are both $l'$.

If $N>p^{l-l'}M$ as tuples, then there is some $k$ such that the tuple
$p^kN$ has more nonzero components than $p^{l-l'+k}M$. For example, if

$$N = (4,3,3,1),\quad p^{l-l'}M = (4,3,2,1),$$

then

$$p^2N = (2,1,1,0),\quad p^{l-l'+2}M = (2,1,0,0).$$

Let $r$ and $s$ be the number of nonzero components in $p^kN$ and
$p^{l-l'+k}M$ respectively. Then $p^kN$ contains the vector space
$\bigl(D/(p)\bigr)^r$ and $p^{l-l'+k}M$ contains the vector space
$\bigl(D/(p)\bigr)^s$; by the same argument concluding that $N\le
p^{l-l'}M$, we conclude that

$$\bigl(D/(p)\bigr)^r \quad\text{embeds into}\quad \bigl(D/(p)\bigr)^s.$$

But this is impossible since $r>s$, and thus $N\le p^{l-l'}M\le M$,
proving the primary case.

In the general case, consider the decompositions

$$M = \bigoplus_i M_{p_i},\quad N = \bigoplus_i N_{p_i}.$$

Since $M_{p_i}$ is the largest submodule of $M$ whose annihilator is
contained in $(p_i)$, we have $N_{p_i}\subseteq M_{p_i}$ as
submodules. Thus $N_{p_i}\le M_{p_i}$ as tuples, completing the
proof. $\qed$

[^1]: In the case $D=\Z$, this is a simple argument about orders.