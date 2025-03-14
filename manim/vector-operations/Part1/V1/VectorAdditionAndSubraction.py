from manim import *
import sys
from pathlib import Path
import numpy as np

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent.parent.parent))

from .VectorAddition import Addition
from .VectorSubtraction import Subtraction
def VectorAdditionAndSubraction(self, plane, plane_container, debug: bool = False):
    # CREATE VECTORS ###########################################
    ############################################################
    vector_a_points = [1, 2]
    vector_b_points = [3, -1]
    
    vector_a = Arrow(
        plane.c2p(0, 0), 
        plane.c2p(vector_a_points[0], vector_a_points[1]), 
        buff=0, color=PURE_GREEN
    )
    vector_a_label = MathTex(
        f"\\vec{{a}} = [{vector_a_points[0]}, {vector_a_points[1]}]", 
        font_size=30
    ).next_to(plane.c2p(vector_a_points[0], vector_a_points[1]), RIGHT).set_color(PURE_GREEN)
    
    vector_b = Arrow(
        plane.c2p(0, 0), 
        plane.c2p(vector_b_points[0], vector_b_points[1]), 
        buff=0, color=YELLOW
    )
    vector_b_label = MathTex(
        f"\\vec{{b}} = [{vector_b_points[0]}, {vector_b_points[1]}]", 
        font_size=30
    ).next_to(plane.c2p(vector_b_points[0], vector_b_points[1]), RIGHT).set_color(YELLOW)
    
    vector_labels = VGroup(vector_a_label, vector_b_label).arrange(DOWN, buff=0.1).next_to(plane, DOWN)
    plane_container.add(vector_a, vector_b, vector_labels)

    self.play(Write(plane))
    self.wait(1.5)
    self.play(Create(vector_a), Write(vector_a_label))
    self.wait(1.5)
    self.play(Create(vector_b), Write(vector_b_label))
    self.wait(1.5)

    # VECTOR ADDITION ##########################################
    ############################################################
    Addition(self, plane=plane, vector_a=vector_a, vector_b=vector_b)

    # VECTOR SUBTRACTION #######################################
    ############################################################
    Subtraction(self, plane=plane, vector_a=vector_a, vector_b=vector_b)

    # CLEAN UP #################################################
    ############################################################
    self.play(
        FadeOut(
            plane,
            vector_a,
            vector_b,
            vector_labels,
        ), 
        run_time=2
    )

    return
