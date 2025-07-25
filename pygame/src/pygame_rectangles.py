import pygame
import random

pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

score = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame_Recangles")

#define colours
BG = (50, 50, 50)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()
myfont = pygame.font.SysFont("Times New Roman", 18)

rect_1 = pygame.Rect(0, 0, 25, 25)

food_rect = pygame.Rect(random.randint(0, 1000), random.randint(0, 750), 25, 25)


run = True
while run:
    screen.fill(BG)

    col = GREEN

    pygame.draw.rect(screen, col, rect_1)
    pygame.draw.rect(screen, BLUE, food_rect)

    score_label = myfont.render(f"Score: ({score})", 1, (2, 239, 238))
    screen.blit(score_label, (0, 0))

    if rect_1.colliderect(food_rect):
        score += 1
        food_rect.x, food_rect.y = random.randint(0, 1000), random.randint(0, 750)


    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and rect_1.y > 0:
        rect_1.y -= 5
    if keys[pygame.K_DOWN] and rect_1.y < 743:
        rect_1.y += 5
    if keys[pygame.K_RIGHT] and rect_1.x < 999:
        rect_1.x += 5
    if keys[pygame.K_LEFT] and rect_1.x > 0:
        rect_1.x -= 5

    pygame.display.flip()

pygame.quit()