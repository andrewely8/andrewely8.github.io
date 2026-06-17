levelMap8 = [
	['a','5','a','2','b','2','b','3','b','8','a','7','a'],
	['b','3','a','4','b','3','a','2','a','3','a','6','b'],
]


import pygame
from sprites import *
from utils import *
import sys,math,random


class Level9:
	def __init__(self,currentLevel):
		self.currentLevel = currentLevel
		self.playerSpeed = 3
		self.spawnLevelY = 568
		self.finishOffset = 0
		self.enemiesDefeated = False
		self.player = Level8Player(350,self.spawnLevelY+8)
		self.floor = Level8Floor(-50,600)
		self.all_enemy1 = pygame.sprite.Group()
		self.all_enemy2 = pygame.sprite.Group()
		self.all_enemy = pygame.sprite.Group()
		currentX = 0
		for item in levelMap8[0]: #enemies that come from the left
			if item == 'a': #enemy type
				e = Level8Enemy1(currentX, self.spawnLevelY+16)
				self.all_enemy1.add(e)
				self.all_enemy.add(e)
			elif item == 'b': #enemey type
				e = Level8Enemy2(currentX, self.spawnLevelY)
				self.all_enemy2.add(e)
				self.all_enemy.add(e)
			else: #number representing amount of space of 32 pixels to add
				currentX -= int(item) * 32
		currentX = 720
		for item in levelMap8[1]: #enemies that come from the right
			if item == 'a': #enemy type
				e = Level8Enemy1(currentX, self.spawnLevelY+16)
				self.all_enemy1.add(e)
				self.all_enemy.add(e)
			elif item == 'b': #enemey type
				e = Level8Enemy2(currentX, self.spawnLevelY)
				self.all_enemy2.add(e)
				self.all_enemy.add(e)
			else: #number representing amount of space of 32 pixels to add
				currentX += int(item) * 32

	def update(self,gameState):
		mouse_pressed = pygame.mouse.get_pressed()
		mouse_pos = pygame.mouse.get_pos()
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_a] and self.player.rect.x >= 8:
			self.player.rect.x -= self.playerSpeed
			self.player.previousDirection = self.player.direction
			self.player.direction = 1
		if keys[pygame.K_d] and self.player.rect.x <= 680 + self.finishOffset:
			self.player.rect.x += self.playerSpeed
			self.player.previousDirection = self.player.direction
			self.player.direction = 2
		if keys[pygame.K_SPACE]:
			self.player.attack()
		if not keys[pygame.K_a] and not keys[pygame.K_d]:
			if self.player.direction != 0:
				self.player.previousDirection = self.player.direction
			self.player.direction = 0

		if len(self.all_enemy) == 0:
			self.enemiesDefeated = True
			self.finishOffset += 64
		if self.enemiesDefeated and self.player.rect.x >= 700:
			gameState.levelActive = False
			changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
			gameState.levelSelect[self.currentLevel]['completed'] = True
			gameState.screen = "mineScreen"

		collisions = pygame.sprite.spritecollide(self.player, self.all_enemy, False)
		for collision in collisions:
			if self.player.attacking and self.player.previousDirection == 1:
				if collision.rect.x <= self.player.rect.x:
					collision.kill()
				else:
					gameState.levelActive = False
					changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
					gameState.screen = "mineScreen"
			elif self.player.attacking and self.player.previousDirection == 2:
				if collision.rect.x >= self.player.rect.x:
					collision.kill()
				else:
					gameState.levelActive = False
					changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
					gameState.screen = "mineScreen"
			else:
				gameState.levelActive = False
				changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
				gameState.screen = "mineScreen"

		self.player.update(gameState.frame)
		self.all_enemy.update(self.player.rect.x,gameState.frame)

		
		DISPLAYSURF.blit(level1Background,(0,-40))
		pygame.draw.rect(DISPLAYSURF, BLACK, (0,0, 720, 330))
		self.all_enemy.draw(DISPLAYSURF)
		if self.enemiesDefeated:
			DISPLAYSURF.blit(level3Finish, (650,330))
		playerHitbox = (self.player.rect[0]-self.player.hitboxOffset[0],self.player.rect[1]-self.player.hitboxOffset[1])
		DISPLAYSURF.blit(self.player.image, playerHitbox)
		DISPLAYSURF.blit(self.floor.image, self.floor.rect)

		pygame.display.flip()