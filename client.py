import pygame
import random
from Player import Player
from Ball import BallClass
from block import Block
from network import Network

pygame.font.init()

width = 500
height = 780
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

player2 = Player(200, 0, 128, 32, 4, pygame.K_LEFT, pygame.K_RIGHT)
ball = BallClass(250, 300, 7, 7, 7, 45, "Left")
block = Block(300, 300, 64, 64, 0, random.randint(0, 1))

def read_pos(str):
    str = str.split(",")
    return float(str[0]), float(str[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def makepos2(tup):
    return str(tup[0]) + "," + str(tup[1]) + "," + str(tup[2])


def redrawWindow(win, p, p2, ball,block):
    win.fill((128, 128, 128))
    p.draw(win)
    p2.draw(win)
    ball.draw(win)
    block.showBlock(win)
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    startPos = read_pos(n.getP())
    player = Player(startPos[0], startPos[1], 128, 32, 4, pygame.K_LEFT, pygame.K_RIGHT)
    while run:
        clock.tick(60)
        p2pos = read_pos(n.send(make_pos((player.X, player.Y))))
        player2.X, player2.Y = p2pos[0], p2pos[1]

        ballpos = read_pos(n.send(makepos2((ball.X, ball.Y, 900))))
        ball.X, ball.Y = ballpos[0], ballpos[1]

        # blockpos = read_pos(n.send(makepos2((block.X,block.Y,1000))))
        # block.X,block.Y = blockpos[0],blockpos[1]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        if player2.X < ball.X < player2.X + player2.Length:
            if ball.Y > 720:
                ball.angle = ball.playerCollision(player2.X)
        redrawWindow(win, player, player2, ball,block)
        player.moveplayer(win)


main()
