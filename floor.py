import pygame
import random
import os
import time
import neat
import pickle
from sglobals import *

class Floor:
    VEL = 5

    def __init__(self, y):
        self.img = base_img
        self.y = y
        self.win = WIN

        self.WIDTH = self.img.get_width()

        self.x1 = 0
        self.x2 = self.WIDTH

    def tick(self, pause=False):
        if not pause:
            self.x1 -= self.VEL
            self.x2 -= self.VEL
            if self.x1 + self.WIDTH < 0:
                self.x1 = self.x2 + self.WIDTH

            if self.x2 + self.WIDTH < 0:
                self.x2 = self.x1 + self.WIDTH

        self.draw() #Always draw sprite, regardless of pause
    def draw(self):
        self.win.blit(self.img, (self.x1, self.y))
        self.win.blit(self.img, (self.x2, self.y))