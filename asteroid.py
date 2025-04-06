import pygame
from circleshape import CircleShape
from constants import *
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
        
        ast_angle = random.uniform(20, 50)
        
        ast_1_velo = self.velocity.rotate(ast_angle)
        ast_2_velo = self.velocity.rotate(-ast_angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        
        new_ast_1 = Asteroid(self.position.x, self.position.y, new_rad)
        new_ast_2 = Asteroid(self.position.x, self.position.y, new_rad)
        new_ast_1.velocity = (ast_1_velo * 1.2)
        new_ast_2.velocity = (ast_2_velo * 1.2)