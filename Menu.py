import pygame


class Menu:
    def __init__(self, Window, font, font1, font2, font3):
        self.Window = Window
        self.font = font
        self.font1 = font1
        self.font2 = font2
        self.font3 = font3

    def mainmenu(self):
        meow = True
        Clicked = False
        while meow:
            self.Window.blit(self.font1.render("4 Player Pong!", True, (255, 255, 255)), [50, 50])
            mx, my = pygame.mouse.get_pos()
            option1 = pygame.draw.rect(self.Window, (255, 255, 255), (120, 200, 250, 75), 3)
            option2 = pygame.draw.rect(self.Window, (255, 255, 255), (120, 300, 250, 75), 3)
            option3 = pygame.draw.rect(self.Window, (255, 255, 255), (120, 400, 250, 75), 3)
            option4 = pygame.draw.rect(self.Window, (255, 255, 255), (120, 500, 250, 75), 3)
            self.Window.blit(self.font1.render("1 v 1", True, (255, 255, 255)), [175, 210])
            self.Window.blit(self.font1.render("4-Player", True, (255, 255, 255)), [135, 310])
            self.Window.blit(self.font1.render("Options", True, (255, 255, 255)), [145, 410])
            self.Window.blit(self.font1.render("Quit", True, (255, 255, 255)), [190, 510])
            self.Window.blit(pygame.image.load("sound.png"), (10,710))
            if option1.collidepoint(mx, my):
                if Clicked:
                    self.StartGame()
                    meow = False
            if option2.collidepoint(mx, my):
                if Clicked:
                    pass
            if option3.collidepoint(mx, my):
                if Clicked:
                    self.mainmenu()
            if option4.collidepoint(mx, my):
                if Clicked:
                    pygame.quit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        Clicked = True
            pygame.display.update()

    def StartGame(self):
        self.Window.fill((255, 255, 255))
        self.Window.blit(pygame.image.load("Backgrounds.jpg"), (-50, -65))
        self.Window.blit(self.font.render("1 V 1", True, (255, 255, 255)), [150, 200])
        self.Window.blit(self.font3.render("Use your left and right arrows to move", True, (255, 255, 255)), [40, 750])
        self.Window.blit(self.font2.render("Press[Q] to Quit ", True, (255, 255, 255)), [120, 420])
        self.Window.blit(self.font2.render("Press[R] to Play ", True, (255, 255, 255)), [120, 370])
        pygame.display.flip()
        check = True
        while check:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_r:
                        check = False
                    if event.key == pygame.K_q:
                        self.Window.blit(pygame.image.load("Backgrounds.jpg"), (-50, -65))
                        self.mainmenu()


    def pause(self):
        self.Window.blit(self.font1.render("Game Paused", True, (255, 255, 255)), [80, 300])
        self.Window.blit(self.font2.render("Press[Q] to Quit ", True, (255, 255, 255)), [120, 420])
        self.Window.blit(self.font2.render("Press[R] to Continue ", True, (255, 255, 255)), [100, 370])
        pygame.display.flip()
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        pygame.quit()
                    if event.key == pygame.K_r:
                        pause = False
