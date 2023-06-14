from Character import character
import pygame

class Player(character):
    walkRight = [pygame.image.load('Images/Player/R1.png'), pygame.image.load('Images/Player/R2.png'), pygame.image.load('Images/Player/R3.png'), pygame.image.load('Images/Player/R4.png'), pygame.image.load('Images/Player/R5.png'), pygame.image.load('Images/Player/R6.png'), pygame.image.load('Images/Player/R7.png'), pygame.image.load('Images/Player/R8.png'), pygame.image.load('Images/Player/R9.png')]
    walkLeft = [pygame.image.load('Images/Player/L1.png'), pygame.image.load('Images/Player/L2.png'), pygame.image.load('Images/Player/L3.png'), pygame.image.load('Images/Player/L4.png'), pygame.image.load('Images/Player/L5.png'), pygame.image.load('Images/Player/L6.png'), pygame.image.load('Images/Player/L7.png'), pygame.image.load('Images/Player/L8.png'), pygame.image.load('Images/Player/L9.png')]

    def __init__(self, x, y, width, height, vel, imageCount):
        super().__init__(x, y, width, height, vel, imageCount)
        self.isJump = False
        self.jumpCount = 10

    def draw(self, window):
        return super().draw(window)

    def move(self, direction):
        if direction == "right":
            self.x += self.vel
            self.right = True
            self.left = False
            self.standing = False
        elif direction == "left":
            self.x -= self.vel
            self.right = False
            self.left = True
            self.standing = False
        else:
            self.standing = True
            self.walkCount = 0

