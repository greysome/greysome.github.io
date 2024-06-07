# Why quaternion multiplication resembles the cross product


Recall the rules of quaternion multiplication are given by

$$\begin{matrix}
ij=k, & ik=-j, & jk=i \\
ji=-k, & ki=j, & kj=-i.
\end{matrix}$$

If $i,j,k$ are interpreted as the standard basis vectors in $\R^3$,
then multiplication corresponds precisely to the cross product! I've
always wondered why, and I finally managed to find a satisfactory
explanation.

I was directly inspired by wy.22/6/2021 where I derived
$\Aut(Q_8)$. In particular I had the idea of interpreting the product
$ijk$ as the $3\times3$ matrix $I=(i\ j\ k)$, and interpreting the
equality $ijk=-1$ as saying that $I$ has positive orientation. (It is
weird that $-1$ should correspond to positive orientation, but it
doesn't lead to any major problems.)

In general, if $a,b,c$ is a permutation of $i,j,k$ then the sign of
the product $abc$ is equal to (the opposite of) the orientation of the
matrix $(a\ b\ c)$. This is because every permutation can be
decomposed into transpositions, and transpositions flip both the sign
of the product $abc$ and the orientation of $(a\ b\ c)$. For instance,
$ij=-ji$ so $jik=1$, and indeed $(j\ i\ k)$ has negative
orientation. Therefore, for $abc=-1$ to be true, we must have
$c=a\times b$, so that by the property of cross product $(a\ b\ c)$
has positive orientation.

This argument easily generalises if we allow $a,b,c$ to be signed,
i.e. take values in $\{\pm i,\pm j,\pm k\}$.