from manim import *

def makePlane(self, debug=False):
    # position plane
    plane = NumberPlane(
        x_range=[-5, 10, 1],
        y_range=[-2, 10, 1],
        x_length=3,
        y_length=3,
        axis_config={"include_numbers": False},
    )
    
    return plane