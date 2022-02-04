import random
import pygame


class Block:
    def __init__(self, X, Y, Length, Width, checkHits, Choice):
        self.X = X
        self.Y = Y
        self.Length = Length
        self.Width = Width
        self.checkHits = checkHits
        self.Choice = Choice
        self.speed = 2
        self.power_y = self.Y
        self.power_x = self.X
        self.gravity = 0
        self.state = False
        self.magnet = False
        self.player = 1
        self.poweractivated = True

    def showBlock(self, Window, b):
        from Powers import powers
        if b != "B3":
            from main import Player1, Player2
        if self.checkHits < 3:
            Window.blit(pygame.image.load("block.png"), (self.X, self.Y))
        elif self.checkHits == 3:
            if not self.poweractivated or b == "B3":
                if b == "B1" or b == "B3":
                    self.X = random.randint(64, 436)
                    self.Y = random.randint(100, 600)
                else:
                    self.X = random.randint(564, 936)
                    self.Y = random.randint(100, 600)

                if self.Choice == 1:
                    if b == "B1":
                        powers.BallSpeedUp(b)
                    elif b == "B2":
                        powers.BallSpeedUp(b)
                    else:
                        powers.BallSpeedUp(b)
                elif self.Choice == 0:
                    self.state = True

                elif self.Choice == 2:
                    powers.particleffect(Window, b)

                elif self.Choice == 3:
                    self.magnet = True
                else:
                    if b == "B1":
                        powers.IncreasePlayer("B1")
                    elif b == "B2":
                        powers.IncreasePlayer("B2")
                    else:
                        powers.IncreasePlayer("B3")
            else:
                self.fallingPower(Window)
                if self.player == 0:
                    if Player1.X < self.power_x < Player1.X + Player1.Width:
                        if self.power_y > 750:
                            self.player = random.randint(0, 1)
                            self.poweractivated = False
                    if self.power_y > 770:
                        self.checkHits = 0
                elif self.player == 1:
                    if Player2.X < self.power_x < Player2.X + Player2.Width:
                        if self.power_y < 30:
                            self.player = random.randint(0, 1)
                            self.poweractivated = False
                    if self.power_y < 10:
                        self.checkHits = 0

    def blockCollision(self, Ball):
        if Ball == "B1":
            from main import Ball1
            ball = Ball1
        elif Ball == "B2":
            from main import Ball2
            ball = Ball2
        else:
            from AI import BallAI
            ball = BallAI
        if (self.X < ball.X < self.X + 62) or (self.X < ball.X + 32 < self.X + 62):
            if self.Y < ball.Y < self.Y + 2:
                ball.angle = 180 - ball.angle
                self.checkHits += 1
            else:
                ball.angle = 180 - ball.angle
                self.checkHits += 1
        elif self.X + 63 < ball.X < self.X + 66 or self.X + 63 < self.X + 32 < self.X + 66:
            ball.angle *= -1
            self.checkHits += 1
        elif self.X < ball.X < self.X + 2 or self.X < ball.X + 32 < self.X + 2:
            ball.angle *= -1
            self.checkHits += 1

    def fallingPower(self, Window):
        Window.blit(pygame.image.load("power.png"), (self.power_x, self.power_y))
        if self.player == 0:
            self.speed += self.gravity
            self.power_y += self.speed
        else:
            self.speed += self.gravity
            self.power_y -= self.speed
