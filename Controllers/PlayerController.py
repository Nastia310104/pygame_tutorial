import pygame

from Classes import Projectile
from Controllers import ProjectileController

def start(player, keys):
    move(player, keys)
    jump(player, keys)

def move(player, keys):
    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.move("left")
    elif keys[pygame.K_RIGHT] and player.x < 500 - player.width - player.vel:
        player.move("right")
    else:
        player.move("")

def jump(player, keys):
    if not(player.isJump):
        if keys[pygame.K_UP]:
            player.isJump = True
            player.move("")
    else:
        if player.jumpCount >= -10:
            negotive = 1
            if player.jumpCount < 0:
                negotive = -1
            player.y -= int((player.jumpCount ** 2) * 0.5 * negotive)
            player.jumpCount -= 1
        else:
            player.isJump = False
            player.jumpCount = 10

def shoot(player, bullets):
    if player.left: 
        facind = -1
    else:
        facind = 1

    if len(bullets) < 5:
        bullets.append(Projectile.Projectile(round(player.x + player.width // 2), round(player.y + player.height // 2), 5, (0, 0, 255), facind))
    
