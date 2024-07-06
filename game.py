import pygame
import time
import random
import gameGraph

pygame.init()
pygame.display.set_caption("Diji")
res = (720, 720)
screen = pygame.display.set_mode(res)


graph = gameGraph.Graph()



#randomly picks one of two ways to get from one vertex to another using two lines
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

#Used to ensure player can only walk on the generated path
def isOnPath(key):
    if (key == 'a'):
        if pygame.Surface.get_at(screen, (player.left - 1, player.top)) == (0,0,0) and pygame.Surface.get_at(screen, (player.left - 1, player.bottom)) == (0,0,0):
            if pygame.Surface.get_at(screen, (player.left - 1, player.centery)) == (0,0,0):
                return True
        for x in vertexList:
            if x.collidepoint(player.left - 1, player.top):
                return True
    elif (key == 'd'):
        if pygame.Surface.get_at(screen, (player.right + 1, player.bottom)) == (0,0,0) and pygame.Surface.get_at(screen, (player.right + 1, player.top)) == (0,0,0):
            if pygame.Surface.get_at(screen, (player.right + 1, player.centery)) == (0,0,0):
                return True
        for x in vertexList:
            if x.collidepoint(player.right + 1, player.bottom):
                return True
    elif (key == 'w'):
        if pygame.Surface.get_at(screen, (player.left, player.top - 1)) == (0,0,0) and pygame.Surface.get_at(screen, (player.right, player.top - 1)) == (0,0,0):
            return True
        for x in vertexList:
            if x.collidepoint(player.x, player.y - 1):
                return True    
    elif (key == 's'):
        if pygame.Surface.get_at(screen, (player.right, player.bottom + 1)) == (0,0,0) and pygame.Surface.get_at(screen, (player.left, player.bottom + 1)) == (0,0,0):
            return True
        for x in vertexList:
            if x.collidepoint(player.right, player.bottom + 1):
                return True
    return False



centerVertex = pygame.Rect((335, 335, 51, 51)) 
#creates target vertices
targetVertex1 = pygame.Rect(0, 335, 51, 51)
targetVertex2 = pygame.Rect(335, 0, 51, 51)
targetVertex3 = pygame.Rect(670,335,51,51)
targetVertex4 = pygame.Rect(335,670,51,51)

#creates vertices in the first quadrant
vertexA = pygame.Rect((generateRandomLocation(70, 230, 70, 230)[0], generateRandomLocation(70,230,70,230)[1], 51, 51)) 
cornerA1 = pygame.Rect((random.randint(51, 280), 0, 51, 51))
cornerA2 = pygame.Rect((0, random.randint(51, 280), 51, 51))
cordsA = generatePath(vertexA, centerVertex)
connectAcenter = pygame.Rect(cordsA[0], cordsA[1], 51, 51)
edgeA1 = pygame.Rect(0, vertexA.top, 51, 51)
edgeA2 = pygame.Rect(vertexA.left, 0, 51, 51)

#creates vertices in the second quadrant
vertexB = pygame.Rect((generateRandomLocation(390, 600, 70, 230)[0], generateRandomLocation(340, 600, 70, 230)[1], 51, 51)) 
cornerB1 = pygame.Rect(random.randint(390,620), 0, 51, 51)
cornerB2 = pygame.Rect(670, random.randint(51,280), 51, 51)
cordsB = generatePath(vertexB, centerVertex)
connectBcenter = pygame.Rect(cordsB[0], cordsB[1], 51, 51)
edgeB1 = pygame.Rect(670, vertexB.top, 51, 51)
edgeB2 = pygame.Rect(vertexB.left, 0, 51, 51)

#creates vertices in the third quadrant
vertexC = pygame.Rect((generateRandomLocation(70, 230, 390, 600)[0], generateRandomLocation(70, 230, 390, 600)[1], 51, 51))
cornerC1 = pygame.Rect(random.randint(51,280), 670, 51, 51)
cornerC2 = pygame.Rect(0, random.randint(390,620), 51, 51)
cordsC = generatePath(vertexC, centerVertex)
connectCcenter = pygame.Rect(cordsC[0], cordsC[1], 51, 51)
edgeC1 = pygame.Rect(0, vertexC.top, 51, 51)
edgeC2 = pygame.Rect(vertexC.left, 670, 51, 51)

#creates vertices in the fourth quadrant
vertexD = pygame.Rect((generateRandomLocation(440, 600, 440, 600)[0], generateRandomLocation(440, 600, 440, 600)[1], 51, 51)) 
cornerD1 = pygame.Rect(random.randint(390,620), 670, 51, 51)
cornerD2 = pygame.Rect(670, random.randint(390,620), 51, 51)
cordsD = generatePath(vertexD, centerVertex)
connectDcenter = pygame.Rect(cordsD[0], cordsD[1], 51, 51)
edgeD1 = pygame.Rect(670, vertexD.top, 51, 51)
edgeD2 = pygame.Rect(vertexD.left, 670, 51, 51)

player = pygame.Rect((345,345,30,30))



#randomly generates the physical roadmap for diji
def set_up_game():
    #spawn in all vertices
    pygame.draw.rect(screen, (0,0,0), centerVertex)
    pygame.draw.rect(screen, (0,0,0), vertexA)
    pygame.draw.rect(screen, (0,0,0), cornerA1)
    pygame.draw.rect(screen, (0,0,0), cornerA2)
    pygame.draw.rect(screen, (0,0,0), edgeA1)
    pygame.draw.rect(screen, (0,0,0), edgeA2)
    pygame.draw.rect(screen, (0,0,0), vertexB)
    pygame.draw.rect(screen, (0,0,0), cornerB1)
    pygame.draw.rect(screen, (0,0,0), cornerB2)
    pygame.draw.rect(screen, (0,0,0), edgeB1)
    pygame.draw.rect(screen, (0,0,0), edgeB2)
    pygame.draw.rect(screen, (0,0,0), vertexC)
    pygame.draw.rect(screen, (0,0,0), cornerC1)
    pygame.draw.rect(screen, (0,0,0), cornerC2)
    pygame.draw.rect(screen, (0,0,0), edgeC1)
    pygame.draw.rect(screen, (0,0,0), edgeC2)
    pygame.draw.rect(screen, (0,0,0), vertexD)
    pygame.draw.rect(screen, (0,0,0), cornerD1)
    pygame.draw.rect(screen, (0,0,0), cornerD2)
    pygame.draw.rect(screen, (0,0,0), edgeD1)
    pygame.draw.rect(screen, (0,0,0), edgeD2)
    pygame.draw.rect(screen, (0,0,0), targetVertex1)
    pygame.draw.circle(screen, (225,225,225), (15,360), 12)
    pygame.draw.rect(screen, (0,0,0), targetVertex2)
    pygame.draw.circle(screen, (225,225,225), (360,15), 12)
    pygame.draw.rect(screen, (0,0,0), targetVertex3)
    pygame.draw.circle(screen, (225,225,225), (705,360), 12)
    pygame.draw.rect(screen, (0,0,0), targetVertex4)
    pygame.draw.circle(screen, (225,225,225), (360,705), 12)
    pygame.draw.line(screen, (0,0,0), (targetVertex1.midtop), (cornerA2.midtop), 51)
    pygame.draw.line(screen, (0,0,0), (targetVertex1.midbottom), (cornerC2.midbottom), 51)
    pygame.draw.line(screen, (0,0,0), (targetVertex2.midleft), (cornerA1.midleft), 51)
    pygame.draw.line(screen, (0,0,0), (targetVertex2.midright), (cornerB1.midright), 51)
    pygame.draw.line(screen, (0,0,0), (targetVertex3.midtop), (cornerB2.midtop), 51)
    pygame.draw.line(screen, (0,0,0), (targetVertex3.midbottom), (cornerD2.midbottom), 51)
    pygame.draw.line(screen, (0,0,0), (targetVertex4.midleft), (cornerC1.midleft), 51)
    pygame.draw.line(screen, (0,0,0), (targetVertex4.midright), (cornerD1.midright), 51)
    pygame.draw.rect(screen, (0,0,255), player)
    

#Connects center vertex to the intermediate vertices, connects the intermediate vertices to the respective quadrant vertex
def connect_center_to_vertices():
        
        pygame.draw.rect(screen, (0,0,0), connectAcenter)
        if cordsA[2] == 1:
            pygame.draw.line(screen, (0,0,0), (centerVertex.midleft), (connectAcenter.midleft), 51)
        else:
            pygame.draw.line(screen, (0,0,0), (centerVertex.midtop), (connectAcenter.midtop), 51)
        pygame.draw.line(screen, (0,0,0), (connectAcenter.center), (vertexA.center), 51)
        
        pygame.draw.rect(screen, (0,0,0), connectBcenter)

        if cordsB[2] == 1:
            pygame.draw.line(screen, (0,0,0), (centerVertex.midright), (connectBcenter.midleft), 51)
        else:
            pygame.draw.line(screen, (0,0,0), (centerVertex.midtop), (connectBcenter.midtop), 51)
        pygame.draw.line(screen, (0,0,0), (connectBcenter.center), (vertexB.center), 51)

        pygame.draw.rect(screen, (0,0,0), connectCcenter)

        if cordsC[2] == 1:
            pygame.draw.line(screen, (0,0,0), (centerVertex.midright), (connectCcenter.midleft), 51)
        else:
            pygame.draw.line(screen, (0,0,0), (centerVertex.midtop), (connectCcenter.midtop), 51)
        pygame.draw.line(screen, (0,0,0), (connectCcenter.center), (vertexC.center), 51)

        pygame.draw.rect(screen, (0,0,0), connectDcenter)

        if cordsD[2] == 1:
            pygame.draw.line(screen, (0,0,0), (centerVertex.midright), (connectDcenter.midleft), 51)
        else:
            pygame.draw.line(screen, (0,0,0), (centerVertex.midtop), (connectDcenter.midtop), 51)

        pygame.draw.line(screen, (0,0,0), (connectDcenter.center), (vertexD.center), 51)

        pygame.draw.rect(screen, (255, 0, 0), player)


#Connects each quadrant vertex to both edges of the map
def connect_vertices_edges():
    pygame.draw.line(screen, (0,0,0), (edgeA1.center), (vertexA.center), 51)
    pygame.draw.line(screen, (0,0,0), (edgeA1.center), (targetVertex1.midtop), 51)
    pygame.draw.line(screen, (0,0,0), (edgeA2.center), (vertexA.center), 51)
    pygame.draw.line(screen, (0,0,0), (edgeA2.center), (targetVertex2.midleft), 51)

    pygame.draw.line(screen, (0,0,0), (edgeB1.center), (vertexB.center), 51)
    pygame.draw.line(screen, (0,0,0), (edgeB1.center), (targetVertex3.midtop), 51)
    pygame.draw.line(screen, (0,0,0), (edgeB2.center), (vertexB.center), 51)
    pygame.draw.line(screen, (0,0,0), (edgeB2.center), (targetVertex2.midright), 51)

    pygame.draw.line(screen, (0,0,0), (edgeC1.center), (vertexC.center), 51)
    pygame.draw.line(screen, (0,0,0), (edgeC1.center), (targetVertex1.midbottom), 51)
    pygame.draw.line(screen, (0,0,0), (edgeC2.center), (vertexC.center), 51)
    pygame.draw.line(screen, (0,0,0), (edgeC2.center), (targetVertex4.midleft), 51)

    pygame.draw.line(screen, (0,0,0), (edgeD1.center), (vertexD.center), 51)
    pygame.draw.line(screen, (0,0,0), (edgeD1.center), (targetVertex3.midbottom), 51)
    pygame.draw.line(screen, (0,0,0), (edgeD2.center), (vertexD.center), 51)
    pygame.draw.line(screen, (0,0,0), (edgeD2.center), (targetVertex4.midright), 51)

#calculates the distance between vertex1 and vertex2 in pixels
def calculate_distance(vertex1, vertex2):
    return abs(vertex1.centerx - vertex2.centerx) + abs(vertex1.centery - vertex2.centery)

#uses gameGraph's Graph and Vertex classes to create an undirected weighted graph with all vertices
def add_to_graph():
    graph = gameGraph.Graph()
    graph.add_vertex(gameGraph.Vertex('centerVertex'))
    graph.add_vertex(gameGraph.Vertex('connectAcenter'))
    graph.add_vertex(gameGraph.Vertex('connectBcenter'))
    graph.add_vertex(gameGraph.Vertex('connectCcenter'))
    graph.add_vertex(gameGraph.Vertex('connectDcenter'))
    graph.add_edge('centerVertex', 'connectAcenter', calculate_distance(centerVertex, connectAcenter))
    graph.add_edge('centerVertex', 'connectBcenter', calculate_distance(centerVertex, connectBcenter))
    graph.add_edge('centerVertex', 'connectCcenter', calculate_distance(centerVertex, connectCcenter))
    graph.add_edge('centerVertex', 'connectDcenter', calculate_distance(centerVertex, connectDcenter))
    graph.add_vertex(gameGraph.Vertex('vertexA'))
    graph.add_vertex(gameGraph.Vertex('vertexB'))
    graph.add_vertex(gameGraph.Vertex('vertexC'))
    graph.add_vertex(gameGraph.Vertex('vertexD'))
    graph.add_edge('connectAcenter', 'vertexA', calculate_distance(connectAcenter, vertexA))
    graph.add_edge('connectBcenter', 'vertexB', calculate_distance(connectBcenter, vertexB))
    graph.add_edge('connectCcenter', 'vertexC', calculate_distance(connectCcenter, vertexC))
    graph.add_edge('connectDcenter', 'vertexD', calculate_distance(connectDcenter, vertexD))
    graph.add_vertex(gameGraph.Vertex('edgeA1'))
    graph.add_vertex(gameGraph.Vertex('edgeB1'))
    graph.add_vertex(gameGraph.Vertex('edgeC1'))
    graph.add_vertex(gameGraph.Vertex('edgeD1'))
    graph.add_vertex(gameGraph.Vertex('edgeA2'))
    graph.add_vertex(gameGraph.Vertex('edgeB2'))
    graph.add_vertex(gameGraph.Vertex('edgeC2'))
    graph.add_vertex(gameGraph.Vertex('edgeD2'))
    graph.add_edge('vertexA', 'edgeA1', calculate_distance(vertexA, edgeA1))
    graph.add_edge('vertexA', 'edgeA2', calculate_distance(vertexA, edgeA2))
    graph.add_edge('vertexB', 'edgeB1', calculate_distance(vertexB, edgeB1))
    graph.add_edge('vertexB', 'edgeB2', calculate_distance(vertexB, edgeB2))
    graph.add_edge('vertexC', 'edgeC1', calculate_distance(vertexC, edgeC1))
    graph.add_edge('vertexC', 'edgeC2', calculate_distance(vertexC, edgeC2))
    graph.add_edge('vertexD', 'edgeD1', calculate_distance(vertexD, edgeD1))
    graph.add_edge('vertexD', 'edgeD2', calculate_distance(vertexD, edgeD2))
    graph.add_vertex(gameGraph.Vertex('targetVertex1'))
    graph.add_vertex(gameGraph.Vertex('targetVertex2'))
    graph.add_vertex(gameGraph.Vertex('targetVertex3'))
    graph.add_vertex(gameGraph.Vertex('targetVertex4'))
    graph.add_edge('targetVertex1', 'edgeA1', calculate_distance(targetVertex1, edgeA1))
    graph.add_edge('targetVertex1', 'edgeC1', calculate_distance(targetVertex1, edgeC1))
    graph.add_edge('targetVertex2', 'edgeA2', calculate_distance(targetVertex2, edgeA2))
    graph.add_edge('targetVertex2', 'edgeB2', calculate_distance(targetVertex2, edgeB2))
    graph.add_edge('targetVertex3', 'edgeB1', calculate_distance(targetVertex3, edgeB1))
    graph.add_edge('targetVertex3', 'edgeD1', calculate_distance(targetVertex3, edgeD1))
    graph.add_edge('targetVertex4', 'edgeC2', calculate_distance(targetVertex4, edgeC2))
    graph.add_edge('targetVertex4', 'edgeD2', calculate_distance(targetVertex4, edgeD2))
    #print(graph.get_weight('targetVertex4', 'edgeD2'))

    #DO CORNERS TO EDGES!!

#Creates a list of all vertices to be used for collision checking and graph implementation
vertexList = [centerVertex, vertexA, cornerA1, cornerA2, vertexB, cornerB1, cornerB2, 
              vertexC, cornerC1, cornerC2, vertexD, cornerD1, cornerD2, targetVertex1, targetVertex2, targetVertex3, targetVertex4,
              edgeA1, edgeA2, edgeB1, edgeB2, edgeC1, edgeC2, edgeD1, edgeD2 ]

#game loop runs and looks for events
run = True;
while run:
    time.sleep(0.003)
    screen.fill((255,255,255)) 
    set_up_game()
    connect_vertices_edges()
    connect_center_to_vertices()
    add_to_graph()
    
    
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
            run = False
            
    pygame.display.update()





pygame.quit()


