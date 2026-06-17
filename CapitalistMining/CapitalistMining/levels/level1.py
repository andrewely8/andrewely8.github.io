
import pygame
from sprites import *
from utils import *
import sys,math,random
from .levelMaps import levelMap0

class Level1:
	def __init__(self,currentLevel):
		self.currentLevel = currentLevel
		self.scrollSpeed = 2
		self.checkStopScrolling = False
		self.all_backgrounds = pygame.sprite.Group()
		self.all_floors = pygame.sprite.Group()
		self.bottom_floors = pygame.sprite.Group()
		for i, row in enumerate(levelMap0):
			currentY = 4 + (i * 32)
			for j, block in enumerate(row):
				currentX = 8+ (j * 32)
				if block == 'p':
					self.player = Player(currentX,currentY)
				if block == 'b':
					new_floor = floorBlock(currentX, currentY)
					self.all_floors.add(new_floor)
				if block == 'e':
					new_floor = bottomFloorBlock(currentX, currentY)
					self.bottom_floors.add(new_floor)
				if block == 'f':
					self.finish = FinishBlock(currentX, currentY)
		self.background1 = Level1Background(0,0)
		self.background2 = Level1Background(0,900)
		self.background3 = Level1Background(0,1800)
		self.background4 = Level1Background(0,2700)
		self.all_backgrounds.add(self.background1, self.background2, self.background3, self.background4)

	def update(self,gameState):
		mouse_pressed = pygame.mouse.get_pressed()
		mouse_pos = pygame.mouse.get_pos()
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:

				pygame.quit()
				sys.exit()

		old_x, old_y = self.player.rect.x, self.player.rect.y
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a] and self.player.rect.x >= 12:
			self.player.rect.x -= 3
			self.player.direction = -1
		if keys[pygame.K_d] and self.player.rect.x <= 690:
			self.player.rect.x += 3
			self.player.direction = 1
		if pygame.sprite.spritecollide(self.player, self.all_floors, False):
			self.player.rect.x = old_x

		if not keys[pygame.K_a] and not keys[pygame.K_d]:
			self.player.direction = 0

		if not self.checkStopScrolling:
			self.player.rect.y += 3
		if self.checkStopScrolling:
			self.player.rect.y += 3 + self.scrollSpeed

		collisions = pygame.sprite.spritecollide(self.player, self.all_floors, False)
		if collisions:
			self.player.rect.bottom = collisions[0].rect.top - 2
		if not collisions:
			self.player.direction = 2

		collisions = pygame.sprite.spritecollide(self.player, self.bottom_floors, False)
		if collisions:
			self.player.rect.bottom = collisions[0].rect.top - 1
			if keys[pygame.K_a]:
				self.player.direction = -1
			elif keys[pygame.K_d]:
				self.player.direction = 1
			else:
				self.player.direction = 0

		if self.player.rect.y <= 0:
			gameState.levelActive = False
			changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
			gameState.screen = "mineScreen"

		if pygame.sprite.collide_rect(self.player, self.finish):
			gameState.levelActive = False
			changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
			gameState.levelSelect[self.currentLevel]['completed'] = True
			gameState.screen = "mineScreen"

		self.player.update(gameState.frame)
		for bf in self.bottom_floors:
			self.checkStopScrolling = bf.getStopScrolling()
			break #Only care about the first (one of) the blocks, using for loop because spriteGroup not iterable
		self.finish.update(self.scrollSpeed)
		self.bottom_floors.update(self.scrollSpeed)
		if self.checkStopScrolling == False:
			self.all_backgrounds.update(self.scrollSpeed)
			self.all_floors.update(self.scrollSpeed)
		self.all_backgrounds.draw(DISPLAYSURF)
		pygame.draw.rect(DISPLAYSURF, BLACK, (0,0,8,900))
		pygame.draw.rect(DISPLAYSURF, BLACK, (712,0,8,900))
		self.all_floors.draw(DISPLAYSURF)
		self.bottom_floors.draw(DISPLAYSURF)
		#Adjust the players hitbox
		playerHitbox = (self.player.rect[0]-self.player.hitboxOffset[0],self.player.rect[1]-self.player.hitboxOffset[1])
		DISPLAYSURF.blit(self.player.image, playerHitbox)
		DISPLAYSURF.blit(self.finish.image,self.finish.rect)

		pygame.display.flip()