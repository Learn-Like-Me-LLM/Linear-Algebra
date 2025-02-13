from manim import *
import sys
from pathlib import Path

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent))

from utils.create_mobject_border import create_border
from utils.next_to_updater import next_to_updater

wait = 1

def create_vector_with_labels(start_point, end_point, plane, color=YELLOW):
    print(f'START POINT: {start_point} {type(start_point)}')
    vector = Arrow(
        start=start_point,
        end=end_point,
        color=color,
        buff=0,
        max_tip_length_to_length_ratio=0.2
    )
    
    # Convert coordinates and round to 0 decimals (integers)
    start_coords = [round(x) for x in plane.point_to_coords(start_point)]
    end_coords = [round(x) for x in plane.point_to_coords(end_point)]
    vector_coords = [round(end_coords[0] - start_coords[0]), 
                    round(end_coords[1] - start_coords[1])]
    
    # Convert to integers if no decimal part
    vector_coords = [int(x) if x.is_integer() else x for x in vector_coords]
    
    # Create stacked labels with bracket notation
    if np.array_equal(start_point, plane.coords_to_point(0, 0)):  
        vector_notation = MathTex(
            f"\\vec{{w_s}} = \\begin{{bmatrix}} {vector_coords[0]} \\\\ {vector_coords[1]} \\end{{bmatrix}}",
            font_size=24,
            color=color
        )
    else:
        vector_notation = MathTex(
            f"\\vec{{w}} = \\begin{{bmatrix}} {vector_coords[0]} \\\\ {vector_coords[1]} \\end{{bmatrix}}",
            font_size=24,
            color=color
        )

    # Stack labels vertically with smaller buffer
    labels = VGroup(vector_notation).arrange(DOWN, buff=0.05)
    
    # Update labels to follow arrow tip
    def update_label_position(m):
        m.next_to(vector.get_end(), DOWN, buff=0.1)
    labels.add_updater(update_label_position)
    
    return vector, labels

def titleScene(self, debug=False):
    # TITLE ################
    ########################
    title = Text("What is a Vector?", font_size=60)

    # DEFINITION ###########
    ########################
    definition = VGroup(
        MarkupText(
            'A <span color="GREEN">vector</span> is an entity that has both:',
            font_size=40,
            should_center=True
        ),
        MarkupText( 
            '<span color="RED">magnitude</span> and <span color="PURPLE">direction</span>',
            font_size=40,
            should_center=True
        )
    ).arrange(DOWN)

    # Group text elements and position left
    title_container = VGroup(title, definition).arrange(DOWN, buff=0.5)
    title_container_rect = create_border(title_container, RED)
    
    # Animation sequence
    if debug:
        self.play(
            Write(title),
            Create(title_container_rect),
        )
    else:
        self.play(
            Write(title),
        )
    self.wait(wait)
    self.play(Write(definition))
    self.wait(wait)
    if debug:
        self.play(FadeOut(title_container, title_container_rect))
    else:    
        self.play(FadeOut(title_container))

def exampleScene(self, debug=False):
    # EXAMPLE ###########
    ########################
    ex_a = Text("wind").set_color(GREEN)
    ex_a_subtitle = MathTex(r"\vec{w}", font_size=30).set_color(GREEN)
    ex_a_subtitle.add_updater(next_to_updater(ex_a_subtitle, ex_a, DOWN))

    ex_b = Text("6mph").set_color(RED)
    ex_b_subtitle = Text("magnitude", font_size=30, slant=ITALIC).set_color(RED)
    ex_b_subtitle.add_updater(next_to_updater(ex_b_subtitle, ex_b, DOWN))

    ex_c = Text("east").set_color(PURPLE)
    ex_c_subtitle = Text("direction", font_size=30, slant=ITALIC).set_color(PURPLE)
    ex_c_subtitle.add_updater(next_to_updater(ex_c_subtitle, ex_c, DOWN))
    
    example_container = VGroup(
        Text("The"),
        ex_a,
        Text("is blowing"),
        ex_b,
        ex_c,
    ).arrange(RIGHT, buff=0.5)

    complete_example = VGroup(
        example_container,
        VGroup(ex_a_subtitle, ex_b_subtitle, ex_c_subtitle)
    ).arrange(DOWN, buff=0.3)
    complete_example_rect = create_border(complete_example, RED)

    # Animation sequence
    if debug:
        self.play(
            Write(example_container),
            Create(complete_example_rect)
        )   
    else:
        self.play(
            Write(example_container),
        )
    self.wait(wait)
    self.play(
        Write(ex_a_subtitle),
        Write(ex_b_subtitle),
        Write(ex_c_subtitle),
    )
    self.wait(wait)

    return complete_example

def makePlane(self, debug=False):
    # position plane
    plane = NumberPlane(
        x_range=[-5, 10, 1],
        y_range=[-2, 10, 1],
        x_length=3,
        y_length=3,
        axis_config={"include_numbers": False},
    )

    # Direction labels
    directions = VGroup(
        Text("North", font_size=16).next_to(plane.y_axis, UP),
        Text("South", font_size=16).next_to(plane.y_axis, DOWN),
        Text("East", font_size=16).next_to(plane.x_axis, RIGHT),
        Text("West", font_size=16).next_to(plane.x_axis, LEFT)
    )

    plane_container = VGroup(plane, directions)

    if debug:
        plane_container_rect = create_border(plane_container, RED)
        self.add(plane_container_rect)
    
    return plane_container, plane

class WhatIsAVector(Scene):
    def construct(self):
        debug = False
        # 1. Title
        ############################################################
        titleScene(self)

        # 2. Initialize all components
        ############################################################
        complete_example = exampleScene(self)
        plane_container, plane = makePlane(self, debug=False)

        # Group them and arrange horizontally
        standard_pos_explanation = VGroup(
            Tex("$\\bullet$ Vector", font_size=28),
            MathTex("\\vec{w_s}", font_size=28, color=GREEN),
            Tex("is in", font_size=28),
            Tex("standard position", font_size=28, color=YELLOW),
            Tex("as it starts at the origin", font_size=28),
            Tex("$(0,0)$", font_size=28, color=YELLOW)
        ).arrange(RIGHT, buff=0.2)

        equivalent_vectors_explanation = VGroup(
            VGroup(
                Tex("$\\bullet$ Equivalent vectors have the same", font_size=28),
                Tex(
                    "magnitude",
                    color=RED,
                    font_size=28
                ),
                Tex("and", font_size=28),
                Tex(
                    "direction",
                    color=PURPLE,
                    font_size=28
                ),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Tex("\\\\regardless of their position in the plane: ", font_size=28),
                MathTex("\\vec{w_s} = \\vec{w}", font_size=28, color=GREEN)
            ).arrange(RIGHT, buff=0.2)
        ).arrange(DOWN, buff=0.2)


        # 3. Position everything relative to center
        ############################################################
        # First, center the plane
        plane_container.move_to(ORIGIN)
        
        # Position example at top
        self.play(complete_example.animate.to_edge(UP, buff=0.5))
        
        # Create and position explanations at bottom
        explanation_container = VGroup(
            standard_pos_explanation,
            equivalent_vectors_explanation
        ).arrange(DOWN, buff=0.2)
        explanation_container.to_edge(DOWN, buff=0.5)

        if debug:
            explanation_container_rect = create_border(explanation_container, BLUE)
            self.add(explanation_container_rect)

        # 5. "wind" vectors
        ############################################################
        vector1, labels1 = create_vector_with_labels(
            plane.coords_to_point(0, 0),
            plane.coords_to_point(6, 0),
            plane,
        )
        
        vector2, labels2 = create_vector_with_labels(
            plane.coords_to_point(2, 3),
            plane.coords_to_point(8, 3),
            plane,
            GREEN
        )
        
        vector3, labels3 = create_vector_with_labels(
            plane.coords_to_point(-3, 7),
            plane.coords_to_point(3, 7),
            plane,
            GREEN
        )
        
        # ANIMATE
        ############################################################
        self.play(Write(plane_container))

        self.play(GrowArrow(vector1), Write(labels1))
        self.wait(wait)
        self.play(Write(standard_pos_explanation))
        self.wait(wait)
        
        self.play(
            GrowArrow(vector2), 
            Write(labels2), 
            GrowArrow(vector3), 
            Write(labels3)
        )
        self.wait(wait)
        
        self.play(Write(equivalent_vectors_explanation))
        self.wait(wait)

        # Optional: Add highlighting animation to emphasize equivalence
        highlight_vectors = VGroup(vector2, vector3)
        self.play(
            Indicate(vector1, color=YELLOW, scale_factor=1.2),
            Indicate(highlight_vectors, color=GREEN, scale_factor=1.2),
        )
        self.wait(wait)