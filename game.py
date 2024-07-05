import pygame
import time
import random

pygame.init()

pygame.display.set_caption("Diji")

#randomly picks one of two ways to get from one object to another using two lines
def generatePath(start, end):
    path = random.randint(1,2)
    if path == 1:
        pygame.Rect((start.x, end.y, 51, 51))
        return (start.x, end.y, 1)
    elif path == 2:
        return (end.x, start.y, 2)

#used to generate random coordinate locations in the specified area of the screen
def generateRandomLocation(startx, endx, starty, endy):
    coordinates = (random.randint(startx, endx), random.randint(starty,endy))
    return coordinates

def pickAPrize(prize1, prize2):
    num = random.randint(1,2)
    if num == 1:
        return prize1
    else:
        return prize2


#randomly generates the physical roadmap for diji
def setUpGame():
    #spawn in all vertices
    pygame.draw.rect(screen, (0,0,0), centerObject)
    pygame.draw.rect(screen, (0,0,0), objectA)
    pygame.draw.rect(screen, (0,0,0), cornerA1)
    pygame.draw.rect(screen, (0,0,0), cornerA2)
    pygame.draw.rect(screen, (0,0,0), edgeA1)
    pygame.draw.rect(screen, (0,0,0), edgeA2)
    pygame.draw.rect(screen, (0,0,0), objectB)
    pygame.draw.rect(screen, (0,0,0), cornerB1)
    pygame.draw.rect(screen, (0,0,0), cornerB2)
    pygame.draw.rect(screen, (0,0,0), edgeB1)
    pygame.draw.rect(screen, (0,0,0), edgeB2)
    pygame.draw.rect(screen, (0,0,0), objectC)
    pygame.draw.rect(screen, (0,0,0), cornerC1)
    pygame.draw.rect(screen, (0,0,0), cornerC2)
    pygame.draw.rect(screen, (0,0,0), edgeC1)
    pygame.draw.rect(screen, (0,0,0), edgeC2)
    pygame.draw.rect(screen, (0,0,0), objectD)
    pygame.draw.rect(screen, (0,0,0), cornerD1)
    pygame.draw.rect(screen, (0,0,0), cornerD2)
    pygame.draw.rect(screen, (0,0,0), edgeD1)
    pygame.draw.rect(screen, (0,0,0), edgeD2)
    pygame.draw.rect(screen, (0,0,0), prizeOb1)
    pygame.draw.circle(screen, (225,225,225), (15,360), 12)
    pygame.draw.rect(screen, (0,0,0), prizeOb2)
    pygame.draw.circle(screen, (225,225,225), (360,15), 12)
    pygame.draw.rect(screen, (0,0,0), prizeOb3)
    pygame.draw.circle(screen, (225,225,225), (705,360), 12)
    pygame.draw.rect(screen, (0,0,0), prizeOb4)
    pygame.draw.circle(screen, (225,225,225), (360,705), 12)
    pygame.draw.line(screen, (0,0,0), (prizeOb1.midtop), (cornerA2.midtop), 51)
    pygame.draw.line(screen, (0,0,0), (prizeOb1.midbottom), (cornerC2.midbottom), 51)
    pygame.draw.line(screen, (0,0,0), (prizeOb2.midleft), (cornerA1.midleft), 51)
    pygame.draw.line(screen, (0,0,0), (prizeOb2.midright), (cornerB1.midright), 51)
    pygame.draw.line(screen, (0,0,0), (prizeOb3.midtop), (cornerB2.midtop), 51)
    pygame.draw.line(screen, (0,0,0), (prizeOb3.midbottom), (cornerD2.midbottom), 51)
    pygame.draw.line(screen, (0,0,0), (prizeOb4.midleft), (cornerC1.midleft), 51)
    pygame.draw.line(screen, (0,0,0), (prizeOb4.midright), (cornerD1.midright), 51)
    

def connectPaths():
        #connect intermediate vertices with lines
        pygame.draw.rect(screen, (0,0,0), connectAcenter)
        if cordsA[2] == 1:
            pygame.draw.line(screen, (0,0,0), (centerObject.midleft), (connectAcenter.midleft), 51)
        else:
            pygame.draw.line(screen, (0,0,0), (centerObject.midtop), (connectAcenter.midtop), 51)
        pygame.draw.line(screen, (0,0,0), (connectAcenter.center), (objectA.center), 51)
        
        pygame.draw.rect(screen, (0,0,0), connectBcenter)

        if cordsB[2] == 1:
            pygame.draw.line(screen, (0,0,0), (centerObject.midright), (connectBcenter.midleft), 51)
        else:
            pygame.draw.line(screen, (0,0,0), (centerObject.midtop), (connectBcenter.midtop), 51)
        pygame.draw.line(screen, (0,0,0), (connectBcenter.center), (objectB.center), 51)

        pygame.draw.rect(screen, (0,0,0), connectCcenter)

        if cordsC[2] == 1:
            pygame.draw.line(screen, (0,0,0), (centerObject.midright), (connectCcenter.midleft), 51)
        else:
            pygame.draw.line(screen, (0,0,0), (centerObject.midtop), (connectCcenter.midtop), 51)
        pygame.draw.line(screen, (0,0,0), (connectCcenter.center), (objectC.center), 51)

        pygame.draw.rect(screen, (0,0,0), connectDcenter)

        if cordsD[2] == 1:
            pygame.draw.line(screen, (0,0,0), (centerObject.midright), (connectDcenter.midleft), 51)
        else:
            pygame.draw.line(screen, (0,0,0), (centerObject.midtop), (connectDcenter.midtop), 51)

        pygame.draw.line(screen, (0,0,0), (connectDcenter.center), (objectD.center), 51)


        pygame.draw.line(screen, (0,0,0), (edgeA1.center), (objectA.center), 51)
        pygame.draw.line(screen, (0,0,0), (edgeA1.center), (prizeOb1.midtop), 51)
        pygame.draw.line(screen, (0,0,0), (edgeA2.center), (objectA.center), 51)
        pygame.draw.line(screen, (0,0,0), (edgeA2.center), (prizeOb2.midleft), 51)

        pygame.draw.line(screen, (0,0,0), (edgeB1.center), (objectB.center), 51)
        pygame.draw.line(screen, (0,0,0), (edgeB1.center), (prizeOb3.midtop), 51)
        pygame.draw.line(screen, (0,0,0), (edgeB2.center), (objectB.center), 51)
        pygame.draw.line(screen, (0,0,0), (edgeB2.center), (prizeOb2.midright), 51)

        pygame.draw.line(screen, (0,0,0), (edgeC1.center), (objectC.center), 51)
        pygame.draw.line(screen, (0,0,0), (edgeC1.center), (prizeOb1.midbottom), 51)
        pygame.draw.line(screen, (0,0,0), (edgeC2.center), (objectC.center), 51)
        pygame.draw.line(screen, (0,0,0), (edgeC2.center), (prizeOb4.midleft), 51)

        pygame.draw.line(screen, (0,0,0), (edgeD1.center), (objectD.center), 51)
        pygame.draw.line(screen, (0,0,0), (edgeD1.center), (prizeOb3.midbottom), 51)
        pygame.draw.line(screen, (0,0,0), (edgeD2.center), (objectD.center), 51)
        pygame.draw.line(screen, (0,0,0), (edgeD2.center), (prizeOb4.midright), 51)

        pygame.draw.rect(screen, (255, 0, 0), player)

res = (720, 720)

#creates target objects
prizeOb1 = pygame.Rect(0, 335, 51, 51)
prizeOb2 = pygame.Rect(335, 0, 51, 51)
prizeOb3 = pygame.Rect(670,335,51,51)
prizeOb4 = pygame.Rect(335,670,51,51)


screen = pygame.display.set_mode(res)
player = pygame.Rect((345,345,30,30))
centerObject = pygame.Rect((335, 335, 51, 51)) 

#creates objects in the first quadrant
objectA = pygame.Rect((generateRandomLocation(70, 230, 70, 230)[0], generateRandomLocation(70,230,70,230)[1], 51, 51)) 

cornerA1 = pygame.Rect((random.randint(51, 280), 0, 51, 51))
cornerA2 = pygame.Rect((0, random.randint(51, 280), 51, 51))

cordsA = generatePath(objectA, centerObject)
connectAcenter = pygame.Rect(cordsA[0], cordsA[1], 51, 51)
edgeA1 = pygame.Rect(0, objectA.top, 51, 51)
edgeA2 = pygame.Rect(objectA.left, 0, 51, 51)


#creates objects in the second quadrant
objectB = pygame.Rect((generateRandomLocation(390, 600, 70, 230)[0], generateRandomLocation(340, 600, 70, 230)[1], 51, 51)) 
cornerB1 = pygame.Rect(random.randint(390,620), 0, 51, 51)
cornerB2 = pygame.Rect(670, random.randint(51,280), 51, 51)

cordsB = generatePath(objectB, centerObject)
connectBcenter = pygame.Rect(cordsB[0], cordsB[1], 51, 51)

edgeB1 = pygame.Rect(670, objectB.top, 51, 51)
edgeB2 = pygame.Rect(objectB.left, 0, 51, 51)
#creates objects in the third quadrant
objectC = pygame.Rect((generateRandomLocation(70, 230, 390, 600)[0], generateRandomLocation(70, 230, 390, 600)[1], 51, 51))
cornerC1 = pygame.Rect(random.randint(51,280), 670, 51, 51)
cornerC2 = pygame.Rect(0, random.randint(390,620), 51, 51)

cordsC = generatePath(objectC, centerObject)
connectCcenter = pygame.Rect(cordsC[0], cordsC[1], 51, 51)

edgeC1 = pygame.Rect(0, objectC.top, 51, 51)
edgeC2 = pygame.Rect(objectC.left, 670, 51, 51)
#creates objects in the fourth quadrant
objectD = pygame.Rect((generateRandomLocation(440, 600, 440, 600)[0], generateRandomLocation(440, 600, 440, 600)[1], 51, 51)) 
cornerD1 = pygame.Rect(random.randint(390,620), 670, 51, 51)
cornerD2 = pygame.Rect(670, random.randint(390,620), 51, 51)

cordsD = generatePath(objectD, centerObject)
connectDcenter = pygame.Rect(cordsD[0], cordsD[1], 51, 51)

edgeD1 = pygame.Rect(670, objectD.top, 51, 51)
edgeD2 = pygame.Rect(objectD.left, 670, 51, 51)



objectList = [centerObject, objectA, cornerA1, cornerA2, objectB, cornerB1, cornerB2, 
              objectC, cornerC1, cornerC2, objectD, cornerD1, cornerD2, prizeOb1, prizeOb2, prizeOb3, prizeOb4,
              edgeA1, edgeA2, edgeB1, edgeB2, edgeC1, edgeC2, edgeD1, edgeD2 ]


#game loop runs and looks for events
run = True;
while run:
    time.sleep(0.003)
    screen.fill((255,255,255)) 
    setUpGame()
    connectPaths()
   
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True and isOnPath('a') and player.left - 1 != 0:
        player.move_ip(-1,0)
    elif key[pygame.K_d] == True and isOnPath('d') and player.right + 1 != 720:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True and isOnPath('w') and player.top - 1 != 0:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True and isOnPath('s') and player.bottom + 1 != 720:
        player.move_ip(0, 1)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False;

    #Used to ensure player can only walk on the generated path
    def isOnPath(key):
        if (key == 'a'):
            if pygame.Surface.get_at(screen, (player.left - 1, player.top)) == (0,0,0) and pygame.Surface.get_at(screen, (player.left - 1, player.bottom)) == (0,0,0):
                if pygame.Surface.get_at(screen, (player.left - 1, player.centery)) == (0,0,0):
                    return True
            for x in objectList:
                if x.collidepoint(player.left - 1, player.top):
                    return True
        elif (key == 'd'):
            if pygame.Surface.get_at(screen, (player.right + 1, player.bottom)) == (0,0,0) and pygame.Surface.get_at(screen, (player.right + 1, player.top)) == (0,0,0):
                if pygame.Surface.get_at(screen, (player.right + 1, player.centery)) == (0,0,0):
                    return True
            for x in objectList:
                if x.collidepoint(player.right + 1, player.bottom):
                    return True
        elif (key == 'w'):
            if pygame.Surface.get_at(screen, (player.left, player.top - 1)) == (0,0,0) and pygame.Surface.get_at(screen, (player.right, player.top - 1)) == (0,0,0):
                return True
            for x in objectList:
                if x.collidepoint(player.x, player.y - 1):
                    return True    
        elif (key == 's'):
            if pygame.Surface.get_at(screen, (player.right, player.bottom + 1)) == (0,0,0) and pygame.Surface.get_at(screen, (player.left, player.bottom + 1)) == (0,0,0):
                return True
            for x in objectList:
                if x.collidepoint(player.right, player.bottom + 1):
                    return True
        return False

    pygame.display.update()

pygame.quit()


