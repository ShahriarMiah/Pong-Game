import pygame


class Menu:
    def __init__(self, Window, font, font1, font2, font3):
        self.Window = Window
        self.font = font
        self.font1 = font1
        self.font2 = font2
        self.font3 = font3
        self.difficulty = "Easy"
        self.mode = "Main"
    def mainmenu(self):
        meow = True
        Clicked = False
        check = False
        counter = 0

        while meow:
            self.Window.blit(pygame.image.load("Backgrounds.jpg"), (0, 0))
            self.Window.blit(self.font1.render("4 Player Pong!", True, (255, 255, 255)), [280, 50])
            mx, my = pygame.mouse.get_pos()

            if not check:
                option1 = pygame.draw.rect(self.Window, (255, 255, 255), (370, 200, 250, 75), 3)
                option2 = pygame.draw.rect(self.Window, (255, 255, 255), (370, 300, 250, 75), 3)
                option3 = pygame.draw.rect(self.Window, (255, 255, 255), (370, 400, 250, 75), 3)
                option4 = pygame.draw.rect(self.Window, (255, 255, 255), (370, 500, 250, 75), 3)
                self.Window.blit(self.font1.render("1 v 1", True, (255, 255, 255)), [425, 210])
                self.Window.blit(self.font1.render("4-Player", True, (255, 255, 255)), [385, 310])
                self.Window.blit(self.font1.render("Options", True, (255, 255, 255)), [395, 410])
                self.Window.blit(self.font1.render("Quit", True, (255, 255, 255)), [440, 510])
                self.Window.blit(pygame.image.load("sound.png"), (10, 710))
            else:
                self.Window.blit(pygame.image.load("Backgrounds.jpg"), (0, 0))
                option5 = pygame.draw.rect(self.Window, (255, 255, 255), (370, 200, 250, 75), 3)
                option6 = pygame.draw.rect(self.Window, (255, 255, 255), (370, 300, 250, 75), 3)
                option7 = pygame.draw.rect(self.Window, (255, 255, 255), (370, 400, 250, 75), 3)
                self.Window.blit(self.font1.render("Easy", True, (255, 255, 255)), [425, 210])
                self.Window.blit(self.font1.render("Medium", True, (255, 255, 255)), [385, 310])
                self.Window.blit(self.font1.render("Hard", True, (255, 255, 255)), [395, 410])
                self.Window.blit(self.font1.render("Quit", True, (255, 255, 255)), [440, 510])

            if not check:
                if option1.collidepoint(mx, my):
                    if Clicked:
                        check = True
                        Clicked = False
                        self.mode = "AI"
                elif option2.collidepoint(mx, my):
                    if Clicked:
                        self.mode = "Main"
                        Clicked = False
                        meow = False
                        self.StartGame()
                elif option3.collidepoint(mx, my):
                    if Clicked:
                        pass
                elif option4.collidepoint(mx, my):
                    if Clicked:
                        pygame.quit()
            else:
                if option5.collidepoint(mx, my):
                    if Clicked:
                        self.difficulty = "Easy"
                        Clicked = False
                        check = False
                        self.mode = "AI"
                        break
                elif option6.collidepoint(mx, my):
                    if Clicked:
                        Clicked = False
                        check = False
                        self.mode = "AI"
                        self.difficulty = "Medium"
                        break
                elif option7.collidepoint(mx, my):
                    if Clicked:
                        Clicked = False
                        check = False
                        self.mode = "AI"
                        self.difficulty = "Hard"
                        break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        Clicked = True
            pygame.display.update()

    def StartGame(self):
        self.Window.fill((255, 255, 255))
        self.Window.blit(pygame.image.load("Backgrounds.jpg"), (0, 0))
        self.Window.blit(self.font.render("1 V 1", True, (255, 255, 255)), [400, 200])
        self.Window.blit(self.font3.render("Use your left and right arrows to move", True, (255, 255, 255)), [290, 750])
        self.Window.blit(self.font2.render("Press[Q] to Quit ", True, (255, 255, 255)), [370, 420])
        self.Window.blit(self.font2.render("Press[R] to Play ", True, (255, 255, 255)), [370, 370])
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

