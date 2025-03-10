from manim import *
import sys
from pathlib import Path

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent))

from Title import Title
from utils.make_number_plane import makeNumberPlane

def Part3(self, title, subtitle, debug: bool = False):
    # CREATE NUMBER PLANE ######################################
    ############################################################
    plane = makeNumberPlane(self, 
                            x_range=[-5, 5, 1], 
                            y_range=[-5, 5, 1], 
                            x_length=3,
                            y_length=3,
                            axis_config={"include_numbers": False},
                            debug=debug)
    plane_container = VGroup(plane).move_to(ORIGIN)

    # CROSS PRODUCT ############################################
    ############################################################
    # CROSS PRODUCT > UPDATE SUBTITLE
    subtitle = Text("Cross Product (Vector Product)", font_size=20, color=BLUE).next_to(title, DOWN, buff=0.1).align_to(title, LEFT)
    
    self.play(Write(subtitle))
    self.wait(1)