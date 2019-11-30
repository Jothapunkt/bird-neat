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

    def __init__(self, x):
        self.win = WIN
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0

        self.PIPE_TOP = pygame.transform.flip(pipe_img, False, True)
        self.PIPE_BOTTOM = pipe_img

        self.passed = False

        self.set_height()

    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def draw(self):
        # draw top
        WIN.blit(self.PIPE_TOP, (self.x, self.top))
        # draw bottom
        WIN.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def tick(self, pause=False):
        global score

        if not pause:
            self.x -= self.VEL
        if not self.passed and self.x < BIRD_X:
            self.passed = True
            increment_score()
            print("Score plus one: " + str(score))

        self.draw()

    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        return b_point or t_point