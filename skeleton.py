import pygame

class Skeleton():

	def __init__(self, screen):
		"""initialize the skeleton and set its starting position"""
		self.screen = screen

		# load the skeleton image and get its rect.
		self.image = pygame.image.load('skeletontypeBY.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		self.speed_factor = 1.5
		self.speed_factor_right= 2

		# start each new skeleton at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""update the skeleton position based on the movement flag"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.speed_factor_right
		if self.moving_left and self.rect.left > 0:
			self.rect.centerx -= self.speed_factor




	def blitme(self):
		"""draw the skeleton at its current location"""
		self.screen.blit(self.image, self.rect)