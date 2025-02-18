from manim import *
import sys
from pathlib import Path
import numpy as np

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent.parent.parent))

from utils.make_number_plane import makeNumberPlane
from VectorAddition import Addition
from VectorSubtraction import Subtraction
def VectorAdditionAndSubraction(self, debug: bool = False):
    # CREATE NUMBER PLANE ######################################
    ############################################################
    plane = makeNumberPlane( self, 
                             x_range=[-5, 7, 1], 
                             y_range=[-5, 7, 1], 
                             x_length=3,
                             y_length=3,
                             axis_config={"include_numbers": False},
                             debug=debug)
    plane_container = VGroup(plane).move_to(ORIGIN)

    # CREATE VECTORS ###########################################
    ############################################################
    vector_a_points = [2, 3]
    vector_b_points = [4, -1]
    
    vector_a = Arrow(
        plane.c2p(0, 0), 
        plane.c2p(vector_a_points[0], vector_a_points[1]), 
        buff=0, color=BLUE
    )
    vector_a_label = MathTex(f"\\vec{{a}} = [{vector_a_points[0]}, {vector_a_points[1]}]", font_size=30).next_to(plane.c2p(vector_a_points[0], vector_a_points[1]), RIGHT).set_color(BLUE)
    
    vector_b = Arrow(
        plane.c2p(0, 0), 
        plane.c2p(vector_b_points[0], vector_b_points[1]), 
        buff=0, color=YELLOW
    )
    vector_b_label = MathTex(f"\\vec{{b}} = [{vector_b_points[0]}, {vector_b_points[1]}]", font_size=30).next_to(plane.c2p(vector_b_points[0], vector_b_points[1]), RIGHT).set_color(YELLOW)
    
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
    Addition(self, plane=plane, vector_a=vector_a, vector_b=vector_b)

    # VECTOR SUBTRACTION #######################################
    ############################################################
    Subtraction(self, plane=plane, vector_a=vector_a, vector_b=vector_b)

    return
