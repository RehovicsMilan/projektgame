import pygame
from pygame.locals import *

size = 1200,900
width, height = size

pygame.init()

screen = pygame.display.set_mode(size)

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        print(event)



pygame.quit()
