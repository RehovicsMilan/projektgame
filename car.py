import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Verseny pálya - fejlesztett autó")

clock = pygame.time.Clock()

# Színek
GRASS = (34, 177, 76)
TRACK = (120, 120, 120)

# 🚗 AUTÓ (részletes sprite)
car_w, car_h = 40, 70
car_surface = pygame.Surface((car_w, car_h), pygame.SRCALPHA)

# Karosszéria
pygame.draw.rect(car_surface, (220, 0, 0), (5, 5, 30, 60), border_radius=6)

# Kabin
pygame.draw.rect(car_surface, (180, 0, 0), (10, 15, 20, 25), border_radius=4)

# Szélvédő
pygame.draw.rect(car_surface, (200, 200, 255), (12, 18, 16, 10), border_radius=3)

# Lámpák
pygame.draw.rect(car_surface, (255, 200, 0), (7, 60, 6, 5))
pygame.draw.rect(car_surface, (255, 200, 0), (27, 60, 6, 5))

# Kerekek (optikai)
for x in [2, 33]:
    pygame.draw.rect(car_surface, (20, 20, 20), (x, 15, 5, 15))
    pygame.draw.rect(car_surface, (20, 20, 20), (x, 45, 5, 15))


# 🏁 Autó állapot
car_x = WIDTH // 2
car_y = HEIGHT // 2

angle = 0
speed = 0

accel = 0.25
friction = 0.05
max_speed = 6
turn_speed = 3

# 🛣️ Pálya
track_surface = pygame.Surface((WIDTH, HEIGHT))
track_surface.fill(GRASS)

pygame.draw.ellipse(track_surface, TRACK, (100, 100, 600, 400))
pygame.draw.ellipse(track_surface, GRASS, (200, 200, 400, 200))


def on_screen(x, y):
    return 0 <= x < WIDTH and 0 <= y < HEIGHT


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    old_x, old_y = car_x, car_y

    # 🚗 gyorsítás
    if keys[pygame.K_w]:
        speed += accel
    if keys[pygame.K_s]:
        speed -= accel

    # súrlódás
    if speed > 0:
        speed -= friction
    elif speed < 0:
        speed += friction

    speed = max(-max_speed, min(max_speed, speed))

    # 🧭 forgás
    if speed != 0:
        if keys[pygame.K_a]:
            angle += turn_speed
        if keys[pygame.K_d]:
            angle -= turn_speed

    # 🚗 mozgás
    rad = math.radians(angle)
    car_x -= math.sin(rad) * speed
    car_y -= math.cos(rad) * speed

    # 🧱 képernyő határ
    if not on_screen(car_x, car_y):
        car_x, car_y = old_x, old_y
        speed = 0

    # 🎨 rajzolás
    screen.blit(track_surface, (0, 0))

    rotated_car = pygame.transform.rotate(car_surface, angle)
    rect = rotated_car.get_rect(center=(car_x, car_y))
    screen.blit(rotated_car, rect.topleft)

    pygame.display.flip()

pygame.quit()
sys.exit()