import pygame
import random


class PowerUps:

    def __init__(self, Timer, currentTime):
        self.timer = Timer
        self.currentTime = currentTime

    def BallSpeedUp(self, block):
        from main import Ball1, Ball2, block1, block2
        if block == "B1":
            Ball1.Velocity = 10
            if self.timer == 0:
                self.currentTime = pygame.time.get_ticks()
                self.timer += 1
            time = pygame.time.get_ticks()
            if time - self.currentTime > 4000:
                Ball1.Velocity = 6
                block1.checkHits = 0
                block1.Choice = random.randint(0,2)
                time = 0
                self.timer = 0
                self.currentTime = 0

        if block == "B2":
            Ball2.Velocity = 10
            if self.timer == 0:
                self.currentTime = pygame.time.get_ticks()
                self.timer += 1
            time = pygame.time.get_ticks()
            if time - self.currentTime > 4000:
                Ball2.Velocity = 6
                block2.checkHits = 0
                block2.Choice = random.randint(0,2)
                time = 0
                self.timer = 0
                self.currentTime = 0

    def IncreasePlayer(self, block):
        from main import Player1, Player3, block1, block2
        if block == "B1":
            Player1.Width = 200
            if self.timer == 0:
                self.currentTime = pygame.time.get_ticks()
                self.timer += 1
            time = pygame.time.get_ticks()
            if time - self.currentTime > 4000:
                Player1.Width = 128
                block1.checkHits = 0
                block1.Choice = random.randint(0, 2)
                time = 0
                self.timer = 0
                self.currentTime = 0
        if block == "B2":
            Player3.Width = 200
            if self.timer == 0:
                self.currentTime = pygame.time.get_ticks()
                self.timer += 1
            time = pygame.time.get_ticks()
            if time - self.currentTime > 4000:
                block2.Choice = random.randint(0,2)
                Player3.Width = 128
                block2.checkHits = 0
                time = 0
                self.timer = 0
                self.currentTime = 0


powers = PowerUps(0, 0)
