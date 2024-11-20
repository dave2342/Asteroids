import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)
	
	def update(self, dt):
		self.position += self.velocity * dt

	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			#self.kill()
			return
		else:
			random_angle = random.uniform(20,50)

			rotate_new_pos = self.velocity.rotate(random_angle)
			rotate_new_neg = self.velocity.rotate(-random_angle)

			new_radius = self.radius - ASTEROID_MIN_RADIUS

			new_ast_1 = Asteroid(self.position, self.position.y, new_radius)
			new_ast_1.velocity = rotate_new_pos * 1.2
			new_ast_1.add(self.groups())

			new_ast_2 = Asteroid(self.position, self.position.y, new_radius)
			new_ast_2.velocity = rotate_new_neg * 1.2
			new_ast_2.add(self.groups())
			#self.kill() 
