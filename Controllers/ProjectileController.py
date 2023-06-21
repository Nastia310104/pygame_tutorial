def bulletShoot(bullets, goblin):
    for bullet in bullets:
        checkEnemyPossition(bullets, bullet, goblin)
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            removeBullet(bullet, bullets)

def checkEnemyPossition(bullets, bullet, goblin):
    if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
        if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
            goblin.die()
            removeBullet(bullet, bullets)

def removeBullet(bullet, bullets):
    bullets.pop(bullets.index(bullet))