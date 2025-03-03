from manim import *
import sys
from pathlib import Path
import numpy as np

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent.parent.parent))

def Subtraction(self, plane, vector_a, vector_b, debug: bool = False):
    # Get vector endpoints in plane coordinates
    a_end = vector_a.get_end()
    b_end = vector_b.get_end()
    
    # Convert scene coordinates back to plane coordinates
    a_components = [int(round(x, 0)) for x in plane.p2c(a_end)]
    b_components = [int(round(x, 0)) for x in plane.p2c(b_end)]
    
    # Calculate result
    c_components = [a_components[0] - b_components[0], a_components[1] - b_components[1]]
    
    # CONFIGURE FULL VECTOR SUBTRACTION WALKTHROUGH ############
    ############################################################
    vector_equation = VGroup(
        VGroup(
            MathTex("\\vec{a}", font_size=30).set_color(BLUE),
            MathTex("-", font_size=30),
            MathTex("\\vec{b}", font_size=30).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex("\\vec{a}", font_size=30).set_color(BLUE),
            MathTex("+", font_size=30),
            MathTex("-\\vec{b}", font_size=30).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {a_components[0]} \\\\ {a_components[1]} \\end{{bmatrix}}", font_size=30).set_color(BLUE),
            MathTex("+", font_size=30),
            MathTex(f"\\begin{{bmatrix}} {b_components[0] * -1} \\\\ {b_components[1] * -1} \\end{{bmatrix}}", font_size=30).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {a_components[0]} + {b_components[0] * -1} \\\\ {a_components[1]} + {b_components[1] * -1} \\end{{bmatrix}}", font_size=30).set_color(GREEN),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {c_components[0]} \\\\ {c_components[1]} \\end{{bmatrix}}", font_size=30).set_color(GREEN),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
    ).arrange(DOWN).to_edge(RIGHT, buff=1)

    commutative_description = VGroup(
        Text("NOT Commutative:", font_size=30).to_edge(LEFT, buff=1),
        MathTex("\\vec{a} - \\vec{b} \\neq \\vec{b} - \\vec{a}", font_size=30).to_edge(LEFT, buff=1),
    ).arrange(DOWN).next_to(vector_equation, DOWN)

    vector_equation_commutative = VGroup(
        VGroup(
            MathTex("\\vec{b}", font_size=30).set_color(YELLOW),
            MathTex("-", font_size=30),
            MathTex("\\vec{a}", font_size=30).set_color(BLUE),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex("\\vec{b}", font_size=30).set_color(YELLOW),
            MathTex("+", font_size=30),
            MathTex("-\\vec{a}", font_size=30).set_color(BLUE),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {b_components[0]} \\\\ {b_components[1]} \\end{{bmatrix}}", font_size=30).set_color(YELLOW),
            MathTex("+", font_size=30),
            MathTex(f"\\begin{{bmatrix}} {a_components[0] * -1} \\\\ {a_components[1] * -1} \\end{{bmatrix}}", font_size=30).set_color(BLUE),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {b_components[0]} + {a_components[0] * -1} \\\\ {b_components[1]} + {a_components[1] * -1} \\end{{bmatrix}}", font_size=30).set_color(GREEN),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
        VGroup(
            MathTex(f"\\begin{{bmatrix}} {b_components[0] + a_components[0] * -1} \\\\ {b_components[1] + a_components[1] * -1} \\end{{bmatrix}}", font_size=30).set_color(GREEN),
        ).arrange(RIGHT, buff=0.5).to_edge(LEFT, buff=1),
    ).arrange(DOWN).to_edge(RIGHT, buff=1)

    # CONFIGURE TIP TO TAIL VISUALIZATION (A) ##################
    ############################################################
    # Create negative vector_a
    vector_a_negative = Arrow(
        plane.c2p(0, 0),  # Start at origin
        plane.c2p(-a_components[0], -a_components[1]),  # Use negative components
        buff=0,
        color=BLUE
    )

    # Create the tip-to-tail version starting at vector_b's tip
    vector_a_tip_to_tail = Arrow(
        vector_b.get_end(),  # Start at tip of vector_b
        vector_b.get_end() + vector_a_negative.get_vector(),  # End at tip + negative vector
        buff=0,
        color=BLUE
    ).set_opacity(0.5)

    resultant_vector_commutative = Arrow(
        plane.c2p(0, 0),
        plane.c2p(-c_components[0], -c_components[1]),
        buff=0,
        color=RED
    )
    
    # CONFIGURE TIP TO TAIL VISUALIZATION (B) ##################
    ############################################################
    # Create negative vector_b 
    vector_b_negative = Arrow(
        plane.c2p(0, 0),  # Start at origin
        plane.c2p(-b_components[0], -b_components[1]),  # Use negative components
        buff=0,
        color=YELLOW
    )

    # Create the tip-to-tail version starting at vector_a's tip
    vector_b_tip_to_tail = Arrow(
        vector_a.get_end(),  # Start at tip of vector_a
        vector_a.get_end() + vector_b_negative.get_vector(),  # End at tip + negative vector
        buff=0,
        color=YELLOW
    ).set_opacity(0.5)

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
        TransformFromCopy(vector_equation[1][0], vector_equation[2][0]),
        TransformFromCopy(vector_equation[1][2], vector_equation[2][2]),
        FadeIn(vector_equation[2][1])
    )
    self.wait(1.5)

    self.play(
        TransformFromCopy(
            VGroup(vector_equation[2][0], vector_equation[2][2]), 
            vector_equation[3][0]
        ),
    )
    self.wait(1.5)

    # Show tip-to-tail method with vector_b moving to tip of vector_a
    self.play(
        TransformFromCopy(vector_b, vector_b_tip_to_tail),
        GrowArrow(resultant_vector),
        TransformFromCopy(
            vector_equation[3][0],
            vector_equation[4][0]
        ),
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
        GrowArrow(resultant_vector_commutative),
    )
    self.wait(1.5)

    # CLEAN UP #################################################
    ############################################################
    self.play(
        FadeOut(
            vector_equation,
            commutative_description,
            vector_a_tip_to_tail,  
            resultant_vector_commutative
        )
    )
    self.wait(1.5)

    return

