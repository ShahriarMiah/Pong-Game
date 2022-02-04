import pygame
import time
import random
from Player import Player
from Ball import BallClass
from Blocks import Block
import math

pygame.init()
Window2 = pygame.display.set_mode((500, 780))
P1score = 0
P2score = 0
Player1AI = Player(200, 750, 128, 32, 4, pygame.K_LEFT, pygame.K_RIGHT)
Player2AI = Player(200, 0, 128, 32, 4, pygame.K_a, pygame.K_d)
BallAI = BallClass(250, 300, 7, 7, 7, 45, "Left", 32)
blockAI = Block(random.randint(64, 436), random.randint(150, 600), 64, 64, 0, 3)
background = pygame.image.load("Backgrounds.jpg")
pong_position = []
pong_pos_list = []
direction = [(0, 0), (0, 0)]
lineDrawn = False
x = 0
y = 0
times = 0
angle = 0
power = 0
check = True
shoot = False
powerup = False
reset = True


def findAngle(position):
    X = BallAI.X
    Y = BallAI.Y

    try:
        angle = math.atan((Y - position[1]) / (X - position[0]))
    except:
        angle = math.pi / 2

    if position[1] < Y and position[0] > X:
        angle = abs(angle)
    elif position[1] < Y and position[0] < X:
        angle = math.pi - angle
    elif position[1] > Y and position[0] < X:
        angle = math.pi + abs(angle)
    elif position[1] > Y and position[0] > X:
        angle = (math.pi * 2) - angle

    return angle


def showscore():
    font = pygame.font.Font("Caramel Sweets.ttf", 32)
    score_rend = font.render(str(P1score), True, (255, 255, 255))
    Window2.blit(score_rend, (10, 10))
    score_rend2 = font.render(str(P2score), True, (255, 255, 255))
    Window2.blit(score_rend2, (10, 730))


run = True
while run:
    pygame.time.delay(10)
    Window2.fill((0, 0, 0))
    Window2.blit(background, (0, 0))

    if blockAI.state:
        powerup = True
    if powerup:

        if shoot == False:
            if blockAI.player == 0:
                BallAI.angle = -135
                BallAI.Y = Player1AI.Y - 30
                BallAI.X = Player1AI.X + 32
                p1 = False
            elif blockAI.player == 1:
                BallAI.angle = 45
                BallAI.Y = Player2AI.Y + 30
                BallAI.X = Player2AI.X - 30
                p1 = True

        if shoot:
            times += 0.05
            pos = BallAI.ballPath(x, y, power, angle, times)
            BallAI.Y = pos[1]
            BallAI.X = pos[0]

        position = pygame.mouse.get_pos()

        line = [(BallAI.X + 16, BallAI.Y + 16), position]

        if p1:
            randomIntX = random.randint(10, 480)
            randomIntY = random.randint(40, 700)
            position = (randomIntX, randomIntY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN or p1:
                if not shoot:
                    shoot = True
                    x = BallAI.X
                    y = BallAI.Y
                    times = 0
                    power = math.sqrt((line[1][1] - line[0][1]) ** 2 + (line[1][0] - line[0][0]) ** 2) / 3
                    angle = findAngle(position)

        if BallAI.X >= 460 or BallAI.X <= 32 or BallAI.Y <= 0 or BallAI.Y >= 780:
            blockAI.state = False
            blockAI.checkHits = 0
            blockAI.Choice = random.randint(0, 2)
            blockAI.player = random.randint(0, 1)
            powerup = False
            x = 0
            y = 0
            times = 0
            angle = 0
            power = 0
            check = True
            shoot = False

        pygame.draw.line(Window2, (255, 255, 255), line[0], line[1])
        BallAI.draw(Window2)



    else:
        angle = math.degrees(angle)
        if check:
            if BallAI.Y <= 20 and angle > 90:
                BallAI.angle = 315
            elif BallAI.Y >= 760 and angle < 90:
                BallAI.angle = -315
        if BallAI.Y >= 20 or BallAI.Y >= 20:
            check = False

        if BallAI.X <= 500 and BallAI.X >= 0:
            check = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if Player1AI.X < BallAI.X < Player1AI.X + Player1AI.Width:
            BallAI.playerCollision(Player1AI, Player2AI)
            lineDrawn = False
        elif Player2AI.X < BallAI.X < Player2AI.X + Player2AI.Width:
            BallAI.playerCollision(Player1AI, Player2AI)
            lineDrawn = False
        if BallAI.Y <= 0:
            P2score += 1
        elif BallAI.Y + 32 >= 780:
            P1score += 1
        if blockAI.checkHits < 3:
            if blockAI.Y < BallAI.Y < blockAI.Y + 62:
                blockAI.blockCollision("B3")

        if P1score == 15:
            font2 = pygame.font.Font("Caramel Sweets.ttf", 50)
            Window2.blit(font2.render("Player 1 has won!! ", True, (255, 255, 255)), [25, 320])
            pygame.display.flip()
            time.sleep(3)
            pygame.quit()
        if P2score == 15:
            font2 = pygame.font.Font("Caramel Sweets.ttf", 50)
            Window2.blit(font2.render("Player 2 has won!! ", True, (255, 255, 255)), [25, 320])
            time.sleep(3)
            pygame.display.flip()
            pygame.quit()
        pong_position = [BallAI.X, BallAI.Y]
        if not lineDrawn:
            if len(pong_position) > 0:
                pong_pos_list.append(pong_position)
                if len(pong_pos_list) >= 2:
                    direction = BallAI.get_direction(pong_pos_list, pong_position[0], pong_position[1])
                    pong_pos_list = []
                    lineDrawn = True
        if lineDrawn and (BallAI.Y <= 0 or BallAI.Y >= 780 or BallAI.X <= 0 or BallAI.X >= 490):
            lineDrawn = False

        if blockAI.magnet:
            if blockAI.player == 0:
                BallAI.magnetmovement(Player1AI, "B3")
            else:
                BallAI.magnetmovement(Player2AI, "B3")
        BallAI.ballmovement(Window2, 0, 500)
        blockAI.showBlock(Window2, "B3")
    showscore()
    Player1AI.moveplayer(Window2, "p1")
    Player2AI.Improved_AI_movement(direction, Window2)
    pygame.display.update()
