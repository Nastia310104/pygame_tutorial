from Character import character
import pygame

class Enemy(character):
    walkRight = [pygame.image.load('Images/Enemy/R1E.png'), pygame.image.load('Images/Enemy/R2E.png'), pygame.image.load('Images/Enemy/R3E.png'), pygame.image.load('Images/Enemy/R4E.png'), pygame.image.load('Images/Enemy/R5E.png'), pygame.image.load('Images/Enemy/R6E.png'), pygame.image.load('Images/Enemy/R7E.png'), pygame.image.load('Images/Enemy/R8E.png'), pygame.image.load('Images/Enemy/R9E.png'), pygame.image.load('Images/Enemy/R10E.png'), pygame.image.load('Images/Enemy/R11E.png')]
    walkLeft = [pygame.image.load('Images/Enemy/L1E.png'), pygame.image.load('Images/Enemy/L2E.png'), pygame.image.load('Images/Enemy/L3E.png'), pygame.image.load('Images/Enemy/L4E.png'), pygame.image.load('Images/Enemy/L5E.png'), pygame.image.load('Images/Enemy/L6E.png'), pygame.image.load('Images/Enemy/L7E.png'), pygame.image.load('Images/Enemy/L8E.png'), pygame.image.load('Images/Enemy/L9E.png'), pygame.image.load('Images/Enemy/L10E.png'), pygame.image.load('Images/Enemy/L11E.png')]

    def __init__(self, x, y, width, height, vel, imageCount, end):
        super().__init__(x, y, width, height, vel, imageCount)
        self.end = end
        self.path = [self.x, self.end]
        self.standing = False
    
    def draw(self, window):
        self.move()
        if self.vel > 0:
            window.blit(self.walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
        else:
            window.blit(self.walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1

        return super().draw(window)

            
    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0

    def die(self):
        print("You shoot me, bitch")