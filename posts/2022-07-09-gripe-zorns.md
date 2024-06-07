# A small gripe on Zorn's lemma

Recall the usual proof that commutative rings have maximal ideals:
every chain of ideals has an upper bound (their union), and apply
Zorn's. However, I always found this unsatisfying because there
doesn't seem to be a relationship between the maximal ideal's
existence and the union construction; it feels somewhat indirect. I
find it cleaner to identify a maximal chain of ideals and directly
construct the maximal ideal as the union. The claim that every poset
has a maximal chain[^1] is called the *Hausdorff Maximality Principle*
and fortunately it is almost trivially equal to Zorn's.

1. HMP $\imp$ Zorn's  
Suppose every chain has an upper bound. By hypothesis there is a
maximal chain, and its upper bound is a maximal element.

2. Zorn's $\imp$ HMP  
Consider the poset $P$ of chains under the subset relation. Every
chain in $P$ has an upper bound, which is its union; thus by Zorn's
there is a maximal element in $P$ which is a maximal chain.

[^1]: Note that actually a cofinal chain suffices and the maximal chain can be realised as its downward closure.