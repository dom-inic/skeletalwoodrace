import sys
# the sys module to help player exit the game
# pygame module that contains the functionality to make the game

import pygame
pygame.init()

running = True
screen = pygame.display.set_mode((1000,600))
caption= pygame.display.set_caption("debug skeleton")

while running:
	# a for loop to watch for keyboard and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type  == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit()


	# make the most recently drawn screen visible
	pygame.display.flip()