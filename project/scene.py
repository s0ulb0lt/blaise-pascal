from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen

class BlaisePascal(Scene):
    def construct(self):
        title = Tex("Blaise Pascal").scale(2)
        span = Tex("1623 - 1662").scale(2)
        span.move_to(2.2*UP)
        imtitle = ImageMobject("bpascal").scale(0.5)
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(title.animate.move_to(2.2*UP))
        self.play(FadeIn(imtitle))
        self.wait(1)
        self.play(Transform(title, span))
