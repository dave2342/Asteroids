import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

PLAYER_SHOOT_COOLDOWN = 0.3

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.timer = 0
    
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
    
	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)

	def rotate(self, dt):
		self.rotation += (PLAYER_TURN_SPEED * dt)
		self.rotation = self.rotation % 360

	def update(self, dt):
		self.timer = max(0, self.timer -dt)

		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
            # ?
			self.rotate(-dt)
		if keys[pygame.K_d]:
            # ?
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_SPACE]:
			self.shoot()

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_MOVE_SPEED * dt

	def shoot(self):
		if self.timer <= 0:
#			print(f"Ship rotation: {self.rotation}")
#			print(f"Initial velocity: {pygame.Vector2(0, -1)}")
			shot = Shot(self.position.x, self.position.y)
		#(0, 1) points down, y-axis flipped in comp graphics
			velocity = pygame.Vector2(0, 1)
#			print(f"Before rotation velocity: {velocity}")
		# negative rotation because pygame rotation is clockwise, but we want counterclockwise to flip
			velocity = velocity.rotate(self.rotation)
#			print(f"after rotation velocity: {velocity}")
			velocity *= PLAYER_SHOOT_SPEED
			shot.velocity = velocity
			self.timer = PLAYER_SHOOT_COOLDOWN

