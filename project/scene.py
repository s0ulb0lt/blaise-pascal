from manim import *
from math import comb

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

class BlaisePascalIntro(Scene):
    def construct(self):
        title = Tex("Blaise Pascal").scale(2)
        span = Tex("1623 - 1662").scale(2)
        span.move_to(2.2*UP)
        imtitle = ImageMobject("bpascal").scale(0.5)
        conimage = SVGMobject("conicsections.svg").scale(1)
        self.play(DrawBorderThenFill(title))
        self.wait(2)
        self.play(title.animate.move_to(2.2*UP))
        self.play(FadeIn(imtitle))
        self.wait(1)
        self.play(Transform(title, span))
        self.wait(3)
        
        rmAnimTitle = [
            FadeOut(title, shift=DOWN),
            FadeOut(imtitle, shift=DOWN)
        ]

        self.play(AnimationGroup(*rmAnimTitle, lag_ratio=0.5))
        self.wait(3)
        mTitle = Tex("Mathematician").scale(2)
        cTitle = Tex("Conics").scale(1)
        self.play(DrawBorderThenFill(mTitle))
        self.wait(3)
        self.play(Transform(mTitle, cTitle))
        self.play(mTitle.animate.move_to(1.2*UP+2.2*LEFT))
        self.play(DrawBorderThenFill(conimage))
        self.play(ScaleInPlace(conimage, 0.5))
        self.play(conimage.animate.move_to(2.2*LEFT))

        self.wait()
        pyramid=VGroup(*[
            VGroup(*[
                MathTex(comb(row, col))
                for col in range(row+1)
            ]).arrange(RIGHT)
            for row in range(4)
        ]).arrange(DOWN)
        self.play(DrawBorderThenFill(pyramid))
        self.wait(1)
        self.play(pyramid.animate.move_to(2.2*RIGHT+0.2*DOWN))

        ptrstitle = Tex("Pascal's Triangle").scale(1)
        ptrstitle.move_to(2.2*RIGHT+1.2*UP)
        self.play(FadeIn(ptrstitle, target_position=mTitle))
        self.wait(2)
        

