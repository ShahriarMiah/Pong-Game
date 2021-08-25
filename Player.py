import pygame


class Player:
    def __init__(self, X, Y, Width, Vel, Key1, Key2):
        self.X = X
        self.Y = Y
        self.Width = Width
        self.Vel = Vel
        self.Key1 = Key1
        self.Key2 = Key2

    def moveplayer(self, Window):
        Window.blit(pygame.image.load("Player.png"), (self.X, self.Y))
        keys = pygame.key.get_pressed()
        if keys[self.Key1] and self.X > self.Vel - 5:
            self.X -= self.Vel
        if keys[self.Key2] and self.X < 371:
            self.X += self.Vel

    def collision(self, X, velY):
        if self.X < X < self.X + self.Width:
            return True
Player1 = Player(200, 699, 128, 4, pygame.K_LEFT, pygame.K_RIGHT)
Player2 = Player(200, -44, 128, 4, pygame.K_a, pygame.K_d)