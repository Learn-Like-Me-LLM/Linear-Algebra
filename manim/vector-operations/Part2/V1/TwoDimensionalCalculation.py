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
    calculation_font_size = 24
    calculation = VGroup(
        VGroup(
            MathTex(r"\vec{a}", font_size=calculation_font_size).set_color(PURE_GREEN),
            MathTex(r"\cdot", font_size=calculation_font_size),
            MathTex(r"\vec{b}", font_size=calculation_font_size).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.25),
        VGroup(
            MathTex(r"\begin{bmatrix}" + f"{a_x_tracker.get_value():.0f}" + r"\\[1pt]" + f"{a_y_tracker.get_value():.0f}" + r"\end{bmatrix}", font_size=calculation_font_size).set_color(PURE_GREEN),
            MathTex(f"\cdot", font_size=calculation_font_size),
            MathTex(r"\begin{bmatrix}" + f"{b_x_tracker.get_value():.0f}" + r"\\[1pt]" + f"{b_y_tracker.get_value():.0f}" + r"\end{bmatrix}", font_size=calculation_font_size).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.25),
        VGroup(
            VGroup(
                Text("("),
                MathTex(f"{a_x_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(PURE_GREEN),
                MathTex(r"\times", font_size=calculation_font_size),
                MathTex(f"{b_x_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(YELLOW),
                Text(")"),
            ).arrange(RIGHT, buff=0.25),
            Text(r"+", font_size=calculation_font_size),
            VGroup(
                Text("("),
                MathTex(f"({a_y_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(PURE_GREEN),
                MathTex(r"\times", font_size=calculation_font_size),
                MathTex(f"{b_y_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(YELLOW),
                Text(")"),
            ).arrange(RIGHT, buff=0.25),
        ).arrange(RIGHT, buff=0.25),
        VGroup(
            MathTex(f"{a_x_tracker.get_value() * b_x_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(PURE_GREEN),
            Text(r"+", font_size=calculation_font_size),
            MathTex(f"{a_y_tracker.get_value() * b_y_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.25),
        VGroup(
            MathTex(f"{(a_x_tracker.get_value() * b_x_tracker.get_value()) + (a_y_tracker.get_value() * b_y_tracker.get_value()):.0f}", font_size=calculation_font_size * 1.5).set_color(ORANGE),
        ).arrange(RIGHT, buff=0.25)
    ).arrange(DOWN, buff=0.25)

    # Add updaters for each calculation step
    def update_matrix_step(mob):
        new_step = VGroup(
            MathTex(r"\begin{bmatrix}" + f"{a_x_tracker.get_value():.0f}" + r"\\[1pt]" + f"{a_y_tracker.get_value():.0f}" + r"\end{bmatrix}", font_size=calculation_font_size).set_color(PURE_GREEN),
            MathTex(f"\cdot", font_size=calculation_font_size),
            MathTex(r"\begin{bmatrix}" + f"{b_x_tracker.get_value():.0f}" + r"\\[1pt]" + f"{b_y_tracker.get_value():.0f}" + r"\end{bmatrix}", font_size=calculation_font_size).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.25)
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
            ).arrange(RIGHT, buff=0.25),
            Text(r"+", font_size=calculation_font_size),
            VGroup(
                Text("(", font_size=calculation_font_size),
                MathTex(f"{a_y_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(PURE_GREEN),
                MathTex(r"\times", font_size=calculation_font_size),
                MathTex(f"{b_y_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(YELLOW),
                Text(")", font_size=calculation_font_size),
            ).arrange(RIGHT, buff=0.25),
        ).arrange(RIGHT, buff=0.25)
        new_step.move_to(mob)
        mob.become(new_step)

    def update_addition_step(mob):
        new_step = VGroup(
            MathTex(f"{a_x_tracker.get_value() * b_x_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(PURE_GREEN),
            Text(r"+", font_size=calculation_font_size),
            MathTex(f"{a_y_tracker.get_value() * b_y_tracker.get_value():.0f}", font_size=calculation_font_size).set_color(YELLOW),
        ).arrange(RIGHT, buff=0.25)
        new_step.move_to(mob)
        mob.become(new_step)

    def update_result_step(mob):
        new_step = VGroup(
            MathTex(f"{(a_x_tracker.get_value() * b_x_tracker.get_value()) + (a_y_tracker.get_value() * b_y_tracker.get_value()):.0f}", font_size=calculation_font_size * 1.5).set_color(ORANGE),
        ).arrange(RIGHT, buff=0.25)
        new_step.move_to(mob)
        mob.become(new_step)

    calculation[1].add_updater(update_matrix_step)
    calculation[2].add_updater(update_multiplication_step)
    calculation[3].add_updater(update_addition_step)
    calculation[4].add_updater(update_result_step)
    
    calculation.to_edge(LEFT)

    # ANIMATE ##################################################
    ############################################################
    count = 0 
    while count < len(calculation):
        scene.play(Write(calculation[count]))
        scene.wait(1)
        count += 1

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

    # CLEAN UP #################################################
    ############################################################
    scene.play(
        FadeOut(calculation)
    )