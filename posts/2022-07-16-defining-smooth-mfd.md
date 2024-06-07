# Defining smooth manifolds


Recall the definition of a *topological* manifold $M\subset\R^n$:
every $x\in M$ has a nbhd $U\cap M$ that is homeomorphic to an open
subset $W\subset\R^k$. It is tempting to define smooth manifolds by
replacing 'homeomorphic' by 'diffeomorphic'[^1], but upon
closer inspection this doesn't make sense: it is meaningless to talk
about whether a map $g:U\cap M\to W$ is differentiable because the
domain is generally not open in $\R^n$.

For our naive definition of smooth manifold to make sense, we have
to extend the notion of diffeomorphism. Milnor defines $f$ to be a
diffeomorphism if $f$ is differentiable and $f^{-1}$ extends to a
differentiable map $G:V\to W$, with $V\subset\R^n$ open. (I'll use the
background assumption that $f:W\to U\cap M$ is always a bijection.)
Given $x\in U\cap M$, $f$ is called a *coordinate system* around $x$.

Note that the composite $dG_{f(x)}\circ df_x:\R^k\to\R^n\to\R^k$ is
just $\id$, by an application of the chain rule. This has two
immediate consequences: $n\ge k$ and $df_x$ has rank $k$. Spivak
points out that there is a sort of converse to the second consequence:
if $f:W\to U\cap M$ is a map such that $df_x$ has rank $k$ everywhere,
and $x\in U\cap M$, then there exists a coordinate system around $x$
(not necessarily $f$). The idea is that $f$ 'factors' as a composite

$$W\hookrightarrow W\times\R^{n-k}\ \xrightarrow{F} F(W\times\R^{n-k})$$

Indeed, we can define

$$F(w_1,\ldots,w_k,y_1,\ldots,y_{n-k})=f(w_1,\ldots,w_k)+(0,\ldots,0,y_1,\ldots,y_{n-k})$$

Note that $dF_x$ is just the $n\times n$ matrix

$$\begin{pmatrix}
&\vphantom{A}& \\
-&df_x&- \\
&\vphantom{A}& \\
\hline
1&& \\
&\ddots& \\
&&1
\end{pmatrix},$$

which has full rank. Then $F$ is a local diffeomorphism by the inverse
function theorem and also $F(W\times0)=U\cap M$. For each $x\in U\cap
M$ there is a unique $y\in W\times0$ such that $F(y)=x$. By taking a
nbhd $W'\ni y$ such that $F|_{W'}$ is a diffeomorphism onto $F(W')$,
we have the 'restricted' composite

$$\{x\in W\mid (x,0)\in W'\}\hookrightarrow W'\xrightarrow{F} F(W')$$

(See Figure 1.) It is straightforward to verify that
this is our desired coordinate system around $x$. The required inverse
$F(W')\to\{x\in W\mid (x,0)\in W'\}$ is differentiable since it is
just $F^{-1}$ followed by projection onto the first $k$ components.

{% include figure.html src="manifold-coord-system-deriv-full-rank.svg"
alt="A coordinate system whose derivative has full rank"
figno=1 %}

### Immersed manifolds

The proof of the converse required that the image of $f$ is an open
subset of $M$. If we drop this condition (while still requiring that
$df_x$ have full rank everywhere) then we can have counterexamples
where $f$ exists but a coordinate system doesn't, thus $M$ is not a
smooth manifold after all. $M$ is merely what is called an
*immersed manifold*.

The simplest example is illustrated in Figure 2. The map $f$ between
blue regions is a bijection and has full rank everywhere, but its
image is not open in $M$, since every nbhd of $x$ has two connected
components. Accordingly, there is no coordinate system $g$ around $x$,
because that would imply the existence of an open subset $U\subset\R$
and a point $x\in U$ such that every nbhd intersects two connected
components of $U$, which is impossible.

{% include figure.html src="immersed-manifold.svg"
alt="Immersed manifold"
figno=2 %}

[^1]: For convenience I'll use diffeomorphic to refer to smoothly diffeomorphic.