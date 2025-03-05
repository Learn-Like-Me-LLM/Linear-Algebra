from manim import *
import sys
from pathlib import Path

def ScalarMultiplication(self, plane, plane_container, debug: bool = False):
    # DEFINE SCALAR ############################################
    ############################################################
    scalar_title = Text("What is a Scalar?", font_size=40).move_to(ORIGIN)
    scalar_title[7:13].set_color(BLUE)
    
    scalar_definition = Text("...a single real number", font_size=30).next_to(scalar_title, DOWN)
    
    # Create brace under just the "real number" portion
    real_number_part = scalar_definition[-10:]  # Get the "real number" part
    brace = Brace(real_number_part, DOWN)
    
    real_number_def = VGroup(
        Text(
            "any number that can be represented on a number",
            font_size=18,
            slant=ITALIC
        ),
        Text(
            "line including rational & irrational numbers",
            font_size=18,
            slant=ITALIC
        )
    ).arrange(DOWN, buff=0.1).next_to(brace, DOWN)
    
    scalar_definition_group = VGroup(scalar_title, scalar_definition, brace, real_number_def)
    
    # CREATE VECTORS ###########################################
    ############################################################
    vector_a_points = [3, 2]
    
    vector_a = Arrow(
        plane.c2p(0, 0), 
        plane.c2p(vector_a_points[0], vector_a_points[1]), 
        buff=0, color=PURE_GREEN
    )
    vector_a_label = MathTex(f"\\vec{{a}} = [{vector_a_points[0]}, {vector_a_points[1]}]", font_size=30).next_to(plane.c2p(vector_a_points[0], vector_a_points[1]), RIGHT).set_color(PURE_GREEN)

    # CREATE SCALAR ############################################
    ############################################################
    scalar = 2
    scalar_label = VGroup(
        MathTex("scalar_1 = ", font_size=30).set_color(YELLOW),
        MathTex(scalar, font_size=30).next_to(vector_a_label, DOWN).set_color(YELLOW)
    ).arrange(RIGHT)

    scalar_2 = -0.5
    scalar_2_label = VGroup(
        MathTex("scalar_2 = ", font_size=30).set_color(YELLOW),
        MathTex(scalar_2, font_size=30).next_to(scalar_label, DOWN).set_color(YELLOW)
    ).arrange(RIGHT)
    
    vector_labels = VGroup(
        vector_a_label,
        scalar_label,
        scalar_2_label
    ).arrange(DOWN).next_to(plane, DOWN)
    plane_container.add(vector_a, vector_labels)

    # CONFIGURE RESULTING VECTOR(s) ############################
    ############################################################
    vector_a_result = Arrow(
        plane.c2p(0, 0), 
        plane.c2p(vector_a_points[0] * scalar, vector_a_points[1] * scalar), 
        buff=0, color=YELLOW
    )

    vector_a_result_2 = Arrow(
        plane.c2p(0, 0), 
        plane.c2p(vector_a_points[0] * scalar_2, vector_a_points[1] * scalar_2), 
        buff=0, color=RED
    )

    # CONFIGURE FULL SCALAR MULTIPLICATION WALKTHROUGH #########
    ############################################################
    vector_equation = VGroup(
        VGroup(
            MathTex("\\vec{a}", font_size=30).set_color(BLUE),
            MathTex("\\times", font_size=30),
            MathTex("s_1", font_size=30).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {vector_a_points[0]} \\\\ {vector_a_points[1]} \\end{{bmatrix}}", font_size=30).set_color(BLUE),
            MathTex("\\times", font_size=30),
            MathTex(scalar, font_size=30).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {vector_a_points[0]} \\times {scalar} \\\\ {vector_a_points[1]} \\times {scalar} \\end{{bmatrix}}", font_size=30).set_color(WHITE),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {vector_a_points[0] * scalar} \\\\ {vector_a_points[1] * scalar} \\end{{bmatrix}}", font_size=30).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
    ).arrange(DOWN, buff=0.5).to_edge(LEFT, buff=1)
    
    vector_equation_2 = VGroup(
        VGroup(
            MathTex("\\vec{a}", font_size=30).set_color(BLUE),
            MathTex("\\times", font_size=30),
            MathTex("s_2", font_size=30).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {vector_a_points[0]} \\\\ {vector_a_points[1]} \\end{{bmatrix}}", font_size=30).set_color(BLUE),
            MathTex("\\times", font_size=30),
            MathTex(scalar_2, font_size=30).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {vector_a_points[0]} \\times {scalar_2} \\\\ {vector_a_points[1]} \\times {scalar_2} \\end{{bmatrix}}", font_size=30).set_color(WHITE),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {vector_a_points[0] * scalar_2} \\\\ {vector_a_points[1] * scalar_2} \\end{{bmatrix}}", font_size=30).set_color(RED),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
    ).arrange(DOWN, buff=0.5).to_edge(RIGHT, buff=1)

    # ANIMATE ##################################################
    ############################################################
    # ANIMATE > SCALAR 1 #######################################
    self.play(Write(scalar_title))
    self.wait(1.5)
    self.play(Write(scalar_definition))
    self.wait(1.5)
    self.play(Write(brace))
    self.wait(0.25)
    self.play(Write(real_number_def))
    self.wait(1.5)
    self.play(FadeOut(scalar_definition_group))

    self.play(Write(plane))
    self.wait(1.5)
    self.play(Create(vector_a), Write(vector_a_label))
    self.wait(1.5)
    self.play(Write(scalar_label))
    self.wait(1.5)

    self.play(
        TransformFromCopy(vector_a_label, vector_equation[0][0]),
        TransformFromCopy(scalar_label, vector_equation[0][2]),
        FadeIn(vector_equation[0][1])
    )
    self.wait(1.5)
    self.play(
        TransformFromCopy(vector_equation[0][0], vector_equation[1][0]),
        TransformFromCopy(vector_equation[0][2], vector_equation[1][2]),
        FadeIn(vector_equation[1][1])
    )
    self.wait(1.5)
    self.play(
        TransformFromCopy(
            VGroup(
                vector_equation[1][0],
                vector_equation[1][2]
            ), vector_equation[2][0]),
    )
    self.wait(1.5)
    self.play(
        TransformFromCopy(vector_equation[2][0], vector_equation[3][0]),
    )
    self.wait(1.5)
    self.play(
        GrowArrow(vector_a_result)
    )

    # ANIMATE > SCALAR 2 #######################################
    self.play(
        Write(scalar_2_label)
    )
    self.wait(1.5)

    self.play(
        TransformFromCopy(vector_a_label, vector_equation_2[0][0]),
        TransformFromCopy(scalar_2_label, vector_equation_2[0][2]),
        FadeIn(vector_equation_2[0][1])
    )
    self.wait(1.5)
    self.play(
        TransformFromCopy(vector_equation_2[0][0], vector_equation_2[1][0]),
        TransformFromCopy(vector_equation_2[0][2], vector_equation_2[1][2]),
        FadeIn(vector_equation_2[1][1])
    )
    self.wait(1.5)
    self.play(
        TransformFromCopy(
            VGroup(
                vector_equation_2[1][0],
                vector_equation_2[1][2]
            ), vector_equation_2[2][0]),
    )
    self.wait(1.5)
    self.play(
        TransformFromCopy(vector_equation_2[2][0], vector_equation_2[3][0]),
    )
    self.wait(1.5)
    self.play(
        GrowArrow(vector_a_result_2)
    )


    # CLEAN UP #################################################
    ############################################################
    self.play(
        FadeOut(
            vector_a,
            vector_a_label,
            vector_a_result,
            vector_a_result_2,
            scalar_label,
            scalar_2_label,
            vector_equation,
            vector_equation_2
        ), 
        run_time=2)
    return
