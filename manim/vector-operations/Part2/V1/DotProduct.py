from manim import *

def DotProduct(scene: Scene, plane, plane_container, debug: bool = False) -> None:
    # Create vectors
    vector_a = Arrow(
        plane.c2p(0, 0),
        plane.c2p(2, 1),
        buff=0,
        color=BLUE
    )
    vector_b = Arrow(
        plane.c2p(0, 0),
        plane.c2p(1, 2),
        buff=0,
        color=RED
    )
    
    # Labels
    label_a = MathTex(r"\vec{a}", color=BLUE).next_to(vector_a.get_end(), RIGHT)
    label_b = MathTex(r"\vec{b}", color=RED).next_to(vector_b.get_end(), UP)
    
    # Dot product formula
    dot_product = MathTex(
        r"\vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}| \cos(\theta)",
        color=WHITE
    ).to_edge(UP)
    
    # Animation sequence
    scene.play(Create(plane))
    scene.play(
        Create(vector_a),
        Create(vector_b),
        Write(label_a),
        Write(label_b)
    )
    scene.wait(1)
    
    # Show angle between vectors
    angle = Angle(vector_a, vector_b, radius=0.5, color=YELLOW)
    angle_label = MathTex(r"\theta", color=YELLOW).next_to(angle, RIGHT, buff=0.1)
    
    scene.play(
        Create(angle),
        Write(angle_label)
    )
    scene.wait(1)
    
    # Show dot product formula
    scene.play(Write(dot_product))
    scene.wait(2)
    
    # Calculate actual dot product
    result = MathTex(
        r"\vec{a} \cdot \vec{b} = (2,1) \cdot (1,2) = 2(1) + 1(2) = 4",
        color=GREEN
    ).next_to(dot_product, DOWN)
    
    scene.play(Write(result))
    scene.wait(2)

    if debug:
        scene.wait(5)
