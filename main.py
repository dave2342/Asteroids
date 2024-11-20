import pygame
import random
from player import Player
from constants import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import sys

def main():
	#Initialize imported pygame modules
	pygame.init()
	
	#set up the game screen with height and width
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	#create a clock object to manage screen updates                                                                        
	clock = pygame.time.Clock() 	

	#set groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable) 
	Player.containers = (updatable, drawable)  
	AsteroidField.containers = updatable
	Shot.containers = (shots, updatable, drawable)

	asteroid_field = AsteroidField()

	#log info
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  
	
	dt = 0

	#game loop
	while True:

		#control the loop's speed to 60fps and calculate delta time (divide by 1000 to get milliseconds)
#		dt = clock.tick(60) / 1000


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
			for shot in shots:
				if asteroid.collision(shot):
					asteroid.split()
					shot.kill()

		#clear screen and fill with black color
		screen.fill("black")

		#draw the screen
		for obj in drawable:
			obj.draw(screen)

		#update the display
		pygame.display.flip()

		dt = clock.tick(60) / 1000

#ensures main is called only when this screen is directly executed
if __name__ == "__main__":
	main()

