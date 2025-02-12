🟢 _Last Updated: Feb 04, 2025_
# Vector(s)

> [!IMPORTANT]
>
> A mathematical entity that simultaneously possesses both `magnitude` ("length" or "size") and `direction`. It can be visualized as an arrow in geometric space, pointing to a specific location from its `tail`. 


Vectors are fundamental components of [VECTOR SPACES](./vector-spaces/vector-space.md). In practical applications, especially within data science, vectors are crucial for representing multi-dimensional data succinctly. Each component of a vector can correspond to a feature or variable in datasets.

## Representation / Notation

Vectors are represented as `ordered collections of numbers` _(typically originating in the `standard position` or origin of the dimensional space)_, where each number corresponds to a `coordinate` in a particular `dimension`. 

[VECTOR NOTATION](./notation.md) is a way to represent vectors using square brackets "[]" as opposed to [POINT NOTATION](./notation.md) that uses smooth brackets "()" to represent individual...points... 😉

> [!IMPORTANT]
>
> $\vec{v} = \begin{bmatrix} x \\ y \\ z \\ ...  \end{bmatrix}$

## Vector Types

| Type | Description | LaTeX Example |
| --- | --- | --- |
| `zero vector` | A vector with all components equal to zero | $\vec{0} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$ |
| `unit vector` | A vector with a magnitude of 1 | $\hat{i} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$ |
| `position vector` | A vector that represents a point in space | $\vec{r} = \begin{bmatrix} x \\ y \\ z \end{bmatrix}$ |
| `free vector` | A vector that can be moved without changing their effect | $\vec{F} = 5\hat{i} + 3\hat{j}$ |
| `bound vector` | A vector that is anchored at specific points | $\vec{AB} = \begin{bmatrix} x_2-x_1 \\ y_2-y_1 \\ z_2-z_1 \end{bmatrix}$ |
| `parallel vectors` | Vectors pointing in the same or opposite directions | $\vec{a} \parallel \vec{b} \iff \vec{a} = k\vec{b}$ |
| `orthogonal vectors` | Vectors perpendicular to each other | $\vec{a} \perp \vec{b} \iff \vec{a} \cdot \vec{b} = 0$ |
| `basis vectors` | Set of vectors that span a vector space | $\{\hat{i}, \hat{j}, \hat{k}\}$ |
| `normal vector` | Vector perpendicular to a surface or plane | $\vec{n} = \begin{bmatrix} a \\ b \\ c \end{bmatrix}$ |
| `displacement vector` | Vector representing change in position | $\Delta\vec{r} = \vec{r}_2 - \vec{r}_1$ |
| ...etc. | ...etc.     |