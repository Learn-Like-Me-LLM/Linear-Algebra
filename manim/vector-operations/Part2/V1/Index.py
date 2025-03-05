from manim import *
import sys
from pathlib import Path

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent))

from Title import Title
from .DotProduct import DotProduct
from utils.make_number_plane import makeNumberPlane

def Part2(self, title, subtitle, debug: bool = False):
    # CREATE NUMBER PLANE ######################################
    ############################################################
    plane = makeNumberPlane( self, 
                                x_range=[-5, 7, 1], 
                                y_range=[-5, 7, 1], 
                                x_length=3,
                                y_length=3,
                                axis_config={"include_numbers": False},
                                debug=debug )
    plane_container = VGroup(plane).move_to(ORIGIN)

    # VECTOR ADDITION ##########################################
    ############################################################
    # VECTOR ADDITION > UPDATE SUBTITLE
    subtitle = MarkupText(
        '<span color="PINK">Dot Product (Inner Product)</span>',
        font_size=20,
        slant=ITALIC
    ).next_to(title, DOWN, buff=0.1).align_to(title, LEFT)
    
    self.play(Write(subtitle))
    self.wait(1)

    # Create dot product demonstration
    DotProduct(self, plane, plane_container, title, subtitle, debug)
    
    # CLEAN UP 
    ############################################################
    mobjects_to_remove = [m for m in self.mobjects]
    self.play(
        FadeOut(*mobjects_to_remove), 
        run_time=2
    )

    