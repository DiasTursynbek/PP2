import pygame
import sys # --> жүйелік функциялармен жұмыс істеу үшін қолданылатын модуль
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Paintqoi")
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
current_color=BLACK

screen.fill(WHITE) #--> background color

brush_size = 5
drawing = False
last_pos = None
start_pos = None
mode = "brush"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_g:
                current_color = GREEN 
            elif event.key == pygame.K_b:
                current_color = BLUE
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_t:
                mode = "brush"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_o:
                mode = "rect"

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos


        if event.type == pygame.MOUSEBUTTONUP:
            if mode == "rect":
                end_pos = event.pos
                rect = pygame.Rect(
                    min(start_pos[0], end_pos[0]),     # x координата (сол жақ)
                    min(start_pos[1], end_pos[1]),     # y координата (жоғарғы жақ)
                    abs(start_pos[0] - end_pos[0]),    # ен (width)
                    abs(start_pos[1] - end_pos[1])     # биіктік (height)
                )
                pygame.draw.rect(screen, current_color, rect, width = 2)

            elif mode == "circle":
                end_pos = event.pos
                radius = int(((start_pos[0] - end_pos[0]) ** 2 
                              +  # --> бастапқы нүкте (start_pos) мен соңғы нүкте (end_pos) аралығындағы қашықтықты 
                              (start_pos[1] - end_pos[1]) ** 2) ** 0.5)
                
                pygame.draw.circle(screen, current_color, start_pos, radius, width = 2)
            drawing = False
        # Мышканың қимылы сурет салғанда
        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "brush":
                pygame.draw.line(screen, current_color, last_pos, event.pos, brush_size)
                last_pos = event.pos
            elif mode == "eraser":
                pygame.draw.line(screen, WHITE, last_pos, event.pos, brush_size * 4)
                last_pos = event.pos
    pygame.display.update()
