import pygame
import random
import os
import time
import neat
import pickle
from sglobals import *

class Bird:
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5
    GRAVITY = 1

    def __init__(self, x, y, win, bird_images):
        self.IMGS = bird_images
        self.win = win
        self.x = x
        self.y = y
        self.tilt = 0
        self.vspeed = 0
        self.animation_counter = 0
        self.img = self.IMGS[0]

    def jump(self):
        self.vspeed = -10.5

    def blitRotateCenter(self):
        rotated_img = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_img.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)

        self.win.blit(rotated_img, new_rect.topleft)

    def draw(self):
        self.animation_counter += 1

        if (self.animation_counter <= self.ANIMATION_TIME):
            self.img = self.IMGS[0]
        elif (self.animation_counter <= 2 * self.ANIMATION_TIME):
            self.img = self.IMGS[1]
        elif (self.animation_counter <= 3 * self.ANIMATION_TIME):
            self.img = self.IMGS[2]
        elif (self.animation_counter <= 4 * self.ANIMATION_TIME):
            self.img = self.IMGS[1]
        else:
            self.img = self.IMGS[0]
            self.animation_counter = 0

        if (self.vspeed >= 0):
            self.tilt -= self.ROT_VEL
            if self.tilt < -self.MAX_ROTATION:
                self.tilt = -self.MAX_ROTATION
        else:
            self.tilt += self.ROT_VEL
            if self.tilt > self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.animation_counter = 2 * self.ANIMATION_TIME

        self.blitRotateCenter()
    def tick(self, pause=False):
        if not pause:
            self.vspeed += self.GRAVITY
            if (self.vspeed > 15):
                self.vspeed = 15

            if (self.y > FLOOR):
                self.kill()

            if (self.y < 0):
                self.y = 0

            self.y += self.vspeed

        self.draw() #Always draw sprite, regardless of pause

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

    def kill(self):
        if (self.vspeed > 0):
            self.vspeed = 0
