from manim import *
import sys
from pathlib import Path

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent))

from utils.create_mobject_border import create_border
from utils.next_to_updater import next_to_updater

from V2_what_is_a_vector_intro import WhatIsAVectorIntro
from V2_what_is_a_vector_example import ExampleScene  # Fixed import name

class V2WhatIsAVector(Scene):
    def construct(self):
        debug = True

        # 1. Generate INTRO Mobjects
        ############################################################
        result = WhatIsAVectorIntro(self, debug=debug)

        # EXAMPLE 
        ############################################################
        example = ExampleScene(self, debug=debug)