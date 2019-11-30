import pygame
import random
import os
import time
import neat
import pickle
from sglobals import *

class Pipe:
    GAP = 200
    VEL = 5

    def __init__(self, x, img):
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0

        self.PIPE_TOP = pygame.transform.flip(pipe_img, False, True)
        self.PIPE_BOTTOM = pipe_img
