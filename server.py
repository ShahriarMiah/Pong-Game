import socket
from _thread import *
import random
from Ball import BallClass
from block import Block

server = "192.168.0.10"
port = 12140
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0

ballpos = [250, 300]
ball = BallClass(ballpos[0], ballpos[1], 7, 7, 7, 45, "Left")


def read_pos(str):
    str = str.split(",")
    if len(str) == 2:
        return float(str[0]), float(str[1])
    else:
        return float(str[0]), float(str[1]), int(str[2])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


playerpos = [(200, 750), (200, 0)]

blockpos = [250, 250]


def threaded_client(conn, p):
    conn.send(str.encode(make_pos(playerpos[p])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())

            if 900 not in data:
                playerpos[p] = data

            if not data:
                break
            else:
                if 900 in data:
                    if playerpos[p][0] < ball.X < playerpos[p][1]:
                        if ball.Y > 720:
                            ball.playerCollision(playerpos[p][0])
                        elif ball.Y <=30:
                            ball.playerCollision(playerpos[p][0])
                    ball.ballmovement()
                    reply = [ball.X, ball.Y]

                else:
                    if p == 1:
                        reply = playerpos[0]
                    else:
                        reply = playerpos[1]
            conn.sendall(str.encode(make_pos(reply)))

        except:
            break

    print("Lost connection")
    conn.close()


p = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    connected.add(conn)
    start_new_thread(threaded_client, (conn, p))
    p += 1
