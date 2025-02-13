from manim import SurroundingRectangle, RED

def create_border(mobject, color=RED):
    rect = SurroundingRectangle(mobject, color=color, buff=0.1)
    rect.add_updater(lambda r: r.move_to(mobject))
    return rect