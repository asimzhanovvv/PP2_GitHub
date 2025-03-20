import pygame 
import random

pygame.init()


# BASE SETTINGS
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Traffic Racer')

# IMAGES
img_road = pygame.image.load('Labs/Lab8/TestR/images/bgroadd.png') # Background (Road)
img_player = pygame.image.load('Labs/Lab8/TestR/images/car.png') # Player
img_enemy = pygame.image.load('Labs/Lab8/TestR/images/enem1.png')  # Enemy
img_coin = pygame.image.load('Labs/Lab8/TestR/images/coin.png') # Coin

# SOUNDS

sound_crash = pygame.mixer.Sound('Labs/Lab8/TestR/sounds/crash.mp3')
sound_crash.set_volume(0.1)

sound_coin = pygame.mixer.Sound('Labs/Lab8/TestR/sounds/coin.mp3')
sound_coin.set_volume(0.1)

sound_bg = pygame.mixer.Sound('Labs/Lab8/TestR/sounds/bg.mp3')
sound_bg.set_volume(0.1)

channel_coin = pygame.mixer.Channel(0)
# PLAYER CLASS
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = img_player
        self.rect = self.image.get_rect()
        self.bottom_pos = HEIGHT - 40
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = self.bottom_pos
        self.speed = 4
        self.scoref = 0
        

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x += self.speed * 0.85 # only 85% of the speed 
            # НАДО ДОБАВИТЬ ВВЕРХ ДО ОДНОГО КОРПУСА
        if keys[pygame.K_a]:
            self.rect.x -= self.speed * 0.85 # only 85% of the speed

        if score >= self.scoref + 5:
            player.speed = min(player.speed * 1.05, 10)
            for enem in enemy_sprites:
                enem.speed = self.speed * 1.3
            for coin in coin_sprites:
                coin.speed = self.speed
            road.speed = self.speed
            self.scoref = score
        # Fun
        # if keys[pygame.K_w]:
        #     self.rect.y -= self.speed
        # if keys[pygame.K_s]:
        #     self.rect.y += self.speed

        self.rect.clamp_ip(screen.get_rect())

# ENEMY CLASS
class Enemy(pygame.sprite.Sprite):

    def __init__(self, number):
        self.number = number
        super().__init__()
        self.image = img_enemy
        self.rect = self.image.get_rect()
        self.speed = player.speed * 1.3
        self.generate_random_rect()

    def generate_random_rect(self):
        self.cordsX = (125,180,235,290)
        self.rect.centerx = random.choice(self.cordsX) # (0, WIDTH - self.rect.w)
        if self.number == 1:
            self.rect.top = random.randint(-250, 0)
        elif self.number == 2:
            self.rect.top = random.randint(-650, -400)
        elif self.number == 3:
            self.rect.top = random.randint(-1050, -800)

    def move(self):
        if not game_over:
            self.rect.move_ip(0, self.speed)
            if self.rect.top > HEIGHT:
                self.generate_random_rect()

# COIN CLASS
class Coins(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = img_coin
        self.rect = self.image.get_rect()
        self.generate_random_rect()
        self.speed = player.speed
        
    def generate_random_rect(self):
        self.cordsX = (125, 180, 235, 290)
        self.rect.centerx = random.choice(self.cordsX)  #random.randint(20, WIDTH - self.rect.w)
        # self.rect.centerx = random.randint(0,2)
        self.rect.top = random.randint(-600, -250)
    
    def move(self):
        if not game_over:
            self.rect.move_ip(0, self.speed)
            if self.rect.top > HEIGHT:
                self.generate_random_rect()

# ROAD CLASS
class Road:
    def __init__(self):
        self.image = img_road
        self.y1 = 0
        self.y2 = -HEIGHT  # Second bg image is above the first one
        self.speed = player.speed  # Speed of moving = player speed

    def move(self):
        # Move the road down
        self.y1 += self.speed
        self.y2 += self.speed

        # If the first image completely disappeared — move it up
        if self.y1 >= HEIGHT:
            self.y1 = self.y2 - HEIGHT  # Move up
        # If the second image completely disappeared — move it up
        if self.y2 >= HEIGHT:
            self.y2 = self.y1 - HEIGHT  # Move up
    def draw(self, screen):
        # Draw two bg images
        screen.blit(self.image, (0, self.y1))
        screen.blit(self.image, (0, self.y2))


# Entities
player = Player()

enemy1 = Enemy(1)
enemy2 = Enemy(2)
enemy3 = Enemy(3)

coin1 = Coins()
coin2 = Coins()
coin3 = Coins()

road = Road()

# Groups
all_sprites = pygame.sprite.Group(player, enemy1, enemy2, enemy3, coin1, coin2, coin3)
enemy_sprites = pygame.sprite.Group(enemy1, enemy2, enemy3)
coin_sprites = pygame.sprite.Group(coin1, coin2, coin3)

all_sprites.add(player, enemy1, enemy2, enemy3, coin1, coin2, coin3)
enemy_sprites.add(enemy1, enemy2, enemy3)
coin_sprites.add(coin1, coin2, coin3)


# FPS
clock = pygame.time.Clock()
FPS = 120

# Flags
running = True
game_over = False  
score = 0
was_crash = False

# Game Loop
while running:

    screen.blit(img_road, (0, 0))
    road.move() 
    road.draw(screen)

    if not game_over:

        font_speed = pygame.font.Font(None, 36)
        text_speed = font_speed.render(f" Speed: {round(player.speed)} ", True, (255, 255, 255), (0, 0, 0))
        font_speed_rect = text_speed.get_rect()
        screen.blit(text_speed, (0, 10))

        # Background Music
        sound_crash.stop()
        sound_bg.play(-1)

        # Enabling sprites to move
        for entity in all_sprites:
            entity.move()
            screen.blit(entity.image, entity.rect)

        # Collision with enemy
        collided_enemy = pygame.sprite.spritecollideany(player, enemy_sprites)
        if collided_enemy:
            was_crash = True
            game_over = True

        # Collecting coins
        collided_coin = pygame.sprite.spritecollideany(player, coin_sprites)
        if collided_coin:
            channel_coin.play(sound_coin)
            collided_coin.generate_random_rect()
            score += 1 # random.randint(1, 5)

        # Disappearance of coins
        for enemy in enemy_sprites:
            collided_coin = pygame.sprite.spritecollideany(enemy, coin_sprites)
            if collided_coin:
                collided_coin.generate_random_rect()

        # Display Score
        font_score = pygame.font.Font(None, 36)
        text = font_score.render(f" Score: {score} ", True, (255, 255, 255), (0, 0, 0))
        font_score_rect = text.get_rect()
        screen.blit(text, (WIDTH - font_score_rect.w, 10))

    
    # Game Over Screen
    else:
        # Stop the background music
        sound_bg.stop()
        if was_crash:
            was_crash = False
            sound_crash.play(0)

        screen.fill("red")

        font_GO = pygame.font.Font(None, 50)
        text_gameOver = font_GO.render("Game Over!", True, (255, 255, 255))
        text_rect = text_gameOver.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_gameOver, text_rect)

        font_restart = pygame.font.Font(None, 25)
        text_restart = font_restart.render('Press "R" to Restart', True, (255, 255, 255))
        text_restart_rect = text_restart.get_rect(center=(WIDTH // 2, HEIGHT - 40))
        screen.blit(text_restart, text_restart_rect)

        text_score = font_score.render(f" Score: {score} ", True, (255, 255, 255))
        text_score_rect = text_score.get_rect(center=(WIDTH//2, HEIGHT//2 - 150))
        screen.blit(text_score, text_score_rect)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:  # Restart game

                # Resetting the game
                game_over = False 

                # Resetting the score
                score = 0
                
                # Resetting the speed
                player.speed = 4
                for enem in enemy_sprites:
                    enem.speed = player.speed * 1.3
                for coin in coin_sprites:
                    coin.speed = player.speed
                road.speed = player.speed
                player.scoref = score

                # Resetting the entities
                player.rect.centerx = WIDTH // 2
                player.rect.bottom = player.bottom_pos
                for en in enemy_sprites: en.generate_random_rect()
                for coin in coin_sprites: coin.generate_random_rect()
                

# UPDATE
    pygame.display.flip() # updates the screen
    clock.tick(FPS) # sets the FPS

pygame.quit()