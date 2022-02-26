import pygame
import random
from Particle import Particle

particle1 = Particle()
PARTICLE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(PARTICLE_EVENT, 50)

class PowerUps:

    def __init__(self):
        self.timer = 0
        self.currentTime = 0

    def BallSpeedUp(self, block):
        #Checks which objects are in use
        if block == "B3":
            from main import BallAI,blockAI
        else:
            from main import Ball1, Ball2, block1, block2
        if block == "B1":
            ball = Ball1
            block = block1
        elif block == "B2":
            ball = Ball2
            block = block2
        else:
            ball = BallAI
            block = blockAI
        ball.Velocity = 10
        if self.timer == 0:
            self.currentTime = pygame.time.get_ticks()
            self.timer += 1
        time = pygame.time.get_ticks()
        if time - self.currentTime > 4000:
            ball.Velocity = 6
            block.checkHits = 0
            block.Choice = random.randint(0,2)
            block.poweractivated = True
            time = 0
            self.timer = 0
            self.currentTime = 0



    def IncreasePlayer(self, block):

        if block == "B3":
            from main import blockAI,Player1AI,Player2AI
        else:
            from main import Player1, Player2, Player3, Player4, block1, block2
        if block == "B1":
            block = block1
            player = Player1
            player2 = Player2
        elif block == "B2":
            block = block2
            player = Player3
            player2 = Player4
        else:
            block = blockAI
            player = Player1AI
            player2 = Player2AI
        if block.player == 1:
            player.Width = 200
        else:
            player2.Width = 200
        if self.timer == 0:
            self.currentTime = pygame.time.get_ticks()
            self.timer += 1
        time = pygame.time.get_ticks()
        if time - self.currentTime > 4000:
            player.Width = 128
            player.Width = 128
            block.checkHits = 0
            block.poweractivated = True
            block.Choice = random.randint(0, 2)
            time = 0
            self.timer = 0
            self.currentTime = 0


    def particleffect(self,screen,b):

        if b == "B3":
            from main import BallAI,blockAI,Window2
        else:
            from main import Ball1, block1, Ball2, block2, Window
        if b == "B1":
            a = Ball1
            block = block1
            screen = Window
        elif b == "B2":
            a = Ball2
            block = block2
            screen = Window
        else:
            a = BallAI
            block = blockAI
            screen = Window2
        for event in pygame.event.get():
            if event.type == PARTICLE_EVENT:
                if particle1.update != "Nyan":
                    particle1.add_particles(0,pygame.Color("Red"),a)
                else:
                    particle1.add_particles(2, pygame.Color("Red"),a)
                    particle1.add_particles(6, pygame.Color("Orange"),a)
                    particle1.add_particles(10, pygame.Color("Yellow"),a)
                    particle1.add_particles(14, pygame.Color("Green"),a)
                    particle1.add_particles(18, pygame.Color("Blue"),a)
                    particle1.add_particles(22, pygame.Color("Purple"),a)
        #Sets timer or power up
        if self.timer == 0:
            self.currentTime = pygame.time.get_ticks()
            self.timer +=1
        time = pygame.time.get_ticks()
        if time - self.currentTime > 10000:
            self.timer = 0
            self.currentTime = 0
            block.checkHits = 0
            block.poweractivated = True
        particle1.emit(screen)



powers = PowerUps()


