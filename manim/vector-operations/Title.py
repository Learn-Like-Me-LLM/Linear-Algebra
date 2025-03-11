from manim import *
import sys
from pathlib import Path

def Title(scene, debug: bool = False, part: str = "Part 1", subtitle = None):
    # TITLE ####################################################
    ############################################################
    title = Text("Vector Operations", font_size=96).move_to(ORIGIN)
    part_text = Text(part, font_size=30, slant=ITALIC, color=BLUE).next_to(title, RIGHT).align_to(title, RIGHT).shift(DOWN * 0.6)

    # TITLE > ANIMATE ##########################################
    ############################################################
    scene.play(Write(title))
    scene.wait(.5)
    scene.play(Write(part_text))
    scene.wait(.5)
    scene.play(Write(subtitle.arrange(DOWN).next_to(title, DOWN, buff=0.5)))
    scene.wait(1.5)
    
    # REMOVE UNNECESSARY MOBJECTS
    ############################################################
    mobjects_to_remove = [m for m in scene.mobjects if m not in [title]]
    scene.play(
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
     
    scene.play(
        Transform(
            title, # this one survives
            new_title
        )
    )
    
    
    return title, subtitle
