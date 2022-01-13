import pygame
import random


class Player:
    def __init__(self, X, Y, Width, Length, Vel, Key1, Key2, set):
        self.X = X
        self.Y = Y
        self.Width = Width
        self.Length = Length
        self.Vel = Vel
        self.Key1 = Key1
        self.Key2 = Key2
        self.set = set

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

    def AImovement(self, Window):
        from AI import BallAI
        pygame.draw.rect(Window, (255, 255, 255), (self.X, self.Y, self.Width, self.Length))

        if BallAI.Y > 200 and 362 > self.X > 50:
            if not self.set:
                self.X += self.Vel / 2
            if self.set:
                self.X -= self.Vel / 2

        if self.X >= 350:
            self.set = True

        if self.X <= 80:
            self.set = False
        if BallAI.Y < 200:
            if BallAI.X >= self.X and self.X < 371:
                self.X += self.Vel / 1.5
            if BallAI.X < self.X > 0:
                self.X -= self.Vel / 1.5

