from manim import *
import sys
from pathlib import Path

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent))

from utils.create_mobject_border import create_border
from utils.next_to_updater import next_to_updater

def ExampleScene(self, debug: bool = False):
    statement = VGroup(
        Text("The"),
        Text("wind").set_color(GREEN),
        Text("is blowing"),
        Text("6mph").set_color(RED),
        Text("east").set_color(PURPLE),
    ).arrange(RIGHT, buff=0.25)

    return statement