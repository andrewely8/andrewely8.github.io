import pygame
from sprites import *
from utils import *
import sys,math,random


class Level3:
	def __init__(self,currentLevel):
		self.currentLevel = currentLevel
		self.player = playerLevel3(334,668)
		self.finish = False
		self.valves_sprites = pygame.sprite.Group()
		self.switch_sprites = pygame.sprite.Group()
		self.currentY = 59
		self.currentValve = 0
		for i, row in enumerate(pipesInitial):
			self.currentY += 48 
			self.currentX = 176
			for j, pipe in enumerate(row):
				self.currentX+= 48
				self.pipes = pipe.copy()
				new_valve = Valve(self.currentX, self.currentY, self.pipes, self.currentValve)
				self.valves_sprites.add(new_valve)
				self.currentValve += 1

		switch1 = ValveSwitch(81,668,[0,1,8,22,27,30])     #blue
		switch2 = ValveSwitch(186,668,[2,7,12,23,28,33])   #red
		switch3 = ValveSwitch(291,668,[3,5,19,24,29,31])   #green
		switch4 = ValveSwitch(396,668,[4,6,11,20,25,35])   #orange
		switch5 = ValveSwitch(501,668,[9,10,14,21,26,34])  #pink
		switch6 = ValveSwitch(606,668,[13,15,16,17,18,32]) #yellow
		self.switch_sprites.add(switch1,switch2,switch3,switch4,switch5,switch6)

	def update(self,gameState):
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					switchCollide = pygame.sprite.spritecollide(self.player,self.switch_sprites,False)
					for switch in switchCollide:
						switchCollide = switch
					if switchCollide:
						for valve in self.valves_sprites:
							if valve.valveNumber in switchCollide.valvesAffected:
								valve.rotate()


		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.player.rect.x -= 3
			self.player.direction = 1
		elif keys[pygame.K_d]:
			self.player.rect.x += 3
			self.player.direction = 2
		else:
			self.player.direction = 0
		if self.player.rect.x <= -16:
			gameState.levelActive = False
			changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
			gameState.screen = "mineScreen"

		if self.player.rect.x >= 684 and not self.finish:
			self.player.rect.x = 684
		if self.player.rect.x >= 704 and self.finish:
			gameState.levelActive = False
			changeMusic('gameAssets/audio/backgroundMusic.ogg',gameState.gameVolume[gameState.gameVolumeIndex])
			gameState.levelSelect[self.currentLevel]['completed'] = True
			gameState.screen = "mineScreen"
		
		
		DISPLAYSURF.blit(level3Background, (0,0))
		self.valves_sprites.update()
		self.valves_sprites.draw(DISPLAYSURF)

		edges = set()
		for valve in self.valves_sprites:
			if valve.pipes[0] == 1:
				DISPLAYSURF.blit(pipeUpImage, (valve.rect.x+12, valve.rect.y-8))
			if valve.pipes[1] == 1:
				DISPLAYSURF.blit(pipeRightImage, (valve.rect.x+32, valve.rect.y+12))
			if valve.pipes[2] == 1:
				DISPLAYSURF.blit(pipeDownImage, (valve.rect.x+12, valve.rect.y+32))
			if valve.pipes[3] == 1:
				DISPLAYSURF.blit(pipeLeftImage, (valve.rect.x-8, valve.rect.y+12))

			currentValve = valve
			valveBelow = -1
			valveAbove = -1
			valveLeft = -1
			valveRight = -1
			for v in self.valves_sprites:
				if v.valveNumber == currentValve.valveNumber + 6:
					valveBelow = v
				if v.valveNumber == currentValve.valveNumber - 1 and currentValve.valveNumber not in [0,6,12,18,24,30]:  
					valveLeft = v
				if v.valveNumber == currentValve.valveNumber + 1 and currentValve.valveNumber not in [5,11,17,23,29,35]: 
					valveRight = v
				if v.valveNumber == currentValve.valveNumber - 6:
					valveAbove = v

			#CONSTRUCT EDGE SET
			if (valveBelow != -1) and (currentValve.pipes[2] == 1 and valveBelow.pipes[0] == 1): #below connection
				e = (valveBelow.valveNumber,currentValve.valveNumber)
				newEdge = tuple(sorted(e))
				edges.add(newEdge)
			if (valveAbove != -1) and (currentValve.pipes[0] == 1 and valveAbove.pipes[2] == 1): #above connection
				e = (valveAbove.valveNumber,currentValve.valveNumber)
				newEdge = tuple(sorted(e))
				edges.add(newEdge)
			if (valveLeft != -1) and (currentValve.pipes[3] == 1 and valveLeft.pipes[1] == 1): #left connection
				e = (valveLeft.valveNumber,currentValve.valveNumber)
				newEdge = tuple(sorted(e))
				edges.add(newEdge)
			if (valveRight != -1) and (currentValve.pipes[1] == 1 and valveRight.pipes[3] == 1): #right connection
				e = (valveRight.valveNumber,currentValve.valveNumber)
				newEdge = tuple(sorted(e))
				edges.add(newEdge)
			if currentValve.valveNumber == 6 and currentValve.pipes[3] == 1:
				edges.add((6,36))

		#RUN DFS 
		V = 37 #ONE EXTRA DUMMY NODE
		adj = [[0] * V for _ in range(V)]
		for s, t in edges:
			add_edge(adj,s,t)
		res = DFS(adj, 36) #STARTING FROM A DUMMY NODE

		for valve in self.valves_sprites:
			if valve.valveNumber in res:
				valve.full = True 
			else:
				valve.full = False
			if 29 in res:
				self.finish = True
			if 29 not in res:
				self.finish = False

		if self.finish:
			DISPLAYSURF.blit(level3Finish, (650,495))
		self.switch_sprites.update()
		self.player.update(gameState.frame)
		self.switch_sprites.draw(DISPLAYSURF)
		DISPLAYSURF.blit(self.player.image,self.player.rect)
		
		pygame.display.flip()