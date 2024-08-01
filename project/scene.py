from manim import *
from math import comb

from pathlib import Path
from openai import OpenAI
import os

client = OpenAI()

speechFilePath = Path(__file__).parent / "speech.mp3"
respone = client.audio.speech.create(
    model="tts-1",
    voice="echo",
    input="This is the story of Blaise Pascal. 1623-1662. Blaise Pascal was, simply, a mathematician from birth. At 16, he invented his conic sections hexagon theorem. Along with expanding the binomial theorem with Pascal’s triangle."
)

respone.stream_to_file(speech_file_path)

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
        self.play(FadeOut(mTitle, conimage, ptrstitle, pyramid))
        self.wait(1)
        ch2title = Tex("Chapter 2: Early Life").scale(2)
        self.wait(1)
        bdate = Tex("June 19, 1623").scale(2)

        bPlace = Tex("Clermont, France").scale(1)
        bPlace.move_to(2*UP)

        self.play(DrawBorderThenFill(ch2title))
        self.wait(1)
        self.play(Transform(ch2title, bdate))
        self.play(ch2title.animate.move_to(UP*3))
        self.wait(1)
        clermontim = ImageMobject("clermont")
        self.play(FadeIn(clermontim, shift=UP))
        self.play(Transform(ch2title, bPlace))
        self.wait(3)

        paperTitle = Tex("Essai pour les Coniques")
        paperImage = SVGMobject("scroll.svg").scale(1)
        self.play(FadeOut(clermontim, ch2title))
        self.wait(1)
        self.play(DrawBorderThenFill(paperTitle))
        self.play(paperTitle.animate.move_to(UP*3))
        self.wait(1)
        self.play(DrawBorderThenFill(paperImage))
        self.play(paperImage.animate.move_to(LEFT*2))
        lCircle = Tex("Académie libre")
        lCircle.move_to(UP*3)

        roundtable = SVGMobject("roundtable.svg")
        roundtable.move_to(RIGHT*2)
        self.play(DrawBorderThenFill(roundtable))
        self.wait(1)
        self.play(Transform(paperTitle, lCircle))
        self.play(FadeOut(paperTitle, roundtable, paperImage))

        ch3title = Tex("Chapter 3: Problem of Points").scale(2)
        pl1 = Tex("Player 1")
        pl2 = Tex("Player 2")
        player2Wins = Tex("Player 2 Wins")
        wRounds = Tex("Win Rounds: 5")
        pl1rWon = Tex("5")
        plr2Won = Tex("3")
        pl1rWon.move_to(RIGHT*3)
        plr2Won.move_to(LEFT*3)
        pl2.move_to(RIGHT*3+UP*2)
        self.play(DrawBorderThenFill(ch3title))
        self.play(Transform(ch3title, pl1))
        self.play(ch3title.animate.move_to(LEFT*3+UP*2))
        self.play(FadeIn(pl2, target_position=ch3title))
        self.play(DrawBorderThenFill(wRounds))
        self.play(wRounds.animate.move_to(UP*1))
        self.play(FadeIn(pl1rWon, target_position=ch3title))
        self.play(FadeIn(plr2Won, target_position=pl2))
        self.play(FadeIn(player2Wins))
        self.wait(1)

        self.play(FadeOut(ch3title, pl2, plr2Won, pl1rWon, player2Wins, wRounds))

        ch4Title = Tex("Chapter 4: Modern Probability").scale(2)
        self.play(DrawBorderThenFill(ch4Title))


        








        

