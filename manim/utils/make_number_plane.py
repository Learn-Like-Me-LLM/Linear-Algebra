from manim import *

def makeNumberPlane(self, x_range, y_range, x_length, y_length, axis_config, debug=False):
    # position plane
    plane = NumberPlane(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        axis_config=axis_config,
    )
    
    return plane