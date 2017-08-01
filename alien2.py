import pygame as pg
from pygame.sprite import Sprite
from time import sleep



class Alien2(Sprite):
	"""A class to represent a single alien in the fleet"""
	def __init__(self, setting, screen):
		"""Initialize the alien and set its starting point"""
		super(Alien2, self).__init__()
		self.screen = screen
		self.setting = setting

		#load the alien image and set its rect attribute
		self.image = pg.image.load('gfx/ae.png')
		self.rect = self.image.get_rect()
		

		#start each new alien near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#store the aliens exact position
		self.x = float(self.rect.x)

		#timer for shooting
		self.timer = 0

	def checkEdges(self):
		"""Returns True if alien is at the edge of screen"""
		screenRect = self.screen.get_rect()
		if self.rect.right >= screenRect.right:
			return True
		elif self.rect.left <= 0:
			return True


	def update(self, setting, screen, ship, aliens2):
		"""Move the alien right or left"""
		self.ship = ship
		self.aliens2 = aliens2
		self.x += (self.setting.alien2Speed * self.setting.fleetDir)
		self.rect.x = self.x			

	def blitme(self):
		"""draw hte alien"""
		self.screen.blit(self.image, self.rect)