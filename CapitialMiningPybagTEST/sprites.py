import pygame

#Load Images 
arrow = pygame.image.load('gameAssets/arrow.png')
logo = pygame.image.load('gameAssets/logo.png')
menu = pygame.image.load('gameAssets/menu.png')
storeBoard = pygame.image.load('gameAssets/storeBoard.png')
managerBoard = pygame.image.load('gameAssets/managerBoard.png')
mainMenu = pygame.image.load('gameAssets/mainMenu.png')
background = pygame.image.load('gameAssets/background.png')
itemSillouete = pygame.image.load('gameAssets/nextItemSillouete.png')
upgradeBoard = pygame.image.load('gameAssets/upgradeBoard.png')
checkBox = pygame.image.load('gameAssets/checkBox.png')
chains = pygame.image.load('gameAssets/menuChains.png')
unlockChain = pygame.image.load('gameAssets/unlockChain.png')
torchLight = pygame.image.load('gameAssets/torchLight.png')
minecartRailUp = pygame.image.load('gameAssets/railUp.png')
minecartRailUpTopLeft = pygame.image.load('gameAssets/railUpTopLeft.png')
minecartRailUpBottomRight = pygame.image.load('gameAssets/railUpBottomRight.png')
minecartRailStraight = pygame.image.load('gameAssets/railStraight.png')
minecartRailDown = pygame.image.load('gameAssets/railDown.png')
minecartRailDownTopRight = pygame.image.load('gameAssets/railDownTopRight.png')
minecartRailDownBottomLeft = pygame.image.load('gameAssets/railDownBottomLeft.png')
minecartPlayer = pygame.image.load('gameAssets/minerMinecartFlat.png')
minecartPlayerJump = pygame.image.load('gameAssets/minerMinecartJump.png')
dynamite = pygame.image.load('gameAssets/dynamite.png')
minecartLevelBackground = pygame.image.load('gameAssets/minecartLevelBackground.png')
finishLevel2 = pygame.image.load('gameAssets/finishLevel2.png')
torchLight_rect = torchLight.get_rect()
torchImage = pygame.image.load('gameAssets/torch.png')
level3Background = pygame.image.load('gameAssets/level3Background.png')
valveEmptyImage = pygame.image.load('gameAssets/valveEmpty.png')
valveFullImage = pygame.image.load('gameAssets/valveFull.png')
pipeUpImage = pygame.image.load('gameAssets/pipeUp.png')
pipeDownImage = pygame.image.load('gameAssets/pipeDown.png')
pipeLeftImage = pygame.image.load('gameAssets/pipeLeft.png')
pipeRightImage = pygame.image.load('gameAssets/pipeRight.png')
valveSwitch = pygame.image.load('gameAssets/valveSwitch.png')
level3Finish = pygame.image.load('gameAssets/level3Finish.png')
minerLeftWalk = pygame.image.load('gameAssets/minerLeft.png')
minerRightWalk = pygame.image.load('gameAssets/minerRight.png')
minerLeftWalk2 = pygame.image.load('gameAssets/minerLeft2.png')
minerRightWalk2 = pygame.image.load('gameAssets/minerRight2.png')
minerIdle = pygame.image.load('gameAssets/minerIdle.png')
airBubble = pygame.image.load('gameAssets/airBubble.png')
squid = pygame.image.load('gameAssets/squid.png')
fish = pygame.image.load('gameAssets/fish.png')
level6Background = pygame.image.load('gameAssets/level6Background.png')
level1Background = pygame.image.load('gameAssets/level1Background.png')
level4Background = pygame.image.load('gameAssets/level4Background.png')
level10Lava = pygame.image.load('gameAssets/level10Lava.png')
minerSwimmingIdle = pygame.image.load('gameAssets/minerSwimmingIdle.png')
minerSwimming1 = pygame.image.load('gameAssets/minerSwimming1.png')
minerSwimming2 = pygame.image.load('gameAssets/minerSwimming2.png')
minerIdleJump = pygame.image.load('gameAssets/minerIdleJump.png')
minerTopView1 = pygame.image.load('gameAssets/minerTopView1.png')
minerTopView2 = pygame.image.load('gameAssets/minerTopView2.png')
minerTopView3 = pygame.image.load('gameAssets/minerTopView3.png')
minerTopView4 = pygame.image.load('gameAssets/minerTopView4.png')
minerTopView5 = pygame.image.load('gameAssets/minerTopView5.png')
minerTopView6 = pygame.image.load('gameAssets/minerTopView6.png')
minerTopView7 = pygame.image.load('gameAssets/minerTopView7.png')
minerTopView8 = pygame.image.load('gameAssets/minerTopView8.png')
minerTopViewIdle = pygame.image.load('gameAssets/minerTopViewIdle.png')
minerLeftJump = pygame.image.load('gameAssets/minerLeftJump.png')
minerRightJump = pygame.image.load('gameAssets/minerRightJump.png')
batStill = pygame.image.load('gameAssets/batStill.png')
bat1 = pygame.image.load('gameAssets/bat1.png')
bat2 = pygame.image.load('gameAssets/bat2.png')
skeleton1 = pygame.image.load('gameAssets/skeleton1.png')
skeleton2 = pygame.image.load('gameAssets/skeleton2.png')
ratRight1 = pygame.image.load('gameAssets/ratRight1.png')
ratRight2 = pygame.image.load('gameAssets/ratRight2.png')
ratLeft1 = pygame.image.load('gameAssets/ratLeft1.png')
ratLeft2 = pygame.image.load('gameAssets/ratLeft2.png')
volume1 = pygame.image.load('gameAssets/volume1.png')
volume2 = pygame.image.load('gameAssets/volume2.png')
volume3 = pygame.image.load('gameAssets/volume3.png')
volume4 = pygame.image.load('gameAssets/volume4.png')


class Arrow(pygame.sprite.Sprite):
	def __init__(self,arrowDir,startX,startY):
		super().__init__()
		self.bounceRange = 10
		self.image = arrow
		self.arrowDir = arrowDir
		self.startX = startX
		self.startY = startY
		self.rewind = False
		if self.arrowDir == "left":
			self.image = pygame.transform.flip(self.image,True,False)
			self.rect = self.image.get_rect(topleft=(startX,startY))
		elif self.arrowDir == "right":
			self.rect = self.image.get_rect(topleft=(startX,startY))
		elif self.arrowDir == "down":
			self.image = pygame.transform.rotate(self.image,-90)
			self.rect = self.image.get_rect(topleft=(startX,startY))
		elif self.arrowDir == "up":
			self.image = pygame.transform.rotate(self.image,90)
			self.rect = self.image.get_rect(topleft=(startX,startY))
		

	def update(self,frame):
		if frame % 3 == 0: #slow animation speed down
			if self.arrowDir == "left":
				if self.rect.x <= self.startX+self.bounceRange and not self.rewind:
					self.rect.x+=1
					if self.rect.x >= self.startX+self.bounceRange:
						self.rewind = True
				if self.rect.x >= self.startX and self.rewind:
					self.rect.x-=1
					if self.rect.x <= self.startX:
						self.rewind = False
			elif self.arrowDir == "right":
				if self.rect.x >= self.startX-self.bounceRange and not self.rewind:
					self.rect.x-=1
					if self.rect.x <= self.startX-self.bounceRange:
						self.rewind = True
				if self.rect.x <= self.startX and self.rewind:
					self.rect.x+=1
					if self.rect.x >= self.startX:
						self.rewind = False
			elif self.arrowDir == "down":
				if self.rect.y >= self.startY-self.bounceRange and not self.rewind:
					self.rect.y-=1
					if self.rect.y <= self.startY-self.bounceRange:
						self.rewind = True
				if self.rect.y <= self.startY and self.rewind:
					self.rect.y+=1
					if self.rect.y >= self.startY:
						self.rewind = False
			elif self.arrowDir == "up":
				if self.rect.y <= self.startY+self.bounceRange and not self.rewind:
					self.rect.y+=1
					if self.rect.y >= self.startY+self.bounceRange:
						self.rewind = True
				if self.rect.y >= self.startY and self.rewind:
					self.rect.y-=1
					if self.rect.y <= self.startY:
						self.rewind = False


class Player(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = minerIdle
		self.rect = self.image.get_rect(topleft=(x,y))
		self.direction = 0

	def update(self,frame):
		if self.direction == -1:
			if frame <= 30:
				self.image = minerLeftWalk
			else:
				self.image = minerLeftWalk2
		elif self.direction == 1:
			if frame <= 30:
				self.image = minerRightWalk
			else:
				self.image = minerRightWalk2
		elif self.direction == 2:
			self.image = minerIdleJump
		else:
			self.image = minerIdle

class PlayerLevel10(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = minerIdle
		self.rect = self.image.get_rect(topleft=(x,y))
		self.direction = 0
		self.isJumping = False
		self.startingY = self.rect.y
		self.isGrounded = False

	def update(self,frame):
		if self.isJumping:
			self.rect.y -= 12
		if self.rect.y <= self.startingY - 120:
			self.isJumping = False

		if self.direction == 0:
			if self.isJumping:
				self.image = minerIdleJump
			else:
				self.image = minerIdle

		if self.direction == 1:
			if self.isJumping:
				self.image = minerLeftJump
			elif frame <= 30:
				self.image = minerLeftWalk
			else:
				self.image = minerLeftWalk2
		if self.direction == 2:
			if self.isJumping:
				self.image = minerRightJump
			elif frame <= 30:
				self.image = minerRightWalk
			else:
				self.image = minerRightWalk2

class LavaLevel10(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = level10Lava
		self.rect = self.image.get_rect(topleft=(x,y))
		self.topOut = False

	def update(self, scrollSpeed):
		if self.rect.y >= 700 and not self.topOut:
			self.rect.y -= scrollSpeed
		if self.topOut and self.rect.y >= 240:
			self.rect.y -= scrollSpeed*2

class FinishBlockLevel10(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = level3Finish
		self.rect = self.image.get_rect(topleft=(x,y))
	def update(self, scrollSpeed):
		if self.rect.y <= 75:
			self.rect.y += scrollSpeed

class floorBlockLevel10(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.Surface((32,32))
		self.image.fill((0,0,0))
		self.rect = self.image.get_rect(topleft=(x,y))

	def update(self, scrollSpeed):
		self.rect.y += scrollSpeed

		if self.rect.y >= 900:
			self.kill()
		
class topFloorBlockLevel10(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.Surface((32,32))
		self.image.fill((0,0,0))
		self.rect = self.image.get_rect(topleft=(x,y))
		self.stopScrolling = False
	def update(self, scrollSpeed):
		if self.rect.y <= 200:
			self.rect.y += scrollSpeed
		else:
			self.stopScrolling = True
	def getStopScrolling(self):
		return self.stopScrolling

class Level10Background(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = level1Background
		self.rect = self.image.get_rect(topleft=(x,y))

	def update(self, scrollSpeed):
		self.rect.y += scrollSpeed

class Level1Background(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = level1Background
		self.rect = self.image.get_rect(topleft=(x,y))

	def update(self, scrollSpeed):
		self.rect.y -= scrollSpeed

class PlayerTopView(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = minerTopViewIdle
		self.rect = self.image.get_rect(topleft=(x,y))
		self.direction = 0

	def update(self,frame):
		if self.direction == 1: #left
			if frame <= 30:
				self.image = minerTopView7
			else:
				self.image = minerTopView8
		elif self.direction == 2: #right
			if frame <= 30:
				self.image = minerTopView5
			else:
				self.image = minerTopView6
		elif self.direction == 3: #up
			if frame <= 30:
				self.image = minerTopView1
			else:
				self.image = minerTopView2
		elif self.direction == 4: #down
			if frame <= 30:
				self.image = minerTopView3
			else:
				self.image = minerTopView4
		else:
			self.image = minerTopViewIdle



pipesInitial = [
	[[1,1,1,1],[1,1,0,1],[1,1,1,0],[1,1,0,0],[1,1,0,0],[0,0,0,1]],
	[[1,1,1,0],[1,0,1,0],[1,1,0,1],[0,1,1,1],[1,1,0,0],[1,1,1,1]],
	[[1,1,0,0],[1,0,1,1],[0,1,1,0],[1,1,0,1],[1,1,0,0],[1,1,0,0]],
	[[1,1,0,0],[1,1,0,0],[1,0,0,0],[1,1,1,0],[1,1,1,1],[1,1,0,0]],
	[[1,1,0,0],[0,1,0,0],[1,1,0,1],[1,1,0,0],[1,1,1,0],[0,1,0,1]],
	[[1,1,0,0],[0,1,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,0],[1,1,0,0]]
]

class Valve(pygame.sprite.Sprite):
	def __init__(self,x,y,pipes, valveNumber):
		super().__init__()
		self.image = valveEmptyImage
		self.rect = self.image.get_rect(topleft=(x,y))
		self.pipes = pipes
		
		self.valveNumber = valveNumber
		self.full = False

	def rotate(self):
		temp = self.pipes.copy()
		self.pipes[0] = temp[3]
		self.pipes[1] = temp[0]
		self.pipes[2] = temp[1]
		self.pipes[3] = temp[2]
		
	def update(self):
		if self.full:
			self.image = valveFullImage
		if self.full == False:
			self.image = valveEmptyImage

class ValveSwitch(pygame.sprite.Sprite):
	def __init__(self,x,y,valvesAffected):
		super().__init__()
		self.image = valveSwitch
		self.rect = self.image.get_rect(topleft=(x,y))
		self.valvesAffected = valvesAffected

	def update(self):
		pass

def dfsValve(adj, visited, s, res):
	visited[s] = True
	res.append(s)

	# Recursively visit all adjacent vertices that are not visited yet
	for i in range(len(adj)):
		if adj[s][i] == 1 and not visited[i]:
			dfsValve(adj, visited, i, res)

def DFS(adj, source):
	visited = [False] * len(adj)
	res = []
	dfsValve(adj, visited, source, res)  # Start DFS from vertex 0
	return res

def add_edge(adj, s, t):
	adj[s][t] = 1
	adj[t][s] = 1  # Since it's an undirected graph



class PlayerMinecart(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = minecartPlayer
		self.rect = self.image.get_rect(topleft=(x,y))
		self.isJumping = False
		self.startingY = self.rect.y
		self.isGrounded = False
 
	def update(self):
		if self.isGrounded == False and self.isJumping == False:
			self.rect.y += 6

		if self.isJumping:
			self.image = minecartPlayerJump
			self.rect.y -= 6

			if self.rect.y <= self.startingY - 110:
				self.isJumping = False
				self.image = minecartPlayer

class floorBlock(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.Surface((32,32))
		self.image.fill((0,0,0))
		self.rect = self.image.get_rect(topleft=(x,y))

	def update(self, scrollSpeed):
		self.rect.y -= scrollSpeed

		if self.rect.y <= -32:
			self.kill()
		
class bottomFloorBlock(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.Surface((32,32))
		self.image.fill((0,0,0))
		self.rect = self.image.get_rect(topleft=(x,y))
		self.stopScrolling = False
	def update(self, scrollSpeed):
		if self.rect.y >= 868 and not self.stopScrolling:
			self.rect.y -= scrollSpeed
		else:
			self.stopScrolling = True
	def getStopScrolling(self):
		return self.stopScrolling
		

class MinecartFinishBlock(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = level3Finish
		self.rect = self.image.get_rect(topleft=(x,y))
	def update(self, scrollSpeed):
		self.rect.x -= scrollSpeed

class FinishBlock(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = level3Finish
		self.rect = self.image.get_rect(topleft=(x,y))
	def update(self, scrollSpeed):
		if self.rect.y >= 736:
			self.rect.y -= scrollSpeed

class FinishLevel2(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = finishLevel2
		self.rect = self.image.get_rect(topleft=(x,y))
	def update(self):
		pass

class stillFloorBlock(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.Surface((32,32))
		self.image.fill((0,0,0))
		self.rect = self.image.get_rect(topleft=(x,y))
	def update(self):
		pass

class SidescrollFloorBlock(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.Surface((32,32))
		self.image.fill((0,0,0))
		self.rect = self.image.get_rect(topleft=(x,y))
	def update(self,scrollSpeed):
		self.rect.x -= scrollSpeed
		if self.rect.x <= -32:
			self.kill()

class SidescrollKillBlock(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = dynamite
		self.rect = self.image.get_rect(topleft=(x,y))
	def update(self, scrollSpeed):
		self.rect.x -= scrollSpeed
		if self.rect.x <= -32:
			self.kill()

class SidescrollUpRail(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = minecartRailUp
		self.rect = self.image.get_rect(topleft=(x,y))
	def update(self, scrollSpeed):
		self.rect.x -= scrollSpeed
		if self.rect.x <= -32:
			self.kill()
class SidescrollUpRailTopLeft(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = minecartRailUpTopLeft
		self.rect = self.image.get_rect(topleft=(x,y))
	def update(self,scrollSpeed):
		self.rect.x -= scrollSpeed
		if self.rect.x <= -32:
			self.kill()
class SidescrollUpRailBottomRight(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = minecartRailUpBottomRight
		self.rect = self.image.get_rect(topleft=(x,y))
	def update(self, scrollSpeed):
		self.rect.x -= scrollSpeed
		if self.rect.x <= -32:
			self.kill()

class SidescrollDownRail(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = minecartRailDown
		self.rect = self.image.get_rect(topleft=(x,y))
	def update(self,scrollSpeed):
		self.rect.x -= scrollSpeed
		if self.rect.x <= -32:
			self.kill()
class SidescrollDownRailBottomLeft(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = minecartRailDownBottomLeft
		self.rect = self.image.get_rect(topleft=(x,y))
	def update(self,scrollSpeed):
		self.rect.x -= scrollSpeed
		if self.rect.x <= -32:
			self.kill()
class SidescrollDownRailTopRight(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = minecartRailDownTopRight
		self.rect = self.image.get_rect(topleft=(x,y))
	def update(self,scrollSpeed):
		self.rect.x -= scrollSpeed
		if self.rect.x <= -32:
			self.kill()

class SidescrollStraightRail(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = minecartRailStraight
		self.rect = self.image.get_rect(topleft=(x,y))
	def update(self,scrollSpeed):
		self.rect.x -= scrollSpeed
		if self.rect.x <= -32:
			self.kill()

class SidescrollBackground(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = minecartLevelBackground
		self.rect = self.image.get_rect(topleft=(x,y))
	def update(self, scrollSpeed):
		self.rect.x -= scrollSpeed

class Torch(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = torchImage
		self.rect = self.image.get_rect(topleft=(x,y))
		self.collected = False
	def update(self):
		pass

class playerLevel3(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = minerIdle
		self.rect = self.image.get_rect(topleft=(x,y))
		self.direction = 0   #  0:idle   1:left   2:right

	def update(self,frame):
		if self.direction == 0:
			self.image = minerIdle
		if self.direction == 1:
			if frame <= 15:
				self.image = minerLeftWalk
			else:
				self.image = minerLeftWalk2
		if self.direction == 2:
			if frame <= 15:
				self.image = minerRightWalk
			else:
				self.image = minerRightWalk2

class Level6FloorBlock(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.Surface((32,32))
		self.image.fill((0,0,0))
		self.rect = self.image.get_rect(topleft=(x,y))

	def update(self, playerX, playerSpeed, direction):
		self.rect.x += (playerSpeed-1)*direction
		
   

class Level6Player(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = minerSwimmingIdle
		self.rect = self.image.get_rect(topleft=(x,y))
		self.direction = 0   #  different than playerDirection variable and param

	def update(self, playerDirection,frame):
		if playerDirection == 1:
			if frame <= 30:
				self.image = minerSwimming1
			else:
				self.image = minerSwimming2
		else:
			self.image = minerSwimmingIdle

class Level6Enemy1(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = fish
		self.rect = self.image.get_rect(topleft=(x,y))

	def update(self,playerSpeed, direction):
		if direction == 1:
			self.rect.x -= 1
		elif direction == -1:
			self.rect.x -= 3
		else:
			self.rect.x -= 2

class Level6Enemy2(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = squid
		self.rect = self.image.get_rect(topleft=(x,y))
		self.topRange = self.rect.y - 150
		self.bottomRange = self.rect.y + 150
		self.direction = 1
		self.collidedWall = False

	def update(self, playerX, playerSpeed, direction):

		if self.rect.y == self.topRange:
			self.direction = 1
		if self.rect.y == self.bottomRange:
			self.direction = -1
		if self.collidedWall:
			self.direction = self.direction * -1
			self.collidedWall = False

		self.rect.x += (playerSpeed-1)*direction

		self.rect.y += self.direction

class Level6Dynamite(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = dynamite
		
		self.rect = self.image.get_rect(topleft=(x,y))

	def update(self, playerX, playerSpeed, direction):
		self.rect.x += (playerSpeed-1)*direction

class Level6Finish(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.Surface((32,32))
		self.image.fill((0,0,255))
		self.rect = self.image.get_rect(topleft=(x,y))

	def update(self, playerX, playerSpeed, direction):
		self.rect.x += (playerSpeed-1)*direction





class Level8Player(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = minerIdle
		self.rect = self.image.get_rect(topleft=(x,y))
		self.direction = 0   #  different than playerDirection variable and param
		self.previousDirection = 1
		self.attacking = False
		self.attackingTrack = 0
		self.attackingCooldown = 0
		

	def update(self,frame):
		if self.direction == 1:
			if frame <= 30:
				if self.attacking:
					self.image = minerIdleJump
				else:
					self.image = minerLeftWalk
			else:
				if self.attacking:
					self.image = minerIdleJump
				else:
					self.image = minerLeftWalk2
		elif self.direction == 2:
			if frame <= 30:
				if self.attacking:
					self.image = minerIdleJump
				else:
					self.image = minerRightWalk
			else:
				if self.attacking:
					self.image = minerIdleJump
				else:
					self.image = minerRightWalk2
		else:
			if self.attacking:
				if self.previousDirection == 1:
					self.image = minerIdleJump
				elif self.previousDirection == 2:
					self.image = minerIdleJump
			else:
				self.image = minerIdle


		if self.attacking:
			self.attackingTrack += 1
			if self.attackingTrack >= 30:
				self.attackingCooldown = 0
				self.attackingTrack = 0
				self.attacking = False
		if not self.attacking:
			self.attackingCooldown += 1

	def attack(self):
		if not self.attacking and self.attackingCooldown >= 15:
			self.attacking = True


class Level8Enemy1(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.Surface((32,32))
		self.rect = self.image.get_rect(topleft=(x,y))
		self.image.fill((0,0,100))
		self.direction = 0   #  different than playerDirection variable and param

	def update(self, playerPosX):
		if self.rect.x <= playerPosX:
			self.rect.x += 1
		if self.rect.x >= playerPosX:
			self.rect.x -= 1

class Level8Enemy2(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.Surface((32,32))
		self.rect = self.image.get_rect(topleft=(x,y))
		self.image.fill((0,0,255))
		self.direction = 0   #  different than playerDirection variable and param

	def update(self, playerPosX):
		if self.rect.x <= playerPosX:
			self.rect.x += 1
		if self.rect.x >= playerPosX:
			self.rect.x -= 1

class Level8Floor(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.Surface((820,300))
		self.rect = self.image.get_rect(topleft=(x,y))
		self.image.fill((0,0,0))

	def update(self):
		pass







class Level4FloorBlock(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.Surface((32,32))
		self.image.fill((0,0,0))
		self.rect = self.image.get_rect(topleft=(x,y))

	def update(self, scrollSpeed,frame):
		self.rect.x -= scrollSpeed

class Level4Finish(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = pygame.Surface((32,32))
		self.rect = self.image.get_rect(topleft=(x,y))
	
	def update(self, scrollSpeed,frame):
		self.rect.x -= scrollSpeed

class Level4ExitSign(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = level3Finish
		self.rect = self.image.get_rect(topleft=(x,y))
	
	def update(self, scrollSpeed,frame):
		self.rect.x -= scrollSpeed

class Level4Player(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = minerIdle
		self.rect = self.image.get_rect(topleft=(x,y))
		self.direction = 0 #0:idle  1:left  2:right  3:up  4:down
		self.isJumping = False
		self.startingY = self.rect.y
		self.isGrounded = False

	def update(self,frame):
		if self.isJumping:
			self.rect.y -= 12
		if self.rect.y <= self.startingY - 120:
			self.isJumping = False

		if self.direction == 0:
			if self.isJumping:
				self.image = minerIdleJump
			else:
				self.image = minerIdle

		if self.direction == 1:
			if self.isJumping:
				self.image = minerLeftJump
			elif frame <= 30:
				self.image = minerLeftWalk
			else:
				self.image = minerLeftWalk2
		if self.direction == 2:
			if self.isJumping:
				self.image = minerRightJump
			elif frame <= 30:
				self.image = minerRightWalk
			else:
				self.image = minerRightWalk2

class Level4Dynamite(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = dynamite
		self.rect = self.image.get_rect(topleft=(x,y))

	def update(self, scrollSpeed,frame):
		self.rect.x -= scrollSpeed

class Level4Enemy1(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = ratRight2
		self.rect = self.image.get_rect(topleft=(x,y))
		self.speed = 1
		self.direction = 1

	def update(self,scrollSpeed,frame):
		self.rect.x -= scrollSpeed

		self.rect.x += self.direction * self.speed

		if self.direction == 1:
			if frame <= 30:
				self.image = ratRight2
			else:
				self.image = ratRight1
		if self.direction == -1:
			if frame <= 30:
				self.image = ratLeft2
			else:
				self.image = ratLeft1

class Level4Enemy2(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = batStill
		self.rect = self.image.get_rect(topleft=(x,y))
		self.spotted = False
		self.swoop = False
		self.xCor = 81
		self.yInitial = y
		self.endPath = False

	def update(self, scrollSpeed,frame):
		self.rect.x -= scrollSpeed

		if self.spotted:
			if frame <= 30:
				self.image = bat2
			else:
				self.image = bat1

			yCor = 0.001*self.xCor**2
			self.rect.x -= 1
			if self.xCor >= 0:
				self.rect.y += yCor
			if self.xCor < 0:
				self.rect.y -= yCor
			self.xCor -= 1

			if self.rect.y < self.yInitial-64:
				self.spotted = False
				self.endPath = True
		if self.endPath:
			self.rect.x -=1
			self.rect.y -=1


		if self.rect.y <= 0:
			self.kill()

class Level4Enemy3(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = skeleton1
		self.rect = self.image.get_rect(topleft=(x,y))
		self.direction = 0 #1:left  2:right  3:up  4:down
		self.isJumping = False
		self.startingY = self.rect.y
		self.isGrounded = True
 
	def update(self, scrollSpeed,frame):
		self.rect.x -= scrollSpeed

		if self.isJumping:
			self.image = skeleton2
			self.rect.y -= 9
		if self.rect.y <= self.startingY - 150:
			self.isJumping = False
		if self.isGrounded:
			self.image = skeleton1

class BackgroundLevel4(pygame.sprite.Sprite):
	def __init__(self,x,y):
		super().__init__()
		self.image = level4Background
		self.rect = self.image.get_rect(topleft=(x,y))
 
	def update(self, scrollSpeed,frame):
		self.rect.x -= scrollSpeed