import pygame

pygame.init()

screen = pygame.display.set_mode((1200,800))
clock = pygame.time.Clock()




auto_surf = pygame.image.load("kepek/auto.png").convert_alpha




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(auto_surf,(100,100))


    clock.tick(60)
    pygame.display.update()

pygame.quit()










