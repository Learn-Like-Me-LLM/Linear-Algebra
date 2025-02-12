from manim import *

wait = 1

class S1(Scene):
    def construct(self):
        # TITLE ################
        ########################
        title = Text("What is a Vector?", font_size=40)

        # DEFINITION ###########
        ########################
        definition = MarkupText(
            'A vector is a mathematical entity that simultaneously \npossesses both <span color="RED">magnitude</span> and <span color="YELLOW">direction</span>.',
            font_size=20,
            should_center=True
        )


        # EXAMPLE ###########
        ########################
        statement = MarkupText(
            "The wind is blowing <span color='RED'>6mph</span> <span color='YELLOW'>east</span>.",
            font_size=30,
        )

        # Group text elements and position left
        left_container = VGroup(title, definition, statement).arrange(DOWN, buff=0.5)
        # text_group.scale(0.7)  # Scale down a bit more
        
        # Animation sequence
        self.play(Write(title))
        self.wait(wait)
        self.play(Write(definition))
        self.wait(wait)
        self.play(Write(statement))
        self.wait(wait)
        
        # Move text to left and show border
        self.play(
            left_container.animate.to_edge(LEFT, buff=1),
        )

        # Scale down and position plane
        plane = NumberPlane(
            x_range=[-2, 10, 1],
            y_range=[-2, 10, 1],
            x_length=4.5,  # Reduced further
            y_length=4.5,  # Reduced further
            axis_config={"include_numbers": True}
        )
        right_container = VGroup(plane)
        self.play(
            right_container.animate.to_edge(RIGHT, buff=1),
        )

        # Direction labels
        directions = VGroup(
            Text("North", font_size=16).next_to(plane.y_axis, UP),
            Text("South", font_size=16).next_to(plane.y_axis, DOWN),
            Text("East", font_size=16).next_to(plane.x_axis, RIGHT),
            Text("West", font_size=16).next_to(plane.x_axis, LEFT)
        )
        
        self.play(Write(directions))
        
        # Create vector showing 6 units east
        vector = Arrow(
            start=plane.coords_to_point(0, 0),
            end=plane.coords_to_point(6, 0),
            color=YELLOW,
            buff=0,
            max_tip_length_to_length_ratio=0.2
        )
        
        # Animate vector creation with growing effect
        self.play(GrowArrow(vector))
        self.wait(wait)
        
