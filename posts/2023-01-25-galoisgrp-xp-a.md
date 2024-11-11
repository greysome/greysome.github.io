# The Galois group of $x^p-a$


**Proposition.** Let $f(x)=x^p-a$ where $a\in\Q$ and $f$ is
  irreducible.  Its Galois group is isomorphic to the group of
  transformations of $\F_p$ of the form $y\mapsto ky+l$ where
  $k,l\in\F_p$ and $k\neq0$.

Before embarking on the proof, I first prove a lemma.

**Lemma.** Let $a\in\Q$. Either $x^p-a$ is irreducible in $\Q[x]$ or
  it has a root in $\Q$.

*Proof.* Since $(x^p-a)'=px^{p-1}$ is coprime with $x^p-a$, it is
 separable and hence has distinct roots. Namely if $b$ is a root of
 $x^p-a$ in some splitting field, then the remaining roots have the
 form $bz,\ldots,bz^{p-1}$ where $z$ is a primitive $p$th root of
 unity. (The powers of $z$ are distinct since $x^p-1$ is separable.)
 Thus the splitting field of $x^p-a$ over $\Q$ arises as a tower

 $$\Q\subset \Q(z)\subset \Q(z,b),\quad [\Q(z):\Q]=p-1.$$

 $\Q(z,b)$ is also a splitting field for $x^p-a$ over $\Q(z)$, and
 $\Q(z)$ contains the requisite roots of unity, so
 $\Gal(\Q(z,b)/\Q(z))$ is cyclic of order dividing $p$. Thus
 $[\Q(z,b):\Q(z)]=1$ or $p$. In the latter case, $x^p-a$ is the desired
 minpoly of $b$ over $\Q(z)$ and hence over $\Q$, hence it is
 irreducible.

 In the former case, we have $b\in\Q(z)$. Let $\eta$ be a generator of
 $\Gal(\Q(z)/\Q)\cong \Z_{p-1}$, so that $\eta(b)=bz^k$ and
 $\eta(z)=z^l$ where $l\neq1$. Setting $n=-k(l-1)^{-1}$, we have

 $$\eta(bz^n) = bz^{k-k(l-1)^{-1}l} = bz^{-k(l-1)^{-1}} = bz^n.$$

 Thus $bz^n$ is fixed by $\Gal(\Q(z)/\Q))$, and so is a root of $x^p-a$
 lying in $\Q$. $\qed$

It turns out that the lemma generalises to all fields $F$, but I
haven't been able to prove it in general, the problem being that
$\Gal(F(z)/F)$ may not be cyclic. (Though, the proof for $p=\char F$
has been done in [this other entry](2023-01-25-separable-poly.html).)
Nevertheless the lemma as stated suffices for our purposes.

Back to the main result. The splitting field of $x^p-a$ can be
expressed as a tower

$$\Q \subset \Q(z) \subset \Q(z,b),$$

where $z$ is a primitive $p$th root of unity and $b$ is a root of
$x^p-a$. Recall from the previous exercise that $[\Q(z,b):\Q(z)]=1$ or
$p$. It cannot be 1 because then some root lies in $\Q$, contradicting
irreducibility of $x^p-a$. Thus $[\Q(z,b):\Q(z)]=p$. I will construct
automorphisms of $\Q(z,b)/\Q$ by first constructing automorphisms of
$\Q(z)/\Q$ and then extending them. All automorphisms of $\Q(z,b)/\Q$
arise in this manner since $\Q(z)/\Q$ is normal. Each
$\varphi\in\Gal(\Q(z)/\Q))$ has the form $z\mapsto z^k$, $k\neq0$. Since
there are $p-1=[\Q(z):\Q]$ such automorphisms, and the degree
$[\Q(z,b):\Q]=p(p-1)$, $\varphi$ has $p$ extensions

$$\varphi: z\mapsto z^k,\ b\mapsto bz^l$$

Now I map $\varphi$ to the transformation $y\mapsto ky+l$. It is
obviously injective so it remains to show it is a homomorphism to
prove the isomorphism. Composing $\varphi$ with

$$\psi: z\mapsto z^{k'},\ b\mapsto bz^{l'}$$

yields

$$\psi\varphi: z\mapsto z^{kk'},\ b\mapsto (bz^{l'})(z^{k'l})=bz^{k'l+l'}.$$

This corresponds to the transformation $x\mapsto kk'x+(k'l+l')$, which
is also the composite of $x\mapsto kx+l$ and $x\mapsto k'x+l'$. This
completes the proof. $\qed$

### Update: 4 Feb 2023

Here is a proof of the very first lemma that works for all fields $F$,
taken from StackExchange. Suppose $x^p-a$ is reducible and $g(x)$ is a
proper divisor. In a splitting field we have

$$g(x) = (x-r_1)\cdots(x-r_k).$$

Then $r=\prod_{i=1}^k r_i\in F$, and $r^p = r_1{}^p\cdots r_k{}^p =
a^k$. Since $k<p$ we have that $p$ and $k$ are relatively prime, so
there are integers $m,n$ such that $mp+nk=1$. Thus,

$$(a^mr^n)^p = a^{mp}r^{np} = a^{mp+nk} = a.$$

Thus $a^mr^n$ is a root of $x^p-a$ in $F$, as desired. $\qed$