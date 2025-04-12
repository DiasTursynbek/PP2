# import pygame
# from pygame.locals import *  #  *  --> барлық функцияны импорттау 
# import random 
# import time
# pygame.init()
# FPS=120
# FramePerSec = pygame.time.Clock() # --> обьект аштық котоорый считает FPS - FramePerSecond
# SCREEN_WIDTH = 400
# SCREEN_HEIGHT = 600
# SPEED=5
# SCORE=0
# COINS_COLLECTED=0

# coin_sound = pygame.mixer.Sound("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/звук монеты.mp3")

# font = pygame.font.SysFont("Verdana", 60)
# font_small = pygame.font.SysFont("Times New Roman", 20)
# game_over = font.render("Game Over", True, (0,0,0)) # --> true болса тексттын жақтары әдемі болып шығады
# background = pygame.image.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/AnimatedStreet.png")

# pygame.mixer.music.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/background.wav")
# pygame.mixer.music.play(-1) # --> infinity

# DISPLAY=pygame.display.set_mode((400,600))
# DISPLAY.fill((255,255,255))
# pygame.display.set_caption("GAME")

# class Enemy(pygame.sprite.Sprite):   # --> pygame.sprite  модульінің ішінде Sprite деген клаасс бар 
#     def __init__(self):    # __init__ --> конструктор
#         super().__init__() # super() -->  (родительский класс) функциясын шақыру үшін қолданылады.
#         self.image = pygame.image.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/enemy.png")
#         self.image = pygame.transform.scale(self.image, (50,100))
#         self.rect = self.image.get_rect()
#         self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)

#     def move(self):
#         global SCORE
#         self.rect.move_ip(0,SPEED)
#         if self.rect.bottom > 600:
#             SCORE+=1
#             self.rect.top = 0
#             self.rect.center = (random.randint(20, SCREEN_WIDTH - 20) , 0)

# class Player(pygame.sprite.Sprite): # --> pygame.sprite  модульінің ішінде Sprite деген клаасс бар 
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/Player.png")
#         self.image = pygame.transform.scale(self.image, (50,100 ))  
#         self.rect = self.image.get_rect()
#         self.rect.center = (207, 520)
#     def move(self):
#         pressed_keys = pygame.key.get_pressed()
#         if self.rect.left > 0:
#             if pressed_keys[K_LEFT]:
#                 self.rect.move_ip(-5, 0)
#         if self.rect.right < SCREEN_WIDTH:
#             if pressed_keys[K_RIGHT]:
#                 self.rect.move_ip(5, 0)

# class Coin(pygame.sprite.Sprite): # --> pygame.sprite  модульінің ішінде Sprite деген клаасс бар 
#     def __init__(self):
#         super().__init__()
#         self.original_image = pygame.image.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/coin1.png")
#         self.image = pygame.transform.scale(self.original_image, (40,40))
#         self.rect = self.image.get_rect()
#         self.respawn()
#     def respawn(self):
#         self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)

#     def move(self):
#         self.rect.move_ip(0, SPEED // 2)
#         if self.rect.top > SCREEN_HEIGHT:
#             self.respawn()
# P1=Player() # --> class
# E1=Enemy() # --> class
# C1=Coin() # --> class

# enemies=pygame.sprite.Group()
# enemies.add(E1)
# coins=pygame.sprite.Group()
# coins.add(C1)
# all_sprites=pygame.sprite.Group()
# all_sprites.add(P1,E1,C1)

# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 1000)

# while True:
#     for event in pygame.event.get():
#         if event.type == INC_SPEED:
#             SPEED += 0.3
#         if event.type == QUIT:
#             pygame.quit()



#     DISPLAY.blit(background, (0, 0))
    
#     scores = font_small.render(str(SCORE), True, (0,0,0))
#     DISPLAY.blit(scores, (10, 10))
#     coins_collected_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, (0,0,0))
#     DISPLAY.blit(coins_collected_text, (300, 10))
    
#     for entity in all_sprites:
#         if isinstance(entity,Enemy) or isinstance(entity , Player) or isinstance(entity, Coin):
#             entity.move()
#         DISPLAY.blit(entity.image, entity.rect)
#     if pygame.sprite.spritecollideany(P1, enemies):  # --> Проверяешь, не столкнулся ли игрок P1 с каким-либо врагом из группы enemies.
#         pygame.mixer.music.stop()
#         pygame.mixer.Sound("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/crash.wav").play()
#         time.sleep(0.7)  # --> ожидания до game over
#         DISPLAY.fill((255,0,0))
#         DISPLAY.blit(game_over, (30, 250))
#         pygame.display.update()
#         for entity in all_sprites:
#             entity.kill()
#         time.sleep(1) # --> ойынның бітуі
#         pygame.quit()

#     if pygame.sprite.spritecollideany(P1, coins):       # spritecollideany -->  Если столкновение есть, возвращает первый найденный спрайт, с которым произошло столкновение. Если столкновения нет, возвращает None.
#         COINS_COLLECTED += 1
#         coin_sound.play()
#         C1.respawn()
    
#     pygame.display.update()
#     FramePerSec.tick(FPS)
    




#     import pygame
# import random

# pygame .init()
# WIDTH,HEIGHT= 600, 600
# CELL_SIZE = 20
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# BLACK = (0, 0, 0)

# screen = pygame.display.set_mode((WIDTH,HEIGHT))
# pygame.display.set_caption("Змейка")

# font = pygame.font.SysFont("Times New Roman", 20)

# fps = pygame.time.Clock()
# snake = [(100, 100), (80, 100), (60, 100)]  # --> басы ортасы аяғы жыланның
# snake_dir = (20, 0) # --> Каждый кадрда 20 пиксельге жылжып отыру
# food_position = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT,CELL_SIZE)) # --> random.randrange(start, stop, step)
# score = 0
# level = 1
# speed = 10

# def generate_food():
#     while True:
#         x=random.randrange(0, WIDTH, CELL_SIZE)
#         y=random.randrange(0, WIDTH, CELL_SIZE)
#         if (x, y) not in snake:
#             return (x, y)
        
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP] and snake_dir != (0, 20):   
#         snake_dir = (0, -20)                            #        +X →
#     if keys[pygame.K_DOWN] and snake_dir != (0, -20):    #(0,0)_________
#         snake_dir = (0, 20)                               #  |         |
#     if keys[pygame.K_LEFT] and snake_dir != (20, 0):      #  |         |
#         snake_dir = (-20, 0)                              #  ↓ +Y      |
#     if keys[pygame.K_RIGHT] and snake_dir != (-20, 0):    
#         snake_dir = (20, 0)

#     new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

#     if new_head[0]<0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
#         break  # --> экраннан  х  у  осьтері бойынша асып кетсе сразу ойынды тоқтату

#     if new_head in snake:
#         break # --> жылан өзіне соғылды ойынды тоқтату

#     snake.insert(0, new_head)

#     if new_head == food_position:
#         score+=1
#         food_position = generate_food()

#         if score % 4 ==0:
#             level += 1
#             speed +=2
#     else:
#         snake.pop()

#     screen.fill (WHITE)

#     for segment in snake: # --> Жыланды экранға салу
#         pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

#     pygame.draw.rect(screen, RED, (food_position[0], food_position[1], CELL_SIZE, CELL_SIZE)) # --> тамақты экранға салу 

#     score_text = font.render(f"Счет: {score}", True, BLACK)
#     level_text = font.render(f"Уровень: {level}", True, BLACK)
#     screen.blit(score_text, (10, 10))
#     screen.blit(level_text, (10, 40))

#     pygame.display.flip()
#     fps.tick(speed)




































# # 1. Мы импортируем необходимые библиотеки: pygame, random, sys.
# # 2. Устанавливаем размеры окна игры и размеры клетки.
# # 3. Задаем базовые цвета, шрифт и начальные параметры.
# # 4. Создаем змею в виде списка кортежей с начальными координатами.
# # 5. Начальное направление движения змеи - вправо.
# # 6. Генерируем случайную позицию для еды, которая не должна совпадать с телом змеи.
# # 7. В основном цикле:
# #    - Проверяем события закрытия окна.
# #    - Слушаем клавиши и меняем направление змеи, если нужно.
# #    - Двигаем змею, добавляя новый сегмент головы.
# #    - Проверяем столкновение с границей или собой.
# #    - Если съедаем еду — увеличиваем счет, уровень и скорость.
# #    - Если не съели — удаляем последний сегмент змеи (хвост).
# # 8. Отрисовываем змею, еду, счет и уровень на экране.
# # 9. Управляем скоростью игры в зависимости от текущего уровня.
# # 10. Если игра заканчивается (столкновение) — программа выходит.

# # Вот так реализуется игра «Змейка» с уровнями, увеличением скорости и подсчетом очков!





# import pygame
# import sys # --> жүйелік функциялармен жұмыс істеу үшін қолданылатын модуль
# pygame.init()

# screen = pygame.display.set_mode((800,600))
# pygame.display.set_caption("Paintqoi")
# WHITE = (255,255,255)
# BLACK = (0,0,0)
# RED = (255,0,0)
# GREEN = (0,255,0)
# BLUE = (0,0,255)
# current_color=BLACK

# screen.fill(WHITE) #--> background color

# brush_size = 5
# drawing = False
# last_pos = None
# start_pos = None
# mode = "brush"

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_r:
#                 current_color = RED
#             elif event.key == pygame.K_g:
#                 current_color = GREEN 
#             elif event.key == pygame.K_b:
#                 current_color = BLUE
#             elif event.key == pygame.K_e:
#                 mode = "eraser"
#             elif event.key == pygame.K_t:
#                 mode = "brush"
#             elif event.key == pygame.K_c:
#                 mode = "circle"
#             elif event.key == pygame.K_o:
#                 mode = "rect"

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             drawing = True
#             start_pos = event.pos
#             last_pos = event.pos


#         if event.type == pygame.MOUSEBUTTONUP:
#             if mode == "rect":
#                 end_pos = event.pos
#                 rect = pygame.Rect(
#                     min(start_pos[0], end_pos[0]),     # x координата (сол жақ)
#                     min(start_pos[1], end_pos[1]),     # y координата (жоғарғы жақ)
#                     abs(start_pos[0] - end_pos[0]),    # ен (width)
#                     abs(start_pos[1] - end_pos[1])     # биіктік (height)
#                 )
#                 pygame.draw.rect(screen, current_color, rect, width = 2)

#             elif mode == "circle":
#                 end_pos = event.pos
#                 radius = int(((start_pos[0] - end_pos[0]) ** 2 
#                               +  # --> бастапқы нүкте (start_pos) мен соңғы нүкте (end_pos) аралығындағы қашықтықты 
#                               (start_pos[1] - end_pos[1]) ** 2) ** 0.5)
                
#                 pygame.draw.circle(screen, current_color, start_pos, radius, width = 2)
#             drawing = False
#         # Мышканың қимылы сурет салғанда
#         if event.type == pygame.MOUSEMOTION and drawing:
#             if mode == "brush":
#                 pygame.draw.line(screen, current_color, last_pos, event.pos, brush_size)
#                 last_pos = event.pos
#             elif mode == "eraser":
#                 pygame.draw.line(screen, WHITE, last_pos, event.pos, brush_size * 4)
#                 last_pos = event.pos
#     pygame.display.update()


















#     99999999999999999999999999999999999999999999999999999

#     import pygame
# from pygame.locals import *
# import random
# import time

# pygame.init()
# FPS = 120
# FramePerSec = pygame.time.Clock() # --> обьект аштық котоорый считает FPS - FramePerSecond

# SCREEN_WIDTH = 400
# SCREEN_HEIGHT = 600
# SPEED = 5
# SCORE = 0
# COINS_COLLECTED = 0
# PREV_MILESTONE = 0 # --> жылдамдық тек нақты жаңа деңгейге жеткенде артуы

# coin_sound = pygame.mixer.Sound("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/звук монеты.mp3")

# DISPLAY = pygame.display.set_mode((400, 600))
# DISPLAY.fill((255,255,255))
# pygame.display.set_caption("Ойын")

# font = pygame.font.SysFont("Times New Roman", 60)
# font_small = pygame.font.SysFont("Times New Roman", 20)
# game_over = font.render("Ұтылдыңыз", True, (0,0,0)) # --> true болса тексттын жақтары әдемі болып шығады

# background = pygame.image.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/AnimatedStreet.png")
# pygame.mixer.music.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/background.wav")
# pygame.mixer.music.play(-1) # --> infinity


# class Enemy (pygame.sprite.Sprite):  # --> pygame.sprite  модульінің ішінде Sprite деген клаасс бар 
#     def __init__(self): # __init__ --> конструктор  объектке айнымалылар тағайындаймыз, бастапқы параметрлерді орнатамыз
#         super().__init__() # super() -->  (родительский класс) функциясын шақыру үшін қолданылады.
#         self.image = pygame.image.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/enemy.png")
#         self.image = pygame.transform.scale(self.image, (50,100) )
#         self.rect = self.image.get_rect()
#         self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)
#     def move(self):
#         global SCORE
#         self.rect.move_ip(0, SPEED) # --> жауды экранда тік төмен (y бағытымен) жылжытады.
#         if self.rect.bottom > SCREEN_HEIGHT: # --> Height-тан асып кетсе, 
#             SCORE += 1
#             self.rect.top = 0 # --> қайтадан жоғарыдан бастап түседі
#             self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)
        
# class Player(pygame.sprite.Sprite): # --> pygame.sprite  модульінің ішінде Sprite деген клаасс бар 
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/Player.png")
#         self.image = pygame.transform.scale(self.image, (50, 100))
#         self.rect = self.image.get_rect() # --> суретті төртбұрыш қылып алады
#         self.rect.center = (207, 520)

#     def move(self):
#         pressed_keys = pygame.key.get_pressed()
#         if self.rect.left > 0 and pressed_keys[K_LEFT]:
#             self.rect.move_ip(-5, 0)
#         if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
#             self.rect.move_ip(5, 0)

# class Coin(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.respawn()
#     def respawn(self):
#         weights = [1, 2, 3]
#         self.weight = random.choice(weights)

#         image_path = f"/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/coin{self.weight}.png"
#         self.original_image = pygame.image.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/coin1.png")
#         size = 30 + self.weight * 5 # --> бастапқысы 30 + [1,2,3]*5
#         self.image = pygame.transform.scale(self.original_image, (size,size))
#         self.rect = self.image.get_rect()
#         self.rect.center = (random.randint(20, SCREEN_WIDTH - 20), 0)

#     def move(self):
#         self.rect.move_ip(0, SPEED // 2)
#         if self.rect.top > SCREEN_HEIGHT:
#             self.respawn()

# # --> class
# P1 = Player()
# E1 = Enemy()
# C1 = Coin()

# enemies = pygame.sprite.Group()
# enemies.add(E1)

# coins = pygame.sprite.Group()
# coins.add(C1)

# all_sprites = pygame.sprite.Group()
# all_sprites.add(P1, E1, C1)

# INC_SPEED = pygame.USEREVENT + 1
# pygame.time.set_timer(INC_SPEED, 1000)

# while True:
#     for event in pygame.event.get():
#         if event.type == INC_SPEED:
#             SPEED += 0.3 # --> каждый раз машина қатты түседі
#         if event.type == QUIT:
#             pygame.quit()
    
#     DISPLAY.blit(background, (0, 0)) # --> DISPLAYге артқы фон салу 0,0 коордан бастап

#     scores = font_small.render(str(SCORE), True, (0, 0, 0))
#     DISPLAY.blit(scores, (10, 10))
#     coins_collected_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, (0, 0, 0))
#     DISPLAY.blit(coins_collected_text, (300, 10))

#     for entity in all_sprites:
#         entity.move()
#         DISPLAY.blit(entity.image, entity.rect)

#     if pygame.sprite.spritecollideany(P1, enemies): # --> Проверяешь, не столкнулся ли игрок P1 с каким-либо врагом из группы enemies.
#         pygame.mixer.music.stop()
#         pygame.mixer.Sound("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/8 lab/crash.wav").play()
#         time.sleep(0.7)  # --> ожидания до game over
#         DISPLAY.fill((255, 0, 0))
#         DISPLAY.blit(game_over, (30, 250))
#         pygame.display.update()
#         for entity in all_sprites:
#             entity.kill()
#         time.sleep(1) # --> ойынның бітуі
#         pygame.quit()

#     if pygame.sprite.spritecollideany(P1, coins): # spritecollideany -->  Если столкновение есть, возвращает первый найденный спрайт, с которым произошло столкновение. Если столкновения нет, возвращает None.
#         COINS_COLLECTED += C1.weight
#         coin_sound.play()
#         C1.respawn()
        
#         if COINS_COLLECTED // 10 > PREV_MILESTONE:
#             SPEED += 0.5
#             PREV_MILESTONE = COINS_COLLECTED // 10

#     pygame.display.update()
#     FramePerSec.tick(FPS)































# # SCREEN_WIDTH = 400      --> Экранның ені (пиксельмен)
# # SCREEN_HEIGHT = 600     --> Экранның биіктігі
# # SPEED = 5               --> Бастапқы жылдамдық (жау мен монетаның түсу жылдамдығы)
# # SCORE = 0               --> Жауды өткізіп жіберген сайын ұпай қосылады
# # COINS_COLLECTED = 0     --> Жиналған монеталардың саны (салмақпен қосылады)
# # PREV_MILESTONE = 0      --> Соңғы 10-дық межесі (жау жылдамдығын артыру үшін қажет)

# # coin_sound              --> Монета алған кездегі дыбыс
# # font                    --> Үлкен мәтіндер үшін шрифт (мысалы, "Game Over")
# # font_small              --> Ұсақ мәтіндер үшін шрифт (мысалы, ұпайлар мен монеталар)
# # game_over               --> "Game Over" мәтінін визуалдау үшін дайын мәтін объектісі

# # background              --> Фондық сурет (көше)
# # pygame.mixer.music      --> Фондық музыка

# # Player                  --> Ойыншы класы (солға/оңға қозғалады)
# # Enemy                   --> Жау класы (жоғарыдан түседі)
# # Coin                    --> Монета класы (әртүрлі салмақта пайда болады)

# # all_sprites             --> Барлық объектілер (ойыншы, жау, монета) біріктірілген топ
# # INC_SPEED               --> Қосымша оқиға: жылдамдықты әр 1 секунд сайын арттыру

# # pygame.sprite.spritecollideany() --> Қақтығысты тексеретін функция (бір объекті екіншімен түйісе ме — соны тексереді)





# import pygame
# import random
# import sys
# import time

# pygame.init()
# WIDTH, HEIGHT = 800, 800
# CELL_SIZE = 20
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# BLACK = (0, 0, 0)
# FPS = 120

# FOOD_COLORS = {
#     1: (255, 0, 0),
#     2: (255, 165, 0),
#     3: (255, 255, 0)
# }

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Snake")
# font = pygame.font.SysFont("Times New Roman", 20, True, True) # --> SysFont, системные шрифты    Жирный, Курсив
# clock = pygame.time.Clock()

# snake = [(300, 300), (280, 300), (260, 300)]
# snake_direction = (20, 0)

# food_pos = None
# food_weight = 1
# food_spawn_time = 0

# score = 0
# level = 1
# speed = 10

# def generate_food():
#     while True:
#         x = random.randrange(0, WIDTH, CELL_SIZE)
#         y = random.randrange(0, HEIGHT, CELL_SIZE)
#         if(x, y) not in snake:
#             return (x, y), random.choice([1, 2, 3])
        
# food_pos, food_weight = generate_food()
# food_spawn_time = time.time()

# while True:

#     screen.fill(WHITE)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP] and snake_direction != (0, 20):
#         snake_direction = (0, -20)
#     if keys[pygame.K_DOWN] and snake_direction != (0, -20):
#         snake_direction = (0, 20)
#     if keys[pygame.K_LEFT] and snake_direction != (20, 0):
#         snake_direction = (-20, 0)
#     if keys[pygame.K_RIGHT] and snake_direction != (-20, 0):
#         snake_direction = (20, 0)
    
#     new_head = (
#         snake[0][0] + snake_direction[0],  # X
#         snake[0][1] + snake_direction[1]   # Y
#     )
    
#     if (
#         new_head[0] < 0 or new_head[0] >= WIDTH or
#         new_head[1] < 0 or new_head[1] >= HEIGHT or
#         new_head in snake
#     ):
#         break

#     snake.insert(0, new_head)

#     if new_head == food_pos:
#         score += food_weight
#         food_pos, food_weight = generate_food()
#         food_spawn_time = time.time()
#         if score // 4 + 1 > level:
#             level += 1
#             speed += 2
#     else:
#         snake.pop()
    
#     if time.time() - food_spawn_time >= 5:
#         food_pos, food_weight = generate_food()
#         food_spawn_time = time.time()
    
    
#     for segment in snake:
#         pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

#     food_color = FOOD_COLORS[food_weight]
#     pygame.draw.rect(screen, food_color, (food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

#     score_text = font.render(f"Счет: {score}", True, BLACK)
#     level_text = font.render(f"Уровень: {level}", True, BLACK)
#     screen.blit(score_text, (10, 10))
#     screen.blit(level_text, (10, 40))

#     pygame.display.flip()
#     clock.tick(speed)









#     import pygame
# import sys


# pygame.init()


# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("paintqoi")
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# current_color = BLACK

# screen.fill(WHITE)


# brush_size = 5
# drawing = False
# last_pos = None
# mode = "brush" 
# start_pos = None


# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

       
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_r:
#                 current_color = RED
#             elif event.key == pygame.K_g:
#                 current_color = GREEN
#             elif event.key == pygame.K_b:
#                 current_color = BLUE
#             elif event.key == pygame.K_e:
#                 mode = "eraser"
#             elif event.key == pygame.K_t:
#                 mode = "brush"
#             elif event.key == pygame.K_c:
#                 mode = "circle"
#             elif event.key == pygame.K_q:
#                 mode = "square"
#             elif event.key == pygame.K_p:
#                 mode = "right_triangle"
#             elif event.key == pygame.K_e:
#                 mode = "equilateral_triangle"
#             elif event.key == pygame.K_d:
#                 mode = "rhombus"
#             elif event.key == pygame.K_l:
#                 mode = "rect"

       
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             drawing = True
#             start_pos = event.pos
#             last_pos = event.pos

        
#         if event.type == pygame.MOUSEBUTTONUP:
#             end_pos = event.pos

#             if mode == "rect":
#                 rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
#                                    abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
#                 pygame.draw.rect(screen, current_color, rect, width=2)

#             elif mode == "circle":
#                 radius = int(((start_pos[0] - end_pos[0])**2 + (start_pos[1] - end_pos[1])**2) ** 0.5)
#                 pygame.draw.circle(screen, current_color, start_pos, radius, width=2)

#             elif mode == "square":
#                 side = max(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
#                 rect = pygame.Rect(start_pos[0], start_pos[1], side, side)
#                 pygame.draw.rect(screen, current_color, rect, width=2)

#             elif mode == "right_triangle":
                
#                 x1, y1 = start_pos
#                 x2, y2 = end_pos
#                 points = [start_pos, (x1, y2), (x2, y2)]
#                 pygame.draw.polygon(screen, current_color, points, width=2)

#             elif mode == "equilateral_triangle":
                
#                 x1, y1 = start_pos
#                 x2, y2 = end_pos
#                 side = max(abs(x2 - x1), abs(y2 - y1))
#                 point1 = (x1, y1)
#                 point2 = (x1 + side, y1)
#                 point3 = (x1 + side / 2, y1 - (3**0.5/2)*side)
#                 pygame.draw.polygon(screen, current_color, [point1, point2, point3], width=2)

#             elif mode == "rhombus":
                
#                 x1, y1 = start_pos
#                 x2, y2 = end_pos
#                 center_x = (x1 + x2) // 2
#                 center_y = (y1 + y2) // 2
#                 dx = abs(x2 - x1) // 2
#                 dy = abs(y2 - y1) // 2
#                 points = [
#                     (center_x, center_y - dy),
#                     (center_x + dx, center_y),
#                     (center_x, center_y + dy),
#                     (center_x - dx, center_y)
#                 ]
#                 pygame.draw.polygon(screen, current_color, points, width=2)

#             drawing = False


#         if event.type == pygame.MOUSEMOTION and drawing:
#             if mode == "brush":
#                 pygame.draw.line(screen, current_color, last_pos, event.pos, brush_size)
#                 last_pos = event.pos
#             elif mode == "eraser":
#                 pygame.draw.line(screen, WHITE, last_pos, event.pos, brush_size * 2)
#                 last_pos = event.pos

#     pygame.display.update()