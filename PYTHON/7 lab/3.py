import pygame
pygame.init()

pygame.display.set_caption("Moving Ball")
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
speed = 5

clock = pygame.time.Clock()

running = True 
while running:
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.display.flip() # --> терезені толық жаңартады экранды

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y - ball_radius - speed >= 0:
        ball_y -= speed
    if keys[pygame.K_DOWN] and ball_y + ball_radius + speed <= HEIGHT:
        ball_y += speed
    if keys[pygame.K_LEFT] and ball_x - ball_radius - speed >= 0:
        ball_x -= speed
    if keys[pygame.K_RIGHT] and ball_x + ball_radius + speed <= WIDTH:
        ball_x += speed
    
    clock.tick(60)
pygame.quit()