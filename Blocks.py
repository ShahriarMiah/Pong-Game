import random
import pygame


class Block:
    def __init__(self, X, Y, Length, Width, checkHits, Choice,State):
        self.X = X
        self.Y = Y
        self.Length = Length
        self.Width = Width
        self.checkHits = checkHits
        self.Choice = Choice
        self.state = State

    def showBlock(self, Window,block,ball,player,b):
        from Powers import powers
        if self.checkHits < 3:
            Window.blit(pygame.image.load("block.png"), (self.X, self.Y))
        elif self.checkHits == 3:
            if b == "B1":
                self.X = random.randint(64, 436)
                self.Y = random.randint(100, 600)
            else:
                self.X = random.randint(564, 936)
                self.Y = random.randint(100, 600)

            if self.Choice == 1:
                if b == "B1":
                    powers.BallSpeedUp("B1")
                else:
                    powers.BallSpeedUp("B2")


            elif self.Choice == 0:
                self.state = True

            else:
                if b == "B1":
                    powers.IncreasePlayer("B1")
                else:
                    powers.IncreasePlayer("B2")


    def blockCollision(self,Ball):
        from main import Ball1
        from main import Ball2
        if Ball == "B1":
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
        else:
            if (self.X < Ball2.X < self.X + 62) or (self.X < Ball2.X + 32 < self.X + 62):
                if self.Y < Ball2.Y < self.Y + 2:
                    Ball2.angle = 180 - Ball2.angle
                    self.checkHits += 1
                else:
                    Ball2.angle = 180 - Ball2.angle
                    self.checkHits += 1
            elif self.X + 63 < Ball1.X < self.X + 66 or self.X + 63 < self.X + 32 < self.X + 66:
                Ball2.angle *= -1
                self.checkHits += 1
            elif self.X < Ball2.X < self.X + 2 or self.X < Ball2.X + 32 < self.X + 2:
                Ball2.angle *= -1
                self.checkHits += 1
