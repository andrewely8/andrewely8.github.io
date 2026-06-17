#capitalistMining Created by Andrew Ely 
import pygame, sys, math, random, asyncio
import time as Time
from decimal import Decimal
from config import *
from utils import *
from sprites import *
import levels

LEVEL_CLASSES = { 0 : levels.Level1, 1 : levels.Level2, 2 : levels.Level3, 3 : levels.Level4, 4 : levels.Level5, 
                  5 : levels.Level4, 6 : levels.Level7, 7 : levels.Level5, 8 : levels.Level9, 9 : levels.Level10}

upgradeWindow = pygame.Rect(100, 800, 500, 45)
firstGameLaunch = True
firstLaunchArrow = Arrow("left",505,554)

storeItemObjects = []
r = 95
for s in STORE_ITEMS_DATA:
    newRect = (20,r,45,45)
    newItem = StoreItem(newRect,s)
    storeItemObjects.append(newItem)
    r+=60

upgradeItemObjects = []
for data in UPGRADE_ITEMS_DATA:
    newRect = (data["position"],805,35,35)
    newItem = UpgradeItem(newRect,data)
    upgradeItemObjects.append(newItem)

game_state = gameState(True,"startScreen",0,[volume1,volume2,volume3,volume4],[1.0,0.6,0.3,0.0],True,True,True,4,False,True,0,None,levelSelect,0,True,0,[0,0,1000,2000,3000,4000,250000],1,1,storeItemObjects,upgradeItemObjects)

#screen buttons
storeButton = button((WINDOW_WIDTH//3.5,WINDOW_HEIGHT//1.8,WINDOW_WIDTH//2.4,WINDOW_HEIGHT//6),txt=["Store"],fontColor=BLACK,lineSpace="CENTER",lineSpaceInc=0,font=font5,backgroundColor=(225, 180, 10),borderColor=BLACK,borderWidth=2,borderRadius=2)
mineButton = button((WINDOW_WIDTH//3.5, WINDOW_HEIGHT//2.85, WINDOW_WIDTH//2.4, WINDOW_HEIGHT//6),txt=["Mine"],fontColor=BLACK,lineSpace="CENTER",lineSpaceInc=0,font=font5,backgroundColor=(225, 180, 10),borderColor=BLACK,borderWidth=2,borderRadius=2)
launchButton = button((50,675,620,150),txt=gameLaunchMessage,fontColor=BLACK,lineSpace=10,lineSpaceInc=25,font=font3,backgroundColor=GRAY,borderColor=BLACK,borderWidth=2,borderRadius=2)
changeVolumeButton = button((600,50,64,64),backgroundColor=GRAY,borderColor=BLACK,borderWidth=3,borderRadius=3,image=volume1)
startScreenButtons = [storeButton,mineButton,launchButton,changeVolumeButton]
mainMenuButton = button((WINDOW_WIDTH-60,WINDOW_HEIGHT-60,48,48),txt=["MAIN","MENU"],fontColor=BLACK,lineSpace=5,lineSpaceInc=15,font=font4,backgroundColor=GRAY,borderColor=BLACK,borderWidth=2,borderRadius=2)
buyModeButton = button((640,32,64,40),txt=buyModeQuantityList[0],fontColor=BLACK,lineSpace="CENTER",lineSpaceInc=0,font=font4,backgroundColor=GRAY,borderColor=BLACK,borderWidth=2,borderRadius=2)
buyModeExtraButton = button((635,5,74,28),txt=["BUY IN","LOTS OF"],fontColor=BLACK,lineSpace=0,lineSpaceInc=10,font=font4,backgroundColor=GRAY,borderColor=BLACK,borderWidth=2,borderRadius=2)
hintButton = button(hints[0]["rect"],txt=hints[0]["text"],fontColor=BLACK,lineSpace=5,lineSpaceInc=25,font=font3,backgroundColor=GRAY,borderColor=BLACK,borderWidth=2,borderRadius=2)

hintArrows = [
    Arrow("down",26,24),
    Arrow("left",500,100),
    Arrow("right",15,735),
    Arrow("up",656,65),
    None,
    Arrow("down",670,780),
    Arrow("right",30,805)]



#function to display the entire start screen, this is called in the main game loop
#when on the start screen.
def startScreen(gameState):
    #event loop 
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if changeVolumeButton.rect.collidepoint(mouse_pos):
            changeVolumeButton.mouseHover = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                gameState.gameVolumeIndex += 1
                if gameState.gameVolumeIndex > len(gameState.gameVolumeImages)-1:
                    gameState.gameVolumeIndex = 0
                pygame.mixer.music.set_volume(gameState.gameVolume[gameState.gameVolumeIndex])
                if gameState.gameVolumeIndex == 3:
                    gameState.sfxOn = False
                elif gameState.gameVolumeIndex != 3:
                    gameState.sfxOn = True
                changeVolumeButton.setImage(gameState.gameVolumeImages[gameState.gameVolumeIndex])
        elif not changeVolumeButton.rect.collidepoint(mouse_pos):
            changeVolumeButton.mouseHover = False

        if storeButton.rect.collidepoint(mouse_pos):
            storeButton.mouseHover = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if gameState.sfxOn:
                    clickButtonSound.play()
                storeButton.mouseHover = False
                gameState.screen = "storeScreen"
                launchButton.visable = False
        elif not storeButton.rect.collidepoint(mouse_pos):
            storeButton.mouseHover = False

        if mineButton.rect.collidepoint(mouse_pos) and not gameState.mineLocked:
            mineButton.mouseHover = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if gameState.sfxOn:
                    clickButtonSound.play()
                mineButton.mouseHover = False
                gameState.screen = "mineScreen"
        elif not mineButton.rect.collidepoint(mouse_pos):
            mineButton.mouseHover = False

        if launchButton.rect.collidepoint(mouse_pos) and launchButton.visable:
            launchButton.mouseHover = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
               launchButton.visable = False
        elif not launchButton.rect.collidepoint(mouse_pos):
            launchButton.mouseHover = False

    #Draw to screen
    DISPLAYSURF.blit(background, (0,0))
    DISPLAYSURF.blit(logo, (275, 100))
    if launchButton.visable:        
        firstLaunchArrow.update(gameState.frame)
        DISPLAYSURF.blit(firstLaunchArrow.image,(firstLaunchArrow.rect.x,firstLaunchArrow.rect.y))
    for b in startScreenButtons:
        if b.visable:
            b.drawButton()
    if gameState.profit >= 2500:
        gameState.mineLocked = False
    if gameState.mineLocked:
        DISPLAYSURF.blit(chains, (125, 225))

    pygame.display.flip()






def mineScreen(gameState):

    DISPLAYSURF.blit(background, (0,0))
    mainMenuButton.drawButton()
    drawTitle('Revenue:', 10, 20, font1)
    drawNumber(gameState.profit, 120, 20, font1, "left")

    mouse_pressed = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    for level in levelSelect:
        r = pygame.Rect(level['rectangle'])
        if r.collidepoint(mouse_pos):
            levelButtonOpacity = 75
        else:
            levelButtonOpacity = 0
        levelButtonSurface = pygame.Surface((level['rectangle'][2],level['rectangle'][3]))
        levelButtonSurface.set_alpha(levelButtonOpacity)     
        levelButtonSurface.fill((0,0,0))     
        DISPLAYSURF.blit(levelButtonSurface, (level['rectangle'][0],level['rectangle'][1]))

        pygame.draw.rect(DISPLAYSURF, BLACK, level['rectangle'], 5)
        drawTitle('Level ' + str((level['levelNumber']+1)) , level['rectangle'][0]+10, level['rectangle'][1]+15, font1)
        if not level['purchased']:
            DISPLAYSURF.blit(unlockChain, (level['rectangle'][0], level['rectangle'][1]-10))
            drawTitle('cost ' , level['rectangle'][0]+135, level['rectangle'][1]+75, font1)
            drawNumber(level['cost'], level['rectangle'][0]+150, level['rectangle'][1]+90, font2, "center")
        if level['purchased']:
            instructText = levelInstructions[level['levelNumber']]
            lineSpace = 25
            lineSpaceInc = 15
            for line in instructText:
                textSurface = font4.render(line,True,BLACK)
                textRect = textSurface.get_rect()
                textRect.center = r.center
                DISPLAYSURF.blit(textSurface,(textRect[0],level['rectangle'][1]+lineSpace))
                lineSpace += lineSpaceInc
        if level['completed']:
            DISPLAYSURF.blit(checkBox, (level['rectangle'][0]+60, level['rectangle'][1]-10))


    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:

            pygame.quit()
            sys.exit()

        #Return to main menu
        if mainMenuButton.rect.collidepoint(mouse_pos):
            mainMenuButton.mouseHover = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                gameState.screen = "startScreen"
                mainMenuButton.mouseHover = False
        elif not mainMenuButton.rect.collidepoint(mouse_pos):
            mainMenuButton.mouseHover = False


        for level in levelSelect:
            r = pygame.Rect(level['rectangle'])
            if r.collidepoint(mouse_pos):
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if gameState.profit >= level['cost'] and not level['purchased']:
                        level['purchased'] = True
                        gameState.profit -= level['cost']
                        if gameState.sfxOn:
                            clickButtonSound.play()
                    elif level['purchased']:
                        currentLevel = level['levelNumber']
                        gameState.screen = currentLevel
                        gameState.level = LEVEL_CLASSES[currentLevel](currentLevel)
                        gameState.levelActive = True
                        changeMusic('gameAssets/audio/levelPlay.ogg',gameState.gameVolume[gameState.gameVolumeIndex])

    pygame.display.flip()




def storeScreen(gameState):

    #checks if there are remaining store items
    if gameState.itemsIndex <= len(gameState.storeItems) - 1:
        #check if next item should be added
        if gameState.profit >= gameState.storeItems[gameState.itemsIndex].cost * 0.6:
            gameState.itemsIndex += 1

    #checks if there are remaining upgrade items
    if gameState.upgradesIndex <= len(gameState.upgradeItems) - 1:
        #check if the next item should be added 
        if gameState.profit >= gameState.upgradeItems[gameState.upgradesIndex].cost * 0.6:
            gameState.upgradesIndex += 1

    #Hint progress
    #This is outside of the event loop so that this behavior still functions when no user inputs.
    if gameState.hintProgress < len(hints):
        if gameState.profit >= hintCheckPoints[gameState.hintProgress]:
            hintButton.changeRect(hints[gameState.hintProgress]["rect"])
            hintButton.changeText(hints[gameState.hintProgress]["text"])
            gameState.hintButtonActive = True
    #Alternate action based ways to close the displayed hints like purchasing first item closes first hint, etc.
    if gameState.hintProgress == 0:
        if gameState.storeItems[0].amountOwned >= 1:
            gameState.hintProgress += 1
            gameState.hintButtonActive = False

    if gameState.hintProgress == 1:
        if gameState.storeItems[0].length >= 1:
            gameState.hintProgress +=1
            gameState.hintButtonActive = False
    if gameState.hintProgress == 2:
        if gameState.storeItems[0].manager == True:
            gameState.hintProgress+=1
            gameState.hintButtonActive = False
    if gameState.hintProgress == 4:
       if len(gameState.storeItems) >= 7:
        gameState.hintProgress+=1
        gameState.hintButtonActive = False
    if gameState.hintProgress == 6:
        if gameState.upgradeItems[0].active == True:
            gameState.hintProgress +=1
            gameState.hintButtonActive=False


    mouse_pressed = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #Return to main menu button
        if mainMenuButton.rect.collidepoint(mouse_pos):
            mainMenuButton.mouseHover = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                gameState.screen = "startScreen"
                mainMenuButton.mouseHover = False
        elif not mainMenuButton.rect.collidepoint(mouse_pos):
            mainMenuButton.mouseHover = False

        #Buy mode button
        if buyModeButton.rect.collidepoint(mouse_pos):
            buyModeButton.mouseHover = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if gameState.buyModeQuantityIndex < len(buyModeQuantityList) - 1:
                    gameState.buyModeQuantityIndex += 1
                else:
                    gameState.buyModeQuantityIndex = 0
                buyModeButton.txt = [buyModeQuantityList[gameState.buyModeQuantityIndex]]
        elif not buyModeButton.rect.collidepoint(mouse_pos):
            buyModeButton.mouseHover = False

        #Hint Button(s)
        if gameState.hintButtonActive and hintButton.rect.collidepoint(mouse_pos):
            hintButton.mouseHover = True
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                gameState.hintButtonActive = False
                gameState.hintProgress += 1
        elif gameState.hintButtonActive and not hintButton.rect.collidepoint(mouse_pos):
            hintButton.mouseHover = False

        #Store Item buttons
        for item in gameState.storeItems:
            #StoreItem Buy Buttons
            if item.rect.collidepoint(mouse_pos):
                item.mouseHover = True
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if gameState.profit >= item.cost:
                        if gameState.buyModeQuantityIndex == 0:
                            if gameState.sfxOn:
                                clickButtonSound.play()
                            gameState.profit -= item.cost
                            item.amountOwned += 1
                            item.cost *= item.costMultiplier
                            item.gain += item.gainMultiplier
                        elif gameState.buyModeQuantityIndex == 1:
                            a = initialCosts[item.itemNumber]
                            b = item.costMultiplier
                            c = item.amountOwned
                            cost = a * (1 - b ** (c + 25)) / (1 - b) - a * (1 - b ** c)/(1 - b)
                            if gameState.profit >= cost:
                                if gameState.sfxOn:
                                    clickButtonSound.play()
                                gameState.profit -= cost
                                item.amountOwned += 25
                                item.cost = initialCosts[item.itemNumber] * item.costMultiplier ** (item.amountOwned)
                                item.gain = 1 * item.gainMultiplier * (item.amountOwned)
                        elif gameState.buyModeQuantityIndex == 2:
                            a = initialCosts[item.itemNumber]
                            b = item.costMultiplier
                            c = item.amountOwned
                            cost = a * (1 - b ** (c + 100)) / (1 - b) - a * (1 - b ** c)/(1 - b)
                            if gameState.profit >= cost:
                                if gameState.sfxOn:
                                    clickButtonSound.play()
                                gameState.profit -= cost
                                item.amountOwned += 100
                                item.cost = initialCosts[item.itemNumber] * item.costMultiplier ** (item.amountOwned)
                                item.gain = 1 * item.gainMultiplier * (item.amountOwned)
                        elif gameState.buyModeQuantityIndex == 3 and (gameState.profit >= item.cost):
                            if gameState.sfxOn:
                                clickButtonSound.play()
                            a = initialCosts[item.itemNumber]
                            b = item.costMultiplier
                            c = item.amountOwned
                            d = gameState.profit
                            logFunction = ((d*(b-1))/(a*(b ** c))) + 1
                            maxPurchase = math.floor(math.log(logFunction, b))
                            cost = a * (1 - b ** (c + maxPurchase)) / (1 - b) - a * (1 - b ** c)/(1 -b)
                            gameState.profit -= cost
                            item.amountOwned += maxPurchase
                            item.cost = initialCosts[item.itemNumber] * item.costMultiplier ** (item.amountOwned)
                            item.gain = 1 * item.gainMultiplier * (item.amountOwned)
            elif not item.rect.collidepoint(mouse_pos):
                item.mouseHover = False

            if (item.gainButtonRect.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONUP and event.button == 1 
                and item.amountOwned != 0 and item.manager == False):
                    item.active = True

            if item.managerButtonRect.collidepoint(mouse_pos):
                item.managerButtonHover = True

                if (gameState.profit >= item.managerCost and event.type == pygame.MOUSEBUTTONUP and item.manager == False 
                    and item.amountOwned >= 1 and event.button == 1):
                    if gameState.sfxOn:
                        clickButtonSound.play()
                    item.manager = True
                    gameState.profit -= item.managerCost

            elif not item.managerButtonRect.collidepoint(mouse_pos):
                item.managerButtonHover = False


        
        scrollItems = 0
        #upgrade window scroll logic 
        if upgradeWindow.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEWHEEL:
                if event.y > 0 and gameState.upgradeItems[gameState.upgradesIndex-1].rect.x > 560:
                     scrollItems = -20
                elif event.y < 0 and gameState.upgradeItems[0].rect.x < 100:
                    scrollItems = 20
        
        for item in gameState.upgradeItems:
            if scrollItems != 0:
                item.changeX(scrollItems)
        #upgrade purchase logic
            if (item.rect.collidepoint(mouse_pos) and upgradeWindow.collidepoint(mouse_pos)):
                item.mouseHover = True
                if gameState.profit >= item.cost and event.type == pygame.MOUSEBUTTONUP and event.button == 1 and item.active == False:
                    if gameState.sfxOn:
                        clickButtonSound.play()
                    item.active = True
                    gameState.profit -= item.cost
                    gameState.storeItems[item.itemInfluenced].gain *= item.effect
                    gameState.storeItems[item.itemInfluenced].gainMultiplier *= item.effect
            elif not (item.rect.collidepoint(mouse_pos) and upgradeWindow.collidepoint(mouse_pos)):
                item.mouseHover = False


    #Draw to screen
    DISPLAYSURF.blit(background,(0,0))
    drawTitle('Revenue:', 10, 20, font1)
    drawNumber(gameState.profit, 120, 20, font1, "left")
    drawTitle('cost', 75, 80, font3)
    drawTitle('number owned', 245, 80, font3)
    drawTitle('profit', 510, 80, font3)
    
    buyModeButton.drawButton()
    buyModeExtraButton.drawButton()
    if gameState.hintButtonActive:
        hintButton.drawButton()

    for i in range(gameState.itemsIndex):
        gameState.storeItems[i].update(gameState)
    for i in range(gameState.upgradesIndex):
        gameState.upgradeItems[i].update(gameState)
    for i in range(gameState.itemsIndex):
        gameState.storeItems[i].drawManagerButton(gameState)

    if gameState.itemsIndex < len(gameState.storeItems):
        DISPLAYSURF.blit(itemSillouete, (20, 155+((gameState.itemsIndex-1)*60)))

    upgradeWindowCoverRight = background.subsurface((600,805,125,50))
    upgradeWindowCoverLeft = background.subsurface((0,805,100,50))
    DISPLAYSURF.blit(upgradeWindowCoverRight, (600,805))
    DISPLAYSURF.blit(upgradeWindowCoverLeft, (0,805))
    mainMenuButton.drawButton()

    if gameState.upgradesIndex >= 10:
        drawTitle('<- SCROLL MOUSE ->', 265, 860, font4)

    if gameState.hintProgress < len(hints):
        if gameState.hintButtonActive:
            currentArrow = hintArrows[gameState.hintProgress]
            if currentArrow:
                currentArrow.update(gameState.frame)
                DISPLAYSURF.blit(currentArrow.image, (currentArrow.rect.x,currentArrow.rect.y))

    pygame.display.flip()


async def main(): #pygbag requires this function.

    #Game loop
    while game_state.running:
        await asyncio.sleep(0) #pygbag requires this sleep call.

        #Check if music ended, and replay
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.rewind()
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(game_state.gameVolume[game_state.gameVolumeIndex])
        
        #update frame
        clock.tick(60)
        game_state.frame +=1
        if game_state.frame >= 60:
            game_state.frame = 0

        #Display current game states screen
        if game_state.screen == "startScreen":
            startScreen(game_state)
        elif game_state.screen == "storeScreen":
            storeScreen(game_state)
        elif game_state.screen == "mineScreen":
            mineScreen(game_state)
        elif game_state.levelActive:
            game_state.level.update(game_state)



asyncio.run(main()) #pygbag requires this call.