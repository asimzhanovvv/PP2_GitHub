import pygame
import time

pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mickeyclock")

# Load images
icon = pygame.image.load('Labs/Lab7/Ex1/images/clock.svg') # logo
pygame.display.set_icon(icon)

bg = pygame.image.load('Labs/Lab7/Ex1/images/clock.png') # Background
min_img = pygame.image.load('Labs/Lab7/Ex1/images/min_hand.png') # Left hand
sec_img = pygame.image.load('Labs/Lab7/Ex1/images/sec_hand.png') # Right hand

running = True
while running:
    screen.blit(bg, (0, 0))  # Draw bg
    
    # Get current time
    current_time = time.localtime()
    #print(current_time.tm_sec) # Test
    sec_angle = -current_time.tm_sec * 6  # 360° / 60 = 6° per second
    min_angle = -current_time.tm_min * 6 - (current_time.tm_sec / 60) * 6 

    # Rotate hands
    rotated_sec = pygame.transform.rotate(sec_img, sec_angle)
    rotated_min = pygame.transform.rotate(min_img, min_angle)
    
    # Center hands
    sec_rect = rotated_sec.get_rect(center=(400, 300))
    min_rect = rotated_min.get_rect(center=(400, 300))

    # Draw hands
    screen.blit(rotated_min, min_rect.topleft)
    screen.blit(rotated_sec, sec_rect.topleft)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()