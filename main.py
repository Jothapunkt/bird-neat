import pygame
import random
import os
import time
import neat
import pickle
from sglobals import *

from bird import Bird
from floor import Floor
from pipe import Pipe

def reset_game():
    global pipes

    for bird in birds:
        bird.y = BIRD_Y
        bird.vspeed = 0

        pipes = []
        reset_score()

if __name__ == '__main__':
    birds = []
    birds.append(Bird(BIRD_X, BIRD_Y))
    floor = Floor(FLOOR)
    clock = pygame.time.Clock()

    pygame.font.init()

    run = True
    pause = False
    manual = True

    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not pause and manual:
                    for bird in birds:
                        bird.jump()
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_p:
                    pause = not pause

        if not pause:
            global_tick += 1
            if global_tick % 100 is 0:
                pipes.append(Pipe(WIN_WIDTH + 100))

        WIN.blit(bg_img, (0, 0))
        floor.tick(pause)

        score_label = STAT_FONT.render(str(get_score()), 1, (255, 255, 255))

        if not pause:
            WIN.blit(score_label, (0.5 * (WIN_WIDTH - score_label.get_width()), 250))

        for pipe in pipes:
            pipe.tick(pause)

        for bird in birds:
            bird.tick(pause)
            if bird.y > FLOOR:
                reset_game()
            else:
                for pipe in pipes:
                    if pipe.collide(bird):
                        reset_game()

        if pause:
            WIN.blit(pause_img, (225, 200))

        pygame.display.flip()