---
layout: post
title: An interesting result on the entries of a matrix inverse
---

**Claim.** Let $M$ be an invertible $n\times n$ matrix which has a row or column of all 1s. Then the sum of entries in $M\inv$ is 1.

I find this quite surprising as an instance of how a 'global' property
of the matrix (its inverse), can be determined by a small number of
entries.

*Proof*. I'll illustrate the proof for a $3\times3$ matrix $M$; the general
case is the same idea. Let

$$M=\begin{pmatrix}a&b&c\\d&e&f\\g&h&i\end{pmatrix},\quad
M\inv=\begin{pmatrix}a'&d'&g'\\b'&e'&h'\\c'&f'&i'\end{pmatrix}\biggm/|M|.$$

Note the $(i,j)$ entry of the second matrix is the $(j,i)$ cofactor of
$M$. For instance, $d'=-\det(b\ c,h\ i)$. The sum of each column can be
expressed as a $3\times3$ determinant, as follows:

$$a'+b'+c'=\begin{vmatrix}1&1&1\\d&e&f\\g&h&i\end{vmatrix},\quad
d'+e'+f'=\begin{vmatrix}a&b&c\\1&1&1\\g&h&i\end{vmatrix},\quad
g'+h'+i'=\begin{vmatrix}a&b&c\\d&e&f\\1&1&1\end{vmatrix}.$$

The equalities hold via cofactor expansion along the rows of 1s. If
$M$ has a row of 1s, then only one of the above sums is nonzero, and
is in fact equal to $\det(M)$. Therefore, the sum of entries in
$M\inv$ is 1. If $M$ has a column of 1s, then we instead consider the
sums along the rows $a'+d'+g'$, $b'+e'+h'$, $c'+f'+i'$. $\qed$
