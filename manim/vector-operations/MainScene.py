from manim import *
import sys
from pathlib import Path

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent))

from Part1.V1.Index import Part1
from Part2.V1.Index import Part2
from Part3.V1.index import Part3

from Title import Title

# sys.setrecursionlimit(3000)  # Increase from default 1000

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
        subtitle = VGroup (
            Text("Vector", font_size=20, slant=ITALIC),
            Text("Addition", font_size=20, slant=ITALIC,  color=BLUE),
            MathTex("\\&", font_size=20),
            Text("Subtraction", font_size=20, slant=ITALIC, color=BLUE),
        ).arrange(RIGHT, buff=0.1)
        subtitle.next_to(title, DOWN, buff=0.1).align_to(title, LEFT)
        
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
                                    Text("Dot Product", font_size=40),
                                ),
                            )

        # PART 2 ##################################################
        # dot product #############################################
        ###########################################################
        Part2(self, title, subtitle, debug)

        # # UPDATE TITLE ############################################
        # ###########################################################
        # title, subtitle = Title(self, 
        #                         debug,
        #                         part="Part 3",
        #                         subtitle = VGroup( 
        #                             Text("Cross Product", font_size=40),
        #                         ),
        #                     )

        # # PART 3 ##################################################
        # # cross product ###########################################
        # ###########################################################
        # # TODO: build: 
        # Part3(
        #     self, 
        #     title, 
        #     subtitle, 
        #     debug
        # )

        # THANK YOU ###############################################
        ###########################################################
        thank_you = Text('Thank you for watching!', font_size=40).move_to(ORIGIN)
        self.play(Write(thank_you))
        self.wait(5)

       