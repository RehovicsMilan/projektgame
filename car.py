import pygame
import sys
import math

pygame.init()

# 🎮 ABLAK
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Autós játék - körök")

clock = pygame.time.Clock()

# 🖊️ FONT
font = pygame.font.SysFont("Arial", 24)

# 🗺️ PÁLYA
track_surface = pygame.image.load("track.png").convert()
track_surface = pygame.transform.scale(track_surface, (WIDTH, HEIGHT))

# 🚗 AUTÓ
car_w, car_h = 25, 45
car_surface = pygame.Surface((car_w, car_h), pygame.SRCALPHA)

pygame.draw.rect(car_surface, (220, 0, 0), (3, 3, 19, 38), border_radius=5)
pygame.draw.rect(car_surface, (180, 0, 0), (6, 10, 13, 15), border_radius=3)
pygame.draw.rect(car_surface, (200, 200, 255), (7, 12, 11, 7), border_radius=2)

pygame.draw.rect(car_surface, (255, 200, 0), (3, 38, 4, 4))
pygame.draw.rect(car_surface, (255, 200, 0), (18, 38, 4, 4))

for x in [1, 20]:
    pygame.draw.rect(car_surface, (20, 20, 20), (x, 10, 4, 10))
    pygame.draw.rect(car_surface, (20, 20, 20), (x, 25, 4, 10))

# 🚗 ÁLLAPOT
car_x = WIDTH // 2
car_y = HEIGHT // 2

angle = 0
speed = 0

accel = 0.25
friction = 0.05
max_speed = 6
turn_speed = 3

# ⏱️ KÖR IDŐ
lap_start = pygame.time.get_ticks()
last_lap = 0


def on_screen(x, y):
    return 0 <= x < WIDTH and 0 <= y < HEIGHT


def on_finish_line(x, y):
    if 0 <= int(x) < WIDTH and 0 <= int(y) < HEIGHT:
        color = track_surface.get_at((int(x), int(y)))[:3]
        return color == (255, 0, 0)
    return False


# 🎮 LOOP
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

    # 🧊 súrlódás
    if speed > 0:
        speed -= friction
    elif speed < 0:
        speed += friction

    speed = max(-max_speed, min(max_speed, speed))

    # 🚗 mozgás
    rad = math.radians(angle)
    car_x -= math.sin(rad) * speed
    car_y -= math.cos(rad) * speed

    # 🧭 fordulás csak mozgásnál
    if abs(speed) > 0.1:
        if keys[pygame.K_a]:
            angle += turn_speed * (1 if speed > 0 else -1)
        if keys[pygame.K_d]:
            angle -= turn_speed * (1 if speed > 0 else -1)

    # 🧱 képernyő határ
    if not on_screen(car_x, car_y):
        car_x, car_y = old_x, old_y
        speed = 0

    # 🏁 KÖR LOGIKA
    if on_finish_line(car_x, car_y):
        now = pygame.time.get_ticks()

        if now - lap_start > 2000:  # anti-double trigger
            last_lap = (now - lap_start) / 1000
            lap_start = now

    # 🎨 RENDER
    screen.blit(track_surface, (0, 0))

    rotated = pygame.transform.rotate(car_surface, angle)
    rect = rotated.get_rect(center=(car_x, car_y))
    screen.blit(rotated, rect.topleft)

    # 📊 SPEED
    speed_text = font.render(f"Speed: {abs(speed):.2f}", True, (0, 0, 0))
    screen.blit(speed_text, (10, 10))

    # ⏱️ AKTUÁLIS KÖR
    current_lap = (pygame.time.get_ticks() - lap_start) / 1000
    lap_text = font.render(f"Lap: {current_lap:.2f}s", True, (0, 0, 0))
    screen.blit(lap_text, (10, 40))

    # 🏁 ELŐZŐ KÖR
    last_text = font.render(f"Last Lap: {last_lap:.2f}s", True, (0, 0, 0))
    screen.blit(last_text, (10, 70))

    pygame.display.flip()

pygame.quit()
sys.exit()