import pygame
import random
import db_handler

pygame.init()


# Basic settings
WIDTH = 600
HEIGHT = 600
CELL = 30
FPS_START = 5.5

# Sounds
sound_eating = pygame.mixer.Sound('Labs/Lab10/Snake/sounds/eating.mp3')
sound_eating.set_volume(0.1)


channel_eating = pygame.mixer.Channel(0)


screen = pygame.display.set_mode((HEIGHT, WIDTH))
game_over = False 

# Colors
colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

# Draw chessboard grid
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# Point class (coordinates)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y  # Comparison of points
    
# Snake class
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy= 0, -1 # Move up initially

    def move(self):
        # Create a new head
        new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)
        
        # Check boundaries
        if new_head.x < 0 or new_head.x >= WIDTH // CELL or new_head.y < 0 or new_head.y >= HEIGHT // CELL:
            return True  # Finish the game

        # # Check self-collision
        if new_head in self.body:
            return True # Finish the game
 
        # Move the body of the snake
        self.body.insert(0, new_head)  # Add new head
        self.body.pop()   # Remove tail
        return False

    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))
    
    def check_collision(self, food):
        global score, FPS, lvl, next_level_score
        if self.body[0] == food.pos: # Eat food
            self.body.append(Point(self.body[-1].x, self.body[-1].y))  # increase the body
            food.move(self)
            score += food.cost
            channel_eating.play(sound_eating) 

            if score >= next_level_score:
                lvl += 1
                FPS += 0.5
                next_level_score += 10  # Set the next threshold

# Food class
class Food:
    def __init__(self):
        self.last_spawn_time = pygame.time.get_ticks() # Memory of Last Time  Spawn
        self.move(snake=None)

    def move(self, snake):
        while True:
            self.x = random.randrange(0, WIDTH // CELL)  
            self.y = random.randrange(0, HEIGHT // CELL)  
            self.pos = Point(self.x, self.y)
            self.cost = random.randrange(1,4)
            

            # Check that food does not appear in the snake's body
            if snake is None or self.pos not in snake.body:
                self.last_spawn_time = pygame.time.get_ticks() # Updating the spawn timer
                break

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

# Game settings
FPS = FPS_START
score = 0
lvl = 1
next_level_score = 10 
clock = pygame.time.Clock()

# Create snake and food
snake = Snake()
food = Food()
db_handler.input_user()
best_lvl = db_handler.show_highest_level()

if best_lvl and best_lvl[0][0]: # Check if the result is not None (best_lvl[0][0] because [(5,)])
    print(f"Best level for {db_handler.current_user}: {best_lvl[0][0]}")
else:
    print(f"No scores found for {db_handler.current_user}. Welcome!")

running = True
paused = True
goq= True

while running:
    if not game_over and not paused:
        
        if pygame.time.get_ticks() - food.last_spawn_time - paused_time > 10000:
            food.move(snake)

        

        draw_grid_chess()
        game_over = snake.move()
        snake.check_collision(food)
        snake.draw()
        food.draw()

        # Display Score
        font_score = pygame.font.Font(None, 36)
        text = font_score.render(f" Score: {score} ", True, (0, 0, 0))
        font_score_rect = text.get_rect()
        screen.blit(text, (WIDTH - font_score_rect.w, 10))

        # Display Level
        font_speed = pygame.font.Font(None, 36)
        text_speed = font_speed.render(f" Level: {lvl} ", True, (0, 0, 0))
        font_speed_rect = text_speed.get_rect()
        screen.blit(text_speed, (0, 10))

    elif game_over:
        # Game Over screen
        db_handler.process_score(score, lvl)
        if goq:
            goq = False
            best_lvl = db_handler.show_highest_level()
            print(f"Your best level is: {best_lvl[0][0]}")
        screen.fill('red')

        font_GO = pygame.font.Font(None, 50)
        text_gameOver = font_GO.render("Game Over!", True, (255, 255, 255))
        text_rect = text_gameOver.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_gameOver, text_rect)

        font_restart = pygame.font.Font(None, 25)
        text_restart = font_restart.render('Press "R" to Restart', True, (255, 255, 255))
        text_restart_rect = text_restart.get_rect(center=(WIDTH // 2, HEIGHT - 40))
        screen.blit(text_restart, text_restart_rect)
        

    elif paused:
        # Pause screen
        if not game_over:
            paused_time = pygame.time.get_ticks() 
            screen.fill('black')

            font_pause = pygame.font.Font(None, 50)
            text_pause = font_pause.render("PAUSED", True, colorWHITE)
            text_pause_rect = text_pause.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text_pause, text_pause_rect)

            font_unpause = pygame.font.Font(None, 25)
            text_unpause = font_unpause.render('Press "Q" to Resume', True, colorWHITE)
            text_unpause_rect = text_unpause.get_rect(center=(WIDTH // 2, HEIGHT - 40))
            screen.blit(text_unpause, text_unpause_rect)

        else:
            paused = not paused

    # Handle events
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                best_lvl = db_handler.show_highest_level()
                print(f"Your best level is: {best_lvl[0][0]}")
                running = False
            elif event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_r:  # Restart game
                    # Reset settings
                    FPS = FPS_START
                    score = 0
                    lvl = 1
                    game_over = False 
                    paused = False
                    next_level_score = 10
                    paused_time = 0
                    goq = True
                    
                    # Recreate the snake and food
                    snake = Snake()
                    food = Food()  # Create new food (resets last_spawn_time)
                snake.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
                snake.dx, snake.dy= 0, -1

            elif event.type == pygame.KEYDOWN and not game_over and not paused:
                 # Control snake with arrow keys or WASD
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    snake.dx = 1
                    snake.dy = 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    snake.dx = -1
                    snake.dy = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    snake.dx = 0
                    snake.dy = 1
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    snake.dx = 0
                    snake.dy = -1

                elif event.key == pygame.K_q:
                    paused = not paused
                    db_handler.process_score(score, lvl)
                    best_lvl = db_handler.show_highest_level()
                    print(f"Your best level is: {best_lvl[0][0]}")
                    if paused:
                        db_handler.process_score(score, lvl)
            
            elif event.type == pygame.KEYDOWN and paused:
                if event.key == pygame.K_q:
                    paused = not paused



    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()