from manim import *
import numpy as np

def CalculateAngleBetweenVectors(
    scene: Scene, 
    plane, 
    plane_container, 
    vector_a, vector_b, 
    a_x_tracker, a_y_tracker, b_x_tracker, b_y_tracker,
    debug: bool = False
):
    # Initial angle formula setup
    dot_product = a_x_tracker.get_value()*b_x_tracker.get_value() + a_y_tracker.get_value()*b_y_tracker.get_value()
    mag_a = np.sqrt(a_x_tracker.get_value()**2 + a_y_tracker.get_value()**2)
    mag_b = np.sqrt(b_x_tracker.get_value()**2 + b_y_tracker.get_value()**2)
    angle = np.arccos(dot_product / (mag_a * mag_b))

    # ANGLE FORMULA ############################################
    
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
    ).arrange(DOWN, buff=0.5).to_edge(LEFT)

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

    # ANGLE VISUALIZATION ######################################
    ############################################################
    # ANGLE VISUALIZATION > ARC ################################
    angle_arc = Angle(
        vector_a, vector_b,
        radius=0.5,
        color=YELLOW,
        other_angle=False
    )
    def update_angle_arc(mob):
        try:
            # Get vector angles in radians
            angle_a = np.arctan2(a_y_tracker.get_value(), a_x_tracker.get_value())
            angle_b = np.arctan2(b_y_tracker.get_value(), b_x_tracker.get_value())
            
            # Calculate the absolute difference between angles
            angle_diff = (angle_b - angle_a) % (2 * PI)
            
            new_angle = Angle(
                vector_a, vector_b,
                radius=0.5,
                color=YELLOW,
                other_angle=(angle_diff > PI)  # Use other_angle when the difference is > 180°
            )
            mob.become(new_angle)
        except ValueError:  # Handles parallel vectors case
            mob.become(VMobject())
    angle_arc.add_updater(update_angle_arc)

    # ANGLE VISUALIZATION > LABEL ##############################
    angle_label = MathTex(
        f"{np.degrees(angle):.0f}°",
        color=YELLOW,
        font_size=24
    ).move_to(
        plane.c2p(0,0) + 
        angle_arc.point_from_proportion(0.5) * 1.2
    )
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
            f"{np.degrees(angle):.0f}°",
            color=YELLOW,
            font_size=24
        ).move_to(
            plane.c2p(0,0) + 
            (angle_arc.point_from_proportion(0.5) if not isinstance(angle_arc, VMobject) else UP*0.5) * 1.2
        )
        mob.become(new_label)
    angle_label.add_updater(update_angle_label)

    # ANIMATE ##################################################
    ############################################################
    scene.play(Write(angle_formula))
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