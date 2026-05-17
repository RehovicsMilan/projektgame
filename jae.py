import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Racer")
clock = pygame.time.Clock()




auto_surf = pygame.image.load("kepek/car.png").convert_alpha()
auto_rect = auto_surf.get






running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(auto_surf,(100,100))

    pygame.display.flip()

pygame.quit()
