from manim import *
import numpy as np

from .CalculateAngleBetweenVectors import CalculateAngleBetweenVectors
from .GenericExample import GenericExample
from .TwoDimensionalCalculation import TwoDimensionalCalculation

def DotProduct(scene: Scene, plane, plane_container, title, subtitle, font_size: int = 35, debug: bool = False) -> None:
    # VECTOR A #################################################
    ############################################################
    # Create trackers for vector coordinates
    a_x_tracker = ValueTracker(0)
    a_y_tracker = ValueTracker(-1)

    # VECTOR A with trackers
    vector_a = Arrow(
        start=plane.c2p(0,0),
        end=plane.c2p(a_x_tracker.get_value(), a_y_tracker.get_value()),
        buff=0,
        color=PURE_GREEN
    )
    
    # Update vector_a position with logging
    def update_vector_a(v):
        start_point = plane.c2p(0, 0)
        end_point = plane.c2p(a_x_tracker.get_value(), a_y_tracker.get_value())
        
        # Check if vector is too small to avoid cross product issues
        if np.allclose(start_point, end_point, atol=1e-6):
            v.set_opacity(0)  # Hide the vector when it's essentially zero
        else:
            # Temporarily remove the updater to avoid recursion
            v.clear_updaters()
            
            # Create a new arrow and copy its properties
            new_arrow = Arrow(
                start=start_point,
                end=end_point,
                buff=0,
                color=PURE_GREEN
            )
            v.become(new_arrow)
            v.set_opacity(1)  # Show the vector when it has meaningful length
            
            # Re-add the updater
            v.add_updater(update_vector_a)
        
        return v
    vector_a.add_updater(update_vector_a)

    # Create the labels
    label_a = MathTex(
        r"\vec{a} = \begin{bmatrix}" + 
        f"{a_x_tracker.get_value():.0f}" + r"\\" + 
        f"{a_y_tracker.get_value():.0f}" + 
        r"\end{bmatrix}",
        color=PURE_GREEN,
        font_size=font_size
    )

    # Add updaters that ONLY update content, not position
    def update_label_a(mob):
        new_label = MathTex(
            r"\vec{a} = \begin{bmatrix}" + 
            f"{a_x_tracker.get_value():.0f}" + r"\\" + 
            f"{a_y_tracker.get_value():.0f}" + 
            r"\end{bmatrix}",
            color=PURE_GREEN,
            font_size=font_size
        )
        new_label.move_to(mob)
        mob.become(new_label)
    label_a.add_updater(update_label_a)

    # Create initial length labels
    vector_a_length = MathTex(
        f"|\\vec{{a}}| = \\sqrt{{{a_x_tracker.get_value():.0f}^2 + {a_y_tracker.get_value():.0f}^2}} = {np.sqrt(a_x_tracker.get_value()**2 + a_y_tracker.get_value()**2):.0f}",
        color=PURE_GREEN,
        font_size=font_size
    )

    # Add updaters for length labels
    def update_length_a(mob):
        new_length = MathTex(
            f"|\\vec{{a}}| = \\sqrt{{{a_x_tracker.get_value():.0f}^2 + {a_y_tracker.get_value():.0f}^2}} = {np.sqrt(a_x_tracker.get_value()**2 + a_y_tracker.get_value()**2):.0f}",
            color=PURE_GREEN,
            font_size=font_size
        )
        new_length.move_to(mob)
        mob.become(new_length)
    vector_a_length.add_updater(update_length_a)

    # VECTOR B #################################################
    ############################################################
    # Create trackers for vector coordinates
    b_x_tracker = ValueTracker(1)
    b_y_tracker = ValueTracker(0)

    # VECTOR B with trackers
    vector_b = Arrow(
        start=plane.c2p(0,0),
        end=plane.c2p(b_x_tracker.get_value(), b_y_tracker.get_value()),
        buff=0,
        color=YELLOW
    )
    
    # Update vector_b position with logging
    def update_vector_b(v):
        start_point = plane.c2p(0, 0)
        end_point = plane.c2p(b_x_tracker.get_value(), b_y_tracker.get_value())
        
        # Check if vector is too small to avoid cross product issues
        if np.allclose(start_point, end_point, atol=1e-6):
            v.set_opacity(0)  # Hide the vector when it's essentially zero
        else:
            # Temporarily remove the updater to avoid recursion
            v.clear_updaters()
            
            # Create a new arrow and copy its properties
            new_arrow = Arrow(
                start=start_point,
                end=end_point,
                buff=0,
                color=YELLOW
            )
            v.become(new_arrow)
            v.set_opacity(1)  # Show the vector when it has meaningful length
            
            # Re-add the updater
            v.add_updater(update_vector_b)
            
        return v
    vector_b.add_updater(update_vector_b)

    # Create the labels
    label_b = MathTex(
        r"\vec{b} = \begin{bmatrix}" + 
        f"{b_x_tracker.get_value():.0f}" + r"\\" + 
        f"{b_y_tracker.get_value():.0f}" + 
        r"\end{bmatrix}",
        color=YELLOW,
        font_size=font_size
    )

    # Add updaters that ONLY update content, not position
    def update_label_b(mob):
        new_label = MathTex(
            r"\vec{b} = \begin{bmatrix}" + 
            f"{b_x_tracker.get_value():.0f}" + r"\\" + 
            f"{b_y_tracker.get_value():.0f}" + 
            r"\end{bmatrix}",
            color=YELLOW,
            font_size=font_size
        )
        new_label.move_to(mob)
        mob.become(new_label)
    label_b.add_updater(update_label_b)

    vector_b_length = MathTex(
        f"|\\vec{{b}}| = \\sqrt{{{b_x_tracker.get_value():.0f}^2 + {b_y_tracker.get_value():.0f}^2}} = {np.sqrt(b_x_tracker.get_value()**2 + b_y_tracker.get_value()**2):.0f}",
        color=YELLOW,
        font_size=font_size
    )

    # Add updaters for length labels
    def update_length_b(mob):
        new_length = MathTex(
            f"|\\vec{{b}}| = \\sqrt{{{b_x_tracker.get_value():.0f}^2 + {b_y_tracker.get_value():.0f}^2}} = {np.sqrt(b_x_tracker.get_value()**2 + b_y_tracker.get_value()**2):.0f}",
            color=YELLOW,
            font_size=font_size
        )
        new_length.move_to(mob)
        mob.become(new_length)
    vector_b_length.add_updater(update_length_b)

    # GROUPS ###################################################
    ############################################################
    # Create VGroups for positioning
    vector_labels = VGroup(label_a, label_b).arrange(RIGHT, buff=1)
    vector_labels.next_to(plane, DOWN, buff=0.5)
    
    length_labels = VGroup(vector_a_length, vector_b_length).arrange(RIGHT, buff=1)
    length_labels.next_to(vector_labels, DOWN, buff=0.5)       

    # ANIMATE ##################################################
    ############################################################

    # AMINATE > Generic Example#################################
    GenericExample(
        scene=scene, 
        plane=plane,
        # debug=debug
    )
    scene.wait(1)

    # # ANIMATE > 2D Calculation ##################################
    TwoDimensionalCalculation(
        scene=scene, 
        plane=plane, 
        plane_container=plane_container, 
        title=title, 
        subtitle=subtitle,
        vector_a=vector_a, vector_b=vector_b, 
        vector_labels=vector_labels,
        a_x_tracker=a_x_tracker, a_y_tracker=a_y_tracker,
        b_x_tracker=b_x_tracker, b_y_tracker=b_y_tracker,
        debug=debug
    )
    scene.wait(1)

    # LEFT EXAMPLE > Calculate Angle Between Vectors############
    ############################################################
    CalculateAngleBetweenVectors(
        scene=scene, 
        plane=plane, 
        plane_container=plane_container, 
        vector_a=vector_a, vector_b=vector_b,  
        vector_labels=vector_labels,
        a_x_tracker=a_x_tracker, a_y_tracker=a_y_tracker,
        b_x_tracker=b_x_tracker, b_y_tracker=b_y_tracker,
        length_labels=length_labels,
        debug=debug
    )
    scene.wait(1)

    # CLEAN UP #################################################
    ############################################################
    mobjects_to_remove = [m for m in scene.mobjects]
    scene.play(
        FadeOut(*mobjects_to_remove), 
        run_time=2
    )
