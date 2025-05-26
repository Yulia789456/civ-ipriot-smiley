import time
from blinkable import Blinkable
from smiley import Smiley

class Angry(Smiley, Blinkable):
    def __init__(self):
        super().__init__(complexion=self.RED)

        self.draw_mouth()
        self.draw_eyes()

    def draw_mouth(self):
        mouth = [49, 54, 41, 42, 43, 44, 45, 46]
        for pixel in mouth:
            self.pixels[pixel] = self.BLANK

    def draw_eyes(self, wide_open=True):
        eyes = [18, 21, 25, 26, 29, 30]
        for pixel in eyes:
            if wide_open:
                eyes = self.BLANK
            else:
                eyes = self.complexion()
            self.pixels[pixel] = eyes
            
    def blink(self, delay=0.25):
        for _ in range(3):
            self.draw_eyes(wide_open=False)
            self.show()
            time.sleep(delay)
            self.draw_eyes(wide_open=True)
            self.show()
            time.sleep(delay)


