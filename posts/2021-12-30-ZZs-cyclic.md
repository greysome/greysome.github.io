# $\ZZs{p^n}$ is cyclic


A few days back someone in the math Discord mentioned that $\ZZs{p^n}$
is cyclic for all primes $>2$, so I took it upon myself to prove it.

My first idea was to arrange the elements of $\ZZs{p^n}$ in a grid mod
$p^{n-1}$, as shown in Figure 1. This is possible because

$$(x,p^n)=1 \iff (x,p^{n-1})=1 \iff (x\,\%\,p^{n-1}, p^{n-1})=1.$$

![$\ZZs{27}$](mod27-mulgroup.svg "The elements of $\ZZs{27}$, arranged in rows mod 9. Note that the first row consists of the elements of $\ZZs{p^{n-1}}$ and there are $p$ rows." 50%)

Observe that the map sending $x\in\ZZs{p^n}$ to its column represents
a group homomorphism 

$$\phi:\ZZs{p^n}\to\ZZs{p^{n-1}}.$$

The kernel is the first column, which forms an order $p$ subgroup
$H$.

Now, by induction $\ZZs{p^{n-1}}$ is cyclic and so has a generator $x$
with order 

$$k=|\ZZs{p^{n-1}}|=p^{n-2}(p-1).$$

In the larger group $\ZZs{p^n}$, the power $x^k$ may not equal 1, but
it is guaranteed to lie in $H$, which is the first column. This
follows from the fact that $\phi$ is a homomorphism.

#### Case 1

If $x^k\neq1$, then $x^k\in H$ has order $p$, so $x$ has order
$pk=|\ZZs{p^n}|$. Therefore $x$ is also a generator for $\ZZs{p^n}$
and this immediately concludes it is cyclic.

#### Case 2

If $x^k=1$, then $x$ generates an order $k$ subgroup
$K\le\ZZs{p^n}$. Since $H=\ker\phi$, $K$ is isomorphic to
$\im\,\phi=\ZZs{p^{n-1}}$ and $H,K$ intersect trivially, we have a
split exact sequence of groups

$$1\to H\to \ZZs{p^n}\to K\to 1,$$

so $\ZZs{p^n}$ is a semidirect product of $H$ and $K$. But $\ZZs{p^n}$
is abelian, so this semidirect product must be a direct product

$$H\times K \cong C_p\times C_{p^{n-2}(p-1)}.$$

For $n=2$ this direct product is also cyclic, so I shall assume
$n\ge3$. I then show this case leads to a contradiction, so
$\ZZs{p^n}$ being cyclic is the only remaining possibility. (As a
bonus, this shows that all generators of $\ZZs{p^{n-1}}$ are also
generators of $\ZZs{p^n}$ for $n\ge3$.)

First we determine the number of elements in $H\times K \cong
C_p\times C_{p^{n-2}(p-1)}$ with order 1 or $p$. I'll call these
*$p$-elements* for brevity; these are simply the elements with
order $p$, plus the identity. The $p$-elements are

1. $(1,1)$
2. $(a,1)$, where $a$ has order $p$
3. $(1,b)$, where $b$ has order $p$
4. $(a,b)$, where $a,b$ have order $p$.

In a cyclic group with order divisible by $p$, the number of order $p$
elements is $\varphi(p)$. Thus, the number of $p$-elements in the
aforementioned product is

$$1+2\varphi(p)+\varphi(p)^2 = (\varphi(p)+1)^2 = p^2.$$

Going back to $\ZZs{p^n}$, we see that if $x$ is a $p$-element in
$\ZZs{p^n}$, then $\phi(x)$ is also a $p$-element in
$\ZZs{p^{n-1}}$. Thus

$$\{\text{$p$-elements in $\ZZs{p^n}$}\} \subseteq
\phi^{-1}\{\text{$p$-elements of $\ZZs{p^{n-1}}$}\}.$$

Since $\phi$ is surjective and its fibres have size $p$, the RHS has
order

$$p\cdot(\text{# $p$-elements in $\ZZs{p^{n-1}}$}) = p^2.$$

(The equality follows since $\ZZs{p^{n-1}}$ is assumed to be cyclic by
induction.) Supposing $\ZZs{p^n}\cong H\times K$, it follows that LHS
and RHS have the same order, so

$$\{\text{$p$-elements in $\ZZs{p^n}$}\} =
\phi^{-1}\{\text{$p$-elements of $\ZZs{p^{n-1}}$}\}.$$

These sets are illustrated in Figure 2.

![The $p$-elements of $\ZZs{27}$"](mod27-mulgroup-pelements.svg "If $\ZZs{27}$ is not cyclic, then the 3-elements of $\ZZs{27}$ are precisely the elements which share the same column as 1, 4 or 7, which are the 3-elements in $\ZZs{9}$." 50%)

To complete the contradiction, I show that a certain element $a$ lies
in the latter set, but not the former set. This special element is
$p^{n-2}+1$.

First, observe that

$$\{1,\,p^{n-1}+1,\,2p^{n-1}+1,\ldots,\,(p-1)p^{n-1}+1\}$$

is an order $p$ cyclic subgroup of $\ZZs{p^n}$. In fact, it is $H$. In
particular, $a$ has order $p$ in $\ZZs{p^{n-1}}$. Since $\phi(a)=a$,
we easily conclude that $a$ lies in the latter set.

It remains to show that $a$ does not have order $p$ in $\ZZs{p^n}$. I
do so by deriving this general identity:

**Lemma.** If $p>2$ and $n\ge3$, then

$$a^p \equiv p^{n-1}+1 \mod p^n.$$

*Proof.* We have

$$a^p = {p\choose p}p^{p(n-2)} + {p\choose p-1}p^{(p-1)(n-2)} + \ldots
+ {p\choose 2}p^{2(n-2)} + {p\choose 1}p^{n-2} + {p\choose 0}.$$

The terms have the form $n_k={p\choose k}p^{k(n-2)}$. For $2\le k\le
p-1$, we have $p\mid {p\choose k}$, so $p^{k(n-2)+1}\mid n_k$. Now, we
have $k(n-2)+1\ge n$ for $k\ge 2$, so the $n_k$'s can be cancelled out
mod $p^n$. This leaves us with

$$a^p \equiv {p\choose p}p^{p(n-2)} + {p\choose 1}p^{n-2} + {p\choose
0} \equiv p^{p(n-2)} + p^{n-1} + 1 \mod p^n.$$

The first term can be cancelled out when $p>2$ and $n\ge3$, since
$p(n-2)\ge 3n-6\ge n$, implying $p^n\mid p^{p(n-2)}$. $\qed$

The lemma shows that $a^p\not\equiv 1$ mod $p^n$, which completes the
proof by contradiction.

Note the lemma only holds for odd primes. In fact $\ZZs{2^n}$ is
easily seen to be not cyclic, because we can exhibit multiple order 2
elements, namely $-1$, $2^{n-1}-1$ and $2^{n-1}+1$. Additionally, I'll
prove that the residue 3 has order $2^{n-2}$, which will be sufficient
to characterise $\ZZs{2^n}$ as the product $C_2\times
C_{2^{n-2}}$. (This makes use of the fact that finite abelian groups
are products of cyclic groups.)

**Lemma.** In $\ZZs{2^n}$, the residue 3 has order $2^{n-2}$.

*Proof.* This can be manually seen for $n=2,3,4$, so suppose $n>4$ and
 that 3 has order $2^{n-3}$ in $\ZZs{2^{n-1}}$.

By the implication $3^k\equiv 1\bmod 2^n \imp 3^k\equiv 1\bmod
2^{n-1}$, we have that the order in $\ZZs{2^n}$ is a multiple of
$2^{n-3}$, the order in $\ZZs{2^{n-1}}$. Furthermore, the order must
be a proper divisor of $\bars{\ZZs{2^n}}=2^{n-1}$ since $\ZZs{2^n}$ is
not cyclic. This forces the orders to be either $2^{n-3}$ or
$2^{n-2}$. Thus it suffices to show that

$$3^{2^{n-3}}\not\equiv 1\bmod 2^n.$$

Before we do the calculations, first observe that
$3^{2^{n-4}}=2^{n-2}k+1$ for some $k$ since $3^{2^{n-4}}\equiv
1\bmod 2^{n-2}$. Furthermore, $2\nmid k$ because otherwise one can
conclude $3^{2^{n-4}}\equiv 1\bmod 2^{n-1}$ which we already know is
false.

Now, we have

$$\begin{align*}
3^{2^{n-3}}-1 &= (3-1)\left(3^{2^{n-3}-1}+\cdots+3^{2^{n-4}}+3^{2^{n-4}-1}+\cdots+3^0\right) \\
&= 2\left[\left(\sum_{i=0}^{2^{n-4}-1} 2^{n-2}(3^i k) + 3^i\right) + \sum_{i=0}^{2^{n-4}-1} 3^i\right] \\
&= 2\left[2^{n-2}k\frac{3^{2^{n-4}}-1}{2} + 3^{2^{n-4}}-1\right] \\
&= 2\left[2^{2n-5}k^2 + 2^{n-2}k\right] \\
&\equiv 2^{n-1}k \\
&\not\equiv 0 \bmod 2^n.\quad\qed
\end{align*}$$