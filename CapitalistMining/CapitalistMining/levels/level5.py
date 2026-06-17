import pygame
from sprites import *
from utils import *
import sys,math,random
from .levelMaps import levelMap4
from .levelMaps import levelMap7

class Level5:
	def __init__(self,currentLevel):
		self.currentLevel = currentLevel
		self.scrollSpeed = 4
		self.background_sprites = pygame.sprite.Group()
		self.all_floors = pygame.sprite.Group()
		self.kill_blocks = pygame.sprite.Group()
		self.finish_blocks = pygame.sprite.Group()
		self.up_rails = pygame.sprite.Group()
		self.visual_rails = pygame.sprite.Group()
		self.straight_rails = pygame.sprite.Group()
		self.down_rails = pygame.sprite.Group()
		background1 = SidescrollBackground(0,0)
		background2 = SidescrollBackground(2160,0)
		background3 = SidescrollBackground(4320,0)
		background4 = SidescrollBackground(6480,0)
		background5 = SidescrollBackground(8640,0)
		self.background_sprites.add(background1, background2, background3, background4, background5)
		step = 0
		stepX = 0

		if self.currentLevel == 4:
			lm = levelMap4
		elif self.currentLevel == 7:
			lm = levelMap7

		for i, row in enumerate(lm):
			currentY = (step * 32)
			if (i+1) % 28 == 0: 
				step = 0
				stepX +=1
			else:
				step+=1
			for j, block in enumerate(row):
				currentX = stepX*704+(j*32)
				if block == 'b':
					new_floor = SidescrollFloorBlock(currentX, currentY)
					self.all_floors.add(new_floor)
				if block == 'p':
					self.player = PlayerMinecart(currentX, currentY)
				if block == 'k':
					new_block = SidescrollKillBlock(currentX, currentY+8)
					self.kill_blocks.add(new_block)
				if block == 'f':
					self.finish = MinecartFinishBlock(currentX, currentY)
				if block == 'u':
					new_block = SidescrollUpRail(currentX, currentY)
					self.up_rails.add(new_block)
				if block == 'd':
					new_block = SidescrollDownRail(currentX, currentY)
					self.down_rails.add(new_block)
				if block == 's':
					new_block = SidescrollStraightRail(currentX, currentY+29)
					self.straight_rails.add(new_block)
				if block == '1':
					new_item = SidescrollUpRailTopLeft(currentX,currentY)
					self.visual_rails.add(new_item)
				if block == '2':
					new_item = SidescrollUpRailBottomRight(currentX,currentY)
					self.visual_rails.add(new_item)
				if block == '3':
					new_item = SidescrollDownRailBottomLeft(currentX,currentY)
					self.visual_rails.add(new_item)
				if block == '4':
					new_item = SidescrollDownRailTopRight(currentX,currentY)
					self.visual_rails.add(new_item)

	def update(self,gameState):
		mouse_pressed = pygame.mouse.get_pressed()
		mouse_pos = pygame.mouse.get_pos()
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				pygame.quit()
				sys.exit()
		
		if pygame.sprite.spritecollide(self.player, self.kill_blocks, False):
			gameState.levelActive = False
			changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
			gameState.screen = "mineScreen"

		if pygame.sprite.collide_rect(self.player, self.finish):
			gameState.levelActive = False
			changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
			gameState.levelSelect[self.currentLevel]['completed'] = True
			gameState.screen = "mineScreen"

		onStraightRail = pygame.sprite.spritecollide(self.player, self.straight_rails, False)
		onUpRail = pygame.sprite.spritecollide(self.player, self.up_rails, False)
		onDownRail = pygame.sprite.spritecollide(self.player, self.down_rails, False)

		if onStraightRail:
			self.player.image = minecartPlayer
			self.player.isGrounded = True
			self.player.isJumping = False
			self.player.rect.bottom = onStraightRail[0].rect.bottom - 2
		elif onUpRail:
			self.player.isGrounded = True
			self.player.isJumping = False
			self.player.rect.y -=11
			rotatePlayerImage = pygame.transform.rotate(minecartPlayer,45)
			self.player.image = rotatePlayerImage
		elif onDownRail:
			self.player.isGrounded = True
			self.player.isJumping = False
			self.player.rect.y -= 1
			rotatePlayerImage = pygame.transform.rotate(minecartPlayer,-45)
			self.player.image = rotatePlayerImage
		else:
			self.player.isGrounded = False
			
		collidedFloor = pygame.sprite.spritecollide(self.player, self.all_floors, False)
		if collidedFloor:
			for floor in collidedFloor:
				overlap = self.player.rect.clip(floor.rect)
				if overlap.height >= 20: #collision with side of a wall
					gameState.levelActive = False
					changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
					gameState.screen = "mineScreen"
				if self.player.rect.y >= floor.rect.y:
					self.player.rect.top = floor.rect.bottom
					self.player.isJumping = False


		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and self.player.isJumping == False and self.player.isGrounded == True:
			self.player.isJumping = True
			self.player.isGrounded = False
			self.player.startingY = self.player.rect.y

	   
		self.player.rect.y += 5
		if self.player.isJumping:
			self.player.rect.y -= 12

		self.background_sprites.update(self.scrollSpeed)
		self.all_floors.update(self.scrollSpeed)
		self.kill_blocks.update(self.scrollSpeed)
		self.finish.update(self.scrollSpeed)
		self.up_rails.update(self.scrollSpeed)
		self.visual_rails.update(self.scrollSpeed)
		self.down_rails.update(self.scrollSpeed)
		self.straight_rails.update(self.scrollSpeed)
		self.player.update()

		self.background_sprites.draw(DISPLAYSURF)
		self.all_floors.draw(DISPLAYSURF)
		self.kill_blocks.draw(DISPLAYSURF)
		self.up_rails.draw(DISPLAYSURF)
		self.visual_rails.draw(DISPLAYSURF)
		self.straight_rails.draw(DISPLAYSURF) 
		self.down_rails.draw(DISPLAYSURF)

		DISPLAYSURF.blit(self.finish.image, self.finish.rect)
		DISPLAYSURF.blit(self.player.image, self.player.rect)
		
		pygame.display.flip()