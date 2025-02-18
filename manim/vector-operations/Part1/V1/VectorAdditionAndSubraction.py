from manim import *
import sys
from pathlib import Path
import numpy as np

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent.parent.parent))

from utils.make_number_plane import makeNumberPlane

def Addition(self, plane, vector_a, vector_b, debug: bool = False):
    # Get vector endpoints in plane coordinates
    a_end = vector_a.get_end()
    b_end = vector_b.get_end()
    
    # Convert scene coordinates back to plane coordinates
    a_components = [int(round(x, 0)) for x in plane.p2c(a_end)]
    b_components = [int(round(x, 0)) for x in plane.p2c(b_end)]
    
    if debug:
        print(f"Vector A components: {a_components}")
        print(f"Vector B components: {b_components}")
    
    # Calculate result
    c_components = [a_components[0] + b_components[0], a_components[1] + b_components[1]]

    # CONFIGURE FULL VECTOR ADDITION WALKTHROUGH ###############
    ############################################################
    vector_equation = VGroup(
        VGroup(
            MathTex("\\vec{a}", font_size=30).set_color(BLUE),
            MathTex("+", font_size=30),
            MathTex("\\vec{b}", font_size=30).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {a_components[0]} \\\\ {a_components[1]} \\end{{bmatrix}}", font_size=30).set_color(BLUE),
            MathTex("+", font_size=30),
            MathTex(f"\\begin{{bmatrix}} {b_components[0]} \\\\ {b_components[1]} \\end{{bmatrix}}", font_size=30).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {a_components[0]} + {b_components[0]} \\\\ {a_components[1]} + {b_components[1]} \\end{{bmatrix}}", font_size=30).set_color(GREEN),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {c_components[0]} \\\\ {c_components[1]} \\end{{bmatrix}}", font_size=30).set_color(GREEN),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
    ).arrange(DOWN).to_edge(LEFT, buff=1)

    commutative_description = VGroup(
        Text("Commutative Property:", font_size=30).to_edge(LEFT, buff=1),
        MathTex("\\vec{a} + \\vec{b} = \\vec{b} + \\vec{a}", font_size=30).to_edge(LEFT, buff=1),
    ).arrange(DOWN).next_to(vector_equation, DOWN)

    vector_equation_commutative = VGroup(
        VGroup(
            MathTex("\\vec{b}", font_size=30).set_color(YELLOW),
            MathTex("+", font_size=30),
            MathTex("\\vec{a}", font_size=30).set_color(BLUE),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {b_components[0]} \\\\ {b_components[1]} \\end{{bmatrix}}", font_size=30).set_color(YELLOW),
            MathTex("+", font_size=30),
            MathTex(f"\\begin{{bmatrix}} {a_components[0]} \\\\ {a_components[1]} \\end{{bmatrix}}", font_size=30).set_color(BLUE),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {b_components[0]} + {a_components[0]} \\\\ {b_components[1]} + {a_components[1]} \\end{{bmatrix}}", font_size=30).set_color(GREEN),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {c_components[0]} \\\\ {c_components[1]} \\end{{bmatrix}}", font_size=30).set_color(GREEN),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
    ).arrange(DOWN).to_edge(LEFT, buff=1)

    # CONFIGURE TIP TO TAIL VISUALIZATION (A) ##################
    ############################################################
    vector_a_tip_to_tail = vector_a.copy().set_opacity(0.5)
    vector_a_tip_to_tail.shift(vector_b.get_vector())
    
    # CONFIGURE TIP TO TAIL VISUALIZATION (B) ##################
    ############################################################
    vector_b_tip_to_tail = vector_b.copy().set_opacity(0.5)
    vector_b_tip_to_tail.shift(vector_a.get_vector())

    # CONFIGURE RESULTANT VECTOR ###############################
    ############################################################
    resultant_vector = Arrow(
        plane.c2p(0, 0),  # Start at origin
        plane.c2p(c_components[0], c_components[1]),  # End at sum of components
        buff=0,
        color=GREEN
    )
    
    # ANIMATE ##################################################
    ############################################################
    self.play(
        TransformFromCopy(vector_a, vector_equation[0][0]),
        TransformFromCopy(vector_b, vector_equation[0][2]),
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
            VGroup(vector_equation[1][0], vector_equation[1][2]), 
            vector_equation[2][0]
        ),
    )
    self.wait(1.5)

    # Show tip-to-tail method with vector_b moving to tip of vector_a
    self.play(
        TransformFromCopy(vector_b, vector_b_tip_to_tail),
        GrowArrow(resultant_vector),
        TransformFromCopy(vector_equation[2][0], vector_equation[3][0]),
    )
    self.wait(1.5)
    
    self.play(
        Write(commutative_description),
    )
    self.wait(1.5)

    self.play(
        Transform(vector_equation, vector_equation_commutative),
        FadeOut(
            vector_b_tip_to_tail,  
            resultant_vector
        )
    )
    self.wait(1.5)

    # Show tip-to-tail method with vector_b moving to tip of vector_a
    self.play(
        TransformFromCopy(vector_a, vector_a_tip_to_tail),
        GrowArrow(resultant_vector),
    )
    self.wait(1.5)

    # CLEAN UP #################################################
    ############################################################
    self.play(
        FadeOut(
            vector_equation,
            commutative_description,
            vector_a_tip_to_tail,  
            resultant_vector
        )
    )
    self.wait(1.5)

    return

def Subtraction(self, debug: bool = False):
    pass

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

    # NEW VECTOR ADDITION ######################################
    ############################################################
    Addition(self, plane=plane, vector_a=vector_a, vector_b=vector_b)

    # # COMMUTATIVE PROPERTY #####################################
    # ############################################################
    # # vector_commutative_property = VGroup(
    # #     MathTex("\\vec{a} + \\vec{b} = \\vec{b} + \\vec{a}", font_size=30).to_edge(LEFT, buff=1),
    # # ).arrange(DOWN).to_edge(LEFT, buff=1)

    return
