import pygame
from sprites import *
from utils import *
import sys,math,random
from .levelMaps import levelMap1

class Level2:
	def __init__(self,currentLevel):
		self.currentLevel = currentLevel
		self.all_floors = pygame.sprite.Group()
		for i, row in enumerate(levelMap1):
			currentY = 4 + (i * 32)
			for j, block in enumerate(row):
				currentX = 8 + (j * 32)
				if block == 'p':
					self.player = PlayerTopView(currentX,currentY+8)
				if block == 'b':
					new_floor = stillFloorBlock(currentX, currentY)
					self.all_floors.add(new_floor)
				if block == 't':
					self.torch = Torch(currentX, currentY)
				if block == 'f':
					self.finish = FinishLevel2(currentX, currentY)

	def update(self,gameState):
		mouse_pressed = pygame.mouse.get_pressed()
		mouse_pos = pygame.mouse.get_pos()
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		old_x, old_y = self.player.rect.x, self.player.rect.y
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a] and self.player.rect.x >= 8:
			self.player.rect.x -= 2
			self.player.direction = 1
		if keys[pygame.K_d] and self.player.rect.x <= 693:
			self.player.rect.x += 2
			self.player.direction = 2
		if pygame.sprite.spritecollide(self.player, self.all_floors, False):
			self.player.rect.x = old_x
		if keys[pygame.K_w] and self.player.rect.y >= 8:
			self.player.rect.y -= 2
			self.player.direction = 3
		if keys[pygame.K_s] and self.player.rect.y <= 860:
			self.player.rect.y += 2
			self.player.direction = 4
		if pygame.sprite.spritecollide(self.player, self.all_floors, False):
			self.player.rect.y = old_y
		if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:
			self.player.direction = 0

		if keys[pygame.K_r]:
			gameState.levelActive = False
			changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
			gameState.screen = "mineScreen"
		if pygame.sprite.collide_rect(self.player, self.finish):
			gameState.levelActive = False
			changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
			gameState.levelSelect[self.currentLevel]['completed'] = True
			gameState.screen = "mineScreen"
		if pygame.sprite.collide_rect(self.player, self.torch):
			self.torch.collected = True

		self.player.update(gameState.frame)
		DISPLAYSURF.blit(background, (0,0))
		pygame.draw.rect(DISPLAYSURF, BLACK, (0,0,8,900))
		pygame.draw.rect(DISPLAYSURF, BLACK, (712,0,8,900))
		pygame.draw.rect(DISPLAYSURF, BLACK, (0,0,720,8))
		pygame.draw.rect(DISPLAYSURF, BLACK, (0,892,720,8))
		DISPLAYSURF.blit(self.finish.image, self.finish.rect)
		DISPLAYSURF.blit(self.player.image, self.player.rect)
		self.all_floors.draw(DISPLAYSURF)
		if self.torch.collected == False:
			DISPLAYSURF.blit(self.torch.image, self.torch.rect)
			torchLight_rect.center = (self.torch.rect.x+16,self.torch.rect.y+16)
		elif self.torch.collected == True:
			torchLight_rect.center = (self.player.rect.x+16,self.player.rect.y+16)
		DISPLAYSURF.blit(torchLight, torchLight_rect)
		pygame.draw.rect(DISPLAYSURF, GRAY, (275,800,165,50),border_radius=2)
		drawTitle('USE R to quit level.', 277,820,font4)

		pygame.display.flip()