from manim import *

class SVGs(Scene):
    def construct(self):

        icon = SVGMobject(f"/Users/spectre/Desktop/TRY/assets/youtube-svgrepo-com.svg")

        self.play(DrawBorderThenFill(icon))