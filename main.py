import pygame
import time
from Player import Player
from Ball import Ball1
from Score import ScoreClass
from Menu import Menu

pygame.init()

Window = pygame.display.set_mode((500, 780))
menu = Menu(Window, pygame.font.Font("Caramel Sweets.ttf", 80), pygame.font.Font("Caramel Sweets.ttf", 60),
            pygame.font.Font("Caramel Sweets.ttf", 35), pygame.font.Font("Caramel Sweets.ttf", 22))
pygame.display.set_caption("4 Player Pong")
Gameover = True
mainMenu = False
running = True
click = False
while running:
    pygame.time.delay(5)
    Window.fill((255, 255, 255))
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
            Score1 = ScoreClass(10, 10, 0, pygame.font.Font("Caramel Sweets.ttf", 32))
            Score2 = ScoreClass(10, 730, 0, pygame.font.Font("Caramel Sweets.ttf", 40))
            menu.StartGame()
            Gameover = False
        # Checks if the ball hits the wall
        if Ball1.Y >= 720:
            if Player1.collision(Ball1.X, Ball1.VelY):
                Ball1.VelY = -abs(Ball1.VelY)
        elif Ball1.Y <= 30:
            if Player2.collision(Ball1.X, Ball1.VelY):
                Ball1.VelY = abs(Ball1.VelY)
        # Checks if the player has missed the ball and changes score
        if Ball1.Y <= 0:
            Ball1.X = 200
            Ball1.Y = 350
            time.sleep(0.3)
            Score2.addscore()
        elif Ball1.Y >= 750:
            Ball1.X = 200
            Ball1.Y = 350
            time.sleep(0.3)
            Score1.addscore()
        if Score1.score == 5:
            font2 = pygame.font.Font("Caramel Sweets.ttf", 50)
            Window.blit(font2.render("Player 2 has won!! ", True, (0, 0, 0)), [25, 320])
            pygame.display.flip()
            time.sleep(2)
            Gameover = True
        if Score2.score == 5:
            font2 = pygame.font.Font("Caramel Sweets.ttf", 50)
            Window.blit(font2.render("Player 1 has won!! ", True, (0, 0, 0)), [25, 320])
            pygame.display.flip()
            time.sleep(2)
            Gameover = True
        Score1.showscore(Window)
        Score2.showscore(Window)
        Player1.moveplayer(Window)
        Player2.moveplayer(Window)
        Ball1.ballmovement(Window)
    else:
        menu.mainmenu()
        mainMenu = True
    pygame.display.update()
pygame.quit()
