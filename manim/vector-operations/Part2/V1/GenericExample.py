from manim import *
import numpy as np

def GenericExample(
        scene: Scene, 
        plane,
        font_size: int = 35,
        debug: bool = True
    ) -> None:
    # GENERIC EXAMPLE ##########################################
    ############################################################
    dot_product_definition = VGroup(
        VGroup(
            Text("a", font_size=font_size*0.75),
            Text("single number (scalar)", slant=ITALIC, font_size=font_size*0.75).set_color(ORANGE),
            Text("representing", font_size=font_size*0.75),
        ).arrange(RIGHT, buff=0.1),
        Text("how closely aligned or perpendicular 2 vectors are", font_size=font_size*0.75)
    ).arrange(DOWN, buff=0.1)

    dot_product_formula = VGroup(
        VGroup(
            MathTex(r"\vec{a}", font_size=font_size).set_color(PURE_GREEN),
            MathTex(r"\cdot", font_size=font_size),
            MathTex(r"\vec{b}", font_size=font_size).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.1),
        Text("=", font_size=font_size),
        VGroup(
            MathTex(r"\sum_{i=1}^{n}", font_size=font_size),
            VGroup(
                MathTex(r"a_i", font_size=font_size).set_color(PURE_GREEN),
                MathTex(r"\cdot", font_size=font_size),
                MathTex(r"b_i", font_size=font_size).set_color(YELLOW),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.1),
    ).arrange(RIGHT, buff=0.1)

    example = VGroup(
        dot_product_definition,
        VGroup(
            VGroup(
                MathTex(r"\vec{a}", font_size=font_size).set_color(PURE_GREEN),
                Text("=", font_size=font_size),
                MathTex(
                    r"\begin{bmatrix} {a_x} \\[1pt] {a_y} \\[1pt] {a_z} \\[1pt] \dots \\[1pt] {a_n} \end{bmatrix}", font_size=font_size
                ).set_color(PURE_GREEN),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"\vec{b}", font_size=font_size).set_color(YELLOW),
                Text("=", font_size=font_size),
                MathTex(
                    r"\begin{bmatrix} {b_x} \\[1pt] {b_y} \\[1pt] {b_z} \\[1pt] \dots \\[1pt] {b_n} \end{bmatrix}",
                    font_size=font_size
                ).set_color(YELLOW)
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.25),
        VGroup(
            VGroup(
                MathTex(r"\vec{a}", font_size=font_size).set_color(PURE_GREEN),
                MathTex(r"\cdot", font_size=font_size),
                MathTex(r"\vec{b}", font_size=font_size).set_color(YELLOW),
            ).arrange(RIGHT, buff=0.1),
            Text("=", font_size=font_size),
            VGroup(
                Text("(", font_size=font_size),
                MathTex(r"{a_x}", font_size=font_size).set_color(PURE_GREEN),
                MathTex(r"\cdot", font_size=font_size),
                MathTex(r"{b_x}", font_size=font_size).set_color(YELLOW),
                Text(")", font_size=font_size),
                MathTex(r" + ", font_size=font_size),
                Text("(", font_size=font_size),
                MathTex(r"{a_y}", font_size=font_size).set_color(PURE_GREEN),
                MathTex(r"\cdot", font_size=font_size),
                MathTex(r"{b_y}", font_size=font_size).set_color(YELLOW),
                Text(")", font_size=font_size),
                MathTex(r" + ", font_size=font_size),
                Text("(", font_size=font_size),
                MathTex(r"{a_z}", font_size=font_size).set_color(PURE_GREEN),
                MathTex(r"\cdot", font_size=font_size),
                MathTex(r"{b_z}", font_size=font_size).set_color(YELLOW),
                Text(")", font_size=font_size),
                MathTex(r" + ", font_size=font_size),
                MathTex(r"\dots", font_size=font_size),
                MathTex(r" + ", font_size=font_size),
                Text("(", font_size=font_size),
                MathTex(r"{a_n}", font_size=font_size).set_color(PURE_GREEN),
                MathTex(r"\cdot", font_size=font_size),
                MathTex(r"{b_n}", font_size=font_size).set_color(YELLOW),
                Text(")", font_size=font_size),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.1),
        dot_product_formula,
    ).arrange(DOWN, buff=0.25).move_to(ORIGIN)
    
    # ANIMATE ##################################################
    ############################################################
    count = 0
    while count < len(example):
        scene.play(Write(example[count]))
        scene.wait(1)
        count += 1

    scene.play(
        FadeOut(example[0:3]),
        example[3].animate.scale(0.75).next_to(plane, UP, buff=0.25),
        run_time=2
    )