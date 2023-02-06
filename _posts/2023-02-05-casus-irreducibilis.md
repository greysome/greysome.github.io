---
layout: post
title: Casus irreducibilis for cubic polynomials
---

Cardano's formulas gives us the roots of a cubic in terms of
radicals. For a depressed cubic $x^3+px+q$, these roots are

$$\begin{equation}
\label{equation:cubic-roots}
r_1 = {z_1+z_2\over 3},\quad
r_2 = {\omega^2 z_1 + \omega z_2 \over 3},\quad
r_3 = {\omega z_1 + \omega^2 z_2 \over 3},
\end{equation}$$

where $\omega$ is a primitive 3rd root of unity, $d=-4p^3-27q^2$ is
the discriminant and

$$z_1 = \sqrt[3]{-27q+3\sqrt{-3d} \over 2},\quad
z_2 = \sqrt[3]{-27q-3\sqrt{-3d} \over 2}.$$

As \eqref{equation:cubic-roots} shows, the solution takes a detour to
the complex numbers, even when all the roots are real. I'll show that
when the cubic is irreducible (*casus irreducibilis*) and has real
roots, this phenomenon is unavoidable (see the below Theorem). Thus
one cannot hope to find some alternative expression for the roots that
avoids complex numbers.

Let $F$ be a subfield of $\R$ and $f(x)\in F[x]$ be an irreducible
cubic with real roots. The degree of the splitting field $E\subset\R$
is at least 3, so $G_f=A_3$ or $S_3$. Note also that if $d$ is the
discriminant, then $\sqrt d\in E$ is real, and so $d>0$, which implies
$G_f=A_3$.

**Lemma.** If $r$ is real and $r^p\in F$ for $p$ a prime, then $F(r)$
  does not contain a splitting field of $f(x)$ over $F$. Furthermore,
  $f(x)$ remains irreducible over $F(r)$.

*Proof.* I proved in [this other entry]({% post_url
2023-01-25-galoisgrp-xp-a %}) that $x^p-r^p$ is either irreducible or
has a root in $F$. Thus $[F(r):F]=1$ or $p$.  Supposing that $F(r)$
contains a splitting field $E$, we can eliminate the first possibility
and by degree considerations also conclude that $p=3$, so that
$F(r)=E$. But this means $F(r)/F$ is normal, so it contains the
conjugates $\omega r$, $\omega^2r$, where $\omega$ is a primitive 3rd
root of unity. So $F(r)\not\subset\R$, implying $r$ is not
real. Lastly, $f(x)$ must be irreducible over $F(r)$, otherwise $F(r)$
contains $F(r_1)$ for some root $r_1$, which is a splitting field
since $[F(r_1):F]=3$. $\qed$

**Theorem.** There exists no subfield $K$ of $\R$ that has a root
  tower of $F$ and contains a splitting field of $f(x)$ over $F$.

*Proof.* Fix a root tower and suppose $L\subset L(\sqrt[n]{a})$ are
 successive elements, where $a\in L$. We can factor the extension
 $L(\sqrt[n]{a})/L$ into a tower of subextensions with prime
 indices. For example if $n=pq$ with $p,q$ prime then we have the tower

 $$L\subset L(\sqrt[p]{a}) \subset L(\sqrt[p]{a},\sqrt[pq]{a}) =
 L(\sqrt[n]{a}).$$

 Since $K\subset\R$, all the radicals are real. So if $L$ does not
 contain a splitting field of $f(x)$ and $f(x)$ is irreducible over
 $L$, then we can repeatedly apply the lemma to conclude that
 $L(\sqrt[n]{a})$ does not contain a splitting field either and $f(x)$
 remains irreducible over $L(\sqrt[n]{a})$. By working our way up the
 root tower starting from $F$, we can conclude that $K$ does not
 contain a splitting field. $\qed$