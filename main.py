import pygame
import time
import random
import math
from Blocks import Block
from Menu import Menu
from Ball import BallClass
from Player import Player

pygame.init()
width = 1000
length = 780
Window = pygame.display.set_mode((1000, 780))
menu = Menu(Window, pygame.font.Font("Caramel Sweets.ttf", 80), pygame.font.Font("Caramel Sweets.ttf", 60),
            pygame.font.Font("Caramel Sweets.ttf", 35), pygame.font.Font("Caramel Sweets.ttf", 22))
pygame.display.set_caption("4 Player Pong")
background = pygame.image.load("Backgrounds.jpg")

counter = 0
Gameover = True
mainMenu = False
running = True
click = False
gamesPlayed = True
P1score = 0
P2score = 0
P3score = 0
P4score = 0
x = 0
y = 0
times = 0
angle = 0
power = 0
check = True
shoot = False
powerup = False
run = True
gameRunning = True
reset = True
pong_position = []
pong_pos_list = []
direction = [(0, 0), (0, 0)]
lineDrawn = False

def showscore():
    font = pygame.font.Font("Caramel Sweets.ttf", 32)
    score_rend = font.render(str(P1score), True, (255, 255, 255))
    Window.blit(score_rend, (10, 10))
    score_rend2 = font.render(str(P2score), True, (255, 255, 255))
    Window.blit(score_rend2, (10, 730))
    score_rend3 = font.render(str(P3score), True, (255, 255, 255))
    Window.blit(score_rend3, (520, 10))
    score_rend4 = font.render(str(P4score), True, (255, 255, 255))
    Window.blit(score_rend4, (520, 730))

def showscore_two():
    font = pygame.font.Font("Caramel Sweets.ttf", 32)
    score_rend = font.render(str(P1score), True, (255, 255, 255))
    Window.blit(score_rend, (10, 10))
    score_rend2 = font.render(str(P2score), True, (255, 255, 255))
    Window.blit(score_rend2, (10, 730))

if gamesPlayed:
    Player1 = Player(200, 770, 128, 32, 4, pygame.K_LEFT, pygame.K_RIGHT)
    Player2 = Player(200, 5, 128, 32, 4, pygame.K_a, pygame.K_d)
    Player3 = Player(200, 750, 128, 32, 6, pygame.K_k, pygame.K_l)
    Player4 = Player(200, 5, 128, 32, 6, pygame.K_z, pygame.K_x)
    Ball1 = BallClass(250, 300, 11, 11, 11, 45, "Left", 32)
    Ball2 = BallClass(750, 300, 11, 11, 11, 45, "Left", 32)
    block1 = Block(random.randint(64, 436), random.randint(150, 600), 64, 64, 0, 2)
    block2 = Block(random.randint(564, 936), random.randint(150, 600), 64, 64, 0, 2)
    Player1AI = Player(200, 750, 128, 32, 4, pygame.K_LEFT, pygame.K_RIGHT)
    Player2AI = Player(200, 0, 128, 32, 4, pygame.K_a, pygame.K_d)
    BallAI = BallClass(250, 300, 9, 9, 9, 45, "Left", 32)
    blockAI = Block(random.randint(64, 436), random.randint(150, 600), 64, 64, 0, 3)

#This function is used to determine the angle of projection based on the input line by the user
def findAngle(position):
    if block1.state:
        X = Ball1.X
        Y = Ball1.Y
    elif block2.state:
        X = Ball2.X
        Y = Ball2.Y
    elif blockAI.state:
        X = blockAI.X
        Y = blockAI.Y
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


clock = pygame.time.Clock()
while gameRunning:
    #The mode for the AI gor the 4 player game is determined by this selection statement
    if menu.mode == "Main":
        Window = pygame.display.set_mode((1000, 780))
        while running:
            pygame.time.delay(10)
            Window.fill((0, 0, 0))
            Window.blit(background, (0, 0))

            if mainMenu and menu.mode == "Main":
                pygame.draw.rect(Window, (255, 255, 255), (500, 0, 15, 780))
                #Checks projectile power up state
                if block1.state or block2.state:
                    powerup = True
                #This begins the power up for the projectile and contains the code for the movement
                if powerup:
                    if block1.state:
                        font1 = pygame.font.Font("Caramel Sweets.ttf", 40)
                        first = 580
                        second = 410
                    else:
                        font1 = pygame.font.Font("Caramel Sweets.ttf", 40)
                        first = 20
                        second = 410

                    Window.blit(font1.render("Projectile Power Up In Use!!", True, (255, 255, 255)), [first, second])
                    if shoot == False:
                        if block1.state:
                            if block1.player == 0:
                                Ball1.angle = -135
                                Ball1.Y = Player1.Y - 30
                                Ball1.X = Player1.X + 32
                            else:
                                Ball1.angle = 45
                                Ball1.Y = Player2.Y + 30
                                Ball1.X = Player2.X - 30
                        else:
                            if block2.player == 1:
                                Ball2.angle = -135
                                Ball2.Y = Player3.Y - 30
                                Ball2.X = Player3.X + 32
                            else:
                                Ball2.angle = 45
                                Ball2.Y = Player4.Y + 30
                                Ball2.X = Player4.X + 32

                    if shoot:
                        times += 0.05

                        if block1.state:
                            pos = Ball1.ballPath(x, y, power, angle, times)
                            Ball1.Y = pos[1]
                            Ball1.X = pos[0]
                        else:
                            pos2 = Ball2.ballPath(x, y, power, angle, times)
                            Ball2.Y = pos2[1]
                            Ball2.X = pos2[0]

                    position = pygame.mouse.get_pos()
                    if block1.state:
                        line = [(Ball1.X + 16, Ball1.Y + 16), position]
                    else:
                        line = [(Ball2.X + 16, Ball2.Y + 16), position]

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if shoot == False:
                                shoot = True
                                if block1.state:
                                    x = Ball1.X
                                    y = Ball1.Y
                                else:
                                    x = Ball2.X
                                    y = Ball2.Y
                                times = 0
                                power = math.sqrt((line[1][1] - line[0][1]) ** 2 + (line[1][0] - line[0][0]) ** 2) / 3
                                angle = findAngle(position)
                    #Resets all values back to original for next use of power up
                    if block1.state:
                        if Ball1.X >= 468 or Ball1.X <= 32 or Ball1.Y <= 0 or Ball1.Y >= 780:
                            block1.state = False
                            block1.checkHits = 0
                            block1.Choice = random.randint(0, 2)
                            block1.player = random.randint(0, 1)
                            powerup = False
                            x = 0
                            y = 0
                            times = 0
                            angle = 0
                            power = 0
                            check = True
                            shoot = False
                    else:
                        if Ball2.X >= 968 or Ball2.X <= 532 or Ball2.Y <= 0 or Ball2.Y >= 780:
                            block2.state = False
                            block2.checkHits = 0
                            block2.Choice = random.randint(0, 2)
                            block1.player = random.randint(0, 1)
                            powerup = False
                            x = 0
                            y = 0
                            times = 0
                            angle = 0
                            power = 0
                            check = True
                            shoot = False
                    pygame.draw.line(Window, (255, 255, 255), line[0], line[1])
                    if block1.state:
                        Ball1.draw(Window)
                    else:
                        Ball2.draw(Window)


                else:
                    angle = math.degrees(angle)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                    if check:
                        if Ball1.Y <= 20 and angle > 90:
                            Ball1.angle = 315
                        elif Ball1.Y <= 20 and angle < 90:
                            Ball1.angle = -315
                    if Ball1.Y >= 20 or Ball2.Y >= 20:
                        check = False

                    if Ball1.X <= 500 and Ball1.X >= 0 or Ball2.X <= 500 and Ball2.X >= 0:
                        check = False

                    key = pygame.key.get_pressed()
                    if key[pygame.K_p]:
                        menu.pause()
                    #Restes all players and objects for a new game
                    if Gameover:
                        Player1 = Player(200, 750, 128, 32, 6, pygame.K_LEFT, pygame.K_RIGHT)
                        Player2 = Player(200, 5, 128, 32, 6, pygame.K_a, pygame.K_d)
                        Player3 = Player(700, 750, 128, 32, 6, pygame.K_k, pygame.K_l)
                        Player4 = Player(700, 5, 128, 32, 6, pygame.K_z, pygame.K_x)
                        Ball1 = BallClass(250, 300, 9,9,9, 45, "Left", 32)
                        Ball2 = BallClass(750, 300, 9,9,9, 45, "Left", 32)
                        block1 = Block(random.randint(64, 436), random.randint(150, 600), 64, 64, 2, 3, )
                        block2 = Block(random.randint(564, 936), random.randint(150, 600), 64, 64, 2, 3, )
                        gamesPlayed = False
                        reset = True
                        menu.StartGame()
                        Gameover = False

                    #Increments score if user loses
                    if Ball1.Y <= 0:
                        P2score += 1
                    elif Ball1.Y + 32 >= 780:
                        P1score += 1
                    if Ball2.Y <= 0:
                        P4score += 1
                    elif Ball2.Y + 32 >= 780:
                        P3score += 1
                    # Checks if the ball hits paddle and if magnet is activated to determine which movement
                    if Player1.X < Ball1.X < Player1.X + Player1.Width:
                        if block1.magnet:
                            if Ball1.Y >= 680:
                                block1.magnet = False
                                block1.checkHits = 0
                                block1.Choice = random.randint(0, 4)
                        Ball1.playerCollision(Player1, Player2)

                    elif Player2.X < Ball1.X < Player2.X + Player2.Width:
                        if block1.magnet:
                            if Ball1.Y <= 30:
                                block1.magnet = False
                                block1.checkHits = 0
                                block1.Choice = random.randint(0, 4)
                        Ball1.playerCollision(Player1, Player2)

                    if Player3.X < Ball2.X < Player3.X + Player3.Width:
                        if block2.magnet:
                            if Ball2.Y >= 680:
                                block2.magnet = False
                                block2.checkHits = 0
                                block2.Choice = random.randint(0, 4)
                        Ball2.playerCollision(Player3, Player4)

                    elif Player4.X < Ball2.X < Player4.X + Player4.Width:
                        if block2.magnet:
                            if Ball2.Y <= 30:
                                block2.magnet = False
                                block2.checkHits = 0
                                block2.Choice = random.randint(0, 4)
                        Ball2.playerCollision(Player3, Player4)
                    #Block collision
                    if block1.checkHits < 3:
                        if block1.Y < Ball1.Y < block1.Y + 62:
                            block1.blockCollision("B1")
                    if block2.checkHits < 3:
                        if block2.Y < Ball2.Y < block2.Y + 62:
                            block2.blockCollision("B2")
                    #End of game and resets all values
                    if P1score == 15:
                        font2 = pygame.font.Font("Caramel Sweets.ttf", 50)
                        Window.blit(font2.render("Player 2 has won!! ", True, (255, 255, 255)), [25, 320])
                        pygame.display.flip()
                        time.sleep(2)
                        P2score = 0
                        P1score = 0
                        P3score = 0
                        P4score = 0
                        block1.checkHits = 0
                        block2.checkHits = 0
                        Gameover = True
                    if P2score == 15:
                        font2 = pygame.font.Font("Caramel Sweets.ttf", 50)
                        Window.blit(font2.render("Player 1 has won!! ", True, (255, 255, 255)), [25, 320])
                        pygame.display.flip()
                        time.sleep(2)
                        P2score = 0
                        P1score = 0
                        P3score = 0
                        P4score = 0
                        block1.checkHits = 0
                        block2.checkHits = 0
                        Gameover = True
                    if P3score == 15:
                        font2 = pygame.font.Font("Caramel Sweets.ttf", 50)
                        Window.blit(font2.render("Player 3 has won!! ", True, (255, 255, 255)), [525, 320])
                        pygame.display.flip()
                        time.sleep(2)
                        P2score = 0
                        P1score = 0
                        P3score = 0
                        P4score = 0
                        block1.checkHits = 0
                        block2.checkHits = 0
                        Gameover = True
                    if P4score == 15:
                        font2 = pygame.font.Font("Caramel Sweets.ttf", 50)
                        Window.blit(font2.render("Player 4 has won!! ", True, (255, 255, 255)), [525, 320])
                        pygame.display.flip()
                        time.sleep(2)
                        P2score = 0
                        P1score = 0
                        P3score = 0
                        P4score = 0
                        block1.checkHits = 0
                        block2.checkHits = 0
                        Gameover = True

                    #Checks if magnet power up is activated else normal movement of ball is used
                    if block1.magnet:
                        if block1.player == 0:
                            Ball1.magnetmovement(Player1,"B1")
                        else:
                            Ball1.magnetmovement(Player2,"B1")
                    if block2.magnet:
                        if block2.player == 0:
                            Ball2.magnetmovement(Player3,"B2")
                        else:
                            Ball2.magnetmovement(Player4,"B2")
                    else:
                        Ball1.ballmovement(Window, 0, 510)
                        Ball2.ballmovement(Window, 515, 1000)
                    block1.showBlock(Window, "B1")
                    block2.showBlock(Window, "B2", )

            else:
                #Starts main menu
                menu.mainmenu()
                mainMenu = True
                if menu.mode != "Main":
                    break
            showscore()
            Player1.moveplayer(Window, "p1")
            Player2.moveplayer(Window, "p1")
            Player3.moveplayer(Window, "p2")
            Player4.moveplayer(Window, "p2")
            pygame.display.update()




    #Checks if AI mode is chosen
    elif menu.mode == "AI":
        Window = pygame.display.set_mode((500, 780))
        mainMenu = True
        while run:
            if mainMenu:
                pygame.time.delay(10)
                Window.fill((0, 0, 0))
                Window.blit(background, (0, 0))

                if blockAI.state:
                    powerup = True
                #Projectile power up is actiavted
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
                    #Cehcks is player has shot the power up
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
                    #Resumes normal motion after power up activated
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

                    pygame.draw.line(Window, (255, 255, 255), line[0], line[1])
                    BallAI.draw(Window)

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

                    #Collision with paddle
                    if Player1AI.X < BallAI.X < Player1AI.X + Player1AI.Width:
                        BallAI.playerCollision(Player1AI, Player2AI)
                        lineDrawn = False
                    elif Player2AI.X < BallAI.X < Player2AI.X + Player2AI.Width:
                        BallAI.playerCollision(Player1AI, Player2AI)
                        lineDrawn = False

                    #Player loses point
                    if BallAI.Y <= 0:
                        P2score += 1
                    elif BallAI.Y + 32 >= 780:
                        P1score += 1

                    #Block collision
                    if blockAI.checkHits < 3:
                        if blockAI.Y < BallAI.Y < blockAI.Y + 62:
                            blockAI.blockCollision("B3")

                    #Gameover, values reset
                    if Gameover:
                        Player1AI = Player(200, 750, 128, 32, 4, pygame.K_LEFT, pygame.K_RIGHT)
                        Player2AI = Player(200, 0, 128, 32, 4, pygame.K_a, pygame.K_d)
                        BallAI = BallClass(250, 300, 9, 9, 9, 45, "Left", 32)
                        blockAI = Block(random.randint(64, 436), random.randint(150, 600), 64, 64, 0, 3)
                        gamesPlayed = False
                        reset = True
                        Gameover = False
                        if counter != 0:
                            counter += 1
                            mainMenu = False
                    #Gameover,values reset
                    if P1score == 5:
                        font2 = pygame.font.Font("Caramel Sweets.ttf", 50)
                        Window.blit(font2.render("Player 1 has won!! ", True, (255, 255, 255)), [25, 320])
                        pygame.display.flip()
                        blockAI.checkHits = 0
                        mainMenu = False
                        Window = pygame.display.set_mode((1000, 780))
                        P1score = 0
                    if P2score == 5:
                        font2 = pygame.font.Font("Caramel Sweets.ttf", 50)
                        Window.blit(font2.render("Player 2 has won!! ", True, (255, 255, 255)), [25, 320])
                        blockAI.checkHits = 0
                        pygame.display.flip()
                        mainMenu = False
                        P2score = 0
                        Window = pygame.display.set_mode((1000, 780))

                    #AI movement algorithm
                    pong_position = [BallAI.X, BallAI.Y]
                    if not lineDrawn:
                        if len(pong_position) > 0:
                            pong_pos_list.append(pong_position)
                            if len(pong_pos_list) >= 2:
                                if menu.difficulty == "Hard":
                                    direction = BallAI.get_trajectory(pong_pos_list, pong_position[0], pong_position[1],Player1AI)
                                else:
                                    direction = BallAI.get_direction(pong_pos_list, pong_position[0], pong_position[1])

                                pong_pos_list = []
                                lineDrawn = True
                    if lineDrawn and (BallAI.Y <= 0 or BallAI.Y >= 780 or BallAI.X <= 0 or BallAI.X >= 490):
                        lineDrawn = False

                    #Checks magnet power up
                    if blockAI.magnet:
                        if blockAI.player == 0:
                            BallAI.magnetmovement(Player1AI, "B3")
                        else:
                            BallAI.magnetmovement(Player2AI, "B3")
                    BallAI.ballmovement(Window, 0, 500)
                    blockAI.showBlock(Window, "B3")
            else:
                #Menu in use
                menu.mainmenu()
                if menu.mode == "Main":
                    Gameover = True
                run = True
                counter = 0
                break
            showscore_two()
            Player1AI.moveplayer(Window, "p1")
            #Determines diffiuclty of AI
            if menu.difficulty == "Easy":
                Player2AI.AI_one(Window,pygame.time.get_ticks())
            elif menu.difficulty == "Medium":
                Player2AI.AI_two(direction,Window)
            else:
                Player2AI.AI_three(direction, Window)
            pygame.display.update()

pygame.quit()
