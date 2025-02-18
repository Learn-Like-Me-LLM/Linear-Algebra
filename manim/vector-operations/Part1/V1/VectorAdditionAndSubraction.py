from manim import *
import sys
from pathlib import Path

def VectorAdditionAndSubraction(self, debug: bool = False):
    text = Text('VECTOR ADDITION & SUBRACTION TEST').move_to(ORIGIN)
    self.play(Write(text))
    self.wait(1)
    
    # Remove the text after it's displayed
    self.remove(text)

    return
