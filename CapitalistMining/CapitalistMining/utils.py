import pygame,math
from config import * 
from collections import deque

class gameState():
    def __init__(self,running,screen,gameVolumeIndex,gameVolumeImages,gameVolume,mineLocked,firstGameLaunch,sfxOn,profit,levelActive,initializeLevel,frame,level,levelSelect,buyModeQuantityIndex,hintButtonActive,hintProgress,hintCheckPoints,itemsIndex,upgradesIndex,storeItems,upgradeItems):
        self.running = running 
        self.screen = screen
        self.gameVolumeIndex = gameVolumeIndex 
        self.gameVolumeImages = gameVolumeImages
        self.gameVolume = gameVolume
        self.mineLocked = mineLocked 
        self.firstGameLaunch = firstGameLaunch
        self.sfxOn = sfxOn 
        self.profit = profit 
        self.levelActive = levelActive 
        self.initializeLevel = initializeLevel 
        self.frame = frame 
        self.level = level 
        self.levelSelect = levelSelect 
        self.buyModeQuantityIndex = buyModeQuantityIndex 
        self.hintButtonActive = hintButtonActive 
        self.hintProgress = hintProgress 
        self.hintCheckPoints = hintCheckPoints
        self.itemsIndex = itemsIndex 
        self.upgradesIndex = upgradesIndex 
        self.storeItems = storeItems
        self.upgradeItems = upgradeItems



class UpgradeItem():
    def __init__(self,rect,itemData):
        self.x,self.y,self.w,self.h = rect
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.mouseHover = False
        self.surface = pygame.Surface((self.w,self.h))

        self.name = itemData["name"]
        self.cost = itemData["cost"]
        self.position = itemData["position"]
        self.itemNumber = itemData["itemNumber"]
        self.offset = itemData["offset"]
        self.effect = itemData["effect"]
        self.itemInfluenced = itemData["itemInfluenced"]
        self.active = itemData["active"]
        self.image = itemData["image"]

    def changeX(self,changeAmount):
        self.x += changeAmount
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.position += changeAmount

    def update(self,gameState):
        DISPLAYSURF.blit(self.image,(self.rect.x,self.rect.y))

        if self.mouseHover:
            self.surface.set_alpha(75)
            pygame.draw.rect(DISPLAYSURF, GRAY,(self.rect.x-73,772,195,31),border_radius=3)
            pygame.draw.rect(DISPLAYSURF, BLACK,(self.rect.x-73,772,195,31),width=2,border_radius=3)
            drawNumber(self.cost, self.rect.x-70, 793, font4, "left")
            drawTitle(self.name, self.rect.x-70, 780, font4)
        elif not self.mouseHover:
            self.surface.set_alpha(0)
        self.surface.fill((0,0,0))
        DISPLAYSURF.blit(self.surface, (self.rect.x,self.rect.y))

        if self.active:
            checkMarkImage = checkBox.subsurface((0,0,35,35))
            DISPLAYSURF.blit(checkMarkImage, (self.rect.x,805))



class StoreItem():
    def __init__(self,rect,itemData):
        self.x,self.y,self.w,self.h = rect
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.mouseHover = False
        self.surface = pygame.Surface((self.w,self.h))

        self.name = itemData["name"]
        self.cost = itemData["cost"]
        self.gain = itemData["gain"]
        self.amountOwned = itemData["amountOwned"] 
        self.itemNumber = itemData["itemNumber"]
        self.length = itemData["length"]
        self.speed = itemData["speed"]
        self.active = itemData["active"]
        self.manager = itemData["manager"]
        self.managerCost = itemData["managerCost"]
        self.costMultiplier = itemData["costMultiplier"]
        self.gainMultiplier = itemData["gainMultiplier"]
        self.image = itemData["image"]
        self.managerInfo = itemData["managerInfo"]

        self.gainButtonRect = pygame.Rect(305, self.y, 195, 45)
        self.managerButtonRect = pygame.Rect(self.y-30, 725, 45, 45)
        self.managerButtonImage = managerBoard.subsurface((0,self.itemNumber*58,45,45))
        self.managerButtonHover = False
        self.managerSurface = pygame.Surface((45,45))
        self.mileStones = deque(mileStones)
        self.currentMileStone = 0

    def drawManagerButton(self,gameState):
        DISPLAYSURF.blit(self.managerButtonImage,self.managerButtonRect)
        if self.manager:
            checkMarkImage = checkBox.subsurface((0,0,35,35))
            DISPLAYSURF.blit(checkMarkImage, (self.y-30,725))
        if self.managerButtonHover:
            self.managerSurface.set_alpha(75)
            pygame.draw.rect(DISPLAYSURF, GRAY, (self.y-94,645,180,75),border_radius=3)
            pygame.draw.rect(DISPLAYSURF, BLACK, (self.y-94,645,180,75),width=2,border_radius=3)
            lineSpace = 2
            lineSpaceInc = 16
            for line in self.managerInfo:
                textSurface = font4.render(line,True,BLACK)
                textRect = textSurface.get_rect()
                DISPLAYSURF.blit(textSurface,(self.y-90,645+lineSpace))
                lineSpace+=lineSpaceInc
            drawNumber(self.managerCost, self.y-90, 645+lineSpace+15, font1, "left")
        elif not self.managerButtonHover:
            self.managerSurface.set_alpha(0)
        self.managerSurface.fill((0,0,0))
        DISPLAYSURF.blit(self.managerSurface, self.managerButtonRect)

    def update(self,gameState):
        if self.image:
            DISPLAYSURF.blit(self.image, (self.x,self.y))

        if self.mouseHover:
            self.surface.set_alpha(75)
        elif not self.mouseHover:
            self.surface.set_alpha(0)
        self.surface.fill((0,0,0))
        DISPLAYSURF.blit(self.surface, (self.x,self.y))

        pygame.draw.rect(DISPLAYSURF,BLACK,self.rect,width=2)
        drawTitle(self.name, self.x+55, self.y+30, font1)

        if self.speed < 15:
            pygame.draw.rect(DISPLAYSURF, GREEN, (306, self.y, self.length, 44))
        elif self.manager:
            pygame.draw.rect(DISPLAYSURF, GREEN, (306, self.y, 194, 44))
        else:
            pygame.draw.rect(DISPLAYSURF, GREEN, (306, self.y, self.length, 44))

        if gameState.buyModeQuantityIndex == 0:
            quantity = 1
            drawNumToBuy = False
        elif gameState.buyModeQuantityIndex == 1:
            quantity = 25
            drawNumToBuy = True
        elif gameState.buyModeQuantityIndex == 2:
            quantity = 100
            drawNumToBuy = True
        elif gameState.buyModeQuantityIndex == 3:
            logFunction = ( (gameState.profit*(self.costMultiplier-1))/(initialCosts[self.itemNumber]*(self.costMultiplier ** self.amountOwned)))+1
            quantity = math.floor(math.log(logFunction ,self.costMultiplier))
            drawNumToBuy = True

        if drawNumToBuy:
            pygame.draw.rect(DISPLAYSURF, BLACK, (37,self.y+25,35,20), width=2,border_radius=2)
            pygame.draw.rect(DISPLAYSURF, BLACK, (37,self.y+25,35,20), border_radius=2)
            numToBuy = font4.render('{0}'.format(quantity), True, GRAY)
            DISPLAYSURF.blit(numToBuy,(40,self.y+25,25,25))

        costCalculation = self.cost * (self.costMultiplier**quantity - 1)/(self.costMultiplier - 1)
        if costCalculation == 0:
            costCalculation = self.cost
        drawNumber(costCalculation, 75, self.y+10, font1, "left")
        drawNumber(self.amountOwned, 295, self.y+10, font1, "right")
        drawNumber(self.gain, 510, self.y+10, font1, "left")
        

        pygame.draw.rect(DISPLAYSURF, BLACK, self.gainButtonRect, 2)
        #Gain button logic
        if self.length <= 195 and self.active or self.manager:
            self.length += self.speed
        if self.length >= 190:
            self.length = 0
            self.active = False
            gameState.profit += self.gain

        #mile Stone logic 
        while self.mileStones and self.amountOwned >= self.mileStones[0]:
            self.mileStones.popleft()
            self.speed *= 2



class button(object):
    def __init__(self,rect,txt=None,fontColor=None,lineSpace=None,lineSpaceInc=None,font=None,backgroundColor=None, borderColor=None, borderWidth = None,borderRadius=None,image=None):
        self.x,self.y,self.w,self.h = rect
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.txt = txt
        self.fontColor = fontColor
        if lineSpace == "CENTER":
            self.lineSpace = (self.h // 4)
        else:
            self.lineSpace = lineSpace
        self.lineSpaceInc = lineSpaceInc
        self.font = font
        self.surface = pygame.Surface((self.w,self.h))
        self.backgroundColor = backgroundColor
        self.borderColor = borderColor
        self.borderWidth = borderWidth
        self.borderRadius = borderRadius
        self.mouseHover = False
        self.image = image
        self.visable = True

    def setImage(self,newImage):
        self.image = newImage

    def changeRect(self,new_rect):
        self.x,self.y,self.w,self.h = new_rect
        self.rect = pygame.Rect(self.x,self.y,self.w,self.h)
        self.surface = pygame.Surface((self.w,self.h))

    def changeText(self,new_txt):
        self.txt = new_txt

    def drawButton(self):
        if self.backgroundColor:
            pygame.draw.rect(DISPLAYSURF,self.backgroundColor,self.rect,border_radius=self.borderRadius)
        if self.borderColor:
            pygame.draw.rect(DISPLAYSURF,self.borderColor,self.rect,width=self.borderWidth,border_radius=self.borderRadius)
        if self.image:
            DISPLAYSURF.blit(self.image, (self.x,self.y))

        if self.txt:
            lineSpace,lineSpaceInc = self.lineSpace,self.lineSpaceInc
            for line in self.txt:
                textSurface = self.font.render(line,True,self.fontColor)
                textRect = textSurface.get_rect()
                textRect.centerx = self.rect.centerx
                DISPLAYSURF.blit(textSurface,(textRect[0],self.y+lineSpace))
                lineSpace += lineSpaceInc

        if self.mouseHover:
            self.surface.set_alpha(75)
        elif not self.mouseHover:
            self.surface.set_alpha(0)
        self.surface.fill((0,0,0))
        DISPLAYSURF.blit(self.surface, (self.x,self.y))






def changeMusic(newMusicPath,currentVolume):
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()
    pygame.mixer.music.load(newMusicPath)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(currentVolume)







#Function to draw Titles to store Screen
def drawNumber(number, x, y, font, pos):
    number = round(number, 2)
    if number >= 100000000000:
        number = '{:.2E}'.format(number)
    else:
        number = '{:,}'.format(number)
    surface = font.render('{0}'.format(number), True, BLACK)
    rect = surface.get_rect()
    if pos == "left":
        rect.midleft = (x, y)
    if pos == "right":
        rect.midright = (x, y)
    if pos == 'center':
        rect.center = (x,y)
    DISPLAYSURF.blit(surface, rect)




def drawTitle(title, x, y, font):
    titleSurface = font.render(title, True, BLACK)
    titleRect = titleSurface.get_rect()
    titleRect.midleft = (x, y)
    DISPLAYSURF.blit(titleSurface, titleRect)


            