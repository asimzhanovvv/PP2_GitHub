import pygame
import os

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Set up the screen
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")

# Load images
icon = pygame.image.load('Labs/Lab7/Ex2/images/icon.png')  # logo
pygame.display.set_icon(icon)

bg = pygame.image.load('Labs/Lab7/Ex2/images/Moonlit Asteroid.jpg') # background

prev_img = pygame.image.load('Labs/Lab7/Ex2/images/prev.png') # Previous
play_img = pygame.image.load('Labs/Lab7/Ex2/images/play.png') # Play
pause_img = pygame.image.load('Labs/Lab7/Ex2/images/pause.png') # Pause
next_img = pygame.image.load('Labs/Lab7/Ex2/images/next.png') # Next

# Button positions
prev_rect = prev_img.get_rect(topleft=(75, 110))
play_rect = play_img.get_rect(topleft=(175, 110))
next_rect = next_img.get_rect(topleft=(275, 110))

# Load font
font = pygame.font.Font(None, 24)

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
    
    # Display current song title
    song_title = (os.path.basename(songs[current_index]) ).replace(".mp3", '')
    text_surface = font.render(song_title, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, 50))
    screen.blit(text_surface, text_rect.topleft)

    # Draw buttons
    screen.blit(prev_img, prev_rect.topleft)  # Prev
    screen.blit(play_img if paused else pause_img, play_rect.topleft)  # Play/Pause
    screen.blit(next_img, next_rect.topleft)  # Next
    
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
        
        # Handle mouse clicks
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if prev_rect.collidepoint(event.pos):  # Previous track
                current_index = (current_index - 1) % len(songs)
                play_song(current_index, keep_paused=paused)
            elif play_rect.collidepoint(event.pos):  # Play/Pause
                if not paused:
                    pygame.mixer.music.pause()
                    paused = True
                    print("Paused")
                else:
                    pygame.mixer.music.unpause()
                    paused = False
                    print("Resumed")
            elif next_rect.collidepoint(event.pos):  # Next track
                current_index = (current_index + 1) % len(songs)
                play_song(current_index, keep_paused=paused)
    
    pygame.display.update()

pygame.quit()
