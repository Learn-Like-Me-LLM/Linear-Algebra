from manim import *

wait = 1

class S1(Scene):
    def construct(self):
        # TITLE ################
        ########################
        title = Text("What is a Vector?", font_size=40)
        self.play(Write(title))
        self.wait(wait)
        self.remove(title)

        # DEFINITION ###########
        ########################
        definition = Text("A vector is a mathematical entity that simultaneously possesses both magnitude and direction.", font_size=20)
        self.play(Write(definition))
        self.wait(wait)
        self.remove(definition)

        statement = Text("The wind is blowing 6mph east.")
        self.play(Write(statement))
        self.wait(wait)
        self.remove(statement)

        # NUMBER LINE ##########
        ########################
        number_line = NumberLine(
            x_range=[0, 10, 1],
            include_ticks=True

        )
        self.play(Create(number_line))

        # Create vector animations with "walking" effect
        start_num = 0
        end_num = 5
        
        # Initial vector at starting point
        vector = Arrow(
            start=number_line.number_to_point(start_num),
            end=number_line.number_to_point(start_num),
            color=YELLOW,
            buff=0,
            max_tip_length_to_length_ratio=0.2
        )
        self.play(Create(vector))
        
        # Walk through each number
        for i in range(start_num + 1, end_num + 1):
            # Create new vector for target position
            new_vector = Arrow(
                start=number_line.number_to_point(start_num),
                end=number_line.number_to_point(i),
                color=YELLOW,
                buff=0,
                max_tip_length_to_length_ratio=0.2
            )
            
            # Transform current vector to new position
            self.play(
                Transform(vector, new_vector),
                run_time=0.5
            )
            
            # Pulse animation at each number
            self.play(
                vector.animate.scale(1.2),
                run_time=0.2
            )
            self.play(
                vector.animate.scale(1/1.2),
                run_time=0.2
            )
            
            # Pause briefly
            self.wait(0.3)

        # ########################
        # # NUMBER PLANE #########
        # ########################
        # number_plane = NumberPlane(
        #     x_range=[-10, 10, 1], 
        #     y_range=[-10, 10, 1], 
        #     x_length=20,         
        #     y_length=20, 
        #     axis_config={"include_numbers": True}
        # )
        # # self.play(Create(number_plane))
        # self.wait(wait)

        # # Create and animate points
        # dot1 = Dot(radius=0.1)
        # dot1.move_to(number_plane.coords_to_point(0, 0))
        
        # dot2 = Dot(radius=0.1, color=RED)
        # dot2.move_to(number_plane.coords_to_point(5, 0))
        
        # self.play(Create(dot1))
        # self.wait(wait)

        # self.play(Create(dot2))
        # self.wait(wait)

        # # Create vector between points
        # vector = Arrow(
        #     start=dot1.get_center(),
        #     end=dot2.get_center(),
        #     color=YELLOW,
        #     buff=0
        # )
        # self.play(Create(vector))
        
