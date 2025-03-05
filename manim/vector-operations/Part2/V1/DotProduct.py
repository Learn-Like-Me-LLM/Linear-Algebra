from manim import *
import numpy as np

from .CalculateAngleBetweenVectors import CalculateAngleBetweenVectors

def DotProduct(scene: Scene, plane, plane_container, debug: bool = False) -> None:
    # VECTOR A #################################################
    ############################################################
    # Create trackers for vector coordinates
    a_x_tracker = ValueTracker(2)
    a_y_tracker = ValueTracker(1)

    # VECTOR A with trackers
    vector_a = Arrow(
        start=plane.c2p(0,0),
        end=plane.c2p(a_x_tracker.get_value(), a_y_tracker.get_value()),
        buff=0,
        color=BLUE
    )
    
    # Update vector_a position
    vector_a.add_updater(
        lambda v: v.put_start_and_end_on(
            plane.c2p(0,0),
            plane.c2p(a_x_tracker.get_value(), a_y_tracker.get_value())
        )
    )

    # Create the labels
    label_a = MathTex(
        r"\vec{a} = \begin{bmatrix}" + 
        f"{a_x_tracker.get_value():.0f}" + r"\\" + 
        f"{a_y_tracker.get_value():.0f}" + 
        r"\end{bmatrix}",
        color=BLUE,
        font_size=24
    )

    # Add updaters that ONLY update content, not position
    def update_label_a(mob):
        new_label = MathTex(
            r"\vec{a} = \begin{bmatrix}" + 
            f"{a_x_tracker.get_value():.0f}" + r"\\" + 
            f"{a_y_tracker.get_value():.0f}" + 
            r"\end{bmatrix}",
            color=BLUE,
            font_size=24
        )
        new_label.move_to(mob)
        mob.become(new_label)
    label_a.add_updater(update_label_a)

    # Create initial length labels
    vector_a_length = MathTex(
        f"|\\vec{{a}}| = \\sqrt{{{a_x_tracker.get_value():.0f}^2 + {a_y_tracker.get_value():.0f}^2}} = {np.sqrt(a_x_tracker.get_value()**2 + a_y_tracker.get_value()**2):.0f}",
        color=BLUE,
        font_size=24
    )

    # Add updaters for length labels
    def update_length_a(mob):
        new_length = MathTex(
            f"|\\vec{{a}}| = \\sqrt{{{a_x_tracker.get_value():.0f}^2 + {a_y_tracker.get_value():.0f}^2}} = {np.sqrt(a_x_tracker.get_value()**2 + a_y_tracker.get_value()**2):.0f}",
            color=BLUE,
            font_size=24
        )
        new_length.move_to(mob)
        mob.become(new_length)
    vector_a_length.add_updater(update_length_a)

    # VECTOR B #################################################
    ############################################################
    # Create trackers for vector coordinates
    b_x_tracker = ValueTracker(1)
    b_y_tracker = ValueTracker(2)

    # VECTOR B with trackers
    vector_b = Arrow(
        start=plane.c2p(0,0),
        end=plane.c2p(b_x_tracker.get_value(), b_y_tracker.get_value()),
        buff=0,
        color=RED
    )
    
    # Update vector_b position
    vector_b.add_updater(
        lambda v: v.put_start_and_end_on(
            plane.c2p(0,0),
            plane.c2p(b_x_tracker.get_value(), b_y_tracker.get_value())
        )
    )

    # Create the labels
    label_b = MathTex(
        r"\vec{b} = \begin{bmatrix}" + 
        f"{b_x_tracker.get_value():.0f}" + r"\\" + 
        f"{b_y_tracker.get_value():.0f}" + 
        r"\end{bmatrix}",
        color=RED,
        font_size=24
    )

    # Add updaters that ONLY update content, not position
    def update_label_b(mob):
        new_label = MathTex(
            r"\vec{b} = \begin{bmatrix}" + 
            f"{b_x_tracker.get_value():.0f}" + r"\\" + 
            f"{b_y_tracker.get_value():.0f}" + 
            r"\end{bmatrix}",
            color=RED,
            font_size=24
        )
        new_label.move_to(mob)
        mob.become(new_label)
    label_b.add_updater(update_label_b)

    vector_b_length = MathTex(
        f"|\\vec{{b}}| = \\sqrt{{{b_x_tracker.get_value():.0f}^2 + {b_y_tracker.get_value():.0f}^2}} = {np.sqrt(b_x_tracker.get_value()**2 + b_y_tracker.get_value()**2):.0f}",
        color=RED,
        font_size=24
    )

    # Add updaters for length labels
    def update_length_b(mob):
        new_length = MathTex(
            f"|\\vec{{b}}| = \\sqrt{{{b_x_tracker.get_value():.0f}^2 + {b_y_tracker.get_value():.0f}^2}} = {np.sqrt(b_x_tracker.get_value()**2 + b_y_tracker.get_value()**2):.0f}",
            color=RED,
            font_size=24
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
    scene.play(Create(plane))
    scene.play(Write(vector_a), Write(vector_b))
    scene.play(Write(vector_labels))
    scene.wait(1)
    
    # LEFT EXAMPLE > Calculate Angle Between Vectors############
    ############################################################
    CalculateAngleBetweenVectors(
        scene, 
        plane, 
        plane_container, 
        vector_a, 
        vector_b, 
        a_x_tracker, 
        a_y_tracker, b_x_tracker, b_y_tracker, 
        length_labels,
        debug
    )
    scene.wait(1)
