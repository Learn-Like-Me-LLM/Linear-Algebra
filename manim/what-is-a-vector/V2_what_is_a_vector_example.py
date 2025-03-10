from manim import *
import sys
from pathlib import Path

# Add the parent directory to Python path to allow imports from utils
sys.path.append(str(Path(__file__).parent.parent))

from utils.create_mobject_border import create_border
from utils.next_to_updater import next_to_updater
from utils.make_number_plane import makeNumberPlane

def create_vector_with_labels(start_point, end_point, plane, color=YELLOW):
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

def ExampleScene(self, debug: bool = False):
    # CREATE STATEMENT ##########################################
    ############################################################
    statement = MathTex(
        r"\text{The }",
        r"\text{wind }",
        r"\text{is blowing }",
        r"\text{6mph }",
        r"\text{east}",
    ).set_color_by_tex_to_color_map({
        "wind": GREEN,
        "6": RED,
        "east": PURPLE
    })
    
    # Create subtexts
    wind_subtext = MathTex(r"\vec{v}", color=GREEN).scale(0.7)
    speed_subtext = MathTex(r"(m)", color=RED).scale(0.7)
    direction_subtext = MathTex(r"(d)", color=PURPLE).scale(0.7)
    
    # Create a VGroup for subtexts to ensure consistent alignment
    subtexts = VGroup(wind_subtext, speed_subtext, direction_subtext)
    
    # Calculate target y-position (use the lowest point of the main text minus some buffer)
    target_y = statement.get_bottom()[1] - 0.3
    
    # Position subtexts below their corresponding words with consistent y-coordinate
    wind_subtext.move_to(statement[1].get_center() + DOWN * 0.3)
    speed_subtext.move_to(statement[3].get_center() + DOWN * 0.3)
    direction_subtext.move_to(statement[4].get_center() + DOWN * 0.3)
    
    # Ensure all subtexts have the same y-coordinate
    for subtext in subtexts:
        subtext.set_y(target_y)
    
    # Group everything together
    complete_statement = VGroup( statement,
                                 wind_subtext,
                                 speed_subtext,
                                 direction_subtext).move_to(UP)
    
    # ANIMATE STATEMENT #########################################
    #############################################################
    self.play(Write(complete_statement))

    # CREATE NUMBER PLANE #######################################
    #############################################################
    plane = makeNumberPlane( self, 
                             x_range=[-3, 10, 1], 
                             y_range=[-3, 8, 1], 
                             x_length=3,
                             y_length=3,
                             axis_config={"include_numbers": False},
                             debug=debug)
    
    directions = VGroup( Text("North", font_size=16).next_to(plane.y_axis, UP),
                         Text("South", font_size=16).next_to(plane.y_axis, DOWN),
                         Text("East", font_size=16).next_to(plane.x_axis, RIGHT),
                         Text("West", font_size=16).next_to(plane.x_axis, LEFT))

    vector1, labels1 = create_vector_with_labels( plane.coords_to_point(0, 0),
                                                  plane.coords_to_point(6, 0),
                                                  plane)
    
    # Create plane container and position it to the left
    plane_container = VGroup(
        plane, directions, 
        vector1, labels1,
    ).next_to(complete_statement, DOWN, buff=0.5)
    self.play(Write(plane), Write(directions))
    self.play(GrowArrow(vector1), Write(labels1))
    self.wait(2)
    self.play(plane_container.animate.to_edge(LEFT, buff=0.5))

    # Create both explanations first
    standard_pos_explanation = VGroup(
        VGroup(
            Tex("$\\bullet$ Vector", font_size=28),
            MathTex("\\vec{w_s}", font_size=28, color=GREEN),
            Tex("is in", font_size=28),
            Tex("standard position", font_size=28, color=YELLOW),
            Tex("as it starts at the origin:", font_size=28),
            Tex("$(0,0)$", font_size=28, color=YELLOW)
        ).arrange(RIGHT, buff=0.2),
    ).arrange(DOWN, buff=0.2)

    equivalent_vectors_explanation = VGroup(
        VGroup(
            Tex("$\\bullet$ Equivalent vectors have", font_size=28),
            Tex("the same", font_size=28),
            Tex("magnitude", color=RED, font_size=28),
            Tex("and", font_size=28),
            Tex("direction", color=PURPLE, font_size=28),
        ).arrange(RIGHT, buff=0.2),
        VGroup(
            Tex("regardless of their position", font_size=28),
            Tex("in the plane:", font_size=28),
            MathTex("\\vec{w_s} = \\vec{w}", font_size=28, color=GREEN)
        ).arrange(RIGHT, buff=0.2),
    ).arrange(DOWN, buff=0.2)

    # Group both explanations together
    all_explanations = VGroup(standard_pos_explanation, equivalent_vectors_explanation)\
        .arrange(DOWN, buff=0.5)
    
    # Position the entire explanation group next to and centered with the plane
    all_explanations.next_to(plane_container, RIGHT, buff=.5)
    all_explanations.set_y(plane_container.get_y())

    # Animate first explanation
    self.play(Write(standard_pos_explanation))

    # Create and animate vector2 and vector3
    vector2, labels2 = create_vector_with_labels(
        plane.coords_to_point(2, 3),
        plane.coords_to_point(8, 3),
        plane,
        GREEN
    )
    
    vector3, labels3 = create_vector_with_labels(
        plane.coords_to_point(-2, 7),
        plane.coords_to_point(4, 7),
        plane,
        GREEN
    )

    self.play(
        GrowArrow(vector2), Write(labels2), 
        GrowArrow(vector3), Write(labels3)
    )

    # Animate second explanation
    self.play(Write(equivalent_vectors_explanation))
    
    return