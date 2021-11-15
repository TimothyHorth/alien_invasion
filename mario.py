class Mario:
	"""Draw Mario into the game window."""
	def __init__(self):
		"""Draw Mario."""
		self.screen_rect = self.screen.get_rect()
		self.image = pygame.image.load('images/Mario.jpg')
		self.rect = self.image.get_rect()
		self.rect.center = self.screen.rect.center