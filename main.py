import pygame
pygame.init()

import sys
sys.path.append("Classes")

from Classes import Player, Enemy, Projectile

window = pygame.display.set_mode((500, 480))

pygame.display.set_caption("Tutorial game")

bg = pygame.image.load('Images/background.jpg')

clock = pygame.time.Clock()

def redrawGameWindow():
    window.blit(bg, (0, 0))
    player.draw(window)
    goblin.draw(window)

    for bullet in bullets:
        bullet.draw(window)

    pygame.display.update()

player = Player.Player(200, 410, 64, 64, 5, 27)
goblin = Enemy.Enemy(100, 410, 64, 64, 3, 33, 450)
bullets = []

run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if player.left: 
            facind = -1
        else:
            facind = 1

        if len(bullets) < 5:
            bullets.append(Projectile.Projectile(round(player.x + player.width // 2), round(player.y + player.height // 2), 5, (0, 0, 255), facind))

    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.move("left")
    elif keys[pygame.K_RIGHT] and player.x < 500 - player.width - player.vel:
        player.move("right")
    else:
        player.move("")

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

    redrawGameWindow()

pygame.quit()
