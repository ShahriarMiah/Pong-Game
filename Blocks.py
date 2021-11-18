import random
import pygame



class Block:
    def __init__(self, X, Y, Length, Width, checkHits):
        self.X = X
        self.Y = Y
        self.Length = Length
        self.Width = Width
        self.checkHits = checkHits

    def showBlock(self, Window):
        from Powers import powers
        if self.checkHits < 3:
            Window.blit(pygame.image.load("block.png"), (self.X, self.Y))
        elif self.checkHits == 3:
            self.X = random.randint(64, 436)
            self.Y = random.randint(100, 600)
            powers.BallSpeedUp()
    def blockCollision(self):
        from main import Ball1
        if (self.X < Ball1.X < self.X + 62) or (self.X < Ball1.X + 32 < self.X + 62):
            if self.Y < Ball1.Y < self.Y + 2:
                Ball1.angle = 180 - Ball1.angle
                self.checkHits += 1
            else:
                Ball1.angle = 180 - Ball1.angle
                self.checkHits += 1
        elif self.X + 63 < Ball1.X < self.X + 66 or self.X + 63 < self.X + 32 < self.X + 66:
            Ball1.angle *= -1
            self.checkHits += 1
        elif self.X < Ball1.X < self.X + 2 or self.X < Ball1.X + 32 < self.X + 2:
            Ball1.angle *= -1
            self.checkHits += 1

