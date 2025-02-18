# Dot Product _(Scalar Product)_

The dot product $\vec{a} \cdot \vec{b}$ has two equivalent definitions:

1. Component-wise multiplication and sum:
   $\vec{a} \cdot \vec{b} = \sum_{i=1}^n a_ib_i$

2. Geometric definition:
   $\vec{a} \cdot \vec{b} = \|\vec{a}\|\|\vec{b}\|\cos(\theta)$

Where $\theta$ is the angle between vectors.

## Key Applications
- Finding angles between vectors: $\theta = \arccos(\frac{\vec{a} \cdot \vec{b}}{\|\vec{a}\|\|\vec{b}\|})$
- Testing perpendicularity: $\vec{a} \perp \vec{b} \iff \vec{a} \cdot \vec{b} = 0$
- Vector projections: $proj_{\vec{b}}\vec{a} = \frac{\vec{a} \cdot \vec{b}}{\|\vec{b}\|^2}\vec{b}$

> [!IMPORTANT]
>
> The dot product is a [SCALAR](./scalar.md) quantity that results from the multiplication of two vectors. It is used to determine the:
> - angle between two vectors
> - projection of one vector onto another

> [!EXAMPLE]
> 
> $\langle \vec{a} * \vec{b}  \rangle = a_1b_1 + a_2b_2 + a_3b_3 +\:... =\sum_{i=1}^3 a_ib_i$

## Inner Product
 
>  a generalization of the dot product. The inner product allows us to define angles between vectors and notions of orthogonality (perpendicularity).