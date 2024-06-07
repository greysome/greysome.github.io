# Solvability by radicals and principal roots


I'll be working over the base field $\Q$. Let's say an element
$\
a\in\C$ is *expressible in radicals* if the extension $\Q(\a)$ lies
within some root tower. That is, $\Q(\a)\s K$, where $K$ lies atop a
tower

$$\eq{
\label{tower}\Q\s K_1\s K_2\s \cdots\s K_n = K,\quad
K_{i+1}=K_i(d_i) \ \ \text{and}\ \ d_i{}^{n_i}=k_i\in K_i.
}$$

Note a polynomial over $\Q$ is solvable in radicals if its root are
expressible in radicals.[^1] Something the reader should note about
the definition is that $d_i$ can be chosen to be any of the $n_i$
roots of $k_i$. Because there is another "pop-mathy" definition of
expressibility in radicals that says $\a$ can be written as an
expression involving whole numbers, the basic arithmetic operations,
and $\sqrt[n]{-}$. Here $\sqrt[n]{-}$ refers to the *principal root*,
which is the root with greatest real part out of all roots with
nonnegative imaginary parts.

[^1]: Not entirely trivial because for each root $\a$ the $K$ containining $\Q(\a)$ may differ, so one has to take the composite of all the $K$'s and show it still admits a root tower. Not hard though.

This definition is basically saying that $\Q(\a)\s K$, where $K$ lies
atop a tower of the form $\eqref{tower}$, where $K_{i+1}=K_i(d_i)$
with $d_i{}^{n_i}=k_i\in K_i$ and $d_i$ is the principal root
$\sqrt[n_i]{k_i}$. Clearly this definition is stronger than the
first. To remove ambiguity, let's say $\a$ satisfying the latter
definition is *expressible in principal roots*. Obviously a primitive
$n$th root of unity is expressible in radicals, but it is not
immediately clear that it is expressible in principal roots---we can't
take $\sqrt[n]{1}$ which would just be 1.

Actually the two definitions can be proven to be equivalent, that is
expressible in radicals $\imp$ expressible in principal roots. In
fact, it clearly suffices to show that every root of unity is
expressible in principal roots.

*Proof.* Let $z_n$ denote a primitive $n$th root of unity. The Galois
  extension $\Q(z_n)/\Q$ has degree $\varphi(n)$ and is abelian hence
  solvable, so $\Q(z_n)$ factors as a tower of cyclic
  extensions. Since $\varphi(n)<n$, by induction we can assume
  $z=z_{\varphi(n)}$ is expressible in principal roots; adjoin it to
  every field $F_i$ in the tower. Thus each extension in the tower
  $F_{i+1}(z)/F_i(z)$ is a radical extension: $F_{i+1}(z) =
  F_i(z,u_i)$ with $u_i{}^{d_i}\in F_i(z)$ and
  $d_i\mid\varphi(n)$. Each $u_i$ can be written as a product of some
  $d_i$th root of unity and a principal root of $F_i$, thus $u_i$ is
  expressible in principal roots. Thus $z_n\in\Q(z,u_1,\ldots,u_k)$ is
  expressible in principal roots as desired. $\qed$