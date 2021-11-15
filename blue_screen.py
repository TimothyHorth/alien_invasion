import sys

import pygame

from mario import Mario

class Blue:
	"""Create a Pygame window with a blue background."""
	def __init__(self):
		"""Initialize a blue background."""
		pygame.init()
		self.screen = pygame.display.set_mode((1200,800))

	def run_game(self):
		"""Run the game."""
		while True:
			for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()

			self.screen.fill((46, 58, 246))

			self.screen_rect = self.screen.get_rect()
			image = pygame.image.load('images/mario.bmp')
			rect = image.get_rect()
			rect.center = self.screen_rect.center

			self.screen.blit(image, rect)

			pygame.display.flip()

			

if __name__ == '__main__':
	blu_background = Blue()
	blu_background.run_game()