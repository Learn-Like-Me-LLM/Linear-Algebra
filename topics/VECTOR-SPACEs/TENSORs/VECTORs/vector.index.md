---
topic: "vector"
parent_topic: "tensor"
linked_content_manim: [
  {
    "title": "What is a Vector?",
    "google_drive_file_path": "https://drive.google.com/file/d/1qk0Q5V8elFQ6rYOLeb-Tq3A4hquRGXP5/view"
  }
]
---

🟢 _Last Updated: Feb 13, 2025_ 
 
# Vector(s)

> [!IMPORTANT]
>
> ...its an `arrow`... ⬇️ | ⬆️ | ⬅️ | ➡️ | ↙️ | ↘️ | ↖️ | ↗️  
> - OR...an `ordered collections of numbers`    
> - OR...a mathematical entity with both a `magnitude` (_"length"_) and `direction`

## Vector Notation / Representation

- Vectors are represented as `ordered collections of numbers` 
  - each number corresponds to a `coordinate` in a particular `dimension`. 
- Vectors are typically represented in the `standard position` or starting at the `origin (0, 0, 0, ...)` of the dimensional space. 

### VS Point Notation
| Notation | Description | LaTex Example| 
| --- | --- | --- | 
| Vector Notation | `square brackets "[]"` | $\text{Vector: } \vec{v} = \begin{bmatrix} x \\ y \\ z \\ \vdots  \end{bmatrix} = \begin{bmatrix} x & y & z & ... \end{bmatrix}$| 
| Point Notation | `smooth brackets "()"` | $\text{Point: } P = (x,y,z)$ |


## Vector Types

| Type                  | Description | LaTeX Example |
| ---                   | ---                                                       | --- |
| `zero vector`         | A vector with all components equal to zero                | $\vec{0} = \begin{bmatrix} 0 \\ 0 \\ 0 \end{bmatrix}$ |
| `unit vector`         | A vector with a magnitude of 1                            | $\hat{i} = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}$ |
| `position vector`     | A vector that represents a point in space                 | $\vec{r} = \begin{bmatrix} x \\ y \\ z \end{bmatrix}$ |
| `free vector`         | A vector that can be moved without changing their effect  | $\vec{F} = 5\hat{i} + 3\hat{j}$ |
| `bound vector`        | A vector that is anchored at specific points              | $\vec{AB} = \begin{bmatrix} x_2-x_1 \\ y_2-y_1 \\ z_2-z_1 \end{bmatrix}$ |
| `parallel vectors`    | Vectors pointing in the same or opposite directions       | $\vec{a} \parallel \vec{b} \iff \vec{a} = k\vec{b}$ |
| `orthogonal vectors`  | Vectors perpendicular to each other                       | $\vec{a} \perp \vec{b} \iff \vec{a} \cdot \vec{b} = 0$ |
| `basis vectors`       | Set of vectors that span a vector space                   | $\{\hat{i}, \hat{j}, \hat{k}\}$ |
| `normal vector`       | Vector perpendicular to a surface or plane                | $\vec{n} = \begin{bmatrix} a \\ b \\ c \end{bmatrix}$ |
| `displacement vector` | Vector representing change in position                    | $\Delta\vec{r} = \vec{r}_2 - \vec{r}_1$ |

## 🔍 📚ManimCE Review Video(s)

> [!IMPORTANT]
> 
> _The accompanying audiovisual pedagogical presentations, meticulously crafted utilizing the sophisticated [MANIM Community Edition](https://www.manim.community/) framework, constitute an alternative modality through which one might assimilate and synthesize the intricate epistemological elucidations heretofore delineated within this multifaceted compendium of scholarly discourse._

| Video | Description |
| --- | --- |
| [What is a Vector?](https://drive.google.com/file/d/13sFo7jNtF66fKB5wqYcQYrTC0ez574xQ/view?usp=drive_link) | A video that explains what a vector is and how it is represented. |