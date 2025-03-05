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
    calculation = VGroup(
        VGroup(
            MathTex(r"\vec{a}"),
            MathTex(r"\cdot"),
            MathTex(r"\vec{b}"),
        ).arrange(RIGHT, buff=0.25),
        VGroup(
            MathTex(r"\begin{bmatrix}" + f"{a_x_tracker.get_value():.0f}" + r"\\[1pt]" + f"{a_y_tracker.get_value():.0f}" + r"\end{bmatrix}"),
            MathTex(f"\cdot"),
            MathTex(r"\begin{bmatrix}" + f"{b_x_tracker.get_value():.0f}" + r"\\[1pt]" + f"{b_y_tracker.get_value():.0f}" + r"\end{bmatrix}")
        ).arrange(RIGHT, buff=0.25),
        VGroup(
            MathTex(f"({a_x_tracker.get_value():.0f}" + r"\times" + f"{b_x_tracker.get_value():.0f})"),
            Text(r"+"),
            MathTex(f"({a_y_tracker.get_value():.0f}" + r"\times" + f"{b_y_tracker.get_value():.0f})"),
        ).arrange(RIGHT, buff=0.25),
        VGroup(
            MathTex(f"{a_x_tracker.get_value() * b_x_tracker.get_value():.0f}"),
            Text(r"+"),
            MathTex(f"{a_y_tracker.get_value() * b_y_tracker.get_value():.0f}"),
        ).arrange(RIGHT, buff=0.25),
        VGroup(
            MathTex(f"{(a_x_tracker.get_value() * b_x_tracker.get_value()) + (a_y_tracker.get_value() * b_y_tracker.get_value()):.0f}"),
        ).arrange(RIGHT, buff=0.25)
    ).arrange(DOWN, buff=0.25)
    calculation[0][0].set_color(BLUE)
    calculation[0][2].set_color(RED)
    calculation[1][0].set_color(BLUE)
    calculation[1][2].set_color(RED)
    
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