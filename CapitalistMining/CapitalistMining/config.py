import pygame
from sprites import *

#pygame initialization
pygame.mixer.pre_init(buffer=8192)
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Capitalist Mining')
pygame.display.set_icon(logo)
clickButtonSound = pygame.mixer.Sound("gameAssets/audio/clickButton.ogg")
pygame.mixer.music.load(gameMusic)
clock = pygame.time.Clock()


#CONSTANTS
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 900
WINDOW_ASPECT_RATIO = 900/720 
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH , WINDOW_HEIGHT))
BLACK = (0,0,0)
GREEN = (95, 180, 90)
GRAY = pygame.Color(230, 230, 230)
font1 = pygame.font.Font('gameAssets/fonts/freesansbold.ttf', 18)
font2 = pygame.font.Font('gameAssets/fonts/freesansbold.ttf', 16)
font3 = pygame.font.Font('gameAssets/fonts/BoldPixels.ttf', 24)
font4 = pygame.font.Font('gameAssets/fonts/BoldPixels.ttf', 18)
font5 = pygame.font.Font('gameAssets/fonts/monaco.ttf', 48)
buyModeQuantityList = ['1','25', '100', 'MAX']

gameLaunchMessage = [
    "Welcome to Capitalist Mining!",
    "The goal of the game is to beat all levels in the Mine.",
    "You will need to earn enough money to unlock the levels,",
    "by developing businesses in the Store.",
    "Vist the Store to begin earning money!",]

hints = {
    0: {"text": ["Welcome to the Store!","Here you will buy businesses to gain money,", "purchase your first business!"], "rect": (100,325,500,90)},
    1: {"text": ["Once you have a garden shovel,", "start using it!"], "rect": (120,325,480,60)},
    2: {"text": ["Managers run your businesses for you,","so you don't have to.","Buy your first manager!"], "rect": (120,600,480,90)},
    3: {"text": ["Buy mode lets you buy many", "of one business in one click!"], "rect": (70,555,580,80)},
    4: {"text": ["The speed of a business increases the more you buy!","every 25 of each business you own", "will increase that businesses speed."], "rect": (0,0,0,0)},
    5: {"text": ["Don't forget to check on your Mines!"], "rect": (255,855,400,30)},
    6: {"text": ["Upgrades increase a businesses profit!"], "rect": (100,855,415,30)},
}
hintCheckPoints = [0,0,1000,2000,3000,4000,250000]

levelInstructions = [
        ["USE A,D to move left and right,",
         "make it to the end of the level",
         "quickly before the roof collapses!"
        ],
        ["USE W,A,S,D to move,",
         "navigate through the maze",
         "to find the exit."
        ],
        ["USE A,D to move left and right,",
         "USE SPACE to activate lever,",
         "direct the flow of water."
        ],
        ["USE A,D to move left and right,",
         "SPACE to jump, avoid enemies",
         "and make it to the end."
        ],
        ["USE SPACE to jump,",
         "avoid Dynamite",
         "to beat the level!"
        ],
        ["USE A,D to move left and right,",
         "SPACE to jump, avoid enemies",
         "and make it to the end."
        ],
        ["USE W,A,S,D to move,",
         "make it to the end of the level",
         "before you run out of breath!"
        ],
        ["USE SPACE to jump,",
         "avoid Dynamite",
         "to beat the level!"
        ],
        ["USE A,D to move left and right,",
         "USE SPACE to attack,",
         "defeat all the enemies!"
        ],
        ["USE A,D to move left and right,",
         "USE SPACE to jump, make it the top",
         "quickly before the lava rises!"
        ]
    ]

#game state data
levelSelect = [
    {"levelNumber": 0 , "rectangle" : (40,50,310,100), "completed": False, "purchased": False, "cost":   2500},
    {"levelNumber": 1 , "rectangle" : (40,200,310,100), "completed": False, "purchased": False, "cost":  25000},
    {"levelNumber": 2 , "rectangle" : (40,350,310,100), "completed": False, "purchased": False, "cost":  500000},
    {"levelNumber": 3 , "rectangle" : (40,500,310,100), "completed": False, "purchased": False, "cost":  1000000},
    {"levelNumber": 4 , "rectangle" : (40,650,310,100), "completed": False, "purchased": False, "cost":  10000000},
    {"levelNumber": 5 , "rectangle" : (370,50,310,100), "completed": False, "purchased": False, "cost":  100000000},
    {"levelNumber": 6 , "rectangle" : (370,200,310,100), "completed": False, "purchased": False, "cost": 500000000},
    {"levelNumber": 7 , "rectangle" : (370,350,310,100), "completed": False, "purchased": False, "cost": 1000000000},
    {"levelNumber": 8 , "rectangle" : (370,500,310,100), "completed": False, "purchased": False, "cost": 33333333333},
    {"levelNumber": 9 , "rectangle" : (370,650,310,100), "completed": False, "purchased": False, "cost": 100000000000}
]

#name, cost, position, itemNumber, offset, effect, itemInfluenced, active
# name, cost, position, itemNumber, offset, effect, itemInfluenced, active

UPGRADE_ITEMS_DATA = [
    {
        "name": "Garden Shovel 3x",
        "cost": 150000,
        "position": 105,
        "itemNumber": 0,
        "offset": 0,
        "effect": 3,
        "itemInfluenced": 0,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(0*58),35,35)),
    },
    {
        "name": "spade 3x",
        "cost": 250000,
        "position": 105+1*45,
        "itemNumber": 1,
        "offset": 0,
        "effect": 3,
        "itemInfluenced": 1,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(1*58),35,35)),
    },
    {
        "name": "pickaxe 3x",
        "cost": 500000,
        "position": 105+2*45,
        "itemNumber": 2,
        "offset": 0,
        "effect": 3,
        "itemInfluenced": 2,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(2*58),35,35)),
    },
    {
        "name": "drill 3x",
        "cost": 3141592,
        "position": 105+3*45,
        "itemNumber": 3,
        "offset": 0,
        "effect": 3,
        "itemInfluenced": 3,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(3*58),35,35)),
    },
    {
        "name": "worker 3x",
        "cost": 5000000,
        "position": 105+4*45,
        "itemNumber": 4,
        "offset": 0,
        "effect": 3,
        "itemInfluenced": 4,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(4*58),35,35)),
    },
    {
        "name": "hardhat 3x",
        "cost": 11235813,
        "position": 105+5*45,
        "itemNumber": 5,
        "offset": 0,
        "effect": 3,
        "itemInfluenced": 5,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(5*58),35,35)),
    },
    {
        "name": "Garden Shovel 5x",
        "cost": 15000000,
        "position": 105+6*45,
        "itemNumber": 6,
        "offset": 0,
        "effect": 5,
        "itemInfluenced": 0,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(0*58),35,35)),
    },
    {
        "name": "spade 5x",
        "cost": 65555555,
        "position": 105+7*45,
        "itemNumber": 7,
        "offset": 0,
        "effect": 5,
        "itemInfluenced": 1,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(1*58),35,35)),
    },
    {
        "name": "dumptruck 3x",
        "cost": 111111111,
        "position": 105+8*45,
        "itemNumber": 8,
        "offset": 0,
        "effect": 3,
        "itemInfluenced": 6,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(6*58),35,35)),
    },
    {
        "name": "mineshaft 3x",
        "cost": 4294967295,
        "position": 105+9*45,
        "itemNumber": 9,
        "offset": 0,
        "effect": 3,
        "itemInfluenced": 7,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(7*58),35,35)),
    },
    {
        "name": "quarry 3x",
        "cost": 8000000000,
        "position": 105+10*45,
        "itemNumber": 10,
        "offset": 0,
        "effect": 3,
        "itemInfluenced": 8,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(8*58),35,35)),
    },
    {
        "name": "Garden Shovel 100x",
        "cost": 15000000000,
        "position": 105+11*45,
        "itemNumber": 11,
        "offset": 0,
        "effect": 100,
        "itemInfluenced": 0,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(0*58),35,35)),
    },
    {
        "name": "Laser Beam 3x",
        "cost": 35000000000,
        "position": 105+12*45,
        "itemNumber": 12,
        "offset": 0,
        "effect": 3,
        "itemInfluenced": 9,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(9*58),35,35)),
    },
    {
        "name": "pickaxe 5x",
        "cost": 500000000000,
        "position": 105+13*45,
        "itemNumber": 13,
        "offset": 0,
        "effect": 5,
        "itemInfluenced": 2,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(2*58),35,35)),
    },
    {
        "name": "drill 5x",
        "cost": 3141592653589,
        "position": 105+14*45,
        "itemNumber": 14,
        "offset": 0,
        "effect": 5,
        "itemInfluenced": 3,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(3*58),35,35)),
    },
    {
        "name": "worker 5x",
        "cost": 6000000000000,
        "position": 105+15*45,
        "itemNumber": 15,
        "offset": 0,
        "effect": 5,
        "itemInfluenced": 4,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(4*58),35,35)),
    },
    {
        "name": "hardhat 5x",
        "cost": 10000000000000,
        "position": 105+16*45,
        "itemNumber": 16,
        "offset": 0,
        "effect": 5,
        "itemInfluenced": 5,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(5*58),35,35)),
    },
    {
        "name": "dumptruck 5x",
        "cost": 500000000000000,
        "position": 105+17*45,
        "itemNumber": 17,
        "offset": 0,
        "effect": 5,
        "itemInfluenced": 6,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(6*58),35,35)),
    },
    {
        "name": "mineshaft 5x",
        "cost": 900000000000000,
        "position": 105+18*45,
        "itemNumber": 18,
        "offset": 0,
        "effect": 5,
        "itemInfluenced": 7,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(7*58),35,35)),
    },
    {
        "name": "quarry 5x",
        "cost": 1123581321345589,
        "position": 105+19*45,
        "itemNumber": 19,
        "offset": 0,
        "effect": 5,
        "itemInfluenced": 8,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(8*58),35,35)),
    },
    {
        "name": "Laser Beam 5x",
        "cost": 90000000000000000,
        "position": 105+20*45,
        "itemNumber": 20,
        "offset": 0,
        "effect": 5,
        "itemInfluenced": 9,
        "active": False,
        "image": upgradeBoard.subsurface((0,0+(9*58),35,35)),
    },
]




STORE_ITEMS_DATA = [
    {
        "name": "garden shovel",
        "cost": 4.00,
        "gain": 0,
        "amountOwned": 0,
        "itemNumber": 0,
        "length": 0,
        "speed": 6,
        "active": False,
        "manager": False,
        "managerCost": 1000,
        "costMultiplier": 1.07,
        "gainMultiplier": 1,
        "image": storeBoard.subsurface((0,0,45,45)),
        "managerInfo" : ["Gardener Bill", "manages garden shovel", "loves to garden!"],
    },
    {
        "name": "spade",
        "cost": 60,
        "gain": 0,
        "amountOwned": 0,
        "itemNumber": 1,
        "length": 0,
        "speed": 1.6,
        "active": False,
        "manager": False,
        "managerCost": 15000,
        "costMultiplier": 1.15,
        "gainMultiplier": 60,
        "image": storeBoard.subsurface((0,58,45,45)),
        "managerInfo" : ["Worker", "manages spade", "Hard working!"],
    },
    {
        "name": "pickaxe",
        "cost": 720,
        "gain": 0,
        "amountOwned": 0,
        "itemNumber": 2,
        "length": 0,
        "speed": 0.88,
        "active": False,
        "manager": False,
        "managerCost": 100000,
        "costMultiplier": 1.14,
        "gainMultiplier": 540,
        "image": storeBoard.subsurface((0,116,45,45)),
        "managerInfo" : ["Miner", "manages pickaxe", "yearns for the mines!"],
    },
    {
        "name": "drill",
        "cost": 8640,
        "gain": 0,
        "amountOwned": 0,
        "itemNumber": 3,
        "length": 0,
        "speed": 0.58,
        "active": False,
        "manager": False,
        "managerCost": 500000,
        "costMultiplier": 1.13,
        "gainMultiplier": 4320,
        "image": storeBoard.subsurface((0,174,45,45)),
        "managerInfo" : ["Drill Specialist", "manages drill", "Precise Drilling!"],
    },
    {
        "name": "workers",
        "cost": 103680,
        "gain": 0,
        "amountOwned": 0,
        "itemNumber": 4,
        "length": 0,
        "speed": 0.45,
        "active": False,
        "manager": False,
        "managerCost": 1200000,
        "costMultiplier": 1.12,
        "gainMultiplier": 51840,
        "image": storeBoard.subsurface((0,232,45,45)),
        "managerInfo" : ["Superviser Frank", "manages workers", "Expert Delegation!"],
    },
    {
        "name": "hardhats",
        "cost": 1244160,
        "gain": 0,
        "amountOwned": 0,
        "itemNumber": 5,
        "length": 0,
        "speed": 0.25,
        "active": False,
        "manager": False,
        "managerCost": 10000000,
        "costMultiplier": 1.11,
        "gainMultiplier": 622080,
        "image": storeBoard.subsurface((0,290,45,45)),
        "managerInfo" : ["Safety Inspector", "manages hardhats", "Saftey First!"],
    },
    {
        "name": "dumptruck",
        "cost": 14929920,
        "gain": 0,
        "amountOwned": 0,
        "itemNumber": 6,
        "length": 0,
        "speed": 0.145,
        "active": False,
        "manager": False,
        "managerCost": 111111111,
        "costMultiplier": 1.10,
        "gainMultiplier": 7464960,
        "image": storeBoard.subsurface((0,348,45,45)),
        "managerInfo" : ["Industrial Engineer", "manages dumptruck", "Quick Repairs!"],
    },
    {
        "name": "mineshaft",
        "cost": 179159040,
        "gain": 0,
        "amountOwned": 0,
        "itemNumber": 7,
        "length": 0,
        "speed": 0.09,
        "active": False,
        "manager": False,
        "managerCost": 555555555,
        "costMultiplier": 1.09,
        "gainMultiplier": 89579520,
        "image": storeBoard.subsurface((0,406,45,45)),
        "managerInfo" : ["Rare Mineral Expert", "manages mineshaft", "Know the value!"],
    },
    {
        "name": "quarry",
        "cost": 2149908480,
        "gain": 0,
        "amountOwned": 0,
        "itemNumber": 8,
        "length": 0,
        "speed": 0.0365,
        "active": False,
        "manager": False,
        "managerCost": 10000000000,
        "costMultiplier": 1.08,
        "gainMultiplier": 1074954240,
        "image": storeBoard.subsurface((0,464,45,45)),
        "managerInfo" : ["Mike", "manages quarry", "Advanced Strategy!"],
    },
    {
        "name": "laser Beam",
        "cost": 25798901760,
        "gain": 0,
        "amountOwned": 0,
        "itemNumber": 9,
        "length": 0,
        "speed": 0.015,
        "active": False,
        "manager": False,
        "managerCost": 100000000000,
        "costMultiplier": 1.07,
        "gainMultiplier": 29686000000,
        "image": storeBoard.subsurface((0,522,45,45)),
        "managerInfo" : ["Gary Laser Eyes", "manages laser beam", "Superb Technology!"],
    },
]


mileStones = [25, 50, 100, 200, 300, 400, 500, 600, 666, 700, 777, 800, 900, 1000]
initialCosts = [4, 60, 720, 8640, 103680, 1244160, 14929920, 179159040, 2149908480, 25798901760]


