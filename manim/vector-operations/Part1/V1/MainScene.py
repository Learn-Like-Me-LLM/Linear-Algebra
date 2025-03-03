from manim import *
import sys
from pathlib import Path

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent))

from Title import Title
from VectorAdditionAndSubraction import VectorAdditionAndSubraction
from ScalarMultiplication import ScalarMultiplication
from utils.make_number_plane import makeNumberPlane

class V1VectorOperationsPart1(Scene):
    def construct(self):
        debug = True

        # TITLE ####################################################
        ############################################################
        titleVGroup = Title(self, debug)

        # VECTOR ADDITION ##########################################
        ############################################################
        # VECTOR ADDITION > UPDATE SUBTITLE
        subtitle = MarkupText(
            'Vector <span color="GREEN">Addition</span> &amp; <span color="RED">Subtraction</span>',
            font_size=20,
            slant=ITALIC
        ).next_to(titleVGroup, DOWN, buff=0.1).align_to(titleVGroup, LEFT)
        
        titleVGroup.add(subtitle)
        self.play(Write(subtitle))
        self.wait(1)

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

        VectorAdditionAndSubraction(self, plane, plane_container, debug)

        # SCALAR MULTIPLICATION ####################################
        ############################################################
        # SCALAR MULTIPLICATION > UPDATE SUBTITLE
        new_subtitle = MarkupText(
            'Scalar <span color="PURPLE">Multiplication</span>',
            font_size=20,
            slant=ITALIC
        ).move_to(subtitle).align_to(titleVGroup, LEFT)
        
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

        thank_you = Text('Thank you for watching!', font_size=40).move_to(ORIGIN)
        self.play(Write(thank_you))
        self.wait(5)
        