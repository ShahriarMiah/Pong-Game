import pygame
import time
from Blocks import Block
from Menu import Menu
from Ball import BallClass
from Player import Player
import math

pygame.init()

Window = pygame.display.set_mode((500, 780))
menu = Menu(Window, pygame.font.Font("Caramel Sweets.ttf", 80), pygame.font.Font("Caramel Sweets.ttf", 60),
            pygame.font.Font("Caramel Sweets.ttf", 35), pygame.font.Font("Caramel Sweets.ttf", 22))
pygame.display.set_caption("4 Player Pong")
background = pygame.image.load("Backgrounds.jpg")
block1 = Block(200, 200, 64, 64, 0)
Gameover = True
mainMenu = False
running = True
click = False
gamesPlayed = True
P1score = 0
P2score = 0


def showscore(self):
    font = pygame.font.Font("Caramel Sweets.ttf", 32)
    score_rend = font.render(str(P1score), True, (255, 255, 255))
    Window.blit(score_rend, (10, 10))
    score_rend2 = font.render(str(P2score), True, (255, 255, 255))
    Window.blit(score_rend2, (10, 730))


if gamesPlayed:
    Player1 = Player(200, 699, 128, 4, pygame.K_LEFT, pygame.K_RIGHT)
    Player2 = Player(200, -44, 128, 4, pygame.K_a, pygame.K_d)
    Ball1 = BallClass(250, 600, 6, 6, 6, 45, "Left")
while running:
    pygame.time.delay(5)
    Window.fill((0, 0, 0))
    Window.blit(background, (-50, -65))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if mainMenu:
        key = pygame.key.get_pressed()
        if key[pygame.K_p]:
            menu.pause()
        if Gameover:
            Player1 = Player(200, 699, 128, 4, pygame.K_LEFT, pygame.K_RIGHT)
            Player2 = Player(200, -44, 128, 4, pygame.K_a, pygame.K_d)
            Ball1.Y = 250
            Ball1.X = 250
            gamesPLayed = False
            menu.StartGame()
            Gameover = False
        if Ball1.Y <= 0:
            P2score += 1
        elif Ball1.Y + 32 >= 780:
            P1score += 1
        # Checks if the ball hits the wall
        if Player1.X < Ball1.X < Player1.X + Player1.Width:
            Ball1.playerCollision()
        elif Player2.X < Ball1.X < Player2.X + Player2.Width:
            Ball1.playerCollision()
        if block1.Y < Ball1.Y < block1.Y + 62:
            block1.blockCollision()

        if P1score == 5:
            font2 = pygame.font.Font("Caramel Sweets.ttf", 50)
            Window.blit(font2.render("Player 2 has won!! ", True, (255, 255, 255)), [25, 320])
            pygame.display.flip()
            time.sleep(2)
            P2score = 0
            P1score = 0
            Gameover = True
        if P2score == 5:
            font2 = pygame.font.Font("Caramel Sweets.ttf", 50)
            Window.blit(font2.render("Player 1 has won!! ", True, (255, 255, 255)), [25, 320])
            pygame.display.flip()
            time.sleep(2)
            P2score = 0
            P1score = 0
            block1.checkHits = 0
            Gameover = True
        showscore(Window)
        Player1.moveplayer(Window)
        Player2.moveplayer(Window)
        Ball1.ballmovement(Window)
        block1.showBlock(Window)
    else:
        menu.mainmenu()
        mainMenu = True
    pygame.display.update()
pygame.quit()

