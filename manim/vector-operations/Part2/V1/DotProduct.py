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

    # LEFT EXAMPLE > Calculate Angle Between Vectors############
    ############################################################
    # Initial angle formula setup
    dot_product = a_x_tracker.get_value()*b_x_tracker.get_value() + a_y_tracker.get_value()*b_y_tracker.get_value()
    mag_a = np.sqrt(a_x_tracker.get_value()**2 + a_y_tracker.get_value()**2)
    mag_b = np.sqrt(b_x_tracker.get_value()**2 + b_y_tracker.get_value()**2)
    angle = np.arccos(dot_product / (mag_a * mag_b))
    
    angle_formula = VGroup(
        MathTex(
            r"\vec{a} \cdot \vec{b} &= \|\vec{a}\|\|\vec{b}\|\cos(\theta) \\",
            color=WHITE,
            font_size=24
        ),
        MathTex(
            f"\\begin{{bmatrix}}{a_x_tracker.get_value():.0f} \\\\ {a_y_tracker.get_value():.0f}\\end{{bmatrix}} \\cdot \\begin{{bmatrix}}{b_x_tracker.get_value():.0f} \\\\ {b_y_tracker.get_value():.0f}\\end{{bmatrix}} &= \\sqrt{{{a_x_tracker.get_value():.0f}^2 + {a_y_tracker.get_value():.0f}^2}}\\sqrt{{{b_x_tracker.get_value():.0f}^2 + {b_y_tracker.get_value():.0f}^2}}\\cos(\\theta) \\\\",
            color=WHITE,
            font_size=24
        ),
        MathTex(
            f"{a_x_tracker.get_value():.0f} \\cdot {b_x_tracker.get_value():.0f} + {a_y_tracker.get_value():.0f} \\cdot {b_y_tracker.get_value():.0f} &= {mag_a:.0f} \\cdot {mag_b:.0f} \\cos(\\theta) \\\\",
            color=WHITE,
            font_size=24
        ),
        MathTex(
            f"{dot_product:.0f} &= {mag_a * mag_b:.0f} \\cos(\\theta) \\\\",
            color=WHITE,
            font_size=24
        ),
        MathTex(
            f"\\theta &= {np.arccos(dot_product / (mag_a * mag_b)):.0f} \\text{{ rad}} \\approx {np.degrees(np.arccos(dot_product / (mag_a * mag_b))):.0f}°",
            color=WHITE,
            font_size=24
        )
    ).arrange(DOWN, buff=0.5)

    def update_angle_formula(mob):
        dot_product = a_x_tracker.get_value()*b_x_tracker.get_value() + a_y_tracker.get_value()*b_y_tracker.get_value()
        mag_a = np.sqrt(a_x_tracker.get_value()**2 + a_y_tracker.get_value()**2)
        mag_b = np.sqrt(b_x_tracker.get_value()**2 + b_y_tracker.get_value()**2)
        angle = np.arccos(np.clip(dot_product / (mag_a * mag_b), -1, 1))  # Clip to avoid floating point errors
        
        new_formula = VGroup(
            MathTex(
                r"\vec{a} \cdot \vec{b} &= \|\vec{a}\|\|\vec{b}\|\cos(\theta) \\",
                color=WHITE,
                font_size=24
            ),
            MathTex(
                f"\\begin{{bmatrix}}{a_x_tracker.get_value():.0f} \\\\ {a_y_tracker.get_value():.0f}\\end{{bmatrix}} \\cdot \\begin{{bmatrix}}{b_x_tracker.get_value():.0f} \\\\ {b_y_tracker.get_value():.0f}\\end{{bmatrix}} &= \\sqrt{{{a_x_tracker.get_value():.0f}^2 + {a_y_tracker.get_value():.0f}^2}}\\sqrt{{{b_x_tracker.get_value():.0f}^2 + {b_y_tracker.get_value():.0f}^2}}\\cos(\\theta) \\\\",
                color=WHITE,
                font_size=24
            ),
            MathTex(
                f"{a_x_tracker.get_value():.0f} \\cdot {b_x_tracker.get_value():.0f} + {a_y_tracker.get_value():.0f} \\cdot {b_y_tracker.get_value():.0f} &= {mag_a:.0f} \\cdot {mag_b:.0f} \\cos(\\theta) \\\\",
                color=WHITE,
                font_size=24
            ),
            MathTex(
                f"{dot_product:.0f} &= {mag_a * mag_b:.0f} \\cos(\\theta) \\\\",
                color=WHITE,
                font_size=24
            ),
            MathTex(
                f"\\theta &= {angle:.0f} \\text{{ rad}} \\approx {np.degrees(angle):.0f}°",
                color=WHITE,
                font_size=24
            )
        ).arrange(DOWN, buff=0.5).to_edge(LEFT)
        mob.become(new_formula)
    
    angle_formula.add_updater(update_angle_formula)

    # RIGHT EXAMPLE > Project Vector A Onto Vector B ###########
    ############################################################

    # GROUPS ###################################################
    ############################################################
    # Create VGroups for positioning
    vector_labels = VGroup(label_a, label_b).arrange(RIGHT, buff=1)
    vector_labels.next_to(plane, DOWN, buff=0.5)
    
    length_labels = VGroup(vector_a_length, vector_b_length).arrange(RIGHT, buff=1)
    length_labels.next_to(vector_labels, DOWN, buff=0.5)   

    # Create initial angle visualization
    angle_arc = Angle(
        vector_a, vector_b,
        radius=0.5,
        color=YELLOW,
        other_angle=False
    )
    
    angle_label = MathTex(
        f"{np.degrees(angle):.1f}°",
        color=YELLOW,
        font_size=24
    ).move_to(
        plane.c2p(0,0) + 
        angle_arc.point_from_proportion(0.5) * 1.2
    )

    # Add updaters for angle visualization
    def update_angle_arc(mob):
        try:
            new_angle = Angle(
                vector_a, vector_b,
                radius=0.5,
                color=YELLOW,
                other_angle=False
            )
            mob.become(new_angle)
        except ValueError:  # Handles parallel vectors case
            # Create an empty VMobject when vectors are parallel
            mob.become(VMobject())

    def update_angle_label(mob):
        dot_product = a_x_tracker.get_value()*b_x_tracker.get_value() + a_y_tracker.get_value()*b_y_tracker.get_value()
        mag_a = np.sqrt(a_x_tracker.get_value()**2 + a_y_tracker.get_value()**2)
        mag_b = np.sqrt(b_x_tracker.get_value()**2 + b_y_tracker.get_value()**2)
        
        # Handle zero magnitude vectors
        if mag_a == 0 or mag_b == 0:
            angle = 0
        else:
            # Clip the value to avoid floating point errors
            cos_theta = np.clip(dot_product / (mag_a * mag_b), -1, 1)
            angle = np.arccos(cos_theta)
        
        new_label = MathTex(
            f"{np.degrees(angle):.1f}°",
            color=YELLOW,
            font_size=24
        ).move_to(
            plane.c2p(0,0) + 
            (angle_arc.point_from_proportion(0.5) if not isinstance(angle_arc, VMobject) else UP*0.5) * 1.2
        )
        mob.become(new_label)

    angle_arc.add_updater(update_angle_arc)
    angle_label.add_updater(update_angle_label)

    # ANIMATE ##################################################
    ############################################################
    scene.play(Create(plane))
    scene.play(Write(vector_a), Write(vector_b))
    scene.play(Write(vector_labels))
    scene.play(Write(length_labels))
    scene.wait(1)
    scene.play(Write(angle_formula))
    scene.wait(1)
    scene.play(
        Create(angle_arc),
        Write(angle_label)
    )
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
