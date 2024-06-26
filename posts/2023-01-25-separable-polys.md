# Separability and polynomials over char $p$


A polynomial is separable if its irreducible factors have distinct
roots, that is to say each irreducible factor $f(x)$ splits into
distinct linear factors in some splitting field of $f$. A necessary
and sufficient condition for a polynomial $f(x)$ (irreducible or not)
to have distinct roots is $(f,f')=1$. If $f(x)$ is irreducible then
the only possibilities for $(f,f')$ are 1 and $f$, since $(f,f')\mid
f$. If $f(x)$ is in addition inseparable, i.e. it has multiple roots,
then $(f,f')=f$ and we are forced $f'=0$, otherwise $\deg(f,f')<\deg
p$ rendering $(f,f')=f$ impossible.

The only way for $f'=0$ to be the case is if the underlying field $F$
has char $p$ and $f$ has the form

$$\begin{equation}
\label{eq:poly-over-xp}
f(x) = x^{mp} + a_{m-1}x^{(m-1)p} + \ldots + a_1x^p + a_0.
\end{equation}$$

The simplest such polynomial has the form $x^p-a$. If $\a,\b$ are
roots of $x^p-a$ in some splitting field $E$, then we have

$$\a^p = a = \b^p \implies (\a-\b)^p = \a^p-\b^p = 0 \implies \a=\b.$$

Thus all roots of $x^p-a$ are equal, and this greatly constrains its
possible factorisations in $F[x]$. Let $\a$ be the (unique) root and
$g(x)\in F[x]$ its minpoly. For any divisor $d(x)$ of $x^p-a$ within
$F[x]$, we have that $\a$ is a root and thus $g(x)\mid d(x)$. Thus we
can keep dividing $g(x)$ out of $x^p-a$, so $x^p-a=g(x)^k$ for some
$k$. But $p=k\deg g$ is prime and so this forces $\deg g = 1$ or $p$,
constraining the possible factorisations further.

1. $\deg g = 1$ corresponds to the case where $\a\in F$, in which case
   $x^p-a=(x-\a)^p$ is separable, since its only irreducible factor
   $x-\a$ obviously has distinct roots.

2. $\deg g = p$ corresponds to the case where $\a\nin F$, in which
   case $x^p-a$ is inseparable since it splits as $(x-\a)^p$ in
   $E[x]$. Also we have that $x^p-a=g(x)$ is irreducible.

Common to these two cases is the fact that $x^p-a$ is a $p$th power in
$E[x]$, just that in the first case $E=F$ while in the second $E/F$
has degree $p$.

Let $F^p$ denote the subfield of all $p$th powers in $F$. As we've
shown, $F=F^p$ is equivalent to the fact that all polynomials of the
form $x^p-a$, $a\in F$ are separable. Remarkably, this is equivalent
to *all* polynomials over $F$ being separable (such an $F$ is called
*perfect*).

*Proof.* One direction is obvious. Now suppose $f(x)\in F[x]$ is an
 irreducible polynomial with multiple roots. We showed already that
 $f$ has the form \eqref{eq:poly-over-xp}. In that case, some $a_i$ is
 not a $p$th power in $F$, otherwise $b_i^p=a_i$ and $f$ admits the
 factorization

 $$x^{mp} + a_{m-1}x^{(m-1)p} + \ldots + a_0 = (x^m + b_{m-1}x^{m-1} + \ldots + b_0)^p,$$

contradicting the irreducibility of $f$. $\qed$

A natural follow-up is to consider polynomials of the form
$x^{p^e}-a$. Suppose $a\nin F^p$; otherwise by induction some $p^e$th
root $\a$ lies in $F$ and we have $x^{p^e}-a = (x-\a)^{p^e}$. In this
case I show that $x^{p^e}-a$ is irreducible in $F[x]$. The analysis
treads much the same path as $x^p-a$: all its roots are equal, and
$x^{p^e}-a = g(x)^k$ where $g$ is the minpoly of the unique root
$\a$. Thus $\deg g$ has prime power $p^l$ and so

$$g(x) = (x-\a)^{p^l} = x^{p^l}-\a^{p^l},\quad \a^{p^l}\in F.$$

If $x^{p^e}-a$ were reducible then $k>1$ and so $l<e$ and $e-l-1\ge 0$, thus

$$\a^{p^{e-1}} = {(\a^{p^l})}^{p^{e-l-1}} \in F.$$

But ${(\a^{p^{e-1}})}^p = a$ which plainly contradicts $a\nin
F^p$. Thus $x^{p^e}-a$ is irreducible.

Next, we consider *$p$-polynomials*, which have the form

$$\begin{equation}
\label{eq:p-poly}
f(x) = x^{p^m} + a_{m-1}x^{p^{m-1}} + \ldots + a_mx.
\end{equation}$$

There is the following result from Jacobson which is left as an
exercise, but sadly I am unable to prove the converse:

**Proposition.** $f(x)$ is a $p$-polynomial iff its roots form an
  additive subgroup of the splitting field and each root has
  the same prime power multiplicity.

*Proof.* ($\imp$) Obviously the roots form an additive subgroup. Now
 we can write $f(x)=g(x^{p^e})$ where $p^e$ is the lowest prime power
 with nonzero coefficient in $f(x)$. The coefficient of $y$ in $g(y)$
 is nonzero, thus $g'(y)$ is a unit and so $g$ is separable. Let
 $g(x)=\prod_i (x-\a_i)$ in some splitting field, so that
 $f(x)=\prod_i (x^{p^e}-\a_i)$. Then let $E$ be a larger field in
 which $\a_i=\b_i^{p^e}$ for some $\b_i$, so that $f(x)=\prod_i
 (x-\b_i)^{p^e}$. The $\b_i$'s are distinct because the $\a_i$'s are
 distinct. Thus every root of $f$ has multiplicity $p^e$.

($\impd$) I don't know oops. $\qed$

Lastly, I analyse the polynomial $f(x)=x^p-x-a$, $a\in F$. It isn't
exactly a $p$-polynomial because of the possibly nonzero cosntant
term, but it behaves very much like one. Since $f'(x)=-1$, $f$ has
distinct roots. More than that, if $\a,\b$ are roots than we have

$$\begin{align*}
\a^p-\a = a = \b^p-\b &\implies (\a-\b)\bigl((\a-\b)^{p-1}-1\bigr) = (\a-\b)^p-(\a-\b) = 0 \\
&\implies \a=\b \quad\text{or}\quad (\a-\b)^{p-1}=1.
\end{align*}$$

In the latter case we have $\a-\b\in\F_p^\ast$, where $\F_p$ is the
prime subfield, since every element of $\F_p^\ast$ is a root of
$x^{p-1}-1$ by Fermat's little theorem! Combined with separability, we
have that if $\a$ is a root and $n\in\F_p$ then $\a+n$ is also a root,
therefore

$$f(x) = \prod_{n\in\F_p} (x-(\a+n)).$$

Note how the roots form the coset $\a+\F_p$, and all have multiplicity 1.
If $\a$ has minpoly $g(x)$ over $F$, then $\a+n$ has minpoly
$g(x-n)$ which has the same degree. Thus the irreducible factors of
$f(x)$ over $F$ all have the same degree. But $p=\deg f$ is prime, so
either the irreducible factors are all linear, or it is $f(x)$
itself. Thus either $x^p-x-a$ is irred or $a=\a^p-\a$ for some $\a\in
F$.