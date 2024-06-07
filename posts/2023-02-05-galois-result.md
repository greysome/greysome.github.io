# A result of Galois on prime degree polynomials


In this entry I build up to the following result.

**Main Theorem (Galois).** Let $F$ be char 0, $f(x)\in F[x]$ be
  irreducible of prime degree $p$, and $E$ be a splitting field. Then
  $f(x)$ is solvable by radicals iff $E=F(r_i,r_j)$ for any two roots
  $r_i,r_j\in E$.

A lot of the pre-work is done in group theory, to prove this auxiliary
theorem.

**Theorem 1.** Any solvable transitive subgroup $G\subset S_p$, $p$ a
  prime, is isomorphic to a subgroup of the group $L$ of
  transformations $x\mapsto ax+b$, $a\neq0$ of $\F_p$, containing the
  subgroup $P$ of translations.

In turn, this theorem relies on a few lemmas about $S_p$.

**Lemma 1.** Let $H$ be a normal subgroup of a transitive subgroup $G$
  of $S_n$. Then the $H$-orbits all have equal size. In particular, if
  $n$ is prime then $H$ is transitive.

*Proof.* Let $S$ be the set being acted on. Given $x\in S$, let
 $\text{Orb}(x)$ denote its $H$-orbit. We have that each $g\in G$ maps
 $\text{Orb}(x)\to\text{Orb}(gx)$, since for each $hx\in\text{Orb}(x)$
 we have

 $$g(hx) = (ghg\inv)(gx) = h'(gx)\in \text{Orb}(gx),\quad
 h'=ghg\inv\in H.$$

 This map is injective and hence bijective, so
 $|\text{Orb}(x)|=|\text{Orb}(gx)|$. This combined with transitivity
 of $G$ completes the proof. $\qed$

**Lemma 2.** Let $L$ act on $\F_p$, so it embeds as a subgroup of
  $S_p$. If $H$ is a subgroup of $S_p$ such that $P\normal H$, then
  $H\subset L$.

*Proof.* Let $\tau:x\mapsto x+1$ and $\eta\in H$. Then
 $\eta\tau\eta\inv:x\mapsto x+k$. So

 $$\eta(\eta\inv(x)+1) = x+k;$$

 replacing $x$ by $\eta(x)$ gives us

 $$\eta(x+1) = \eta(x)+k.$$

 From this we can conclude $\eta$ has the form $x\mapsto kx+b$. $\qed$

*Proof of Theorem 1.* Let $G$ be solvable transitive, and let

$$1\normal G_1\normal \cdots\normal G_k\normal G$$

be a composition series. By repeatedly applying lemma 1 we can
conclude that $G_k,G_{k-1},\ldots,G_1$ are all transitive. Since $G$
is solvable, $|G_1|=|G_1/1|$ is a prime, and by the orbit-stabiliser
theorem it is divisible by $p$. Thus $|G_1|=p$.

Next I'll show that if $H_1\normal H_2$ are two terms in the
composition series such that $H_1\neq1$ and $x\in H_2$ has order $p$,
then $x\in H_1$. First we know that $|H_2/H_1|$ is a prime $q\neq p$,
since $p$ is already taken up by $|G_1/1|$ and $p^2\nmid p!$. Thus
there are integers $a,b$ such that $ap+bq=1$. Since $x^q\in H_1$ and
$x^p=1\in H_1$, we can conclude

$$x=x^{ap+bq}\in H_1.$$

Now, since $G$ is transitive it contains at least one order
$p$-subgroup, thus at least $p-1$ order $p$ elements, all of which are
contained in $G_1$. Thus $G$ has exactly $p-1$ order $p$ elements,
making up a unique order $p$ subgroup $H$. In fact, $H$ is a Sylow
subgroup, so $H\normal G$. If $x$ is a generator of $H$, it must be a
$p$-cycle; relabelling the letters if necessary we can assume $x=(0
\ 1\ \cdots\ p-1)$, so that $H=P$. By lemma 2, we can conclude that
$G\subset L$ as desired. $\qed$

The group-theoretic preliminaries are complete. We can now move on to
the meat.

*Proof of Main Theorem.* ($\imp$) If $f(x)$ is irreducible and
  solvable by radicals then $G_f$ is solvable transitive, so
  $G_f\subset L$. Let $H$ be the subgroup corresponding to $F(r_i)$,
  so that $r_i$ is fixed by $H$. But every nontrivial transformation
  in $L$ fixes at most one point, so any other $r_j$ is fixed only by 1.
  Therefore, $\Gal(E/F(r_i,r_j))=1$, i.e. $E=F(r_i,r_j)$.

($\impd$) We have $[F(r_i):F]=p$ which divides $[E:F]=|G_f|$, so $G_f$
contains a subgroup $N$ of order $p$. Because $E=F(r_i,r_j)$ we have
$[E:F]=pk\mid p(p-1)$, so $N$ is actually Sylow. Furthermore, it is
the unique Sylow subgroup, because otherwise $G_f$ has at least $p+1$
of them, whose union contains $(p+1)(p-1)+1=p^2>pk$ elements, a
contradiction. Thus $N\normal G_f$.

Let $H$ be the subgroup corresponding to $F(r_i)$; it has order
$k$. If $K$ is the subfield corresponding to $N\subset G_f$, then by
degree considerations $K\cap F(r_i)=1$, so $G_f$ is an internal
semidirect product $NH$. In fact, the conjugation action of $H$ on $N$
must be faithful, otherwise have

$$(h\a_1\ \cdots\ h\a_p) = h(\a_1\ \cdots\ \a_p)h\inv = (\a_1\ \cdots\
\a_p),\quad
\text{for some $h\neq1\in H$},$$

implying that $h$ is a $p$-cycle. But this cannot be the case since
$p\nmid|H|=k$. So, the structure map $H\to\Aut(N)\cong\Z_{p-1}$ is
injective, and $N\rtimes H$ is isomorphic to a subgroup of $N\rtimes
\Z_{p-1}\cong \Z_p\rtimes \Z_{p-1}$. The latter has a normal series
$1\normal \Z_p\rtimes 1\normal \Z_p\rtimes \Z_{p-1}$ with abelian factors
$\Z_p,\Z_{p-1}$, and is hence solvable, so $G_f\cong N\rtimes H$ is also
solvable as desired. $\qed$

In fact, $\Z_p\rtimes \Z_{p-1}$ is isomorphic to $L$, where $\Z_p\rtimes
1$ corresponds to $P$ and $1\rtimes \Z_{p-1}$ corresponds to the
nonzero scalings $x\mapsto ax$.