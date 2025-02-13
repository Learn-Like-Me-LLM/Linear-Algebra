from manim import *
import sys
from pathlib import Path

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent))  

from utils.create_mobject_border import create_border

def WhatIsAVectorIntro(self, debug=False):
    title = VGroup(
        Text("What is a Vector", font_size=60),
        MathTex("\\vec{v}", font_size=90, color=GREEN),
        Text("?", font_size=60)
    ).arrange(RIGHT, buff=0.1)
    title[0][7:13].set_color(GREEN)
    
    # Create all three definition states
    definition1 = Text("an arrow", font_size=40, color=GREEN)
    definition2 = Text("an ordered list of numbers", font_size=40, color=GREEN)
    
    definition3 = VGroup(
        Text("an entity with a ", font_size=40),
        VGroup(
            Text("magnitude", font_size=50, color=RED),
            Text("&", font_size=40),
            Text("direction", font_size=50, color=PURPLE)
        ).arrange(RIGHT, buff=0.2)
    ).arrange(RIGHT, buff=0.2)

    # Group definitions for easier management
    definitions = VGroup(definition1, definition2, definition3)

    # Position all definitions at the same spot as definition1
    for def_item in definitions[1:]:
        def_item.move_to(definition1)

    # ORDERED LIST MOBJECTS
    ############################################################
    numbers_horizontal = MathTex("1 \\ 2 \\ 3", font_size=40, color=GREEN)
    numbers_with_commas = MathTex("1, \\ 2, \\ 3", font_size=40, color=GREEN)
    numbers_with_brackets = MathTex("[1, \\ 2, \\ 3]", font_size=40, color=GREEN)
    numbers_with_vars = MathTex("[x, \\ y, \\ z]", font_size=40, color=GREEN)
    ordered_list_matrix = MathTex(
        "\\begin{bmatrix} x \\\\ y \\\\ z \\\\ \\dots \\end{bmatrix}",
        font_size=40,
        color=GREEN
    ).next_to(definition2, DOWN, buff=1.5)

    number_displays = VGroup(
        numbers_horizontal,
        numbers_with_commas,
        numbers_with_brackets,
        numbers_with_vars,
        ordered_list_matrix
    )

    # Position all number displays relative to the first one
    first_number = numbers_horizontal.next_to(definition2, DOWN, buff=1.5)
    for display in number_displays[1:]:
        display.move_to(first_number)

    statement = Text("A vector is:", font_size=40)

    # Create animated arrow for definition1
    arrow = Arrow(
        start=LEFT * 1.5,
        end=RIGHT * 1.5,
        color=GREEN,
        buff=0
    ).next_to(statement, DOWN, buff=1)

    arrow_animation = Succession( # TODO: move this back to intro file and run arrow_animation
        Transform(arrow, arrow.copy().scale(2)),
        Transform(arrow, arrow.copy().scale(0.5)),
        Rotate(arrow, angle=PI, about_point=arrow.get_center()),
        Rotate(arrow, angle=2*PI, rate_func=linear, about_point=arrow.get_center()),
        Rotate(arrow, angle=-PI, rate_func=linear, about_point=arrow.get_center()),
    )

    
    current_def = definitions[0].next_to(statement, DOWN, buff=.25)
    
    # Initial animations
    self.play(Write(title))
    self.wait(2)
    self.play(title.animate.scale(0.5).to_corner(UL, buff=0.5).to_edge(LEFT, buff=0.5))
    self.play(Write(statement))
    self.play(Write(current_def))
    self.wait(0.5)
    self.play(GrowArrow(arrow), arrow_animation)

    # Loop through definitions once
    for i in range(len(definitions) - 1):
        next_def = definitions[i + 1].copy()
        next_def.next_to(statement, DOWN, buff=.25)
        
        if i == 0:  # Transition from "arrow" to "ordered list"
            self.play(
                FadeOut(current_def),
                FadeOut(arrow),
                FadeIn(next_def)
            )
            
            # Play number sequence animations
            current_number = numbers_horizontal
            self.play(Write(current_number))
            
            for next_number in [numbers_with_commas, numbers_with_brackets, 
                              numbers_with_vars, ordered_list_matrix]:
                self.play(Transform(current_number, next_number))
                self.wait(0.5)
            
            self.play(FadeOut(current_number))
        else:  # Transition to "magnitude & direction"
            self.play(
                FadeOut(current_def),
                FadeIn(next_def)
            )
        
        current_def = next_def
        self.wait(1)

    # Create new title components
    main_title = VGroup(
        Text("What is a Vector", font_size=60),
        MathTex("\\vec{v}", color=GREEN, font_size=90),
        Text("?", font_size=60)
    ).arrange(RIGHT, buff=0.1)

    subtitle = VGroup(
        Text("• ", font_size=40),
        Text("has magnitude (", font_size=40, slant=ITALIC),
        MathTex("m", color=RED, font_size=60),
        Text(") & direction (", font_size=40, slant=ITALIC),
        MathTex("d", color=PURPLE, font_size=60),
        Text(")", font_size=40, slant=ITALIC)
    ).arrange(RIGHT, buff=0.1)
    subtitle[1][3:12].set_color(RED)
    subtitle[3][2:11].set_color(PURPLE)

    new_title = VGroup(main_title, subtitle).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
    new_title.scale(0.5).to_corner(UL, buff=0.5).to_edge(LEFT, buff=0.5)

    mobjects_to_remove = [m for m in self.mobjects if m not in [title]]

    self.play(
        Transform(title, new_title),
        FadeOut(*mobjects_to_remove),
        run_time=2
    )
    self.wait(1)

    result = {
        "title": title,
    }

    return result