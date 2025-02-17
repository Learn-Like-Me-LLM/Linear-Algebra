---
title: "vector-space"
parent_topic: null
linked_content_manim: [
    {
        "title": "What is a Vector Space?",
        "google_drive_file_path": null
    }
]
---

🟡 _Last Updated: Feb 17, 2025_

# Vector Space(s)

> [!IMPORTANT]
> 
> a vector space is a non-empty `set or field` of vectors that respect a list of fundamental [Axioms](./axioms.md) across 2 categories:  
> - `Additive Properties`  
>   - Closure under addition  
>   - Associativity of addition  
>   - Existence of additive identity  
>   - Existence of additive inverses  
> - `Scalar Multiplication Properties`  
>   - Closure under scalar multiplication  
>   - Compatibility with field addition  
>   - Compatibility with vector addition  
>   - Identity scalar multiplication  

### Functional Properties 

#### Closure

| Name                          | Mathematical Statement                                            | Description                                           | Example | 
| ---                           | ---                                                               | ---                                                   | --- |
| Additive Closure              | For $\vec{u}, \vec{v} \in V$:     <br> $\vec{u} + \vec{v} \in V$  | The sum of any two vectors remains in V               | In $\mathbb{R}^2$: <br> $\begin{bmatrix} 1 \\ 2 \end{bmatrix} + \begin{bmatrix} 3 \\ 4 \end{bmatrix} = \begin{bmatrix} 4 \\ 6 \end{bmatrix} \in \mathbb{R}^2$ |
| Scalar Multiplication Closure | For $a \in F, \vec{u} \in V$:             <br> $a\vec{u} \in V$   | Scaling a vector by a scalar keeps the result in V    | In $\mathbb{R}^2$: <br> $3\begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 6 \\ 3 \end{bmatrix} \in \mathbb{R}^2$ |

#### Axioms

> [Vector Space Axioms](./axioms.md)

### Structural Properties

#### Subspaces
tbd...

#### Linear Independence
tbd...

#### Span
tbd...

#### Basis
tbd...

#### Dimension
tbd...

## Type(s)

### [Real Coordinate Space ($\mathbb{R}^n$)](./real-coordinate-space.md)
The most fundamental and widely-used vector spaces are [real coordinate spaces](./real-coordinate-space.md). These spaces consist of ordered lists of real numbers and provide the foundation for most practical applications of vector spaces. The familiar 2D plane ($\mathbb{R}^2$) and 3D space ($\mathbb{R}^3$) are special cases of these spaces.

[!WARNING]
> 
> There are _many_ more types of vector spaces -- this list will be expanded as we continue to explore the properties of vector spaces.

## Resources


| link | 
| --- | 
| [Abstract vector spaces \| Chapter 16, Essence of linear algebra > (YT : 3Blue1Brown)](https://www.youtube.com/watch?v=TgKwz5Ikpc8) |
| [Understanding Vector Spaces > (YT)](https://www.youtube.com/watch?v=EP2ghkO0lSk) |
| [What is a Vector Space (Abstract Algebra) > (YT)](https://www.youtube.com/watch?v=ozwodzD5bJM) |
| [Vector Spaces \| Definition & Examples > (YT)](https://www.youtube.com/watch?v=72GtkP6nP_A) |
| [Oxford Linear Algebra: What is a Vector Space? > (YT)](https://www.youtube.com/watch?v=draqOOUoWQM) |
