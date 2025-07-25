import random

import pygame

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Groups")

clock = pygame.time.Clock()
FPS = 60

colours = ["crimson", "chartreuse", "coral", "darkorange", "forestgreen", "lime", "navy"]

class Square(pygame.sprite.Sprite):
    def __init__(self, col, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

squares = pygame.sprite.Group()

#todo
#pygame.sprite.spritecollide()

square = Square("crimson", 500, 300)
squares.add(square)

run = True
while run:
    clock.tick(FPS)

    screen.fill("cyan")

    squares.update()

    squares.draw(screen)

    print(squares)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            square = Square(random.choice(colours), pos[0], pos[1])
            squares.add(square)

        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()






























#https://www.youtube.com/watch?v=4TfZjhw0J-8