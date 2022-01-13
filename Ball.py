import pygame
import math


class BallClass:
    def __init__(self, X, Y, VelX, VelY, Velocity, angle, check, radius):
        self.X = X
        self.Y = Y
        self.VelX = VelX
        self.VelY = VelY
        self.Velocity = Velocity
        self.angle = angle
        self.check = check
        self.radius = radius

    def draw(self, Window):
        Window.blit(pygame.image.load("ball.png"), (self.X, self.Y))

    def ballPath(self, startX, startY, power, ang, time):
        velX = math.cos(ang) * power
        velY = math.sin(ang) * power
        distanceX = velX * time
        distanceY = (velY * time) + ((-4.9 * time ** 2) / 2)
        newX = round(distanceX + startX)
        newY = round(startY - distanceY)
        return newX, newY

    def ballmovement(self, Window, p1, p2):
        Window.blit(pygame.image.load("ball.png"), (self.X, self.Y))
        # Calculating the speed of the ball dependent upon the angle
        # This will change once the ball hits the paddle
        self.VelX = self.Velocity * math.sin(math.radians(self.angle))
        self.VelY = self.Velocity * math.cos(math.radians(self.angle))

        self.X += self.VelX
        self.Y += self.VelY
        if self.X <= p1:
            self.check = "Left"
            self.angle = -1 * self.angle
        elif self.X + 32 >= p2:
            self.angle = -1 * self.angle
            self.check = "Right"
        elif self.Y <= 0:
            self.angle = 180 - self.angle
        elif self.Y + 32 >= 780:
            self.angle = 180 - self.angle

    def playerCollision(self, Player1, Player2):

        if self.Y >= 720:
            if Player1.X < self.X < Player1.X + 10 or Player1.X < self.X + 32 < Player1.X + 10:
                self.angle = -130
            if Player1.X + 10 < self.X < Player1.X + 20 or Player1.X + 10 < self.X + 32 < Player1.X + 20:
                self.angle = -145
            if Player1.X + 20 < self.X < Player1.X + 40 or Player1.X + 20 < self.X + 32 < Player1.X + 40:
                self.angle = -160
            if Player1.X + 40 < self.X < Player1.X + 60 or Player1.X + 40 < self.X + 32 < Player1.X + 60:
                self.angle = 160
            if Player1.X + 60 < self.X < Player1.X + 80 or Player1.X + 60 < self.X + 32 < Player1.X + 80:
                self.angle = 180
            if Player1.X + 100 < self.X < Player1.X + 110 or Player1.X + 100 < self.X + 32 < Player1.X + 110:
                self.angle = 175
            if Player1.X + 110 < self.X < Player1.X + 128 or Player1.X + 110 < self.X + 32 < Player1.X + 128:
                self.angle = 160
            if Player1.Length == 200:
                if Player1.X + 128 < self.X < Player1.X + 200 or Player1.X + 128 < self.X < Player1.X + 200:
                    self.angle = 160
        elif self.Y <= 30:
            if Player2.X < self.X < Player2.X + 10 or Player2.X < self.X + 32 < Player2.X + 10:
                if self.check == "Left":
                    self.angle = 55
                else:
                    self.angle = -55
            if Player2.X + 10 < self.X < Player2.X + 20 or Player2.X + 10 < self.X + 32 < Player2.X + 20:
                if self.check == "Left":
                    self.angle = 40
                else:
                    self.angle = -40
            if Player2.X + 20 < self.X < Player2.X + 40 or Player2.X + 20 < self.X + 32 < Player2.X + 40:
                if self.check == "Left":
                    self.angle = 25
                else:
                    self.angle = -25
            if Player2.X + 40 < self.X < Player2.X + 60 or Player2.X + 40 < self.X + 32 < Player2.X + 60:
                if self.check == "Left":
                    self.angle = 20
                else:
                    self.angle = -20
            if Player2.X + 60 < self.X < Player2.X + 80 or Player2.X + 60 < self.X + 32 < Player2.X + 80:
                if self.check == "Left":
                    self.angle = 20
                else:
                    self.angle = -20
            if Player2.X + 80 < self.X < Player2.X + 100 or Player2.X + 80 < self.X + 32 < Player2.X + 100:
                if self.check == "Left":
                    self.angle = 25

            if Player2.X + 100 < self.X < Player2.X + 128 or Player2.X + 100 < self.X + 32 < Player2.X + 128:
                if self.check == "Left":
                    self.angle = 40
                else:
                    self.angle = -40
            if Player2.Length == 200:
                if Player2.X + 128 < self.X < Player2.X + 200 or Player2.X + 128 < self.X < Player2.X + 200:
                    self.angle = 40

