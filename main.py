import pygame
from player import Player
from constants import *

def main():
	#Initialize imported pygame modules
	pygame.init()
	
	#set up the game screen with height and width
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	#log info
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	
	#create a clock object to manage screen updates
	clock = pygame.time.Clock()
	
	#delta time variable
	dt = 0

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  
	
	#game loop
	while True:
		#process all events in game
		for event in pygame.event.get():
			#if QUIT event(such as ctrl+c, or X in program screen, exit the game
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		#clear screen and fill with black color
		screen.fill("black")

		#draw the screen
		player.draw(screen)

		#update the display
		pygame.display.flip()

	#control the loop's speed to 60fps and calculate delta time (divide by 1000 to get milliseconds)
	dt = clock.tick(60) / 1000

#ensures main is called only when this screen is directly executed
if __name__ == "__main__":
	main()

