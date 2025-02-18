from manim import *
import sys
from pathlib import Path

def Title(self, debug: bool = False):
    # TITLE ####################################################
    ############################################################
    title = Text("Vector Operations", font_size=96).move_to(ORIGIN)
    part = Text("Part 1", font_size=30, slant=ITALIC, color=BLUE).next_to(title, RIGHT).align_to(title, RIGHT).shift(DOWN * 0.6)
    subtitle = VGroup( 
        Text("Vector Addition / Subtraction", font_size=40),
        Text("Scalar Multiplication", font_size=40)  
    ).arrange(DOWN).next_to(title, DOWN, buff=0.5)

    # TITLE > ANIMATE ##########################################
    ############################################################
    self.play(Write(title))
    self.wait(.5)
    self.play(Write(part))
    self.wait(.5)
    self.play(Write(subtitle))
    self.wait(1.5)
    
    # REMOVE UNNECESSARY MOBJECTS
    ############################################################
    mobjects_to_remove = [m for m in self.mobjects if m not in [title]]
    self.play(
        FadeOut(*mobjects_to_remove), 
        run_time=2
    )

    # CONFIGURE NEW TITLE
    ############################################################
    new_title = VGroup(
        title.copy().scale(0.35),
    ).arrange(DOWN, buff=0.1, aligned_edge=LEFT) \
     .to_corner(UL, buff=0.5) \
     .to_edge(LEFT, buff=0.5)
     
    self.play(
        Transform(
            title, # this one survives
            new_title
        )
    )
    
    titleVGroup = title
    return titleVGroup
