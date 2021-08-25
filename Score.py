import pygame


class ScoreClass:
    def __init__(self, X, Y, score, font):
        self.X = X
        self.Y = Y
        self.score = score
        self.font = font

    def showscore(self, Window):
        score_rend = self.font.render(str(self.score), True, (0, 0, 0))
        Window.blit(score_rend, (self.X, self.Y))

    def addscore(self):
        self.score += 1

    def gameover(self, Window):
        font = pygame.font.Font("Caramel Sweets.ttf", 60)
        font2 = pygame.font.Font("Caramel Sweets.ttf", 35)
        font3 = pygame.font.Font("Caramel Sweets.ttf", 22)
        Window.blit(font.render("4 Player Pong!", True, ((0, 0, 0))), [50, 300])
        Window.blit(font3.render("Use your left and right arrows to move", True, (0, 0, 0)), [60, 750])
        Window.blit(font2.render("Press[Q] to Quit ", True, (0, 0, 0)), [120, 420])
        Window.blit(font2.render("Press[R] to Play ", True, (0, 0, 0)), [120, 370])
        pygame.display.flip()
        check = True
        while check:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        pygame.quit()
                    if event.key == pygame.K_r:
                        check = False

