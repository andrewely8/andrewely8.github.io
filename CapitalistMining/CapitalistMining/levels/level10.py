import pygame
from sprites import *
from utils import *
import sys,math,random
from .levelMaps import levelMap9

class Level10:
	def __init__(self,currentLevel):
		self.currentLevel = currentLevel
		self.scrollSpeed = 1
		self.level10StopScrolling = False
		self.gravity = 6
		self.jumpHeight = 6
		self.all_backgrounds = pygame.sprite.Group()
		self.all_floors = pygame.sprite.Group()
		self.bottom_floors = pygame.sprite.Group()
		self.offset = 0
		for i, row in enumerate(levelMap9):
			currentY = (i * 32)  - 900*((len(levelMap9)-28)/28)
			for j, block in enumerate(row):
				currentX = 8+ (j * 32)
				if block == 'p':
					self.player = PlayerLevel10(currentX,currentY)
				if block == 'b':
					new_floor = floorBlockLevel10(currentX, currentY)
					self.all_floors.add(new_floor)
				if block == 'e':
					new_floor = topFloorBlockLevel10(currentX, currentY)
					self.bottom_floors.add(new_floor)
					self.all_floors.add(new_floor)
				if block == 'f':
					self.finish = FinishBlockLevel10(currentX, currentY)

		
		background1 = Level10Background(0,0)
		background2 = Level10Background(0,-900)
		background3 = Level10Background(0,-1800)
		background4 = Level10Background(0,-2700)
		self.all_backgrounds.add(background1, background2, background3, background4)
		self.lava = LavaLevel10(0,880)

	def update(self,gameState):
		mouse_pressed = pygame.mouse.get_pressed()
		mouse_pos = pygame.mouse.get_pos()
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		old_x = self.player.rect.x
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a] and self.player.rect.x >= 12:
			self.player.rect.x -= 3
			self.player.direction = 1
		if keys[pygame.K_d] and self.player.rect.x <= 690:
			self.player.rect.x += 3
			self.player.direction = 2
		if pygame.sprite.spritecollide(self.player, self.all_floors, False):
			self.player.rect.x = old_x

		if not keys[pygame.K_a] and not keys[pygame.K_d]:
			self.player.direction = 0

		old_y = self.player.rect.y
		if keys[pygame.K_SPACE] and self.player.isGrounded and not self.player.isJumping:
			self.player.isJumping = True
			self.player.isGrounded = False
			self.player.startingY = self.player.rect.y

		if self.player.isJumping:
			self.player.rect.y -= self.jumpHeight
		else:
			self.player.rect.y += self.gravity
	   
		  
		collisions = pygame.sprite.spritecollide(self.player,self.all_floors,False)
		self.player.isGrounded = False
		for floor in collisions:
			# Player was above the block last frame, so they landed on top
			if old_y + self.player.rect.height <= floor.rect.top:
				self.player.rect.bottom = floor.rect.top
				self.player.isGrounded = True
				self.player.isJumping = False
			# Player was below the block last frame, so they hit the ceiling
			elif old_y >= floor.rect.bottom:
				self.player.rect.top = floor.rect.bottom
				self.player.isJumping = False

		if  pygame.sprite.collide_rect(self.player, self.lava):
			gameState.levelActive = False
			changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
			gameState.screen = "mineScreen"

		if pygame.sprite.collide_rect(self.player, self.finish):
			gameState.levelActive = False
			changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
			gameState.levelSelect[self.currentLevel]['completed'] = True
			gameState.screen = "mineScreen"


		self.player.update(gameState.frame)
		self.finish.update(self.scrollSpeed)
		self.lava.update(self.scrollSpeed)


		for bf in self.bottom_floors:
			self.checkStopScrolling = bf.getStopScrolling()
			break #Only care about the first (one of) the blocks, using for loop because spriteGroup not iterable

		if self.checkStopScrolling == False:
			self.all_backgrounds.update(self.scrollSpeed)
			self.all_floors.update(self.scrollSpeed)
		else:
			self.lava.topOut = True
		

		self.all_backgrounds.draw(DISPLAYSURF)
		pygame.draw.rect(DISPLAYSURF, BLACK, (0,0,8,900))
		pygame.draw.rect(DISPLAYSURF, BLACK, (712,0,8,900))
		self.all_floors.draw(DISPLAYSURF)
		self.bottom_floors.draw(DISPLAYSURF)
		playerHitbox = (self.player.rect[0]-self.player.hitboxOffset[0],self.player.rect[1]-self.player.hitboxOffset[1])
		DISPLAYSURF.blit(self.player.image, playerHitbox)
		DISPLAYSURF.blit(self.finish.image,self.finish.rect)
		DISPLAYSURF.blit(self.lava.image,self.lava.rect)

		pygame.display.flip()