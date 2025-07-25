import pygame
from sys import exit

GAME_WIDTH = 1024
GAME_HEIGHT = 768
UPGRADE_BUTTON_HEIGHT = 20
BUTTON_HEIGHT = 50

background_image = pygame.image.load("resources/images/background.png")
upgrade_image = pygame.image.load("resources/images/upgrade.png")
upgrade_image = pygame.transform.scale(upgrade_image, (UPGRADE_BUTTON_HEIGHT, UPGRADE_BUTTON_HEIGHT))
upgrade_image_greyscale = pygame.image.load("resources/images/upgrade_greyscale.png")
upgrade_image_greyscale = pygame.transform.scale(upgrade_image_greyscale, (UPGRADE_BUTTON_HEIGHT, UPGRADE_BUTTON_HEIGHT))
ore_image = pygame.image.load("resources/images/ore.png")
ore_image = pygame.transform.scale(ore_image, (BUTTON_HEIGHT, BUTTON_HEIGHT))


pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Clicki Bunti")
myfont = pygame.font.SysFont("Times New Roman", 18)
clock = pygame.time.Clock()

class UpgradeButton(pygame.Rect):
    def __init__(self, x_pos, y_pos, cost, value, amount):
        pygame.Rect.__init__(self, x_pos, y_pos, UPGRADE_BUTTON_HEIGHT, UPGRADE_BUTTON_HEIGHT)
        self.image = upgrade_image_greyscale
        self.upgrade_cost = cost
        self.value = value
        self.amount = amount
        self.tooltip = myfont.render("Cost: " + str(round(self.upgrade_cost, 1)), False, (0, 0, 0), (255, 255, 0))

    def update_cost(self):
        self.upgrade_cost *= global_cost_factor
        self.tooltip = myfont.render("Cost: " + str(round(self.upgrade_cost, 1)), False, (0, 0, 0), (255, 255, 0))


class GlobalUpgradeButton(pygame.Rect):
    def __init__(self, x_pos, y_pos, cost, image, global_multiplier_addition):
        pygame.Rect.__init__(self, x_pos, y_pos, UPGRADE_BUTTON_HEIGHT, UPGRADE_BUTTON_HEIGHT)
        self.image = image
        self.global_multiplier_addition = global_multiplier_addition
        self.upgrade_cost = cost
        self.tooltip = myfont.render("Cost: " + str(round(self.upgrade_cost, 1)), False, (0, 0, 0), (255, 255, 0))


main_button = pygame.Rect(150, 150, 50, 50)

click_upgrade_button = UpgradeButton(750, 100, 50, 0, 1)
upgrade_button_1 = UpgradeButton(750, 140, 150, 0.2, 0)
upgrade_button_2 = UpgradeButton(750, 180, 250, 0.3, 0)
upgrade_button_3 = UpgradeButton(750, 220, 500, 0.5, 0)
upgrade_button_4 = UpgradeButton(750, 260, 1000, 1.0, 0)
upgrade_button_5 = UpgradeButton(750, 300, 2000, 2.0, 0)

global_upgrade_button_1 = GlobalUpgradeButton(100, 700, 1000, upgrade_image_greyscale, 0.1)
global_upgrade_button_2 = GlobalUpgradeButton(130, 700, 1500, upgrade_image_greyscale, 0.2)
global_upgrade_button_3 = GlobalUpgradeButton(160, 700, 3000, upgrade_image_greyscale, 0.5)
global_upgrade_button_4 = GlobalUpgradeButton(190, 700, 5000, upgrade_image_greyscale, 1.0)
global_upgrade_button_5 = GlobalUpgradeButton(220, 700, 10000, upgrade_image_greyscale, 1.5)

global_upgrade_list = [global_upgrade_button_1, global_upgrade_button_2, global_upgrade_button_3, global_upgrade_button_4, global_upgrade_button_5]
upgrade_button_list = [click_upgrade_button, upgrade_button_1, upgrade_button_2, upgrade_button_3, upgrade_button_4, upgrade_button_5]

counter = 0
click_upgrades = 1
click_value = 1
global_cost_factor = 1.6
global_multiplier = 1
global_auto_gain = 0
cheat_counter = 0

def draw():
    window.fill((20, 18, 167))
    window.blit(background_image, (0, 0))

    window.blit(ore_image, main_button)

    thingslabel = myfont.render("Things:", 1, (2, 239, 238))
    thingsdisplay = myfont.render(str(round(counter, 1)), 1, (2, 239, 238))
    window.blit(thingslabel, (770, 10))
    window.blit(thingsdisplay, (900, 10))

    things_per_second_label = myfont.render("Things/s:", 1, (2, 239, 238))
    things_per_second_display = myfont.render(str(round(global_auto_gain * global_multiplier, 1)), 1, (2, 239, 238))
    window.blit(things_per_second_label, (770, 40))
    window.blit(things_per_second_display, (900, 40))

    global_mult_label = myfont.render("Global Mult:", 1, (2, 239, 238))
    global_mult_display = myfont.render(str(round(global_multiplier, 1)), 1, (2, 239, 238))
    window.blit(global_mult_label, (770, 70))
    window.blit(global_mult_display, (900, 70))

    click_upgrades_label = myfont.render("Things per click:", 1, (2, 239, 238))
    click_upgrades_display = myfont.render(str(click_upgrades), 1, (2, 239, 238))
    window.blit(click_upgrades_label, (770, 100))
    window.blit(click_upgrades_display, (900, 100))
    window.blit(click_upgrade_button.image, click_upgrade_button)

    upgradeslabel_1 = myfont.render(f"Upgrades: ({upgrade_button_1.amount})", 1, (2, 239, 238))
    upgradesdisplay_1 = myfont.render(str(round(upgrade_button_1.amount * upgrade_button_1.value, 1)), 1, (2, 239, 238))
    window.blit(upgradeslabel_1, (770, 140))
    window.blit(upgradesdisplay_1, (900, 140))
    window.blit(upgrade_button_1.image, upgrade_button_1)

    upgradeslabel_2 = myfont.render(f"Upgrades: ({upgrade_button_2.amount})", 1, (2, 239, 238))
    upgradesdisplay_2 = myfont.render(str(round(upgrade_button_2.amount * upgrade_button_2.value, 1)), 1, (2, 239, 238))
    window.blit(upgradeslabel_2, (770, 180))
    window.blit(upgradesdisplay_2, (900, 180))
    window.blit(upgrade_button_2.image, upgrade_button_2)

    upgradeslabel_3 = myfont.render(f"Upgrades: ({upgrade_button_3.amount})", 1, (2, 239, 238))
    upgradesdisplay_3 = myfont.render(str(round(upgrade_button_3.amount * upgrade_button_3.value, 1)), 1, (2, 239, 238))
    window.blit(upgradeslabel_3, (770, 220))
    window.blit(upgradesdisplay_3, (900, 220))
    window.blit(upgrade_button_3.image, upgrade_button_3)

    upgradeslabel_4 = myfont.render(f"Upgrades: ({upgrade_button_4.amount})", 1, (2, 239, 238))
    upgradesdisplay_4 = myfont.render(str(round(upgrade_button_4.amount * upgrade_button_4.value, 1)), 1, (2, 239, 238))
    window.blit(upgradeslabel_4, (770, 260))
    window.blit(upgradesdisplay_4, (900, 260))
    window.blit(upgrade_button_4.image, upgrade_button_4)

    upgradeslabel_5 = myfont.render(f"Upgrades: ({upgrade_button_5.amount})", 1, (2, 239, 238))
    upgradesdisplay_5 = myfont.render(str(round(upgrade_button_5.amount * upgrade_button_5.value, 1)), 1, (2, 239, 238))
    window.blit(upgradeslabel_5, (770, 300))
    window.blit(upgradesdisplay_5, (900, 300))
    window.blit(upgrade_button_5.image, upgrade_button_5)

def draw_global_upgrades():
    for global_upgrade_button in global_upgrade_list:
        window.blit(global_upgrade_button.image, global_upgrade_button)


def auto_calc():
    global counter
    counter += (global_auto_gain * global_multiplier) / 60


def check_upgrade_buyable(checkable_button):
    if counter >= checkable_button.upgrade_cost:
        checkable_button.image = upgrade_image
    else:
        checkable_button.image = upgrade_image_greyscale


def reorg_global_upgrades():
    initial_x = 100
    button_distance = 30
    for i in range(len(global_upgrade_list)):
        global_upgrade_list[i].x = initial_x + i * button_distance


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if main_button.collidepoint(event.pos):
                counter += click_upgrades * click_value * global_multiplier

            if click_upgrade_button.collidepoint(event.pos) and counter >= click_upgrade_button.upgrade_cost:
                click_upgrades += 1
                counter -= click_upgrade_button.upgrade_cost
                click_upgrade_button.update_cost()


            for button in upgrade_button_list:
                if button.collidepoint(event.pos) and counter >= button.upgrade_cost:
                    counter -= button.upgrade_cost
                    button.update_cost()
                    global_auto_gain += button.value
                    button.amount += 1

            for button in global_upgrade_list:
                if button.collidepoint(event.pos) and counter >= button.upgrade_cost:
                    counter -= button.upgrade_cost
                    global_multiplier += button.global_multiplier_addition
                    global_upgrade_list.remove(button)
                    reorg_global_upgrades()

    #check for cheat code (DEV_MODE -> motherlode)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_m] and cheat_counter == 0:
        cheat_counter += 1
    if keys[pygame.K_o] and cheat_counter == 1 or cheat_counter == 7:
        cheat_counter += 1
    if keys[pygame.K_t] and cheat_counter == 2:
        cheat_counter += 1
    if keys[pygame.K_h] and cheat_counter == 3 or cheat_counter == 9:
        cheat_counter += 1
    if keys[pygame.K_e] and cheat_counter == 4:
        cheat_counter += 1
    if keys[pygame.K_r] and cheat_counter == 5:
        cheat_counter += 1
    if keys[pygame.K_l] and cheat_counter == 6:
        cheat_counter += 1
    if keys[pygame.K_d] and cheat_counter == 8:
        cheat_counter += 1

    if cheat_counter == 9:
        cheat_counter = 0
        counter += 500000

    auto_calc()

    draw()
    draw_global_upgrades()

    for checkable_button in upgrade_button_list + global_upgrade_list:
        check_upgrade_buyable(checkable_button)
        (mx, my) = pygame.mouse.get_pos()
        if checkable_button.collidepoint((mx, my)):
            window.blit(checkable_button.tooltip, (mx + 20, my))

    pygame.display.update()
    clock.tick(60)