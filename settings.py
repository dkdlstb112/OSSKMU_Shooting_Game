import pygame as pg

class Settings():
	"""A class to store all settings for game"""
	def __init__(self):
		"""Initialize the class"""
		self.windowCaption = 'Work, Slavers'
		self.screenWidth = 1280
		self.screenHeight = 720
		self.bgColor = (245, 245, 245)
		self.bg = pg.image.load("gfx/background9.png")

		#Ships speed
		self.shipLimit = 3

		#Bullet settings
		self.bulletWidth = 10
		self.bulletHeight = 25
		self.bulletColor = (60, 60, 60)

		#Alien settings
		#self.explosion = pg.image.load('gfx/explosion.gif')

		#How quickly the game speeds up
		self.speedUp = 1.2
		self.scoreSpeedUp = 1.5

		self.initDynamicSettings()

	def initDynamicSettings(self):
		self.shipSpeed = 2
		self.bulletSpeed = 9
		self.alienSpeed = 6
		self.alien2Speed = 3
		self.fleetDropSpeed = 8
		self.fleetDir = 1
		self.alienPoints = 30
		self.alien2Points = 50

	def increaseSpeed(self):
		"""Increase the speed settings"""
		#self.shipSpeed *= self.speedUp
		#self.bulletSpeed *= self.speedUp
		if self.alienSpeed <= 1.5:
			self.alienSpeed *= self.speedUp
			self.fleetDropSpeed *= self.speedUp
		self.alienPoints = int(self.alienPoints * self.scoreSpeedUp)

#	def increaseSpeed2(self):
#		"""Increase the speed settings"""
		#self.shipSpeed *= self.speedUp
		#self.bulletSpeed *= self.speedUp
#		if self.alien2Speed <= 1.5:
#			self.alien2Speed *= self.speedUp
#			self.fleetDropSpeed *= self.speedUp
#		self.alien2Points = int(self.alien2Points * self.scoreSpeedUp)