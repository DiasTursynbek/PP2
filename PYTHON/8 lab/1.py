import pygame
from pygame.locals import * 
import random 
import time

pygame.init()
FPS = 120
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0

coin_sound = pygame.mixer.Sound("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/звук монеты.mp3")
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Times New Roman", 20)
game_over = font.render("Game Over", True, (0, 0, 0))
background = pygame.image.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/AnimatedStreet.png")

pygame.mixer.music.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/background.wav")
pygame.mixer.music.play(-1)

DISPLAY = pygame.display.set_mode((400, 600))
DISPLAY.fill((255, 255, 255))
pygame.display.set_caption("GAME")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):    
        super().__init__() 
        self.image = pygame.image.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/Player.png")
        self.image = pygame.transform.scale(self.image, (50, 100))  
        self.rect = self.image.get_rect()
        self.rect.center = (207, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/coin1.png")
        self.image = pygame.transform.scale(self.original_image, (40, 40))
        self.rect = self.image.get_rect()
        self.respawn()

    def respawn(self):
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)

    def move(self):
        self.rect.move_ip(0, SPEED // 2)
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()

P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.3
        if event.type == QUIT:
            pygame.quit()

    DISPLAY.blit(background, (0, 0))
    
    scores = font_small.render(str(SCORE), True, (0, 0, 0))
    DISPLAY.blit(scores, (10, 10))
    
    coins_collected_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, (0, 0, 0))
    DISPLAY.blit(coins_collected_text, (300, 10))
    
    for entity in all_sprites:
        if isinstance(entity, Enemy) or isinstance(entity, Player) or isinstance(entity, Coin):
            entity.move()
        DISPLAY.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()
        pygame.mixer.Sound("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/crash.wav").play()
        time.sleep(0.7)
        DISPLAY.fill((255, 0, 0))
        DISPLAY.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(1)
        pygame.quit()

    if pygame.sprite.spritecollideany(P1, coins):
        COINS_COLLECTED += 1
        coin_sound.play()
        C1.respawn()
    
    pygame.display.update()
    FramePerSec.tick(FPS)