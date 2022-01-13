import pygame
from Player import Player
from Ball import BallClass

Window = pygame.display.set_mode((500, 780))

Player1 = Player(200, 750, 128, 32, 4, pygame.K_LEFT, pygame.K_RIGHT,False)
Player2 = Player(200, 0, 128, 32, 4, pygame.K_a, pygame.K_d,False)
BallAI = BallClass(250, 300, 7, 7, 7, 45, "Left", 32)
background = pygame.image.load("Backgrounds.jpg")

run = True
while run:
    pygame.time.delay(10)
    Window.fill((0, 0, 0))
    Window.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if Player1.X < BallAI.X < Player1.X + Player1.Width:
        BallAI.playerCollision(Player1, Player2)
    elif Player2.X < BallAI.X < Player2.X + Player2.Width:
        BallAI.playerCollision(Player1, Player2)

    Player1.moveplayer(Window, "p1")
    Player2.AImovement(Window)
    BallAI.ballmovement(Window, 0, 500)
    pygame.display.update()
