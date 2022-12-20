---
layout: post
title: Computing pullbacks of $k$-forms over $k$-chains
---
Let $\omega$ be a $k$-form in $\R^n$ and $c$ be a $k$-cube. Spivak
defines the integral $\int_c\omega$ to be $\int_{[0,1]^k}c^\*\omega$,
but by computing the pullback $c^*\omega$, one can find a more
explicit expression for the latter in terms of iterated integrals over
$[0,1]$. I'll do the computations for $k=1$ and $k=2$, and hopefully
the general pattern should be clear.

### The case $k=1$

I'll use $x^1,\ldots,x^n$ to denote the coordinates in $\R^n$, so we have

$$\omega=f^1dx^1+\ldots+f^ndx^n$$

for functions $f^1,\ldots,f^n:\R^n\to\R$. Since $c$ is a path, the
pullback $c^*\omega$ is a 1-form $F\,dt$[^1] on $[0,1]$, where
$F:[0,1]\to\R$ is to be determined. First, we can exploit the useful
fact that pullbacks respect linearity and multiplication by a 0-form:

$$c^*\omega=(f^1\circ c)\,c^*dx^1+\ldots+(f^n\circ c)\,c^*dx^n$$

So it suffices to find $c^*dx^i$. By the definition of $c^\*$ we have
that for $t\in[0,1]$ and $v\in\R_t$ (the tangent space at $t$),

$$\begin{align*}
c^*dx^i(t)(v) &= \underbrace{dx^i\bigl(c(t)\bigr)}_{=\pi^i}(Dc_t v) \\
&= \pi^i\begin{pmatrix}Dc^1_t\cdot v\\\vdots\\Dc^n_t\cdot v\end{pmatrix}\quad\text{(note that $Dc^i_t$ is a scalar)} \\
&= Dc^i_t\cdot v
\end{align*}$$

Put in words, the linear functional $c^\*dx^i(t)\in\mathfrak I^1(\R)$
is scalar multiplication by $Dc^i_t$, i.e. $c^\*dx^i(t)=Dc^i_t\,dt$,
and thus $c^\*dx^i$ can be abbreviated as $Dc^i\,dt$. So

$$c^*\omega=\left(\sum_i(f^i\circ c)\,Dc^i\right)\,dt,$$

and

$$\begin{align*}
\int_c\omega &= \int_{[0,1]} \sum_i(f^i\circ c)\,Dc^i \\
&= \int_0^1\sum_i f^i\bigl(c(t)\bigr)\cdot Dc^i_t\,dt \\
&= \int_0^1 \begin{pmatrix}f^1\bigl(c(t)\bigr)\\\vdots\\f^n\bigl(c(t)\bigr)\end{pmatrix}\cdot\begin{pmatrix}Dc^1_t\\\vdots\\Dc^n_t\end{pmatrix}\ dt
\end{align*}$$

Thus an integral of a 1-form over a 1-cube (i.e. a line integral) is
an integral of dot products. Physically, this is the work done by a
force along a path.

### The case $k=2$

Now $\omega$ is a sum $\sum_{i<j}f^{ij}\,dx^i\wedge dx^j$. As before,
we can reduce the computation of $c^\*\omega$ (a 2-form on $[0,1]^2$)
to the computation of the $c^\*dx^i$'s, using the fact that pullbacks
preserve wedge products:

$$c^*\omega = \sum_{i<j}(f^{ij}\circ c)\,c^*dx^i\wedge c^*dx^j$$

Now

$$\begin{align*}
c^*dx^i(t_1,t_2)(v_1,v_2) &= \underbrace{dx^i\bigl(c(t_1,t_2)\bigr)}_{=\pi^i}\left[\begin{pmatrix}D_1c^1&D_2c^1\\\vdots&\vdots\\D_1c^n&D_2c^n\end{pmatrix}_{(t_1,t_2)}\begin{pmatrix}v_1\\v_2\end{pmatrix}\right] \\
&= D_1c^i_{(t_1,t_2)}v_1+D_2c^i_{(t_1,t_2)}v_2.
\end{align*}$$

Thus $c^*dx^i=D_1c^i\,dt^1+D_2c^i\,dt^2$. Then we have

$$\begin{align*}
c^*dx^i\wedge c^*dx^j &= (D_1c^i\,dt^1+D_2c^i\,dt^2)\wedge(D_1c^j\,dt^1+D_2c^j\,dt^2) \\
&= (D_1c^i\cdot D_2c^j-D_1c^j\cdot D_2c^i)\,dt^1\wedge dt^2 \\
&= \begin{vmatrix}D_1c^i&D_2c^i\\D_1c^j&D_2c^j\end{vmatrix}\,dt^1\wedge dt^2,
\end{align*}$$

so

$$\begin{align*}
\int_c\omega &= \int_{[0,1]^2}\left[\sum_{i<j}(f^{ij}\circ c)\,\begin{vmatrix}D_1c^i&D_2c^i\\D_1c^j&D_2c^j\end{vmatrix}\right]\,dt^1\wedge dt^2 \\
&= \int_0^1\int_0^1\left[\sum_{i<j}\bigl(f^{ij}\bigl(c(t_1,t_2)\bigr)\bigr)\,\begin{vmatrix}D_1c^i&D_2c^i\\D_1c^j&D_2c^j\end{vmatrix}_{(t_1,t_2)}\right]\,dt^2\,dt^1\quad\text{(by Fubini)}
\end{align*}$$

### The case $k=3,\ldots,n-1$

Same thing: $\int_c\omega$ is a $k$-fold iterated integral of a
weighted sum of $k$-fold determinants of the partial
derivatives. (That's quite a mouthful.)

### The case $k=n$

Lastly I want to draw special attention to this case. We have
$\omega=f\,dx^1\wedge\cdots\wedge dx^n$, and from the same logic we
have

$$\int_c\omega=\int_{[0,1]^k}(f\circ c)\det Dc$$

If $\det Dc\ge0$ then by the change of variables formula it follows that

$$\int_c\omega=\int_{c([0,1]^k)}f$$

This doesn't really say anything new but it's somewhat reassuring.

[^1]: I use $t$ instead of $x$ so as not to confuse the coordinates in $[0,1]^k$ and the coordinates in $\R^n$.