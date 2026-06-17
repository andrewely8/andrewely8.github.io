import pygame
from sprites import *
from utils import *
import sys,math,random
from .levelMaps import levelMap6

class Level7:
	def __init__(self,currentLevel):
		self.currentLevel = currentLevel
		self.all_floors = pygame.sprite.Group()
		self.all_enemey1 = pygame.sprite.Group()
		self.all_enemey2 = pygame.sprite.Group()
		self.all_dynamite = pygame.sprite.Group()
		self.all_finish = pygame.sprite.Group()
		self.breath = 10 #10 air bubbles, lose one every ~10-12 seconds 
		self.startTime = pygame.time.get_ticks() #in milliseconds
		self.playerSpeed = 2
		step = 0
		stepX = 0
		for i, row in enumerate(levelMap6):
			currentY = (step * 32)
			if (i+1) % 28 == 0: 
				step = 0
				stepX +=1
			else:
				step+=1
			for j, block in enumerate(row):
				currentX = stepX*704+(j*32)
				if block == 'b':
					new_floor = Level6FloorBlock(currentX, currentY)
					self.all_floors.add(new_floor)
				if block == 'p':
					self.player = Level6Player(currentX, currentY)
				if block == '1':
					new_e = Level6Enemy1(currentX, currentY)
					self.all_enemey1.add(new_e)
				if block == '2':
					new_e = Level6Enemy2(currentX, currentY)
					self.all_enemey2.add(new_e)
				if block == 'd':
					new_d = Level6Dynamite(currentX, currentY+8)
					self.all_dynamite.add(new_d)
				if block == 'f':
					new_f = Level6Finish(currentX, currentY)
					self.all_finish.add(new_f)

	def update(self,gameState):
		mouse_pressed = pygame.mouse.get_pressed()
		mouse_pos = pygame.mouse.get_pos()
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		keys = pygame.key.get_pressed()
		old_x, old_y = self.player.rect.x, self.player.rect.y
		if keys[pygame.K_a]:
			self.player.rect.x -= self.playerSpeed
			self.playerDirection = 1
		if keys[pygame.K_d]:
			self.player.rect.x += self.playerSpeed
			self.playerDirection = 1
		
		if pygame.sprite.spritecollide(self.player, self.all_floors, False):
			self.player.rect.x = old_x
		if keys[pygame.K_w]:
			self.player.rect.y -= self.playerSpeed+1
			self.playerDirection = 1
		if keys[pygame.K_s]:
			self.player.rect.y += self.playerSpeed
			self.playerDirection = 1
		elif not keys[pygame.K_s] and not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_d]:
			self.player.rect.y += self.playerSpeed-1
			self.playerDirection = 0

		if pygame.sprite.spritecollide(self.player, self.all_floors, False):
			self.player.rect.y = old_y

		if self.player.rect.x <= 335:
			self.direction = 1
			self.player.rect.x += 1
		elif self.player.rect.x >= 375:
			self.direction = -1
			self.player.rect.x -= 1
		else:
			self.direction = 0

		if not pygame.sprite.spritecollide(self.player, self.all_floors, False):
			self.all_floors.update(self.player.rect.x, self.playerSpeed,self.direction)
			self.all_enemey2.update(self.player.rect.x, self.playerSpeed, self.direction)
			self.all_dynamite.update(self.player.rect.x, self.playerSpeed, self.direction)
			self.all_finish.update(self.player.rect.x, self.playerSpeed, self.direction)
		else:
			self.player.rect.x += self.direction+5
		
		self.currentTime = pygame.time.get_ticks() #in milliseconds
		if self.currentTime - self.startTime >= 10000: #every 10 seconds
			self.breath -= 1 
			self.startTime = self.currentTime

		if (self.breath <= 0 or pygame.sprite.spritecollide(self.player, self.all_enemey1, False) or   
			pygame.sprite.spritecollide(self.player, self.all_enemey2, False) or 
			pygame.sprite.spritecollide(self.player, self.all_dynamite, False)):
			gameState.levelActive = False
			changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
			gameState.screen = "mineScreen"

		if pygame.sprite.spritecollide(self.player, self.all_finish, False):
			gameState.levelActive = False
			changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
			gameState.levelSelect[self.currentLevel]['completed'] = True
			gameState.screen = "mineScreen"

		for enemey in self.all_enemey2:
			if pygame.sprite.spritecollide(enemey, self.all_floors, False):
				enemey.collidedWall = True

		self.player.update(self.playerDirection,gameState.frame)
		self.all_enemey1.update(self.playerSpeed, self.direction)
		
		DISPLAYSURF.blit(level6Background , (0,0))
		playerHitbox = (self.player.rect[0]-self.player.hitboxOffset[0],self.player.rect[1]-self.player.hitboxOffset[1])
		DISPLAYSURF.blit(self.player.image, playerHitbox)
		self.all_floors.draw(DISPLAYSURF)
		self.all_enemey1.draw(DISPLAYSURF)
		self.all_enemey2.draw(DISPLAYSURF)
		self.all_dynamite.draw(DISPLAYSURF)
		self.all_finish.draw(DISPLAYSURF)

		for i in range(self.breath):
			DISPLAYSURF.blit(airBubble, (280+i*17,825,16,16))
		pygame.display.flip()