import random

import pygame

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

score = 0
amount_of_targets = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Groups Pew!")
myfont = pygame.font.SysFont("Times New Roman", 18)

clock = pygame.time.Clock()
FPS = 60

colours = ["crimson", "chartreuse", "coral", "darkorange", "forestgreen", "lime", "navy"]

class Shot(pygame.sprite.Sprite):
    def __init__(self, col, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(col)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.target_vector = ((x - (SCREEN_WIDTH/2))/10, (y - (SCREEN_HEIGHT/2))/10)
        self.gravity = 1.1

    def update(self):
        #TODO: Add ballistic curve
        # (x, y) = self.target_vector
        # target_vector_with_gravity = (x, y + 0.1 * self.gravity)
        # self.gravity *= self.gravity
        # self.rect.move_ip(target_vector_with_gravity)

        self.rect.move_ip(self.target_vector)
        if self.rect.top > SCREEN_HEIGHT or self.rect.bottom < 0 or self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.kill()
        self.check_collisions()

    def check_collisions(self):
        if pygame.sprite.spritecollide(self, targets, True):
            global score
            score += 1
            self.kill()

class Target(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill("blue")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

shots = pygame.sprite.Group()
targets = pygame.sprite.Group()
players = pygame.sprite.Group()

for _ in range(amount_of_targets):
    targets.add(Target(random.randint(0,SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))

player = Player()
players.add(player)

run = True
while run:
    clock.tick(FPS)

    screen.fill("black")
    pygame.draw.rect(screen, (0,0,255), player)

    shots.update()
    shots.draw(screen)

    targets.draw(screen)

    players.draw(screen)

    score_label = myfont.render(f"Score: ({score})", 1, (2, 239, 238))
    screen.blit(score_label, (0, 0))

    if len(targets) < amount_of_targets:
        targets.add(Target(random.randint(0,SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            square = Shot(random.choice(colours), pos[0], pos[1])
            shots.add(square)

        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()






























#https://www.youtube.com/watch?v=4TfZjhw0J-8