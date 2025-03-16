import pygame
import os

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Set up the screen
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")
screen.fill((255, 255, 255))

# Load images
icon = pygame.image.load('Labs/Lab7/Ex2/images/icon.png') # logo
pygame.display.set_icon(icon)

bg = pygame.image.load('Labs/Lab7/Ex2/images/Moonlit Asteroid.jpg') # background

# Load songs from folder
songs_folder = "Labs/Lab7/Ex2/songs"
songs = [os.path.join(songs_folder, f) for f in os.listdir(songs_folder) if f.endswith(".mp3")]

if not songs:
    print("No songs found!")
    exit()

current_index = 0
paused = False

# Function to play a song
def play_song(index, keep_paused=False):
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()
    if keep_paused:
        pygame.mixer.music.pause()
    print(f"Playing: {os.path.basename(songs[index])}{' (Paused)' if keep_paused else ''}")

# Start playing the first song
play_song(current_index)

running = True

while running:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle key presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Play/Pause
                if not paused:
                    pygame.mixer.music.pause()
                    paused = True
                    print("Paused")
                else:
                    pygame.mixer.music.unpause()
                    paused = False
                    print("Resumed")

            elif event.key == pygame.K_RIGHT:  # Next track
                current_index = (current_index + 1) % len(songs)
                play_song(current_index, keep_paused=paused)
            elif event.key == pygame.K_LEFT:  # Previous track
                current_index = (current_index - 1) % len(songs)
                play_song(current_index, keep_paused=paused)
    
    pygame.display.update()

pygame.quit()
