from manim import *
import sys
from pathlib import Path

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent))

from Title import Title
from .VectorAdditionAndSubraction import VectorAdditionAndSubraction
from .ScalarMultiplication import ScalarMultiplication
from utils.make_number_plane import makeNumberPlane

def Part1(self, title, subtitle, debug: bool = False):
    # CREATE NUMBER PLANE ######################################
    ############################################################
    plane = makeNumberPlane( self, 
                                x_range=[-5, 5, 1], 
                                y_range=[-5, 5, 1], 
                                x_length=3,
                                y_length=3,
                                axis_config={"include_numbers": False},
                                debug=debug )
    plane_container = VGroup(plane).move_to(ORIGIN)

    VectorAdditionAndSubraction(self, plane, plane_container, debug)

    # SCALAR MULTIPLICATION ####################################
    ############################################################
    # SCALAR MULTIPLICATION > UPDATE SUBTITLE
    new_subtitle = VGroup(
        Text("Scalar", font_size=20, slant=ITALIC),
        Text("Multiplication", font_size=20, slant=ITALIC, color=BLUE),
    ).arrange(RIGHT, buff=0.1).move_to(subtitle).align_to(title, LEFT)
    
    self.play(Transform(subtitle, new_subtitle))
    self.wait(1)

    ScalarMultiplication(self, plane, plane_container, debug)

    # CLEAN UP 
    ############################################################
    mobjects_to_remove = [m for m in self.mobjects]
    self.play(
        FadeOut(*mobjects_to_remove), 
        run_time=2
    )
 