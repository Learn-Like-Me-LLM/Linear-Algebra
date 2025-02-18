from manim import *
import sys
from pathlib import Path

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent))

from Title import Title

class V1VectorOperations(Scene):
    def construct(self):
        debug = True

        # TITLE ####################################################
        ############################################################
        Title(self, debug)

        

        
        
        