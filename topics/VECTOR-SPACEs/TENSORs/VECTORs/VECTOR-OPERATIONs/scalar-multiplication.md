# Scalar Multiplication

Scalar multiplication $c\vec{v}$ scales a vector by a real number:

$c\vec{v} = \begin{bmatrix} cv_1 \\ cv_2 \\ \vdots \\ cv_n \end{bmatrix}$

## Properties

1. Distributive over vector addition:
   $c(\vec{v} + \vec{w}) = c\vec{v} + c\vec{w}$

2. Distributive over scalar addition:
   $(c + d)\vec{v} = c\vec{v} + d\vec{v}$

3. Associative with scalar multiplication:
   $c(d\vec{v}) = (cd)\vec{v}$

## Geometric Interpretation
- For $c > 0$: Vector length is stretched by factor $c$
- For $c < 0$: Vector is reversed and stretched by $|c|$
- For $c = 0$: Vector becomes zero vector
- For $|c| < 1$: Vector is shortened

## Examples

### Scaling by $\frac{1}{3}$ (Shortening)
$\frac{1}{3}\begin{bmatrix} 9 \\ 3 \end{bmatrix} = \begin{bmatrix} 3 \\ 1 \end{bmatrix}$

### Scaling by $2$ (Stretching)
$2\begin{bmatrix} 2 \\ -3 \end{bmatrix} = \begin{bmatrix} 4 \\ -6 \end{bmatrix}$

### Scaling by $-1$ (Reversing)
$-1\begin{bmatrix} 2 \\ 3 \end{bmatrix} = \begin{bmatrix} -2 \\ -3 \end{bmatrix}$