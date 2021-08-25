import pygame

class BallClass:
    def __init__(self, X, Y, VelX,VelY):
        self.X = X
        self.Y = Y
        self.VelX = VelX
        self.VelY = VelY

    def ballmovement(self, Window):
        Window.blit(pygame.image.load("Ball.png"), (self.X, self.Y))
        if self.X <= -10:
            self.VelX = abs(self.VelX)
        elif self.X >= 480:
            self.VelX = -abs(self.VelX)
        elif self.Y <= 0:
            self.VelY = abs(self.VelY)
        elif self.Y >= 760:
            self.VelY = -abs(self.VelY)
        else:
            self.Y += self.VelY
            self.X += self.VelX
        self.X += self.VelX
        self.Y += self.VelY

Ball1 = BallClass(250, 500, 1.5, 1.5)
