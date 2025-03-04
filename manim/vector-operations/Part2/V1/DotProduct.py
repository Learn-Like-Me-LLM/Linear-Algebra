from manim import *
import numpy as np

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
        f"{a_x_tracker.get_value():.2f}" + r"\\" + 
        f"{a_y_tracker.get_value():.2f}" + 
        r"\end{bmatrix}",
        color=BLUE
    )

    # Add updaters that ONLY update content, not position
    def update_label_a(mob):
        new_label = MathTex(
            r"\vec{a} = \begin{bmatrix}" + 
            f"{a_x_tracker.get_value():.2f}" + r"\\" + 
            f"{a_y_tracker.get_value():.2f}" + 
            r"\end{bmatrix}",
            color=BLUE
        )
        new_label.move_to(mob)
        mob.become(new_label)
    label_a.add_updater(update_label_a)

    # Length labels with updaters
    vector_a_length = MathTex(
        f"|\\vec{{a}}| = \\sqrt{{{a_x_tracker.get_value():.2f}^2 + {a_y_tracker.get_value():.2f}^2}} = {np.sqrt(a_x_tracker.get_value()**2 + a_y_tracker.get_value()**2):.2f}",
        color=BLUE
    )

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
        f"{b_x_tracker.get_value():.2f}" + r"\\" + 
        f"{b_y_tracker.get_value():.2f}" + 
        r"\end{bmatrix}",
        color=RED
    )

    # Add updaters that ONLY update content, not position
    def update_label_b(mob):
        new_label = MathTex(
            r"\vec{b} = \begin{bmatrix}" + 
            f"{b_x_tracker.get_value():.2f}" + r"\\" + 
            f"{b_y_tracker.get_value():.2f}" + 
            r"\end{bmatrix}",
            color=RED
        )
        new_label.move_to(mob)
        mob.become(new_label)
    label_b.add_updater(update_label_b)

    vector_b_length = MathTex(
        f"|\\vec{{b}}| = \\sqrt{{{b_x_tracker.get_value():.2f}^2 + {b_y_tracker.get_value():.2f}^2}} = {np.sqrt(b_x_tracker.get_value()**2 + b_y_tracker.get_value()**2):.2f}",
        color=RED
    )

    # # Create VGroup and position
    # labels = VGroup(label_a, label_b)
    # labels.arrange(RIGHT, buff=1, center=True)  # Ensure centered arrangement
    # labels.next_to(plane, DOWN, buff=0.5)

    # GROUPS ###################################################
    ############################################################
    # One VGroup, side by side, under plane. That's it.
    labels = VGroup(label_a, label_b)
    labels.arrange(RIGHT, buff=1)
    labels.next_to(plane, DOWN, buff=0.5)

    # ANIMATE ##################################################
    ############################################################
    scene.play(Create(plane))
    scene.play(Write(vector_a), Write(vector_b))
    scene.play(Write(labels))
    scene.wait(1)

    # RANDOMIZE VECTOR(s) #######################################
    ############################################################
    count = 0
    while count < 2:
        new_ax = np.random.randint(-5, 6)
        new_ay = np.random.randint(-5, 6)
        new_bx = np.random.randint(-5, 6)
        new_by = np.random.randint(-5, 6)
        
        scene.play(
            a_x_tracker.animate.set_value(new_ax),
            a_y_tracker.animate.set_value(new_ay),
            b_x_tracker.animate.set_value(new_bx),
            b_y_tracker.animate.set_value(new_by)
        )
        scene.wait(2)
        count += 1

    # # FORMULA(s) ###############################################
    # ############################################################
    # # dot_product = MathTex(
    # #     r"\vec{a} \cdot \vec{b} = |\vec{a}| |\vec{b}| \cos(\theta)",
    # #     color=WHITE
    # # ).to_edge(UP)
    
    # # Show angle between vectors
    # angle = Angle(vector_a, vector_b, radius=0.5, color=YELLOW)
    # angle_label = MathTex(r"\theta", color=YELLOW).next_to(angle, RIGHT, buff=0.1)
    
    # scene.play(
    #     Create(angle),
    #     Write(angle_label)
    # )
    # scene.wait(1)
    
    # # Show dot product formula
    # scene.play(Write(dot_product))
    # scene.wait(2)
    
    # # Calculate actual dot product
    # result = MathTex(
    #     r"\vec{a} \cdot \vec{b} = (2,1) \cdot (1,2) = 2(1) + 1(2) = 4",
    #     color=GREEN
    # ).next_to(dot_product, DOWN)
    
    # scene.play(Write(result))
    # scene.wait(2)

    # if debug:
    #     scene.wait(5)
