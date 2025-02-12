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
            'A <span color="GREEN">vector</span> is a mathematical entity that simultaneously \npossesses both <span color="RED">magnitude</span> and <span color="YELLOW">direction</span>.',
            font_size=20,
            should_center=True
        )


        # EXAMPLE ###########
        ########################
        statement = MarkupText(
            "The <span color='GREEN'>wind</span> is blowing <span color='RED'>6mph</span> <span color='YELLOW'>east</span>.",
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
            x_range=[-5, 10, 1],
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
        vector2 = Arrow(
            start=plane.coords_to_point(2, 3),
            end=plane.coords_to_point(8, 3),
            color=GREEN,
            buff=0,
            max_tip_length_to_length_ratio=0.2
        )
        vector3 = Arrow(
            start=plane.coords_to_point(-3, 7),
            end=plane.coords_to_point(3, 7),
            color=GREEN,
            buff=0,
            max_tip_length_to_length_ratio=0.2
        )
        
        # Add standard position description
        standard_position = MarkupText(
            "<span color='YELLOW'>Standard Position</span> refers to the vector's \nstarting point being at the origin (0,0).",
            font_size=10
        ).next_to(left_container, DOWN)
        self.play(GrowArrow(vector))
        self.play(Write(standard_position))
        self.wait(wait)

        # Add vector equivalence description
        non_standard_position = MarkupText(
            "All these vectors are the same <span color='GREEN'>vector</span>,\ndespite their different starting points.", 
            font_size=10
        ).next_to(standard_position, DOWN)
        self.play(GrowArrow(vector2), GrowArrow(vector3))
        self.play(Write(non_standard_position))
        self.wait(wait)
        
