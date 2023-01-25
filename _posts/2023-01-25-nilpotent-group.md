---
layout: post
title: Nilpotent groups and central series
---
A *central series* for a group $G$ is a sequence of normal subgroups

$$1 = G_1 \subset G_2 \subset \cdots \subset G_n = G$$

such that $G_{i+1}/G_i \subset Z(G/G_i)$. $G$ is *nilpotent* if it admits
a central series. Recall that $G$ being solvable (i.e. admitting a
normal series with abelian factors) is equivalent to a special normal
series called the derived series $G \supset G' \supset G'' \supset \cdots$
eventually reaching 1. Likewise, $G$ being nilpotent is equivalent to
any one of two special central series terminating. The first is the
*lower central series* $G^1\supset G^2\supset \cdots$, defined by

$$G^1=G,\quad G^{i+1}=(G^i,G).$$

To prove it is indeed a central series we need to prove three things:
$G^i\normal G$, $G^{i+1}\subset G^i$ and $G^i/(G^i,G)\subset
Z(G/(G^i,G))$. The first follows by induction: supposing $G^i\normal
G$ we have

$$g(G^i,G)g\inv \subset (gG^ig\inv, gGg\inv) \subset (G^i,G)\quad
\text{for all $g\in G$}.$$

The second fact follows from the first, because given $h\in G^i$ and
$g\in G$ we have $gh\inv g\inv\in G^i$ and so

$$(h,g) = h(gh\inv g\inv)\in G^i.$$

The last follows from a more general observation which characterises
subgroups of the form $(H,G)$. In fact, it generalises the
characterisation of $G'$ as the smallest normal subgroup yielding an
abelian quotient.

**Proposition 1.** Let $H,N\normal G$, and $H/N$ denote the image of
  $H$ under the projection $G\to G/N$. (Think of $G\Normal H$ as fixed
  and $N$ as varying.) Then

  $$H/N\subset Z(G/N) \iff (H,G)\subset N.$$

*Proof.* Note that $(H,G)\normal G$ has been shown above, in the
 context $H=G^i$. The proof is just definition-chasing:

$$\begin{align*}
H/N \subset Z(G/N) &\iff (hN)(gN)=(gN)(hN)\ \text{for all $h\in H, g\in G$} \\
&\iff (hN,gN) = 1 \\
&\iff (h,g)\in N \\
&\iff (H,G)\subset N.\ \qed
\end{align*}$$

This result justifies the descriptor 'lower', since by the proposition
$(G^i,G)$ is the smallest subgroup $N$ satisfying the property $G/N\subset
Z(G/N)$. Next we have the *upper central series* $C_1\subset
C_2\subset\cdots$, defined upwards by

$$C_1=1,\quad C_{i+1}\ \text{is the unique subgroup $\supset C_i$ satisfying $C_{i+1}/C_i=Z(G/C_i)$}.$$

In particular, $C_2=Z(G)$. It is quite easy to see why this series is
given the descriptor 'upper'. The conditions $C_i\subset C_{i+1}$,
$C_{i+1}/C_i\subset Z(G/C_i)$ are satisfied by definition, and we have
$C_{i+1}\normal G$ since $C_{i+1}$ is the kernel of a certain map
$G\to (G/C_i)/(C_{i+1}/C_i)$.

I now prove that $G$ being nilpotent is equivalent to either the lower
central series terminating at 1, or the upper central series
terminating at $G$.

**Proposition 2.** $G$ nilpotent $\iff$ lower central series terminates.

*Proof.* Backward direction is trivial. As for the forward direction,
 let $G=G_1\supset G_2\supset \cdots \supset G_n=1$ be a central series. I'll show
 by induction that $G^i\subset G_i$ for all $i$. Suppose this is the case
 for some $i$. Then $G\supset G_i\supset G_{i+1}$ is a tower of normal
 subgroups satisfying $G_i/G_{i+1}\subset Z(G/G_{i+1})$, and so by
 Proposition 1 we have $G_{i+1}\supset(G_i,G)$, and by the induction
 hypothesis we can conclude $G_{i+1}\supset (G_i,G)\supset (G^i,G) =
 G^{i+1}$. $\qed$

**Proposition 3.** Lower central series terminates $\iff$ upper central series terminates.

*Proof.* Backward direction follows from Proposition 2. As for the
 forward direction, suppose $1=G^n\subset G^{n-1}\subset \cdots\subset G^1=G$ is
 the lower central series and $1=C_1\subset C_2\subset\cdots$ is the upper
 central series. I will show by induction that $C_i\supset
 G^{n-i}$. Suppose this is the case for $i$. Then consider the normal
 subgroups $G^{n-i-1},C_i\normal G$. Since $C_i\supset G^{n-i} =
 (G^{n-i-1},G)$, by Proposition 1 we have $G_{n-i-1}/C_i\subset Z(G/C_i) =
 C_{i+1}/C_i$ and so $G_{n-i-1}\subset \pi^{-1}(G^{n-i-1}/C_i)\subset
 C_{i+1}$, where $\pi$ is the projection onto $C_i$. $\qed$

Finally, I outline the relationship between nilpotent and
solvable. All nilpotent groups are solvable, because the lower central
series terminates and $G^{(i)}\subset G^i$ for all $i$, so the derived
series also terminates. However, not all solvable groups are
nilpotent. In fact, any solvable group with trivial center will do,
because the upper central series will never terminate. The simplest
example is $S_3$. The center is the set of elements fixed by
conjugation by every element, but by the behaviour of conjugation in
symmetric groups, it shouldn't be hard to see that no such element
exists. However, $S_3$ admits the normal series $S_3\Normal A_3\Normal
1$ with abelian factors.