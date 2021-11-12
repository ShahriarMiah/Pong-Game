import pygame
import math


class BallClass:
    def __init__(self, X, Y, VelX, VelY, Velocity, angle, check):
        self.X = X
        self.Y = Y
        self.VelX = VelX
        self.VelY = VelY
        self.Velocity = Velocity
        self.angle = angle
        self.check = check

    def ballmovement(self, Window):
        Window.blit(pygame.image.load("ball.png"), (self.X, self.Y))
        # Calculating the speed of the ball dependent upon the angle
        # This will change once the ball hits the paddle
        self.VelX = self.Velocity * math.sin(math.radians(self.angle))
        self.VelY = self.Velocity * math.cos(math.radians(self.angle))

        self.X += self.VelX
        self.Y += self.VelY
        if self.X <= 0:
            self.check = "Left"
            self.angle = -1 * self.angle
        elif self.X + 32 >= 500:
            self.angle = -1 * self.angle
            self.check = "Right"
        elif self.Y <= 0:
            self.angle = 180 - self.angle
        elif self.Y + 32 >= 780:
            self.angle = 180 - self.angle

    def playerCollision(self):
        from main import Player1
        from main import Player2
        if self.Y >= 720:
            if Player1.X < self.X < Player1.X + 10 or Player1.X < self.X + 32 < Player1.X + 10:
                self.angle = -135
            if Player1.X + 10 < self.X < Player1.X + 20 or Player1.X + 10 < self.X + 32 < Player1.X + 20:
                self.angle = -150
            if Player1.X + 20 < self.X < Player1.X + 40 or Player1.X + 20 < self.X + 32 < Player1.X + 40:
                self.angle = -165
            if Player1.X + 40 < self.X < Player1.X + 60 or Player1.X + 40 < self.X + 32 < Player1.X + 60:
                self.angle = 170
            if Player1.X + 60 < self.X < Player1.X + 80 or Player1.X + 60 < self.X + 32 < Player1.X + 80:
                self.angle = 190
            if Player1.X + 100 < self.X < Player1.X + 110 or Player1.X + 100 < self.X + 32 < Player1.X + 110:
                self.angle = 165
            if Player1.X + 110 < self.X < Player1.X + 128 or Player1.X + 110 < self.X + 32 < Player1.X + 128:
                self.angle = 150
        elif self.Y <= 30:
            if Player2.X < self.X < Player2.X + 10 or Player2.X < self.X + 32 < Player2.X + 10:
                if self.check == "Left":
                    self.angle = 45
                else:
                    self.angle = -45
            if Player2.X + 10 < self.X < Player2.X + 20 or Player2.X + 10 < self.X + 32 < Player2.X + 20:
                if self.check == "Left":
                    self.angle = 30
                else:
                    self.angle = -30
            if Player2.X + 20 < self.X < Player2.X + 40 or Player2.X + 20 < self.X + 32 < Player2.X + 40:
                if self.check == "Left":
                    self.angle = 15
                else:
                    self.angle = -15
            if Player2.X + 40 < self.X < Player2.X + 60 or Player2.X + 40 < self.X + 32 < Player2.X + 60:
                if self.check == "Left":
                    self.angle = 10
                else:
                    self.angle = -10
            if Player2.X + 60 < self.X < Player2.X + 80 or Player2.X + 60 < self.X + 32 < Player2.X + 80:
                if self.check == "Left":
                    self.angle = 10
                else:
                    self.angle = -10
            if Player2.X + 80 < self.X < Player2.X + 100 or Player2.X + 80 < self.X + 32 < Player2.X + 100:
                if self.check == "Left":
                    self.angle = 15

            if Player2.X + 100 < self.X < Player2.X + 128 or Player2.X + 100 < self.X + 32 < Player2.X + 128:
                if self.check == "Left":
                    self.angle = 30
                else:
                    self.angle = -30
