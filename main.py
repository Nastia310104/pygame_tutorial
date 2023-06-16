import pygame
pygame.init()

import sys
sys.path += ["Classes", "Controllers"]

from Classes import Player, Enemy, Projectile
from Controllers import PlayerController, EnemyController

window = pygame.display.set_mode((500, 480))
pygame.display.set_caption("Tutorial game")

bg = pygame.image.load('Images/background.jpg')
clock = pygame.time.Clock()

player = Player.Player(200, 410, 64, 64, 5, 27)
goblin = Enemy.Enemy(100, 410, 64, 64, 3, 33, 450)
bullets = []

run = True

def redrawGameWindow():
    window.blit(bg, (0, 0))
    player.draw(window)
    goblin.draw(window)

    for bullet in bullets:
        bullet.draw(window)

    pygame.display.update()

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    PlayerController.start(player, keys, bullets)

    redrawGameWindow()

pygame.quit()
