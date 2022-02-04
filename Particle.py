import pygame, random


class Particle:
    def __init__(self):
        self.particles = []
        self.update = "Nyan"
        self.size = 8

    def emit(self,screen):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                if self.update != "Nyan":
                    particle[0][1] += particle[2][1]
                    particle[0][0] += particle[2][0]
                    particle[1] -= 0.2

                if self.update == "Circles":
                    pygame.draw.circle(screen, pygame.Color('White'), particle[0], int(particle[1]))
                elif self.update == "Rectangles":
                    pygame.draw.rect(screen, (255, 255, 255),
                                     (particle[0][0], particle[0][1], int(particle[1]) + 8, int(particle[1]) + 8))

                else:
                    particle[0].x -=2
                    pygame.draw.rect(screen, particle[1], particle[0])


    def add_particles(self, offset, colour,ball):
        if self.update != "Nyan":
            x = ball.X + 16
            y = ball.Y + 16
            radius = 10
            directionx = random.uniform((-1 * ball.VelX) - 4, (-1 * ball.VelX) + 4)
            directiony = random.uniform((-1 * ball.VelY) - 4, (-1 * ball.VelY) + 4)
            particle_circle = [[x, y], radius, [directionx, directiony]]
            self.particles.append(particle_circle)
        else:

            x = ball.X +16
            y = ball.Y + offset
            particle_rect = pygame.Rect(int(x - self.size / 2), int(y - self.size / 2), self.size, self.size)
            self.particles.append((particle_rect, colour))

    def delete_particles(self):
        if self.update != "Nyan":
            particle_copy = [particle for particle in self.particles if particle[1] > 0]
        else:
            particle_copy = [particle for particle in self.particles if particle[0].x > 0]

        self.particles = particle_copy