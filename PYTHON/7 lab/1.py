import pygame
import sys
import time
pygame.init() #include pygame


pygame.display.set_caption("Mickey Mouse Clock")
WIDTH, HEIGHT = 1200, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))

CENTER = (WIDTH // 2, HEIGHT // 2)


clock_image = pygame.image.load("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/7 lab/clock.png")
clock_image = pygame.transform.scale(clock_image, (WIDTH, HEIGHT))     #  -->  Бұл функция суретті қажетті өлшемге созады немесе кішірейтеді.
minute_hand = pygame.image.load('/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/7 lab/min_hand.png')  
second_hand = pygame.image.load('/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/7 lab/sec_hand.png')  
minute_hand = pygame.transform.scale(minute_hand, (700, 700))  
second_hand = pygame.transform.scale(second_hand, (650, 650))  

def rotate_hand(image, angle, pivot):
    """Сағат тілдерін айналдыру функциясы."""
    rotated_image = pygame.transform.rotate(image, -angle)     # -angle --> Себебі, pygame-да айналу бағыты сағат тіліне қарсы жүреді,
    new_rect = rotated_image.get_rect(center=pivot)            # --> 	get_rect(center=pivot) — бұралған суреттің орнын сағаттың ортасына (pivot) дәл келтіріп қайта қояды. 	•	Егер осы жолды жазбасақ, сурет айналған кезде жылжып кетеді.
    return rotated_image, new_rect

running = True
while running:
    
    screen.blit(clock_image, (0, 0))  # --> Бұл жол арқылы біз сағаттың негізгі суретін (фонды) экранға (0,0) координатасынан бастап салып қойдық.

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec
    milliseconds = time.time() % 1 
    print(f" ----\n{minutes}\n{seconds}")

    minute_angle = 6 * (minutes + seconds / 60) + 45  
    second_angle = 6 * (seconds + milliseconds) -48 

    # Тілдерді экранға шығару
    rotated_minute_hand, minute_rect = rotate_hand(minute_hand, minute_angle, CENTER)
    screen.blit(rotated_minute_hand, minute_rect.topleft) # --> topleft — суреттің жоғарғы сол жақ бұрыш координаты, осы жерден бастап сурет экранға салынады.

    rotated_second_hand, second_rect = rotate_hand(second_hand, second_angle, CENTER)
    screen.blit(rotated_second_hand, second_rect.topleft)
    
    pygame.display.flip() # --> экранды жаңарту.

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
sys.exit()


























# pygame — библиотека для работы с графикой и играми.
# sys — используется для закрытия программы (sys.exit()).
# math — нужна для работы с тригонометрическими функциями (чтобы поворачивать стрелки).
# time — используется для получения текущего времени.

# pygame.init() --> Эта строка инициализирует Pygame, подготавливая его для работы с графикой и звуком.

	# •	WIDTH, HEIGHT = 700, 700 — размеры окна (700x700 пикселей).
	# •	pygame.display.set_mode((WIDTH, HEIGHT)) — создаёт окно для отображения графики.
	# •	pygame.display.set_caption("Mickey Mouse Clock task 1") — устанавливает заголовок окна.

	# •	pygame.image.load("mickeyclock.jpeg") — загружает изображение часов.
	# •	pygame.transform.scale(clock_image, (WIDTH, HEIGHT)) — изменяет размер изображения, чтобы оно заполнило окно.
# -------------------------------
# def rotate_hand(image, angle, position):                         
#     rotated_image = pygame.transform.rotate(image, angle)
#     new_rect = rotated_image.get_rect(center=position)
#     return rotated_image, new_rect

	# •	image — изображение стрелки.
	# •	angle — угол поворота в градусах.
	# •	position — центр вращения.
	# •	pygame.transform.rotate(image, angle) — поворачивает изображение.
	# •	get_rect(center=position) — сохраняет центр после поворота.
# -------------------------------

# def draw_hands():
#     # Текущее время
#     current_time = time.localtime()
#     minutes = current_time.tm_min
#     seconds = current_time.tm_sec
#     	•	time.localtime() получает текущее время.
# 	•	minutes = current_time.tm_min — извлекает минуты.
# 	•	seconds = current_time.tm_sec — извлекает секунды.
# ------------------------------

    # minute_angle = 6 * minutes
    # second_angle = 6 * seconds
	# •	minute_angle = 6 * minutes — минутная стрелка двигается на 6° за каждую минуту (6 × 60 = 360° за полный круг).
	# •	second_angle = 6 * seconds — секундная стрелка двигается 6° за каждую секунду.
    # ------------------------------

    # min_x = center_x + minute_length * math.sin(math.radians(minute_angle))
    # min_y = center_y - minute_length * math.cos(math.radians(minute_angle))
    # sec_x = center_x + second_length * math.sin(math.radians(second_angle))
    # sec_y = center_y - second_length * math.cos(math.radians(second_angle))
	# •	math.sin(math.radians(angle)) и math.cos(math.radians(angle)) используются для вычисления координат конца стрелки:
	# •	math.sin() — определяет горизонтальное смещение.
	# •	math.cos() — определяет вертикальное смещение.
	# •	math.radians(angle) — переводит угол из градусов в радианы.
	# •	center_x + minute_length * sin(angle) — находим X-координату конца стрелки.
	# •	center_y - minute_length * cos(angle) — находим Y-координату конца стрелки.
    # ------------------------------
    #     pygame.draw.line(screen, (0, 0, 0), (center_x, center_y), (min_x, min_y), 8)
    # pygame.draw.line(screen, (255, 0, 0), (center_x, center_y), (sec_x, sec_y), 4)
	# •	pygame.draw.line(screen, color, (start_x, start_y), (end_x, end_y), width)
	# •	(0, 0, 0) — чёрный цвет для минутной стрелки.
	# •	(255, 0, 0) — красный цвет для секундной стрелки.
	# •	(center_x, center_y) — начало стрелки (центр часов).
	# •	(min_x, min_y) — конец минутной стрелки.
	# •	(sec_x, sec_y) — конец секундной стрелки.
	# •	8, 4 — толщина линий.
    # --------------------------------







# ---------------------------------------------------------------------------------------------------------
    # 	•	pygame кітапханасын іске қосамыз. Ол графикамен және ойын жасаумен жұмыс істеуге көмектеседі.
	# •	sys – бағдарламаны жабу үшін (sys.exit()).
	# •	math – тригонометриялық функцияларды қолдану үшін (бұрыштарды есептеу).
	# •	time – нақты уақытты алу үшін (time.localtime()).
	# •	pygame.init() – Pygame-ді іске қосады.

	# •	pygame.image.load("clock.png") – сағаттың суретін жүктейді.
	# •	pygame.transform.scale(clock_image, (WIDTH, HEIGHT)) – суретті терезенің өлшеміне сәйкес келтіреді.

    # 	•	CENTER_X = WIDTH // 2 – сағаттың ортасының X координатасын анықтайды (350).
	# •	CENTER_Y = HEIGHT // 2 – сағаттың ортасының Y координатасын анықтайды (350).

	# •	Функция стрелканы бұрады (айналдырады).
	# •	pygame.transform.rotate(image, -angle) – берілген бұрышқа (angle) бұрады.
	# •	get_rect(center=pivot) – айналу нүктесін (pivot) сақтайды.

 	# •	clock = pygame.time.Clock() – кадр жиілігін (FPS) басқаруға көмектеседі.
	# •	running = True – ойын (сағат) циклын бастайды.

    # 	•	time.localtime() – ағымдағы уақытты алады.
	# •	minutes = current_time.tm_min – минутты алады.
	# •	seconds = current_time.tm_sec – секундты алады.
	# •	milliseconds = time.time() % 1 – секундтың бөлшек бөлігін алады.

	# •	Минуттық стрелка: 6 * (minutes + seconds / 60)
	# •	1 минут = 6 градус (өйткені 360° / 60 = 6°).
	# •	Секундтың үлесін ескеріп, тегіс қозғалыс жасайды.
	# •	Секундтық стрелка: 6 * (seconds + milliseconds)
	# •	1 секунд = 6 градус.
     
    #  	•	rotate_hand(minute_hand, minute_angle, (CENTER_X, CENTER_Y + 20)) – стрелканы бұрады.
	# •	screen.blit(rotated_minute_hand, minute_rect.topleft) – экранға қояды.
     
    #  	•	pygame.display.flip() – экранды жаңартады.
	# •	clock.tick(60) – кадр жиілігін 60 FPS-қа шектейді.