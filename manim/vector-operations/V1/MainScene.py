from manim import *
import sys
from pathlib import Path

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent))

class V1VectorOperations(Scene):
    def construct(self):
        debug = True

        # TITLE ####################################################
        ############################################################
        title = Text("Vector Operations", font_size=96).move_to(ORIGIN)

        # TITLE > ANIMATE ##########################################
        ############################################################
        self.play(Write(title))
        self.wait()
        
        