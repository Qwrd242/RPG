import pygame
from SETTINGS import *
import game_functions as gf

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("RPG")

while True:
    gf.update_screen(screen)
    gf.check_events()
