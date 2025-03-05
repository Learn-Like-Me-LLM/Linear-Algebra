from manim import *
import sys
from pathlib import Path
import numpy as np

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent.parent.parent))

def Addition(self, plane, vector_a, vector_b, debug: bool = False):
    # Get vector endpoints in plane coordinates
    a_end = vector_a.get_end()
    b_end = vector_b.get_end()
    
    # Convert scene coordinates back to plane coordinates
    a_components = [int(round(x, 0)) for x in plane.p2c(a_end)]
    b_components = [int(round(x, 0)) for x in plane.p2c(b_end)]
    
    # Calculate result
    c_components = [a_components[0] + b_components[0], a_components[1] + b_components[1]]

    # CONFIGURE FULL VECTOR ADDITION WALKTHROUGH ###############
    ############################################################
    vector_equation = VGroup(
        VGroup(
            MathTex("\\vec{a}", font_size=30).set_color(PURE_GREEN),
            MathTex("+", font_size=30),
            MathTex("\\vec{b}", font_size=30).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {a_components[0]} \\\\ {a_components[1]} \\end{{bmatrix}}", font_size=30).set_color(PURE_GREEN),
            MathTex("+", font_size=30),
            MathTex(f"\\begin{{bmatrix}} {b_components[0]} \\\\ {b_components[1]} \\end{{bmatrix}}", font_size=30).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {a_components[0]} + {b_components[0]} \\\\ {a_components[1]} + {b_components[1]} \\end{{bmatrix}}", font_size=30).set_color(WHITE),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {c_components[0]} \\\\ {c_components[1]} \\end{{bmatrix}}", font_size=30).set_color(WHITE),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
    ).arrange(DOWN).to_edge(LEFT, buff=1)

    commutative_description = VGroup(
        Text("Commutative:", font_size=30).to_edge(LEFT, buff=1).set_color(BLUE),
        MathTex("\\vec{a} + \\vec{b} = \\vec{b} + \\vec{a}", font_size=30).to_edge(LEFT, buff=1).set_color(BLUE),
    ).arrange(DOWN).next_to(vector_equation, DOWN)

    vector_equation_commutative = VGroup(
        VGroup(
            MathTex("\\vec{b}", font_size=30).set_color(YELLOW),
            MathTex("+", font_size=30),
            MathTex("\\vec{a}", font_size=30).set_color(PURE_GREEN),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {b_components[0]} \\\\ {b_components[1]} \\end{{bmatrix}}", font_size=30).set_color(YELLOW),
            MathTex("+", font_size=30),
            MathTex(f"\\begin{{bmatrix}} {a_components[0]} \\\\ {a_components[1]} \\end{{bmatrix}}", font_size=30).set_color(PURE_GREEN),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {b_components[0]} + {a_components[0]} \\\\ {b_components[1]} + {a_components[1]} \\end{{bmatrix}}", font_size=30).set_color(WHITE),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {c_components[0]} \\\\ {c_components[1]} \\end{{bmatrix}}", font_size=30).set_color(WHITE),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
    ).arrange(DOWN).to_edge(LEFT, buff=1)

    # CONFIGURE TIP TO TAIL VISUALIZATION (A) ##################
    ############################################################
    vector_a_tip_to_tail = vector_a.copy().set_opacity(0.5)
    vector_a_tip_to_tail.shift(vector_b.get_vector())
    
    # CONFIGURE TIP TO TAIL VISUALIZATION (B) ##################
    ############################################################
    vector_b_tip_to_tail = Arrow(
        vector_a.get_end(),  # Start at tip of vector_a
        vector_a.get_end() + vector_b.get_vector(),  # Use vector_b's vector directly
        buff=0,
        color=YELLOW
    ).set_opacity(0.5)

    # CONFIGURE RESULTANT VECTOR ###############################
    ############################################################
    resultant_vector = Arrow(
        plane.c2p(0, 0),  # Start at origin
        plane.c2p(c_components[0], c_components[1]),  # End at sum of components
        buff=0,
        color=WHITE
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

