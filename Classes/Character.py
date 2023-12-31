import pygame

class character(object):
    def __init__(self, x, y ,width, height, vel, imageCount):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.walkCount = 0
        self.left = False
        self.right = False
        self.standing = True
        self.imageCount = imageCount
        self.hitbox = (self.x + 17, self.y + 2, 29, 59)


    def draw(self, window):
        if self.walkCount + 1 >= self.imageCount:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                window.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                window.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                window.blit(self.walkRight[0], (self.x, self.y))
            else:
                window.blit(self.walkLeft[0], (self.x, self.y))

        self.hitbox = (self.x + 17, self.y + 2, 29, 59)
        pygame.draw.rect(window, (0, 150, 150), self.hitbox, 2)

    def move(self):
        pass