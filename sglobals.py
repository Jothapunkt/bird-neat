import pygame
import os

pygame.init()

pygame.font.init()

WIN_WIDTH = 600
WIN_HEIGHT = 800
FLOOR = 730
DRAW_LINES = False
BIRD_X = 120
BIRD_Y = 350
STAT_FONT = pygame.font.SysFont("comicsans", 90)

score = 0
global_tick = 0
pipes = []

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","pipe.png")).convert_alpha())
bg_img = pygame.transform.scale(pygame.image.load(os.path.join("imgs","bg.png")).convert_alpha(), (600, 900))
bird_images = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","bird" + str(x) + ".png"))) for x in range(1,4)]
base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs","base.png")).convert_alpha())

pause_img = pygame.transform.scale(pygame.image.load(os.path.join("imgs","pause.png")).convert_alpha(), (150, 150))

gen = 0

def increment_score():
    global score
    print("Score: " + str(score))
    score += 1
    print("New Score: " + str(score))

def get_score():
    return score

def reset_score():
    global score
    score = 0