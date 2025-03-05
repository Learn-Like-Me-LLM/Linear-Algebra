from manim import *
import sys
from pathlib import Path

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent))

from Part1.V1.Index import Part1
from Part2.V1.Index import Part2

from Title import Title

class VectorOperations(Scene):
    def construct(self):
        debug = True

        # TITLE ####################################################
        ############################################################
        title, subtitle = Title(
            scene=self,
            debug=debug,
            part="Part 1",
            subtitle=VGroup(
                Text("Vector Addition / Subtraction", font_size=40),
                Text("Scalar Multiplication", font_size=40)
            )
        )

        # VECTOR ADDITION ##########################################
        ############################################################
        # VECTOR ADDITION > UPDATE SUBTITLE
        subtitle = MarkupText(
            'Vector <span color="GREEN">Addition</span> &amp; <span color="RED">Subtraction</span>',
            font_size=20,
            slant=ITALIC
        ).next_to(title, DOWN, buff=0.1).align_to(title, LEFT)
        
        # titleVGroup.add(subtitle)
        self.play(Write(subtitle))
        self.wait(1)

        # PART 1 ##################################################
        # vector addition / subtraction & scalar multiplication ###
        ###########################################################
        Part1(self, title, subtitle, debug)

        # UPDATE TITLE ############################################
        ###########################################################
        title, subtitle = Title(self, 
                                debug,
                                part="Part 2",
                                subtitle = VGroup( 
                                    Text("Dot Product (Inner Product)", font_size=40),
                                ),
                            )

        # PART 2 ##################################################
        # dot product #############################################
        ###########################################################
        Part2(self, title, subtitle, debug)

        # PART 3 ##################################################
        # cross product ###########################################
        ###########################################################
        # TODO: build: 
        # Part3(self, title, subtitle, debug)

        # THANK YOU ###############################################
        ###########################################################
        thank_you = Text('Thank you for watching!', font_size=40).move_to(ORIGIN)
        self.play(Write(thank_you))
        self.wait(5)

       