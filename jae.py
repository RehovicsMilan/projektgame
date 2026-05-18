import pygame

pygame.init()



Screen_Widht,Screen_Height = 800,600
screen = pygame.display.set_mode((Screen_Widht,Screen_Height))

pygame.display.set_caption("Racer")
clock = pygame.time.Clock()




auto_surf = pygame.image.load("kepek/car.png").convert_alpha()
auto_rect = auto_surf.get_frect(center =(Screen_Widht/2,Screen_Height/2) )





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('chartreuse4')






    screen.blit(auto_surf,auto_rect)
    auto_rect.top += 0.4

    pygame.display.update()

pygame.quit()
