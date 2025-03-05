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
            r"\vec{a} \cdot \vec{b} = {a_x} \cdot {b_x} + {a_y} \cdot {b_y} + {a_z} \cdot {b_z} + \dots + {a_n} \cdot {b_n}",
            # font_size=24
        ),
        MathTex(
            r"\vec{a} \cdot \vec{b} = \sum_{i=1}^{n} a_i \cdot b_i",
            # font_size=24
        ),
    ).arrange(DOWN, buff=0.25).move_to(ORIGIN)

    # FULL CALCULATION #########################################
    ############################################################
    calculation = VGroup(
        VGroup(
            MathTex(r"\vec{a}"),
            MathTex(r"\cdot"),
            MathTex(r"\vec{b}"),
        ).arrange(RIGHT, buff=0.25),
        VGroup(
            MathTex(r"\begin{bmatrix}" + f"{a_x_tracker.get_value():.0f}" + r"\\[1pt]" + f"{a_y_tracker.get_value():.0f}" + r"\end{bmatrix}"),
            MathTex(f"\cdot"),
            MathTex(r"\begin{bmatrix}" + f"{b_x_tracker.get_value():.0f}" + r"\\[1pt]" + f"{b_y_tracker.get_value():.0f}" + r"\end{bmatrix}")
        ).arrange(RIGHT, buff=0.25),
        VGroup(
            MathTex(f"({a_x_tracker.get_value():.0f}" + r"\times" + f"{b_x_tracker.get_value():.0f})"),
            Text(r"+"),
            MathTex(f"({a_y_tracker.get_value():.0f}" + r"\times" + f"{b_y_tracker.get_value():.0f})"),
        ).arrange(RIGHT, buff=0.25),
        VGroup(
            MathTex(f"{a_x_tracker.get_value() * b_x_tracker.get_value():.0f}"),
            Text(r"+"),
            MathTex(f"{a_y_tracker.get_value() * b_y_tracker.get_value():.0f}"),
        ).arrange(RIGHT, buff=0.25),
        VGroup(
            MathTex(f"{(a_x_tracker.get_value() * b_x_tracker.get_value()) + (a_y_tracker.get_value() * b_y_tracker.get_value()):.0f}"),
        ).arrange(RIGHT, buff=0.25)
    ).arrange(DOWN, buff=0.25)
    calculation[0][0].set_color(BLUE)
    calculation[0][2].set_color(RED)
    calculation[1][0].set_color(BLUE)
    calculation[1][2].set_color(RED)
    
    calculation.to_edge(LEFT)

    # ANIMATE ##################################################
    ############################################################
    scene.play(Write(example[0]))
    scene.wait(1)
    scene.play(Write(example[1]))
    scene.wait(1)

    # UPDATE SUBTITLE
    new_subtitle = VGroup(
        MarkupText(
            '<span color="PURPLE">Dot Product (Inner Product)</span>',
            font_size=20,
            slant=ITALIC
        ),
        MathTex(
            r"\vec{a} \cdot \vec{b} = \sum_{i=1}^{n} a_i \cdot b_i",
            font_size=25
        ).align_to(LEFT),
    ).arrange(DOWN).next_to(title, DOWN).align_to(title, LEFT)
    
    scene.play(
        Transform(subtitle, new_subtitle),
        Write(example[2])
    )

    scene.play(
        FadeOut(example), 
        run_time=2
    )

    # ANIMATE > Plane & Vectors ################################
    scene.play(Create(plane))
    scene.play(Write(vector_a), Write(vector_b))
    scene.play(Write(vector_labels))
    scene.wait(1)

    count = 0 
    while count < len(calculation):
        scene.play(Write(calculation[count]))
        scene.wait(1)
        count += 1

    # CLEAN UP 
    ############################################################
    scene.play(
        FadeOut(plane, vector_a, vector_b, vector_labels, calculation), 
        run_time=2
    )
