import pygame
from sys import exit


pygame.init()
width,height = 800,600
screen = pygame.display.set_mode((width,height))


talaj_surf = pygame.Surface((width,100))
talaj_surf.fill("Green")
talaj_rect = talaj_surf.get_rect(bottomleft= (0,height))




labda = pygame.image.load("ball.gif").convert_alpha()
labda_rect = labda.get_rect(midbottom = (100, talaj_rect.top))



labda_x = 100


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("black")    
    screen.blit(talaj_surf,talaj_rect)


    screen.blit(labda,(labda_rect))
    labda_x += 1

    pygame.display.update()
