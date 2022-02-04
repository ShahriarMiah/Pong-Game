import random

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
        from Powers import particle1
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
            particle1.particles = []
            particle1.update = "Circles"
        elif self.X + 32 >= p2:
            self.angle = -1 * self.angle
            self.check = "Right"
            particle1.particles = []
            particle1.update = "Rectangles"
        elif self.Y <= 0:
            self.angle = 180 - self.angle
            particle1.particles = []
            particle1.update = "Nyan"
        elif self.Y + 32 >= 780:
            self.angle = 180 - self.angle
            particle1.particles = []
            particle1.update = "Circles"

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

    def magnetmovement(self, Player1, ball):
        if ball == "B3":
            from AI import blockAI
        if Player1.Y > 500:

            if self.Y > 400:
                dx, dy = (Player1.X - self.X, Player1.Y - self.Y)
                stepx, stepy = (dx / 30, dy / 30)
                self.X += stepx
                self.Y -= stepy
                if Player1.X < self.X < Player1.X + Player1.Width:
                    if self.Y >= 720:
                        blockAI.magnet = False
                        blockAI.checkHits = 0
                        blockAI.player = random.randint(0, 1)
                        blockAI.Choice = random.randint(0, 4)
        else:
            if self.Y < 380:
                dx, dy = (Player1.X - self.X, Player1.Y - self.Y)
                stepx, stepy = (dx / 60, dy / 60)
                self.X += stepx
                self.Y += stepy
                if Player1.X < self.X < Player1.X + Player1.Width:
                    if self.Y <= 30:
                        blockAI.magnet = False
                        blockAI.checkHits = 0
                        blockAI.player = random.randint(0, 1)
                        blockAI.Choice = random.randint(0, 4)

        if self.X <= 0:
            self.angle = -1 * self.angle
        elif self.X + 10 >= 500:
            self.angle = -1 * self.angle
        elif self.Y <= 0:
            self.angle = 180 - self.angle
        elif self.Y + 10 >= 700:
            self.angle = 180 - self.angle

    def get_direction(self, ponglist, new_coordinates_x, new_coordinates_y):
        vec_list = []

        for i in range(len(ponglist) - 1):
            x1, y1 = ponglist[i]
            x2, y2 = ponglist[i + 1]
            vec = [x2 - x1, y2 - y1]
            vec_list.append(vec)

        while 0 <= new_coordinates_x <= 500 and 0 <= new_coordinates_y <= 780:
            new_coordinates_y += vec_list[0][1]
            new_coordinates_x += vec_list[0][0]
        return new_coordinates_x

    def draw_line(self, coordinates, Window):
        pygame.draw.line(Window, (255, 255, 255), (self.X + 16, self.Y + 16), coordinates[0])


