---
layout: post
title: Certain maximal subgroups of $S_n$
---

The O'Nan-Scott theorem classifies the maximal subgroups of $S_n$ into
6 types. I will only talk about 3 of them, because I haven't fully
understood the rest.

### Intransitive subgroup

If $H$ is an intransitive subgroup of $S_n$, then it has at least two
orbits with sizes $n_1,\ldots,n_k$. Then $H$ is a subgroup of
$S_{n_1}\times\cdots\times S_{n_k}$. If $k>2$, then $H$ is not maximal
because $S_{n_1}\times\cdots\times S_{n_k}$ is a subgroup of
$S_{n_1}\times S_{n_2+\ldots+n_k}$, which mixes up all but the first
orbit. If $k=2$ then maximality depends on whether $n_1=n_2$. If
$n_1=n_2$ then $S_{n_1}\times S_{n_2}$ is not maximal because it is
contained in $S_{n_1}\wr S_2$ (in fact, this is how the next type of
maximal subgroups is constructed). On the other hand:

**Proposition.** If $n=n_1+n_2$ and $n_1\neq n_2$, then $S_{n_1}\times
  S_{n_2}$ is maximal in $S_n$.

*Proof.* I show that if $K$ properly contains $S_{n_1}\times S_{n_2}$
 then $K$ contains all transpositions and so $K=S_n$.

Assume WLOG that $n_1<n_2$ and the orbits are $\Omega_1,\Omega_2$. If
$g\in K\setminus S_{n_1}\times S_{n_2}$, then $g$ maps some point from
$\Omega_2$ into $\Omega_1$ but not all of $\Omega_2$. Choose
$i,j\in\Omega_2$ such that $g$ maps $i$ into $\Omega_1$ while mapping
$j$ into $\Omega_2$. Conjugating the transposition $(ij)$ by $g$
yields another transposition $h\in K$ that acts across orbits (see
Figure 1). In turn, conjugating $h$ by a suitable element of
$S_{n_1}\times S_{n_2}$ yields all the transpositions across both
orbits. Since $S_{n_1}\times S_{n_2}$ (and thus $K$) also contains
transpositions within orbits, it follows that $K$ contains all
transpositions and so $K=S_n$. $\qed$

{% include figure.html src="orbit-conjugation.svg"
alt=""
figno=1
caption="How to obtain $h$" %}

As an example, the intransitive maximal subgroups of $S_6$ are
$S_2\times S_4$ and $S_5$.

### Transitive imprimitive subgroups

The next class of subgroups have the form $S_k\wr S_m$ where
$n=km$. Given a partition of $\\{1,\ldots,n\\}$ into $m$ subsets of size
$k$, the base group $S_k\times\cdots\times S_k$ permutes
*within* subsets whereas the $S_m$ permutes the subsets
themselves. Besides being transitive, this action can also be
described as *imprimitive*: there is a nontrivial partition of
$\\{1,\ldots,n\\}$ that is preserved by the action of $S_k\wr S_m$,
namely the aforementioned partition into $m$ subsets. On the other
hand, a *primitive* subgroup of $S_n$ preserves only trivial
partitions: namely the partition into singletons and the partition
consisting of just the set itself.

**Propoition.** If $n=km$ then $S_k\wr S_m$ is maximal in $S_n$.

*Proof.* Same argument as above. I show if $K$ properly contains
 $S_k\wr S_m$ then $K$ contains all transpositions and so $K=S_n$.

Choose some $g\in K\setminus S_k\wr S_m$. Since $g$ doesn't preserve
the partition into $m$ size-$k$ subsets $\Omega_1,\ldots,\Omega_m$,
there is some $\Omega_k$ and some $i,j\in\Omega_k$ such that $g$ maps
$i$ to another subset while mapping $j$ within $\Omega_k$. Conjugating
the transposition $(ij)$ by $g$ yields another transposition $h\in K$
across subsets, and conjugating $h$ by a suitable element of $S_k\wr
S_m$ yields all the transpositions across subsets. Since $S_k\wr S_m$
(and hence $K$) also contains all transpositions within subsets, $K$
contains all transpositions and so $K=S_n$. $\qed$

For example, the transitive imprimitive subgroups of $S_6$ are $S_3\wr
S_2$ and $S_2\wr S_3$. Note that they are not isomorphic!

### Primitive wreath products

I first consider the special case of 2 dimensions. If $n=k^2$, then
arrange the elements of $\\{1,\ldots,n\\}$ into a $k\times k$ matrix
$M$. A copy of $S_k$ acts by permuting columns, whereas another copy
of $S_k$ acts by permuting rows. Combining these two actions yields
the subgroup $S_k\times S_k$; note it is imprimitive because it
preserves the partition into columns, as well as the partition into
rows. However, we can form a primitive subgroup by adding the
permutation that reflects about the main diagonal, i.e. it maps
$M_{ij}\mapsto M_{ji}$. This primitive group is a wreath product
$S_k\wr S_2$, but it is different in nature from the transitive
imprimitive wreath product explained above, where $n=2k$.

The idea can be generalised to $m$ dimensions: if $n=k^m$, then
arrange $\\{1,\ldots,n\\}$ into a $k\times\cdots\times k$
multidimensional array. Then the primitive wreath product $S_k\wr S_m$
acts on this array: the base group $S_k\times\cdots\times S_k$
permutes elements within each coordinate, while $S_m$ permutes the
coordinates themselves. It turns out there is this result, which I
haven't read the proof of yet.

**Proposition.** The primitive wreath product $S_k\wr S_m$ is maximal
  in $S_n$ if $k\ge 5$ and $4\nmid k^{m-1}$.

### Mini exercises

1. Is the action of $D_8$ on 4 points primitive?
2. Describe the maximal subgroup that preserves a given partition of
$\\{1,\ldots,n\\}$ into subsets of arbitrary sizes.
3. Convince yourself that the primitive wreath product $S_k\wr S_2$
really is primitive.