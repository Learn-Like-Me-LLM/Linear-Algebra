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

    formula = VGroup(
        VGroup(
            MathTex(r"\vec{a}").set_color(PURE_GREEN),
            MathTex(r"\cdot"),
            MathTex(r"\vec{b}").set_color(YELLOW),
        ).arrange(RIGHT, buff=0.1),
        Text("="),
        VGroup(
            MathTex(r"\sum_{i=1}^{n}"),
            VGroup(
                MathTex(r"a_i").set_color(PURE_GREEN),
                MathTex(r"\cdot"),
                MathTex(r"b_i").set_color(YELLOW),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.1),
    ).arrange(RIGHT, buff=0.1)
    

    example = VGroup(
        VGroup(
            MathTex(
                r"\vec{a} = \begin{bmatrix} {a_x} \\[1pt] {a_y} \\[1pt] {a_z} \\[1pt] \dots \\[1pt] {a_n} \end{bmatrix}",
                # font_size=24
            ).set_color(PURE_GREEN),
            MathTex(
                r"\vec{b} = \begin{bmatrix} {b_x} \\[1pt] {b_y} \\[1pt] {b_z} \\[1pt] \dots \\[1pt] {b_n} \end{bmatrix}",
                # font_size=24
            ).set_color(YELLOW)
        ).arrange(RIGHT, buff=0.25),
        VGroup(
            VGroup(
                MathTex(r"\vec{a}").set_color(PURE_GREEN),
                MathTex(r"\cdot"),
                MathTex(r"\vec{b}").set_color(YELLOW),
            ).arrange(RIGHT, buff=0.1),
            Text("="),
            VGroup(
                Text("("),
                MathTex(r"{a_x}").set_color(PURE_GREEN),
                MathTex(r"\cdot"),
                MathTex(r"{b_x}").set_color(YELLOW),
                Text(")"),
                MathTex(r" + "),
                Text("("),
                MathTex(r"{a_y}").set_color(PURE_GREEN),
                MathTex(r"\cdot"),
                MathTex(r"{b_y}").set_color(YELLOW),
                Text(")"),
                MathTex(r" + "),
                Text("("),
                MathTex(r"{a_z}").set_color(PURE_GREEN),
                MathTex(r"\cdot"),
                MathTex(r"{b_z}").set_color(YELLOW),
                Text(")"),
                MathTex(r" + "),
                MathTex(r"\dots"),
                MathTex(r" + "),
                Text("("),
                MathTex(r"{a_n}").set_color(PURE_GREEN),
                MathTex(r"\cdot"),
                MathTex(r"{b_n}").set_color(YELLOW),
                Text(")"),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.1),
        formula,
    ).arrange(DOWN, buff=0.25).move_to(ORIGIN)
    
    # ANIMATE ##################################################
    ############################################################
    count = 0
    while count < len(example):
        scene.play(Write(example[count]))
        scene.wait(1)
        count += 1

    scene.play(
        FadeOut(example[0:2]),
        example[2].animate.scale(0.6).next_to(plane, UP, buff=0.25),
        run_time=2
    )

    # ANIMATE > Plane & Vectors ################################
    scene.play(Create(plane))
    scene.play(Write(vector_a), Write(vector_b))
    scene.play(Write(vector_labels))
    scene.wait(1)

    # CLEAN UP 
    ############################################################
