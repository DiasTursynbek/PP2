# color_buttons = {
#     "red":    pygame.Rect(10, 10, 40, 40),
#     "green":  pygame.Rect(60, 10, 40, 40),
#     "blue":   pygame.Rect(110, 10, 40, 40),
#     "black":  pygame.Rect(160, 10, 40, 40)
# }

# color_map = {
#     "red": RED,
#     "green": GREEN,
#     "blue": BLUE,
#     "black": BLACK
# }



# Оны while True: ішінде pygame.display.update()-ке дейінгі жерге қос:
# for name, rect in color_buttons.items():
#     pygame.draw.rect(screen, color_map[name], rect)
#     pygame.draw.rect(screen, BLACK, rect, 2)  # шеті



# Мына бөлікті MOUSEBUTTONDOWN ішіне қос:
# for name, rect in color_buttons.items():
#     if rect.collidepoint(event.pos):
#         current_color = color_map[name]








# import pygame
# import sys

# pygame.init()

# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption("Paintqoi")

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED   = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE  = (0, 0, 255)
# current_color = BLACK

# screen.fill(WHITE)

# brush_size = 5
# drawing = False
# last_pos = None
# start_pos = None
# mode = "brush"

# # 🎨 Түсті батырмалар
# color_buttons = {
#     "red": pygame.Rect(10, 10, 40, 40),
#     "green": pygame.Rect(60, 10, 40, 40),
#     "blue": pygame.Rect(110, 10, 40, 40),
#     "black": pygame.Rect(160, 10, 40, 40)
# }

# color_map = {
#     "red": RED,
#     "green": GREEN,
#     "blue": BLUE,
#     "black": BLACK
# }

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
#             # 🖱️ Егер батырмаға басылса — түс өзгерту
#             for name, rect in color_buttons.items():
#                 if rect.collidepoint(event.pos):
#                     current_color = color_map[name]
#                     break
#             else:
#                 drawing = True
#                 start_pos = event.pos
#                 last_pos = event.pos

#         if event.type == pygame.MOUSEBUTTONUP:
#             if mode == "rect":
#                 end_pos = event.pos
#                 rect = pygame.Rect(
#                     min(start_pos[0], end_pos[0]),
#                     min(start_pos[1], end_pos[1]),
#                     abs(start_pos[0] - end_pos[0]),
#                     abs(start_pos[1] - end_pos[1])
#                 )
#                 pygame.draw.rect(screen, current_color, rect, width=2)

#             elif mode == "circle":
#                 end_pos = event.pos
#                 radius = int(((start_pos[0] - end_pos[0]) ** 2 +
#                               (start_pos[1] - end_pos[1]) ** 2) ** 0.5)
#                 pygame.draw.circle(screen, current_color, start_pos, radius, width=2)
#             drawing = False

#         if event.type == pygame.MOUSEMOTION and drawing:
#             if mode == "brush":
#                 pygame.draw.line(screen, current_color, last_pos, event.pos, brush_size)
#                 last_pos = event.pos
#             elif mode == "eraser":
#                 pygame.draw.line(screen, WHITE, last_pos, event.pos, brush_size * 4)
#                 last_pos = event.pos

#     # 🎨 Батырмаларды экранға сызу
#     for name, rect in color_buttons.items():
#         pygame.draw.rect(screen, color_map[name], rect)
#         pygame.draw.rect(screen, BLACK, rect, 2)  # контур

#     pygame.display.update()