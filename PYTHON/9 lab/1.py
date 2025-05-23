import pygame
from pygame.locals import *
import random
import time

pygame.init()
FPS = 120
FramePerSec = pygame.time.Clock() # --> обьект аштық котоорый считает FPS - FramePerSecond

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0
PREV_MILESTONE = 0 # --> жылдамдық тек нақты жаңа деңгейге жеткенде артуы

coin_sound = pygame.mixer.Sound("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/звук монеты.mp3")

DISPLAY = pygame.display.set_mode((400, 600))
DISPLAY.fill((255,255,255))
pygame.display.set_caption("Ойын")

font = pygame.font.SysFont("Times New Roman", 60)
font_small = pygame.font.SysFont("Times New Roman", 20)
game_over = font.render("Жеңілдіңіз", True, (0,0,0)) # --> true болса тексттын жақтары әдемі болып шығады

background = pygame.image.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/AnimatedStreet.png")
pygame.mixer.music.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/background.wav")
pygame.mixer.music.play(-1) # --> infinity


class Enemy (pygame.sprite.Sprite):
    def __init__(self): # __init__ --> конструктор  объектке айнымалылар тағайындаймыз, бастапқы параметрлерді орнатамыз
        super().__init__() # super() -->  (родительский класс) функциясын шақыру үшін қолданылады.
        self.image = pygame.image.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/enemy.png")
        self.image = pygame.transform.scale(self.image, (50,100) )
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED) # --> жауды экранда тік төмен (y бағытымен) жылжытады.
        if self.rect.bottom > SCREEN_HEIGHT: 
            SCORE += 1
            self.rect.top = 0 # --> қайтадан жоғарыдан бастап түседі
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
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.respawn()
    def respawn(self):
        weights = [1, 2, 3]
 
# --> class
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
            SPEED += 0.3 # --> каждый раз машина қатты түседі
        if event.type == QUIT:
            pygame.quit()
    
    DISPLAY.blit(background, (0, 0)) # --> DISPLAYге артқы фон салу 0,0 коордан бастап

    scores = font_small.render(str(SCORE), True, (0, 0, 0))
    DISPLAY.blit(scores, (10, 10))
    coins_collected_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, (0, 0, 0))
    DISPLAY.blit(coins_collected_text, (300, 10))

    for entity in all_sprites:
        entity.move()
        DISPLAY.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(P1, enemies): # --> Проверяешь, не столкнулся ли игрок P1 с каким-либо врагом из группы enemies.
        pygame.mixer.music.stop()
        pygame.mixer.Sound("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/crash.wav").play()
        time.sleep(0.7)  # --> ожидания до game over
        DISPLAY.fill((255, 0, 0))
        DISPLAY.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(1) 
        pygame.quit()

    if pygame.sprite.spritecollideany(P1, coins): # spritecollideany -->  Если столкновение есть, возвращает первый найденный спрайт, с которым произошло столкновение. Если столкновения нет, возвращает None.
        COINS_COLLECTED += C1.weight
        coin_sound.play()
        C1.respawn()
        
        if COINS_COLLECTED // 10 > PREV_MILESTONE:
            SPEED += 0.5
            PREV_MILESTONE = COINS_COLLECTED // 10

    pygame.display.update()
    FramePerSec.tick(FPS)































# SCREEN_WIDTH = 400      --> Экранның ені (пиксельмен)
# SCREEN_HEIGHT = 600     --> Экранның биіктігі
# SPEED = 5               --> Бастапқы жылдамдық (жау мен монетаның түсу жылдамдығы)
# SCORE = 0               --> Жауды өткізіп жіберген сайын ұпай қосылады
# COINS_COLLECTED = 0     --> Жиналған монеталардың саны (салмақпен қосылады)
# PREV_MILESTONE = 0      --> Соңғы 10-дық межесі (жау жылдамдығын артыру үшін қажет)

# coin_sound              --> Монета алған кездегі дыбыс
# font                    --> Үлкен мәтіндер үшін шрифт (мысалы, "Game Over")
# font_small              --> Ұсақ мәтіндер үшін шрифт (мысалы, ұпайлар мен монеталар)
# game_over               --> "Game Over" мәтінін визуалдау үшін дайын мәтін объектісі

# background              --> Фондық сурет (көше)
# pygame.mixer.music      --> Фондық музыка

# Player                  --> Ойыншы класы (солға/оңға қозғалады)
# Enemy                   --> Жау класы (жоғарыдан түседі)
# Coin                    --> Монета класы (әртүрлі салмақта пайда болады)

# all_sprites             --> Барлық объектілер (ойыншы, жау, монета) біріктірілген топ
# INC_SPEED               --> Қосымша оқиға: жылдамдықты әр 1 секунд сайын арттыру

# pygame.sprite.spritecollideany() --> Қақтығысты тексеретін функция (бір объекті екіншімен түйісе ме — соны тексереді)