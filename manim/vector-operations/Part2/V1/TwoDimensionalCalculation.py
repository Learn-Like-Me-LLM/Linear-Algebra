from manim import *

def TwoDimensionalCalculation(
    scene: Scene, 
    plane, plane_container, 
    title, subtitle, 
    vector_a, vector_b,
    vector_labels,
    a_x_tracker, a_y_tracker,
    b_x_tracker, b_y_tracker,
    debug: bool = False
) -> None:
    

    # FULL CALCULATION #########################################
    ############################################################
    calculation_font_size = 35
    buff = 0.1
    calculation = VGroup(
        VGroup(
            MathTex(r"\vec{a}", font_size=calculation_font_size).set_color(PURE_GREEN),
            MathTex(r"\cdot", font_size=calculation_font_size),
            MathTex(r"\vec{b}", font_size=calculation_font_size).set_color(YELLOW),
        ).arrange(RIGHT, buff=buff),
        VGroup(
            MathTex(r"\begin{bmatrix}" + f"{a_x_tracker.get_value():.0f}" + r"\\[1pt]" + f"{a_y_tracker.get_value():.0f}" + r"\end{bmatrix}", font_size=calculation_font_size).set_color(PURE_GREEN),
            MathTex(f"\cdot", font_size=calculation_font_size),
            MathTex(r"\begin{bmatrix}" + f"{b_x_tracker.get_value():.0f}" + r"\\[1pt]" + f"{b_y_tracker.get_value():.0f}" + r"\end{bmatrix}", font_size=calculation_font_size).set_color(YELLOW),
        ).arrange(RIGHT, buff=buff),
        VGroup(
            VGroup(
                Text("("),
                MathTex(f"{a_x_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(PURE_GREEN),
                MathTex(r"\times", font_size=calculation_font_size),
                MathTex(f"{b_x_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(YELLOW),
                Text(")"),
            ).arrange(RIGHT, buff=buff),
            Text(r"+", font_size=calculation_font_size),
            VGroup(
                Text("("),
                MathTex(f"({a_y_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(PURE_GREEN),
                MathTex(r"\times", font_size=calculation_font_size),
                MathTex(f"{b_y_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(YELLOW),
                Text(")"),
            ).arrange(RIGHT, buff=buff),
        ).arrange(RIGHT, buff=buff),
        VGroup(
            MathTex(f"{a_x_tracker.get_value() * b_x_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(WHITE),
            Text(r"+", font_size=calculation_font_size),
            MathTex(f"{a_y_tracker.get_value() * b_y_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(WHITE),
        ).arrange(RIGHT, buff=buff),
        VGroup(
            MathTex(f"{(a_x_tracker.get_value() * b_x_tracker.get_value()) + (a_y_tracker.get_value() * b_y_tracker.get_value()):.0f}", font_size=calculation_font_size * 1.5).set_color(ORANGE),
        ).arrange(RIGHT, buff=buff),
    ).arrange(DOWN, buff=buff*2)

    # Add updaters for each calculation step
    def update_matrix_step(mob):
        new_step = VGroup(
            MathTex(r"\begin{bmatrix}" + f"{a_x_tracker.get_value():.0f}" + r"\\[1pt]" + f"{a_y_tracker.get_value():.0f}" + r"\end{bmatrix}", font_size=calculation_font_size).set_color(PURE_GREEN),
            MathTex(f"\cdot", font_size=calculation_font_size),
            MathTex(r"\begin{bmatrix}" + f"{b_x_tracker.get_value():.0f}" + r"\\[1pt]" + f"{b_y_tracker.get_value():.0f}" + r"\end{bmatrix}", font_size=calculation_font_size).set_color(YELLOW),
        ).arrange(RIGHT, buff=buff)
        new_step.move_to(mob)
        mob.become(new_step)

    def update_multiplication_step(mob):
        new_step = VGroup(
            VGroup(
                Text("(", font_size=calculation_font_size),
                MathTex(f"{a_x_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(PURE_GREEN),
                MathTex(r"\times", font_size=calculation_font_size),
                MathTex(f"{b_x_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(YELLOW),
                Text(")", font_size=calculation_font_size),
            ).arrange(RIGHT, buff=buff),
            Text(r"+", font_size=calculation_font_size),
            VGroup(
                Text("(", font_size=calculation_font_size),
                MathTex(f"{a_y_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(PURE_GREEN),
                MathTex(r"\times", font_size=calculation_font_size),
                MathTex(f"{b_y_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(YELLOW),
                Text(")", font_size=calculation_font_size),
            ).arrange(RIGHT, buff=buff),
        ).arrange(RIGHT, buff=buff)
        new_step.move_to(mob)
        mob.become(new_step)

    def update_addition_step(mob):
        new_step = VGroup(
            MathTex(f"{a_x_tracker.get_value() * b_x_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(WHITE),
            Text(r"+", font_size=calculation_font_size),
            MathTex(f"{a_y_tracker.get_value() * b_y_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(WHITE),
        ).arrange(RIGHT, buff=buff)
        new_step.move_to(mob)
        mob.become(new_step)

    def update_result_step(mob):
        new_step = VGroup(
            MathTex(f"{(a_x_tracker.get_value() * b_x_tracker.get_value()) + (a_y_tracker.get_value() * b_y_tracker.get_value()):.0f}", font_size=calculation_font_size * 1.5).set_color(ORANGE),
        ).arrange(RIGHT, buff=buff)
        new_step.move_to(mob)
        mob.become(new_step)

    calculation[1].add_updater(update_matrix_step)
    calculation[2].add_updater(update_multiplication_step)
    calculation[3].add_updater(update_addition_step)
    calculation[4].add_updater(update_result_step)
    
    calculation.to_edge(LEFT)

    # ANIMATE ##################################################
    ############################################################
    scene.play(Create(plane))
    scene.play(Write(vector_a), Write(vector_b))
    scene.play(Write(vector_labels))
    scene.wait(1)
    
    count = 0 
    while count < len(calculation):
        scene.play(Write(calculation[count]))
        scene.wait(1)
        count += 1

    # RANDOMIZE VECTOR(s) ######################################
    initial_plane_width = plane.get_width()
    initial_plane_height = plane.get_height()

    # Unit vector demonstrations
    unit_vector_dot_product_bounds = VGroup(
        Text("Unit Vector Dot Products are bound between", font_size=round(calculation_font_size*0.75)),
        Text("-1 and 1 with 0 representing perpendicular vectors", font_size=round(calculation_font_size*0.75))
    ).arrange(DOWN, buff=buff).next_to(plane, DOWN)
    scene.play(Write(unit_vector_dot_product_bounds))

    count = 0
    existing = set()
    while count < 5:
        while True:
            new_ax = np.random.randint(-1, 2)
            new_ay = np.random.randint(-1, 2)
            new_bx = np.random.randint(-1, 2)
            new_by = np.random.randint(-1, 2)
            
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
    scene.play(FadeOut(unit_vector_dot_product_bounds))

    # Optional: Demonstrate with larger vectors
    count = 0
    existing = set()
    while count < 5:
        while True:
            new_ax = np.random.randint(-4, 7)
            new_ay = np.random.randint(-4, 7)
            new_bx = np.random.randint(-4, 7)
            new_by = np.random.randint(-4, 7)
            
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
    scene.play(
        FadeOut(calculation, plane, vector_a, vector_b, vector_labels)
    )