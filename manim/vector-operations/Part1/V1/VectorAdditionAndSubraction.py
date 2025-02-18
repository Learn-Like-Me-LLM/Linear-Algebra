from manim import *
import sys
from pathlib import Path
import numpy as np

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent.parent.parent))

from utils.make_number_plane import makeNumberPlane

def VectorAdditionAndSubraction(self, debug: bool = False):
    # CREATE NUMBER PLANE ######################################
    ############################################################
    plane = makeNumberPlane( self, 
                             x_range=[-3, 10, 1], 
                             y_range=[-3, 8, 1], 
                             x_length=3,
                             y_length=3,
                             axis_config={"include_numbers": False},
                             debug=debug)
    plane_container = VGroup(plane).move_to(ORIGIN)

    # CREATE VECTORS ###########################################
    ############################################################
    vector_a = Arrow(plane.c2p(0, 0), plane.c2p(3, 5), buff=0, color=BLUE)
    vector_a_label = MathTex("\\vec{a} = [3, 5]", font_size=30).next_to(plane.c2p(3, 5), RIGHT).set_color(BLUE)
    
    vector_b = Arrow(plane.c2p(0, 0), plane.c2p(7, -2), buff=0, color=YELLOW)
    vector_b_label = MathTex("\\vec{b} = [7, -2]", font_size=30).next_to(plane.c2p(7, -2), RIGHT).set_color(YELLOW)
    
    vector_labels = VGroup(vector_a_label, vector_b_label).arrange(DOWN).next_to(plane, DOWN)
    plane_container.add(vector_a, vector_b, vector_labels)

    self.play(Write(plane))
    self.wait(1.5)
    self.play(Create(vector_a), Write(vector_a_label))
    self.wait(1.5)
    self.play(Create(vector_b), Write(vector_b_label))
    self.wait(1.5)

    # VECTOR ADDITION ##########################################
    ############################################################
    vector_equation = VGroup(
        VGroup(
            MathTex("\\vec{a}", font_size=30).set_color(BLUE),
            MathTex("+", font_size=30),
            MathTex("\\vec{b}", font_size=30).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex("\\begin{bmatrix} 3 \\\\ 5 \\end{bmatrix}", font_size=30).set_color(BLUE),
            MathTex("+", font_size=30),
            MathTex("\\begin{bmatrix} 7 \\\\ -2 \\end{bmatrix}", font_size=30).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex("\\begin{bmatrix} 3 + 7 \\\\ 5 + (-2) \\end{bmatrix}", font_size=30).set_color(GREEN),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex("\\begin{bmatrix} 10 \\\\ 3 \\end{bmatrix}", font_size=30).set_color(GREEN),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
    ).arrange(DOWN).to_edge(LEFT, buff=1)

    vector_b_dashed = vector_b.copy().set_stroke(opacity=0.5)
    # Get the end point of vector_a to use as start point for vector_b_dashed
    start_point = vector_a.get_end()
    end_point = start_point + vector_b.get_vector()
    vector_b_dashed.put_start_and_end_on(start_point, end_point)

    vector_c = Arrow(plane.c2p(0, 0), plane.c2p(10, 3), buff=0, color=GREEN).set_stroke(opacity=0.5)
    vector_c_label = MathTex("\\vec{c} = [10, 3]", font_size=30).next_to(plane.c2p(10, 3), RIGHT).set_color(GREEN)

    # ANIMATE ##################################################
    ############################################################

    
    # ANIMATE > initial vector LaTex
    self.play(
        TransformFromCopy(vector_a, vector_equation[0][0]),
        TransformFromCopy(vector_b, vector_equation[0][2]),
        FadeIn(vector_equation[0][1])
    )
    self.wait(1.5)

    # ANIMATE > actual vector notation LaTex
    self.play(
        TransformFromCopy(vector_equation[0][0], vector_equation[1][0]),
        TransformFromCopy(vector_equation[0][2], vector_equation[1][2]),
        FadeIn(vector_equation[1][1])
    )
    self.wait(1.5)
    
    self.play(
        TransformFromCopy(VGroup(vector_equation[1][0], vector_equation[1][2]), vector_equation[2][0]),
    )
    self.wait(1.5)

    # ANIMATE > dashed vector
    self.play(
        TransformFromCopy(vector_b, vector_b_dashed),
    )
    self.wait(.5)

    self.play(
        Write(vector_c),
        FadeIn(vector_equation[3][0])
    )
    self.wait(1.5)

    # REMOVE VECTOR ADDITION 1 #################################
    ############################################################
    self.play(
        FadeOut(vector_c, vector_b_dashed)
    )
    self.wait(1.5)

    # CLEAN UP ################################################
    ###########################################################
    self.play(
        FadeOut(plane_container, vector_equation), 
        run_time=2
    )

    return
