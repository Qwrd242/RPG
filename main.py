import pygame
import sys
from SETTINGS import *

pygame.init()

pygame.display.set_caption("RPG")

pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.update()

while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                sys.exit()


pygame.display.update()
