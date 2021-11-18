import pygame


class PowerUps:
    def __init__(self, Timer, currentTime):
        self.timer = Timer
        self.currentTime = currentTime

    def BallSpeedUp(self):
        from main import Ball1
        from main import block1
        Ball1.Velocity = 10
        if self.timer == 0:
            self.currentTime = pygame.time.get_ticks()
            self.timer += 1
        time = pygame.time.get_ticks()
        if time - self.currentTime > 4000:
            Ball1.Velocity = 6
            block1.checkHits = 0
            time = 0
            self.timer = 0
            self.currentTime = 0


powers = PowerUps(0, 0)
