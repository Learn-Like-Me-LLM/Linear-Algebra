# Dot Product _(Inner Product / Scalar Product)_

> The dot product is a [SCALAR](../../SCALARs/scalar.md) quantity that results from the multiplication of two vectors. It is used to determine the:
> - angle between two vectors
> - projection of one vector onto another

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

## Properties

- Commutative: $\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}$
- Distributive: $\vec{a} \cdot (\vec{b} + \vec{c}) = \vec{a} \cdot \vec{b} + \vec{a} \cdot \vec{c}$
