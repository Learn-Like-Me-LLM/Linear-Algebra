from manim import *
import numpy as np

def GenericExample(
        scene: Scene, 
        plane, plane_container, 
        title, subtitle, 
        vector_a, vector_b,
        vector_labels,
        a_x_tracker, a_y_tracker,
        b_x_tracker, b_y_tracker,
        debug: bool = False
    ) -> None:

    # GENERIC EXAMPLE ##########################################
    ############################################################
    example = VGroup(
        VGroup(
            MathTex(
                r"\vec{a} = \begin{bmatrix} {a_x} \\[1pt] {a_y} \\[1pt] {a_z} \\[1pt] \dots \\[1pt] {a_n} \end{bmatrix}",
                # font_size=24
            ),
            MathTex(
                r"\vec{b} = \begin{bmatrix} {b_x} \\[1pt] {b_y} \\[1pt] {b_z} \\[1pt] \dots \\[1pt] {b_n} \end{bmatrix}",
                # font_size=24
            )
        ).arrange(RIGHT, buff=0.25),
        MathTex(
            r"\vec{a} \cdot \vec{b} = ({a_x} \cdot {b_x}) + ({a_y} \cdot {b_y}) + ({a_z} \cdot {b_z}) + \dots + ({a_n} \cdot {b_n})",
            # font_size=24
        ),
        MathTex(
            r"\vec{a} \cdot \vec{b} = \sum_{i=1}^{n} a_i \cdot b_i",
            # font_size=24
        ),
    ).arrange(DOWN, buff=0.25).move_to(ORIGIN)
    
    # ANIMATE ##################################################
    ############################################################
    count = 0
    while count < len(example):
        scene.play(Write(example[count]))
        scene.wait(1)
        count += 1

    formula = MathTex(
        r"\vec{a} \cdot \vec{b} = \sum_{i=1}^{n} a_i \cdot b_i",
        font_size=25
    ).arrange(DOWN).next_to(plane, UP, buff=0.25)
    
    scene.play(
        FadeOut(example), 
        TransformFromCopy(
            example[2], 
            formula,
        ),
        run_time=2
    )

    # ANIMATE > Plane & Vectors ################################
    scene.play(Create(plane))
    scene.play(Write(vector_a), Write(vector_b))
    scene.play(Write(vector_labels))
    scene.wait(1)

    # CLEAN UP 
    ############################################################
