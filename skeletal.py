# the sys module to help exit the game
import  sys
import pygame 
from skeleton import Skeleton


def run_game():
	# initialize the game and create a screen object using the pygame class. we create an instance screen
	pygame.init()
	screen= pygame.display.set_mode((1000,600))
	caption=pygame.display.set_caption("skeleton on wood race")
	# set the background colour
	bg_color =(255,255,0)
	# create an instance of skeleton
	skeleton = Skeleton(screen)

	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					sys.exit()
				if event.key == pygame.K_RIGHT:
					# move the skeleton to the right
					skeleton.moving_right = True
				if event.key == pygame.K_LEFT:
					skeleton.moving_left = True

			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					skeleton.moving_right = False
				if event.key == pygame.K_LEFT:
					skeleton.moving_left = False

		skeleton.update()
		# redraw the screen during each pass through the loop
		screen.fill(bg_color)
		skeleton.blitme()
		# make the most recently drawn screen visible
		pygame.display.flip()
		

run_game()