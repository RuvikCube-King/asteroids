from circleshape import *
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(angle)
            vel2 = self.velocity.rotate(-angle)
            rad = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position.x, self.position.y, rad)
            ast2 = Asteroid(self.position.x, self.position.y, rad)
            ast1.velocity = vel1 * 1.2
            ast2.velocity = vel2 * 1.2
            return