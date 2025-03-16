import pygame

pygame.init()

# Screen
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Red Ball")
screen.fill((255, 255, 255))

# Window sizes
WIDTH = 900
HEIGHT = 500
circle_x = WIDTH // 2
circle_y = HEIGHT // 2

# Constants
RADIUS = 25
SPEED = 20

# Load images
icon = pygame.image.load('Labs/Lab7/Ex3/images/ball.png') # logo
pygame.display.set_icon(icon)

running = True

# FPS
clock = pygame.time.Clock()
FPS = 60 

while running: # game loop
    for event in pygame.event.get(): # event loop
        if event.type == pygame.QUIT:
            running = False
    pressed_keys = pygame.key.get_pressed() 
    if not (circle_y <= RADIUS) and pressed_keys[pygame.K_UP]:
        circle_y -= SPEED
    if not (circle_y >= HEIGHT - RADIUS) and pressed_keys[pygame.K_DOWN]:
        circle_y += SPEED
    if not (circle_x >= WIDTH - RADIUS) and pressed_keys[pygame.K_RIGHT]:
        circle_x += SPEED
    if not (circle_x <= RADIUS) and pressed_keys[pygame.K_LEFT]:
        circle_x -= SPEED

    screen.fill((255,255,255)) 
    pygame.draw.circle(screen, (255, 0, 0), (circle_x, circle_y),  RADIUS)

    pygame.display.flip() # updates the screen
    clock.tick(FPS) # sets the FPS
    # delay is 1000.0 / FPS