import pygame
import random

tempTime = 0
paddleTempTime = 0

class Player:
    def __init__(self, X, Y, Width, Length, Vel, Key1, Key2, ):
        self.X = X
        self.Y = Y
        self.Width = Width
        self.Length = Length
        self.Vel = Vel
        self.Key1 = Key1
        self.Key2 = Key2
        self.set = False

    def moveplayer(self, Window, State):
        pygame.draw.rect(Window, (255, 255, 255), (self.X, self.Y, self.Width, self.Length))
        keys = pygame.key.get_pressed()
        if State == "p1":
            if keys[self.Key1] and self.X > self.Vel - 5 and self.X > 0:
                self.X -= self.Vel
            if keys[self.Key2] and self.X < 371:
                self.X += self.Vel
        else:
            if keys[self.Key1] and self.X > self.Vel - 5 and self.X > 500:
                self.X -= self.Vel
            if keys[self.Key2] and self.X < 871:
                self.X += self.Vel

    def AI_one(self, Window, time):
        from main import BallAI
        global paddleTempTime
        global tempTime
        pygame.draw.rect(Window, (255, 255, 255), (self.X, self.Y, self.Width, self.Length))
        probability = random.randint(1, 10)
        if BallAI.Y > 200 and 362 > self.X > 50:
            if not self.set:
                self.X += self.Vel / 1.5
            if self.set:
                self.X -= self.Vel / 1.5

        if self.X >= 350:
            self.set = True

        if self.X <= 80:
            self.set = False
        if BallAI.Y < 200:
            self.Vel = 0
            paddleTempTime = time
            if BallAI.X >= self.X and self.X < 371:
                self.X += self.Vel
            if BallAI.X < self.X > 0:
                self.X -= self.Vel

        if 0 < time % 8000 < 50 and probability > 2:
            tempTime = time
            self.Vel = 0
        if time - tempTime > 1300:
            self.Vel = 4
        if time - paddleTempTime >200:
            self.Vel = 4

    def AI_two(self, coordinates, Window):
        from main import BallAI
        pygame.draw.rect(Window, (255, 255, 255), (self.X, self.Y, self.Width, self.Length))
        if BallAI.Y < 500:
            try:
                if self.X < coordinates and self.X < 371:
                    self.X += self.Vel
                elif self.X >= coordinates and self.X > 0:
                    self.X -= self.Vel
            except:
                pass

    def AI_three(self, coordinates, Window):
        from main import BallAI
        pygame.draw.rect(Window, (255, 255, 255), (self.X, self.Y, self.Width, self.Length))
        if coordinates[0][1] < 50:
            if BallAI.Y < 500:
                try:
                    if self.X < coordinates[0][0] and self.X < 371:
                        self.X += self.Vel
                    elif self.X >= coordinates[0][0] and self.X > 0:
                        self.X -= self.Vel
                except:
                    pass
        elif coordinates[1][1] < 50:
            if BallAI.Y < 500:
                try:
                    if self.X < coordinates[1][0] and self.X < 371:
                        self.X += self.Vel
                    elif self.X >= coordinates[1][0] and self.X > 0:
                        self.X -= self.Vel
                except:
                    pass
        else:
            if BallAI.X >= self.X and self.X < 371:
                self.X += self.Vel
            if BallAI.X < self.X > 0:
                self.X -= self.Vel
