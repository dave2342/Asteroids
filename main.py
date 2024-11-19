import pygame
import random
from player import Player
from constants import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
import sys

def main():
	#Initialize imported pygame modules
	pygame.init()
	
	#set up the game screen with height and width
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	#set groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	Player.containers = (updatable, drawable)  
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable

	#log info
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	#create a clock object to manage screen updates
	clock = pygame.time.Clock()
	
	#delta time variable
	#dt = 0

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  

	# Create asteroids
#	NUM_ASTEROIDS = 10   # Decide how many asteroids you want
#	for _ in range(NUM_ASTEROIDS):
		# Random position and radius
#		x = random.randint(0, SCREEN_WIDTH)
#		y = random.randint(0, SCREEN_HEIGHT)
#		radius = random.randint(5, 20)  # Example range for radius

#		asteroid = Asteroid(x, y, radius)
#		asteroids.add(asteroid)


	asteroid_field = AsteroidField()

	#game loop
	while True:

		#control the loop's speed to 60fps and calculate delta time (divide by 1000 to get milliseconds)
		dt = clock.tick(60) / 1000


	#process all events in game
		for event in pygame.event.get():
			#if QUIT event(such as ctrl+c, or X in program screen, exit the game
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		#update game state
		for obj in updatable:
			obj.update(dt)

		for asteroid in asteroids:
			if player.collision(asteroid):
				print("Game over!")
				sys.exit()

		#clear screen and fill with black color
		screen.fill("black")

		#draw the screen
		for obj in drawable:
			obj.draw(screen)

		#update the display
		pygame.display.flip()

#ensures main is called only when this screen is directly executed
if __name__ == "__main__":
	main()

