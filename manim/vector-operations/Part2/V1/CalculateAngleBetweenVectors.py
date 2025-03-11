from manim import *
import numpy as np

def get_vector_angle(vector):
    """Calculate angle of vector relative to positive x-axis"""
    return np.arctan2(vector[1], vector[0])

def CalculateAngleBetweenVectors(
    scene: Scene, 
    plane, 
    plane_container, 
    vector_a, vector_b, 
    vector_labels,
    a_x_tracker, a_y_tracker, 
    b_x_tracker, b_y_tracker,
    length_labels,
    font_size: int = 25,
    debug: bool = True
):
    
    # Initial angle formula setup
    dot_product = a_x_tracker.get_value()*b_x_tracker.get_value() + a_y_tracker.get_value()*b_y_tracker.get_value()
    mag_a = np.sqrt(a_x_tracker.get_value()**2 + a_y_tracker.get_value()**2)
    mag_b = np.sqrt(b_x_tracker.get_value()**2 + b_y_tracker.get_value()**2)
    angle = np.arccos(dot_product / (mag_a * mag_b))

    dot_product_usage = VGroup(
        Text("The Dot Product can also be used", font_size=font_size),
        Text("to calculate the angle between 2 vectors", font_size=font_size),
    ).arrange(DOWN, buff=0.1).next_to(plane, RIGHT, buff=0.25)

    # ANGLE FORMULA ############################################
    angle_formula = VGroup(
        VGroup(
            VGroup(
                MathTex(r"\vec{a}", font_size=font_size).set_color(PURE_GREEN),
                MathTex(r"\cdot", font_size=font_size),
                MathTex(r"\vec{b}", font_size=font_size).set_color(YELLOW),
            ).arrange(RIGHT, buff=0.1),
            Text("=", font_size=font_size),
            VGroup(
                MathTex(r"\|\vec{a}\|",color=PURE_GREEN, font_size=font_size),
                MathTex(r"\|\vec{b}\|",color=YELLOW, font_size=font_size),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"\cos(", font_size=font_size),
                MathTex(r"\theta", color=ORANGE, font_size=font_size),
                MathTex(r")", font_size=font_size),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.1),
        VGroup(
            VGroup(
                MathTex(r"\sum_{i=1}^{n}", font_size=font_size),
                VGroup(
                    MathTex(r"a_i", font_size=font_size).set_color(PURE_GREEN),
                    MathTex(r"\cdot", font_size=font_size),
                    MathTex(r"b_i", font_size=font_size).set_color(YELLOW),
                ).arrange(RIGHT, buff=0.1),
            ).arrange(RIGHT, buff=0.1),
            Text("=", font_size=font_size),
            VGroup(
                MathTex(r"\sqrt{", r"{a_x}^2 + {a_y}^2", r"}", r"}", font_size=font_size).set_color(PURE_GREEN),
                MathTex(r"\sqrt{", r"{b_x}^2 + {b_y}^2", r"}",font_size=font_size).set_color(YELLOW),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"\cos(", font_size=font_size),
                MathTex(r"\theta", color=ORANGE, font_size=font_size),
                MathTex(r")", font_size=font_size),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.1),
        VGroup(
            VGroup(
                MathTex(f"{dot_product:.0f}", font_size=font_size).set_color(WHITE),
            ).arrange(RIGHT, buff=0.1),
            Text("=", font_size=font_size),
            VGroup(
                MathTex(r"\sqrt{", f"{{{a_x_tracker.get_value():.0f}}}^2 + {{{a_y_tracker.get_value():.0f}}}^2", r"}", font_size=font_size).set_color(PURE_GREEN),
                MathTex(r"\sqrt{", f"{{{b_x_tracker.get_value():.0f}}}^2 + {{{b_y_tracker.get_value():.0f}}}^2", r"}", font_size=font_size).set_color(YELLOW),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"\cos(", font_size=font_size),
                MathTex(r"\theta", color=ORANGE, font_size=font_size),
                MathTex(r")", font_size=font_size),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.1),
        VGroup(
            VGroup(
                MathTex(f"{dot_product:.0f}", font_size=font_size).set_color(WHITE),
            ).arrange(RIGHT, buff=0.1),
            Text("=", font_size=font_size),
            VGroup(
                MathTex(
                    r"\sqrt{" + f"{(a_x_tracker.get_value()**2):.0f} + {(a_y_tracker.get_value()**2):.0f}" + r"}", 
                    font_size=font_size
                ).set_color(PURE_GREEN),
                MathTex(
                    r"\sqrt{" + f"{(b_x_tracker.get_value()**2):.0f} + {(b_y_tracker.get_value()**2):.0f}" + r"}", 
                    font_size=font_size
                ).set_color(YELLOW),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"\cos(", font_size=font_size),
                MathTex(r"\theta", color=ORANGE, font_size=font_size),
                MathTex(r")", font_size=font_size),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.1),
        VGroup(
            VGroup(
                MathTex(f"{dot_product:.0f}", font_size=font_size).set_color(WHITE),
            ).arrange(RIGHT, buff=0.1),
            Text("=", font_size=font_size),
            VGroup(
                MathTex(f"{mag_a:.1f}", 
                    font_size=font_size
                ).set_color(PURE_GREEN),
                MathTex(
                    f"{mag_b:.1f}", 
                    font_size=font_size
                ).set_color(YELLOW),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"\cos(", font_size=font_size),
                MathTex(r"\theta", color=ORANGE, font_size=font_size),
                MathTex(r")", font_size=font_size),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.1),
        VGroup(
            VGroup(
                MathTex(f"{dot_product:.0f}", font_size=font_size).set_color(WHITE),
            ).arrange(RIGHT, buff=0.1),
            Text("=", font_size=font_size),
            VGroup(
                MathTex(f"{(mag_a * mag_b):.1f}", font_size=font_size).set_color(WHITE),
                VGroup(
                    MathTex(r"\cos(", font_size=font_size),
                    MathTex(r"\theta", color=ORANGE, font_size=font_size),
                    MathTex(r")", font_size=font_size),
                ).arrange(RIGHT, buff=0.1),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.1),
        VGroup(
            VGroup(
                MathTex(r"\cos(", font_size=font_size),
                MathTex(r"\theta", color=ORANGE, font_size=font_size),
                MathTex(r")", font_size=font_size),
            ).arrange(RIGHT, buff=0.1),
            Text("=", font_size=font_size),
            VGroup(
                MathTex(f"{dot_product / (mag_a * mag_b):.1f}", font_size=font_size).set_color(WHITE),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.1),
        VGroup(
            MathTex(r"\theta", color=ORANGE, font_size=font_size),
            Text("=", font_size=font_size),
            MathTex(f"{np.degrees(angle):.0f}°", font_size=font_size).set_color(ORANGE),
        ).arrange(RIGHT, buff=0.1),
    ).arrange(DOWN, buff=0.25).to_edge(LEFT)

    # Instead, add individual updaters for each step
    def update_step_3(mob):
        dot_product = a_x_tracker.get_value()*b_x_tracker.get_value() + a_y_tracker.get_value()*b_y_tracker.get_value()
        new_step = VGroup(
            VGroup(
                MathTex(f"{dot_product:.0f}", font_size=font_size).set_color(WHITE),
            ).arrange(RIGHT, buff=0.1),
            Text("=", font_size=font_size),
            VGroup(
                MathTex(r"\sqrt{", f"{{{a_x_tracker.get_value():.0f}}}^2 + {{{a_y_tracker.get_value():.0f}}}^2", r"}", font_size=font_size).set_color(PURE_GREEN),
                MathTex(r"\sqrt{", f"{{{b_x_tracker.get_value():.0f}}}^2 + {{{b_y_tracker.get_value():.0f}}}^2", r"}", font_size=font_size).set_color(YELLOW),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"\cos(", font_size=font_size),
                MathTex(r"\theta", color=ORANGE, font_size=font_size),
                MathTex(r")", font_size=font_size),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.1)
        
        # Preserve the position
        new_step.move_to(mob)
        mob.become(new_step)
    
    def update_step_4(mob):
        dot_product = a_x_tracker.get_value()*b_x_tracker.get_value() + a_y_tracker.get_value()*b_y_tracker.get_value()
        new_step = VGroup(
            VGroup(
                MathTex(f"{dot_product:.0f}", font_size=font_size).set_color(WHITE),
            ).arrange(RIGHT, buff=0.1),
            Text("=", font_size=font_size),
            VGroup(
                MathTex(
                    r"\sqrt{" + f"{(a_x_tracker.get_value()**2):.0f} + {(a_y_tracker.get_value()**2):.0f}" + r"}", 
                    font_size=font_size
                ).set_color(PURE_GREEN),
                MathTex(
                    r"\sqrt{" + f"{(b_x_tracker.get_value()**2):.0f} + {(b_y_tracker.get_value()**2):.0f}" + r"}", 
                    font_size=font_size
                ).set_color(YELLOW),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"\cos(", font_size=font_size),
                MathTex(r"\theta", color=ORANGE, font_size=font_size),
                MathTex(r")", font_size=font_size),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.1)
        
        # Preserve the position
        new_step.move_to(mob)
        mob.become(new_step)
    
    def update_step_5(mob):
        dot_product = a_x_tracker.get_value()*b_x_tracker.get_value() + a_y_tracker.get_value()*b_y_tracker.get_value()
        mag_a = np.sqrt(a_x_tracker.get_value()**2 + a_y_tracker.get_value()**2)
        mag_b = np.sqrt(b_x_tracker.get_value()**2 + b_y_tracker.get_value()**2)
        
        new_step = VGroup(
            VGroup(
                MathTex(f"{dot_product:.0f}", font_size=font_size).set_color(WHITE),
            ).arrange(RIGHT, buff=0.1),
            Text("=", font_size=font_size),
            VGroup(
                MathTex(f"{mag_a:.1f}", font_size=font_size).set_color(PURE_GREEN),
                MathTex(f"{mag_b:.1f}", font_size=font_size).set_color(YELLOW),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"\cos(", font_size=font_size),
                MathTex(r"\theta", color=ORANGE, font_size=font_size),
                MathTex(r")", font_size=font_size),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.1)
        
        # Preserve the position
        new_step.move_to(mob)
        mob.become(new_step)
    
    def update_step_6(mob):
        dot_product = a_x_tracker.get_value()*b_x_tracker.get_value() + a_y_tracker.get_value()*b_y_tracker.get_value()
        mag_a = np.sqrt(a_x_tracker.get_value()**2 + a_y_tracker.get_value()**2)
        mag_b = np.sqrt(b_x_tracker.get_value()**2 + b_y_tracker.get_value()**2)
        
        new_step = VGroup(
            VGroup(
                MathTex(f"{dot_product:.0f}", font_size=font_size).set_color(WHITE),
            ).arrange(RIGHT, buff=0.1),
            Text("=", font_size=font_size),
            VGroup(
                MathTex(f"{(mag_a * mag_b):.1f}", font_size=font_size).set_color(WHITE),
                VGroup(
                    MathTex(r"\cos(", font_size=font_size),
                    MathTex(r"\theta", color=ORANGE, font_size=font_size),
                    MathTex(r")", font_size=font_size),
                ).arrange(RIGHT, buff=0.1),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.1)
        
        # Preserve the position
        new_step.move_to(mob)
        mob.become(new_step)
    
    def update_step_7(mob):
        dot_product = a_x_tracker.get_value()*b_x_tracker.get_value() + a_y_tracker.get_value()*b_y_tracker.get_value()
        mag_a = np.sqrt(a_x_tracker.get_value()**2 + a_y_tracker.get_value()**2)
        mag_b = np.sqrt(b_x_tracker.get_value()**2 + b_y_tracker.get_value()**2)
        
        new_step = VGroup(
            VGroup(
                MathTex(r"\cos(", font_size=font_size),
                MathTex(r"\theta", color=ORANGE, font_size=font_size),
                MathTex(r")", font_size=font_size),
            ).arrange(RIGHT, buff=0.1),
            Text("=", font_size=font_size),
            VGroup(
                MathTex(f"{dot_product / (mag_a * mag_b):.1f}", font_size=font_size).set_color(WHITE),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.1)
        
        # Preserve the position
        new_step.move_to(mob)
        mob.become(new_step)
    
    def update_step_8(mob):
        dot_product = a_x_tracker.get_value()*b_x_tracker.get_value() + a_y_tracker.get_value()*b_y_tracker.get_value()
        mag_a = np.sqrt(a_x_tracker.get_value()**2 + a_y_tracker.get_value()**2)
        mag_b = np.sqrt(b_x_tracker.get_value()**2 + b_y_tracker.get_value()**2)
        angle = np.arccos(np.clip(dot_product / (mag_a * mag_b), -1, 1))
        
        new_step = VGroup(
            MathTex(r"\theta", color=ORANGE, font_size=font_size),
            Text("=", font_size=font_size),
            MathTex(f"{np.degrees(angle):.0f}°", font_size=font_size).set_color(ORANGE),
        ).arrange(RIGHT, buff=0.1)
        
        # Preserve the position
        new_step.move_to(mob)
        mob.become(new_step)
    
    # Add updaters to each step individually
    angle_formula[2].add_updater(update_step_3)
    angle_formula[3].add_updater(update_step_4)
    angle_formula[4].add_updater(update_step_5)
    angle_formula[5].add_updater(update_step_6)
    angle_formula[6].add_updater(update_step_7)
    angle_formula[7].add_updater(update_step_8)

    # ANGLE VISUALIZATION ######################################
    ############################################################
    # ANGLE VISUALIZATION > ARC ################################
    angle_arc = AnnularSector(
        inner_radius=0.5,
        outer_radius=0.7,
        angle=0,
        start_angle=0,
        color=ORANGE,
        fill_opacity=0.3
    )

    def update_angle_arc(mob):
        try:
            # Get current vector positions
            vec_a_start = vector_a.get_start()
            vec_a_end = vector_a.get_end()
            vec_b_start = vector_b.get_start() 
            vec_b_end = vector_b.get_end()

            # Calculate vectors from origin
            v1 = vec_a_end - vec_a_start
            v2 = vec_b_end - vec_b_start

            # Get start angle (angle of first vector)
            start_angle = get_vector_angle(v1)
            
            # Calculate angle between vectors
            angle = calculate_angle_between_vectors(v1, v2)
            
            # Check if we need to flip the start angle
            v2_angle = get_vector_angle(v2)
            angle_diff = (v2_angle - start_angle) % (2 * np.pi)
            if angle_diff > np.pi:
                start_angle = v2_angle
            
            # Create new arc
            new_arc = AnnularSector(
                inner_radius=0.5,
                outer_radius=0.7,
                angle=angle,
                start_angle=start_angle,
                color=ORANGE
            )
            
            mob.points = new_arc.points
            
        except Exception as e:
            print(f"Angle calculation error: {e}")
            mob.points = VMobject().points

    # Add updater to angle arc
    angle_arc.add_updater(update_angle_arc)

    # ANGLE VISUALIZATION > LABEL ##############################
    angle_label = MathTex(
        f"{np.degrees(angle):.0f}°",
        color=ORANGE,
        font_size=font_size
    ).move_to(
        plane.c2p(0,0) + 
        (angle_arc.get_center() - plane.c2p(0,0)) * 0.6
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
        
        # Calculate midpoint angle for label positioning
        vec_a_end = vector_a.get_end() - vector_a.get_start()
        vec_b_end = vector_b.get_end() - vector_b.get_start()
        angle_a = get_vector_angle(vec_a_end)
        angle_b = get_vector_angle(vec_b_end)
        
        # Calculate midpoint angle
        mid_angle = (angle_a + angle_b) / 2
        if abs(angle_a - angle_b) > np.pi:
            mid_angle += np.pi  # Adjust for angle wrapping
            
        # Position at center of arc
        label_position = plane.c2p(0,0) + 0.6 * np.array([
            np.cos(mid_angle),
            np.sin(mid_angle),
            0
        ])
        
        new_label = MathTex(
            f"{np.degrees(angle):.0f}°",
            color=ORANGE,
            font_size=font_size
        ).move_to(label_position)
        
        mob.become(new_label)
    
    angle_label.add_updater(update_angle_label)

    # ANIMATE ##################################################
    ############################################################
    # scene.play(FadeIn(plane, vector_a, vector_b, vector_labels))
    scene.play(Write(angle_formula[0]), Write(dot_product_usage))
    scene.wait(1)
    scene.play(Write(angle_formula[1:]))
    scene.wait(1)
    scene.play(
        Create(angle_arc),
        Write(angle_label)
    )
    scene.wait(1)

    # RANDOMIZE VECTOR(s) #######################################
    ############################################################
    count = 0
    existing = set()
    while count < 3:
        while True:
            new_ax = np.random.randint(-4, 5)
            new_ay = np.random.randint(-4, 5)
            new_bx = np.random.randint(-4, 5)
            new_by = np.random.randint(-4, 5)
            
            # Skip if either vector is zero
            if (new_ax == 0 and new_ay == 0) or (new_bx == 0 and new_by == 0):
                continue
                
            # Skip if vectors are the same
            if new_ax == new_bx and new_ay == new_by:
                continue
                
            # Create tuple of vector components for tracking
            vector_combo = (new_ax, new_ay, new_bx, new_by)
            if vector_combo not in existing:
                existing.add(vector_combo)
                break

        scene.play(
            a_x_tracker.animate.set_value(new_ax),
            a_y_tracker.animate.set_value(new_ay),
            b_x_tracker.animate.set_value(new_bx),
            b_y_tracker.animate.set_value(new_by)
        )
        scene.wait(1.5)
        count += 1

    # CLEAN UP #################################################
    ############################################################
    # Remove Updaters to fix fade out
    angle_arc.remove_updater(update_angle_arc)
    angle_label.remove_updater(update_angle_label)
    angle_formula.remove_updater(update_step_3)
    angle_formula.remove_updater(update_step_4)
    angle_formula.remove_updater(update_step_5)
    angle_formula.remove_updater(update_step_6)
    angle_formula.remove_updater(update_step_7)
    angle_formula.remove_updater(update_step_8)
    scene.play(
        FadeOut(angle_arc), 
        FadeOut(angle_label), 
        FadeOut(angle_formula),
        FadeOut(dot_product_usage)
    )

def calculate_angle_between_vectors(v1, v2):
    # Normalize vectors
    v1_norm = np.linalg.norm(v1)
    v2_norm = np.linalg.norm(v2)
    
    if v1_norm == 0 or v2_norm == 0:
        return 0
        
    # Calculate dot product and angle
    dot_product = np.dot(v1, v2)
    cos_angle = dot_product / (v1_norm * v2_norm)
    
    # Handle numerical errors
    cos_angle = np.clip(cos_angle, -1.0, 1.0)
    angle = np.arccos(cos_angle)
    
    # Always return the acute angle (≤ 180 degrees)
    return min(angle, 2 * np.pi - angle)