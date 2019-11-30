import pygame
import random
import os
import time
import neat
import pickle
from sglobals import *

from bird import Bird
from floor import Floor

if __name__ == '__main__':
    bird = Bird(150, 350, WIN, bird_images)
    floor = Floor(FLOOR, WIN, base_img)
    clock = pygame.time.Clock()

    run = True
    pause = False

    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_p:
                    pause = not pause

        WIN.blit(bg_img, (0, 0))
        floor.tick(pause)
        bird.tick(pause)

        pygame.display.flip()