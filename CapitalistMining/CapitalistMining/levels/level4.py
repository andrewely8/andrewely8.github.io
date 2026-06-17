import pygame
from sprites import *
from utils import *
import sys,math,random
from .levelMaps import levelMap3
from .levelMaps import levelMap5

class Level4:
	def __init__(self,currentLevel):
		self.currentLevel = currentLevel
		self.all_floors = pygame.sprite.Group()
		self.all_dynamite = pygame.sprite.Group()
		self.all_enemey1 = pygame.sprite.Group()
		self.all_enemey2 = pygame.sprite.Group()
		self.all_enemey3 = pygame.sprite.Group()
		self.finish_blocks = pygame.sprite.Group()
		self.all_backgrounds = pygame.sprite.Group()
		self.scroll_sprites = pygame.sprite.Group()
		self.scrollSpeed = 3
		self.playerSpeed = 3
		self.gravity = 5
		self.step = 0
		self.stepX = 0
		if self.currentLevel == 3:
			levelMap = levelMap3
		if self.currentLevel == 5:
			levelMap = levelMap5
		for i, row in enumerate(levelMap):
			currentY = (self.step * 32)
			if (i+1) % 28 == 0: 
				self.step = 0
				self.stepX += 1
			else:
				self.step += 1
			for j, block in enumerate(row):
				currentX = self.stepX*704+(j*32)
				if block == 'b':
					new_floor = Level4FloorBlock(currentX, currentY)
					self.all_floors.add(new_floor)
					self.scroll_sprites.add(new_floor)
				if block == 'p':
					self.player = Level4Player(currentX, currentY)
				if block == 'd':
					new_block = Level4Dynamite(currentX, currentY+8)
					self.scroll_sprites.add(new_block)
					self.all_dynamite.add(new_block)
				if block == '1':
					new_block = Level4Enemy1(currentX,currentY+16)
					self.scroll_sprites.add(new_block)
					self.all_enemey1.add(new_block)
				if block == '2':
					new_block = Level4Enemy2(currentX,currentY)
					self.scroll_sprites.add(new_block)
					self.all_enemey2.add(new_block)
				if block == '3':
					new_block = Level4Enemy3(currentX, currentY)
					self.scroll_sprites.add(new_block)
					self.all_enemey3.add(new_block)
				if block == 'f':
					new_block = Level4Finish(currentX, currentY)
					self.scroll_sprites.add(new_block)
					self.finish_blocks.add(new_block)
				if block == 'e':
					self.finishSign = Level4ExitSign(currentX,currentY)
					self.scroll_sprites.add(self.finishSign)
		background1 = BackgroundLevel4(0,0)
		background2 = BackgroundLevel4(2160,0)
		background3 = BackgroundLevel4(4320,0)
		background4 = BackgroundLevel4(6480,0)
		background5 = BackgroundLevel4(8640,0)
		self.scroll_sprites.add(background1, background2, background3, background4, background5)
		self.all_backgrounds.add(background1, background2, background3, background4, background5)

	def update(self,gameState):
		mouse_pressed = pygame.mouse.get_pressed()
		mouse_pos = pygame.mouse.get_pos()
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		keys = pygame.key.get_pressed()
		old_x = self.player.rect.x
		if keys[pygame.K_a]:
			self.player.rect.x -= self.playerSpeed
			self.player.direction = 1
		if keys[pygame.K_d]:
			self.player.rect.x += self.playerSpeed
			self.player.direction = 2
		if pygame.sprite.spritecollide(self.player, self.all_floors, False):
			self.player.rect.x = old_x

		old_y = self.player.rect.y
		if keys[pygame.K_SPACE] and self.player.isGrounded:
			self.player.isJumping = True
			self.player.isGrounded = False
			self.player.startingY = self.player.rect.y
		if self.player.isJumping:
			self.player.rect.y -= 12

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
		if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d]:
			self.player.direction = 0
		for enemey in self.all_enemey1:
			collisions = pygame.sprite.spritecollide(enemey, self.all_floors, False)
			if collisions:
				enemey.direction = enemey.direction * -1
		for enemey in self.all_enemey2:
			distance = math.sqrt((self.player.rect.x-enemey.rect.x)**2+(self.player.rect.y-enemey.rect.y)**2)
			if distance <= 200:
				enemey.spotted = True
		for enemey in self.all_enemey3:
			collisions = pygame.sprite.spritecollide(enemey,self.all_floors,False)
			if collisions:
				if enemey.isJumping:
					enemey.rect.top = collisions[0].rect.bottom
					enemey.isJumping = False
				else:
					enemey.rect.bottom = collisions[0].rect.top
					enemey.isGrounded = True
			elif not collisions:
				enemey.isGrounded = False

			enemey.rect.y += self.gravity//2
			if enemey.isGrounded == True and enemey.isJumping == False:
				if gameState.frame >= 59:
					random_int = random.randint(1,10)
					if random_int <= 5 and enemey.isGrounded:
						enemey.isGrounded = False
						enemey.startingY = enemey.rect.y
						enemey.isJumping = True
						


		if (pygame.sprite.spritecollide(self.player,self.all_enemey1,False) or 
			pygame.sprite.spritecollide(self.player,self.all_enemey2,False) or
			pygame.sprite.spritecollide(self.player,self.all_enemey3,False) or
			pygame.sprite.spritecollide(self.player,self.all_dynamite,False)): #Level failed
				gameState.levelActive = False
				changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
				gameState.screen = "mineScreen"
		if pygame.sprite.spritecollide(self.player, self.finish_blocks, False): #Level Completed
			gameState.levelActive = False
			changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
			gameState.levelSelect[self.currentLevel]['completed'] = True
			gameState.screen = "mineScreen"


		if self.player.rect.x <= 240:
			self.currentScroll = -1 * self.scrollSpeed
			self.player.rect.x += self.playerSpeed
		elif self.player.rect.x >= 480:
			self.currentScroll = self.scrollSpeed
			self.player.rect.x -= self.playerSpeed
		else:
			self.currentScroll = 0


		self.player.update(gameState.frame)
		self.scroll_sprites.update(self.currentScroll,gameState.frame)

		self.all_backgrounds.draw(DISPLAYSURF)
		self.all_floors.draw(DISPLAYSURF)
		self.all_dynamite.draw(DISPLAYSURF)
		self.all_enemey1.draw(DISPLAYSURF)
		self.all_enemey2.draw(DISPLAYSURF)
		self.all_enemey3.draw(DISPLAYSURF)
		self.finish_blocks.draw(DISPLAYSURF)
		DISPLAYSURF.blit(self.finishSign.image,self.finishSign.rect)
		#Adjust the players hitbox
		playerHitbox = (self.player.rect[0]-self.player.hitboxOffset[0],self.player.rect[1]-self.player.hitboxOffset[1])
		DISPLAYSURF.blit(self.player.image, playerHitbox)
		
		
		pygame.display.flip()