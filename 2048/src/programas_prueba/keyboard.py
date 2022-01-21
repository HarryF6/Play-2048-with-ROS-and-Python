import autopy
import math
import time
import random
import sys

TWO_PI = math.pi * 2.0

#autopy.key.type_string("Hello, world!") # Prints out "Hello, world!" as quickly as OS will allow.
#autopy.key.type_string("Hello, world!\n", wpm=60) # Prints out "Hello, world!" at 60 WPM.
"""autopy.key.tap(autopy.key.Code.LEFT_ARROW)
autopy.key.tap(autopy.key.Code.RIGHT_ARROW)
autopy.key.tap(autopy.key.Code.DOWN_ARROW)
autopy.key.tap(autopy.key.Code.UP_ARROW)"""
"""i = 0
width, height = autopy.screen.size()
height /= 2
height -= 10  # Stay in the screen bounds.

for x in range(int(width)):
    y = int(height * math.sin((TWO_PI * x) / width) + height)
    autopy.mouse.move(x, y)
    time.sleep(random.uniform(0.001, 0.003))"""
autopy.mouse.move(500, 200)

#click del raton
autopy.mouse.click()
autopy.key.tap(autopy.key.Code.UP_ARROW)
time.sleep(5)
autopy.key.tap(autopy.key.Code.DOWN_ARROW)
time.sleep(5)

