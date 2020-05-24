import os
from os import path

#  meta:
GAME_FOLDER = os.path.dirname(__file__)
INPUT_FILE = os.path.join(GAME_FOLDER, "input.txt")

#  general settings:
FPS = 60
WIDTH = 900
HEIGHT = 600
TITLE = "Artillery Clone"
FONT = "arial"

#  colors:
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 155, 155)

#  game settings:
P_SIZE = 15  # player size
B_SIZE = 5  # bullet size
METER = 60  # 1 [m] = 60 [pixels]
SECOND = FPS  # 1 [s] = FPS [frames]
MpS = METER / SECOND
GRAVITY = 9.81 * METER / (SECOND**2)  # m / (s / frame rate per second)^2 or [meters per frame, per frame]
WIND_CHANGE_RATE = 3 * FPS
ARROW_SCALE = 30
W_X_LIMIT = 10  # wind x axis acceleration limit
W_Y_LIMIT = 3  # wind y axis acceleration limit
