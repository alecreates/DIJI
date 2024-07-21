import pygame
import time
import random
import gameGraph

pygame.init()
pygame.display.set_caption("Diji")
res = (720, 720)
screen = pygame.display.set_mode(res)
graph = gameGraph.Graph()

#used to generate random coordinate locations in the specified area of the screen
def generateRandomLocation(startx, endx, starty, endy):
    coordinates = (random.randint(startx, endx), random.randint(starty,endy))
    return coordinates

#randomly picks one of two ways to get from one vertex to another using two lines
def generatePath(start, end):
    path = random.randint(1,2)
    if path == 1:
        pygame.Rect((start.x, end.y, 51, 51))
        return (start.x, end.y, 1)
    elif path == 2:
        return (end.x, start.y, 2)

centerVertex = pygame.Rect((335, 335, 51, 51)) 
#creates target vertices
targetVertex1 = pygame.Rect(0, 335, 51, 51)
targetVertex2 = pygame.Rect(335, 0, 51, 51)
targetVertex3 = pygame.Rect(670,335,51,51)
targetVertex4 = pygame.Rect(335,670,51,51)

#creates vertices in the first quadrant
vertexA = pygame.Rect((generateRandomLocation(70, 230, 70, 230)[0], generateRandomLocation(70,230,70,230)[1], 51, 51)) 
cordsA = generatePath(vertexA, centerVertex)
connectAcenter = pygame.Rect(cordsA[0], cordsA[1], 51, 51)
edgeA1 = pygame.Rect(0, vertexA.top, 51, 51)
edgeA2 = pygame.Rect(vertexA.left, 0, 51, 51)

#creates vertices in the second quadrant
vertexB = pygame.Rect((generateRandomLocation(390, 600, 70, 230)[0], generateRandomLocation(340, 600, 70, 230)[1], 51, 51)) 
cordsB = generatePath(vertexB, centerVertex)
connectBcenter = pygame.Rect(cordsB[0], cordsB[1], 51, 51)
edgeB1 = pygame.Rect(670, vertexB.top, 51, 51)
edgeB2 = pygame.Rect(vertexB.left, 0, 51, 51)

#creates vertices in the third quadrant
vertexC = pygame.Rect((generateRandomLocation(70, 230, 390, 600)[0], generateRandomLocation(70, 230, 390, 600)[1], 51, 51))
cordsC = generatePath(vertexC, centerVertex)
connectCcenter = pygame.Rect(cordsC[0], cordsC[1], 51, 51)
edgeC1 = pygame.Rect(0, vertexC.top, 51, 51)
edgeC2 = pygame.Rect(vertexC.left, 670, 51, 51)

#creates vertices in the fourth quadrant
vertexD = pygame.Rect((generateRandomLocation(440, 600, 440, 600)[0], generateRandomLocation(440, 600, 440, 600)[1], 51, 51)) 
cordsD = generatePath(vertexD, centerVertex)
connectDcenter = pygame.Rect(cordsD[0], cordsD[1], 51, 51)
edgeD1 = pygame.Rect(670, vertexD.top, 51, 51)
edgeD2 = pygame.Rect(vertexD.left, 670, 51, 51)

player = pygame.Rect((345,345,30,30))   



#Used to ensure player can only walk on the generated path
def isOnPath(key):
    if (key == 'a'):
        if pygame.Surface.get_at(screen, (player.left - 1, player.top)) == (44, 21, 0) and pygame.Surface.get_at(screen, (player.left - 1, player.bottom)) == (44, 21, 0):
            if pygame.Surface.get_at(screen, (player.left - 1, player.centery)) == (44, 21, 0):
                return True
        for x in vertexList:
            if x.collidepoint(player.left - 1, player.top):
                return True
    elif (key == 'd'):
        if pygame.Surface.get_at(screen, (player.right + 1, player.bottom)) == (44, 21, 0) and pygame.Surface.get_at(screen, (player.right + 1, player.top)) == (44, 21, 0):
            if pygame.Surface.get_at(screen, (player.right + 1, player.centery)) == (44, 21, 0):
                return True
        for x in vertexList:
            if x.collidepoint(player.right + 1, player.bottom):
                return True
    elif (key == 'w'):
        if pygame.Surface.get_at(screen, (player.left, player.top - 1)) == (44, 21, 0) and pygame.Surface.get_at(screen, (player.right, player.top - 1)) == (44, 21, 0):
            return True
        for x in vertexList:
            if x.collidepoint(player.x, player.y - 1):
                return True    
    elif (key == 's'):
        if pygame.Surface.get_at(screen, (player.right, player.bottom + 1)) == (44, 21, 0) and pygame.Surface.get_at(screen, (player.left, player.bottom + 1)) == (44, 21, 0):
            return True
        for x in vertexList:
            if x.collidepoint(player.right, player.bottom + 1):
                return True
    return False


#randomly generates the physical roadmap for diji
def set_up_game():
    screen.fill((104, 0, 255)) 
    #spawn in all vertices
    pygame.draw.rect(screen, (44, 21, 0), centerVertex)
    pygame.draw.rect(screen, (44, 21, 0), vertexA)
    pygame.draw.rect(screen, (44, 21, 0), edgeA1)
    pygame.draw.rect(screen, (44, 21, 0), edgeA2)
    pygame.draw.rect(screen, (44, 21, 0), vertexB)
    pygame.draw.rect(screen, (44, 21, 0), edgeB1)
    pygame.draw.rect(screen, (44, 21, 0), edgeB2)
    pygame.draw.rect(screen, (44, 21, 0), vertexC)
    pygame.draw.rect(screen, (44, 21, 0), edgeC1)
    pygame.draw.rect(screen, (44, 21, 0), edgeC2)
    pygame.draw.rect(screen, (44, 21, 0), vertexD)
    pygame.draw.rect(screen, (44, 21, 0), edgeD1)
    pygame.draw.rect(screen, (44, 21, 0), edgeD2)
    pygame.draw.rect(screen, (44, 21, 0), targetVertex1)
    pygame.draw.circle(screen, (225,225,225), (15,360), 12)
    pygame.draw.rect(screen, (44, 21, 0), targetVertex2)
    pygame.draw.circle(screen, (225,225,225), (360,15), 12)
    pygame.draw.rect(screen, (44, 21, 0), targetVertex3)
    pygame.draw.circle(screen, (225,225,225), (705,360), 12)
    pygame.draw.rect(screen, (44, 21, 0), targetVertex4)
    pygame.draw.circle(screen, (225,225,225), (360,705), 12)
    pygame.draw.rect(screen, (232, 214, 203), player)
    

#Connects center vertex to the intermediate vertices, connects the intermediate vertices to the respective quadrant vertex
def connect_center_to_vertices():
        pygame.draw.rect(screen, (44, 21, 0), connectAcenter)
        if cordsA[2] == 1:
            pygame.draw.line(screen, (44, 21, 0), (centerVertex.midleft), (connectAcenter.midleft), 51)
        else:
            pygame.draw.line(screen, (44, 21, 0), (centerVertex.midtop), (connectAcenter.midtop), 51)
        pygame.draw.line(screen, (44, 21, 0), (connectAcenter.center), (vertexA.center), 51)
        
        pygame.draw.rect(screen, (44, 21, 0), connectBcenter)

        if cordsB[2] == 1:
            pygame.draw.line(screen, (44, 21, 0), (centerVertex.midright), (connectBcenter.midleft), 51)
        else:
            pygame.draw.line(screen, (44, 21, 0), (centerVertex.midtop), (connectBcenter.midtop), 51)
        pygame.draw.line(screen, (44, 21, 0), (connectBcenter.center), (vertexB.center), 51)

        pygame.draw.rect(screen, (44, 21, 0), connectCcenter)

        if cordsC[2] == 1:
            pygame.draw.line(screen, (44, 21, 0), (centerVertex.midright), (connectCcenter.midleft), 51)
        else:
            pygame.draw.line(screen, (44, 21, 0), (centerVertex.midtop), (connectCcenter.midtop), 51)
        pygame.draw.line(screen, (44, 21, 0), (connectCcenter.center), (vertexC.center), 51)

        pygame.draw.rect(screen, (44, 21, 0), connectDcenter)

        if cordsD[2] == 1:
            pygame.draw.line(screen, (44, 21, 0), (centerVertex.midright), (connectDcenter.midleft), 51)
        else:
            pygame.draw.line(screen, (44, 21, 0), (centerVertex.midtop), (connectDcenter.midtop), 51)

        pygame.draw.line(screen, (44, 21, 0), (connectDcenter.center), (vertexD.center), 51)

        pygame.draw.rect(screen, (232, 214, 203), player)


#Connects each quadrant vertex to both edges of the map
def connect_vertices_edges():
    pygame.draw.line(screen, (44, 21, 0), (edgeA1.center), (vertexA.center), 51)
    pygame.draw.line(screen, (44, 21, 0), (edgeA1.center), (targetVertex1.midtop), 51)
    pygame.draw.line(screen, (44, 21, 0), (edgeA2.center), (vertexA.center), 51)
    pygame.draw.line(screen, (44, 21, 0), (edgeA2.center), (targetVertex2.midleft), 51)

    pygame.draw.line(screen, (44, 21, 0), (edgeB1.center), (vertexB.center), 51)
    pygame.draw.line(screen, (44, 21, 0), (edgeB1.center), (targetVertex3.midtop), 51)
    pygame.draw.line(screen, (44, 21, 0), (edgeB2.center), (vertexB.center), 51)
    pygame.draw.line(screen, (44, 21, 0), (edgeB2.center), (targetVertex2.midright), 51)

    pygame.draw.line(screen, (44, 21, 0), (edgeC1.center), (vertexC.center), 51)
    pygame.draw.line(screen, (44, 21, 0), (edgeC1.center), (targetVertex1.midbottom), 51)
    pygame.draw.line(screen, (44, 21, 0), (edgeC2.center), (vertexC.center), 51)
    pygame.draw.line(screen, (44, 21, 0), (edgeC2.center), (targetVertex4.midleft), 51)

    pygame.draw.line(screen, (44, 21, 0), (edgeD1.center), (vertexD.center), 51)
    pygame.draw.line(screen, (44, 21, 0), (edgeD1.center), (targetVertex3.midbottom), 51)
    pygame.draw.line(screen, (44, 21, 0), (edgeD2.center), (vertexD.center), 51)
    pygame.draw.line(screen, (44, 21, 0), (edgeD2.center), (targetVertex4.midright), 51)

#calculates the distance between vertex1 and vertex2 in pixels
def calculate_distance(vertex1, vertex2):
    return abs(vertex1.centerx - vertex2.centerx) + abs(vertex1.centery - vertex2.centery)

#uses gameGraph's Graph and Vertex classes to create an undirected weighted graph with all vertices
def add_to_graph():
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


#Creates a list of all vertices to be used for collision checking and graph implementation
vertexList = [centerVertex, connectAcenter, connectBcenter, connectCcenter, connectDcenter,
              vertexA, vertexB, vertexC, vertexD, 
              edgeA1, edgeA2, edgeB1, edgeB2, edgeC1, edgeC2, edgeD1, edgeD2, 
              targetVertex1, targetVertex2, targetVertex3, targetVertex4]

#Creates a list of all target objects
targetObjects = [targetVertex1, targetVertex2, targetVertex3, targetVertex4]

#initializes one graph 
add_to_graph()

#counts current pixel count until the next target vertex is reached
current_pixel_count = 0
total_pixel_count = 0

#keeps track of which targets have already been collected
collected_targets = []
collected_targets.append(centerVertex)

crash_sound = pygame.mixer.Sound("pluck_sound.mp3")

#handles pixel counts when player "collects" a target
def collectTarget(target):
    pygame.mixer.Sound.play(crash_sound)

    collected_targets.append(target)
    global total_pixel_count 
    global current_pixel_count    
    total_pixel_count += current_pixel_count
    current_pixel_count = 0
    global last_collected_target 
    last_collected_target = target

#Finds the pixel count using Dijstra's algorithm (gameGraph.shortest_path()) for each of the target vertices in order of collection
def find_shortest_route():
    shortest_route = 0
    for x in range(4):
        global source
        global target
        if (collected_targets[x] == centerVertex):
            source = 'centerVertex'
            if (collected_targets[x+1] == targetVertex1):
                target = 'targetVertex1'
            elif(collected_targets[x+1] == targetVertex2):
                target = 'targetVertex2'
            elif(collected_targets[x+1] == targetVertex3):
                target = 'targetVertex3'
            elif(collected_targets[x+1] == targetVertex4):
                target = 'targetVertex4'
        elif(collected_targets[x] == targetVertex1):
            source = 'targetVertex1'
            if (collected_targets[x+1] == targetVertex2):
                target = 'targetVertex2'
            elif(collected_targets[x+1] == targetVertex3):
                target = 'targetVertex3'
            elif(collected_targets[x+1] == targetVertex4):
                target = 'targetVertex4'
            elif(collected_targets[x+1] == centerVertex):
                target = 'centerVertex'
        elif(collected_targets[x] == targetVertex2):
            source = 'targetVertex2'
            if (collected_targets[x+1] == targetVertex1):
                target = 'targetVertex1'
            elif(collected_targets[x+1] == targetVertex3):
                target = 'targetVertex3'
            elif(collected_targets[x+1] == targetVertex4):
                target = 'targetVertex4'
            elif(collected_targets[x+1] == centerVertex):
                target = 'centerVertex'
        elif(collected_targets[x] == targetVertex3):
            source = 'targetVertex3'
            if (collected_targets[x+1] == targetVertex2):
                target = 'targetVertex2'
            elif(collected_targets[x+1] == targetVertex1):
                target = 'targetVertex1'
            elif(collected_targets[x+1] == targetVertex4):
                target = 'targetVertex4'
            elif(collected_targets[x+1] == centerVertex):
                target = 'centerVertex'
        elif(collected_targets[x]== targetVertex4):
            source = 'targetVertex4'
            if (collected_targets[x+1] == targetVertex1):
                target = 'targetVertex1'
            elif(collected_targets[x+1] == targetVertex2):
                target = 'targetVertex2'
            elif(collected_targets[x+1] == targetVertex3):
                target = 'targetVertex3'
            elif(collected_targets[x+1] == centerVertex):
                target = 'centerVertex'
        shortest_route += graph.shortest_path(source)[target]
    return shortest_route

#Start screen loop
def start_screen():
    run = True
    while run:
        background = pygame.image.load("background.webp")
        background_top = screen.get_height() - background.get_height()
        background_left = screen.get_width()/2 - background.get_width()/2
        screen.blit(background, (background_left, background_top))
        startButton = pygame.Rect(310, 335, 100, 50)
        pygame.draw.rect(screen, (47,79,79), startButton)
        pygame.font.init()
        buttonFont = pygame.font.SysFont('courier', 15)
        collectFont = pygame.font.SysFont('courier', 23, True)
        titleFont = pygame.font.SysFont('courier', 100)
        collectText = collectFont.render("How efficiently can you reach all of the targets?", True, (0,0,0))
        buttonText = buttonFont.render('START', True, (255,255,255))
        titleText = titleFont.render('DIJI', True, (0,0,0))
        titleText_rect = titleText.get_rect(center=(720/2, 200))
        collectText_rect = collectText.get_rect(center=(720/2, 300))
        startText_rect = buttonText.get_rect(center= (720/2, 360))
        screen.blit(buttonText, startText_rect)
        screen.blit(collectText, collectText_rect)
        screen.blit(titleText, titleText_rect)
        
        ev = pygame.event.get()
        for event in ev:
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if startButton.collidepoint(pos):
                    run = False

        pygame.display.update()

#level1 game loop runs and looks for events
def game_loop():
    global current_pixel_count
    run = True
    while run:
        ev = pygame.event.get()
        time.sleep(0.000)
        
        set_up_game()
        connect_vertices_edges()
        connect_center_to_vertices()

        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True and isOnPath('a') and player.left - 1 != 0: 
            player.move_ip(-1,0)
            current_pixel_count += 1
            for x in targetObjects:
                if (x.collidepoint(player.left - 1, player.top) and x not in collected_targets):
                    collectTarget(x)
                    if len(collected_targets) == 5:
                        run = False

        elif key[pygame.K_d] == True and isOnPath('d') and player.right + 2 != 720:
            player.move_ip(1, 0)
            current_pixel_count += 1
            for x in targetObjects:
                if (x.collidepoint(player.right + 1, player.top) and x not in collected_targets):
                    collectTarget(x)
                    if len(collected_targets) == 5:
                        run = False
        elif key[pygame.K_w] == True and isOnPath('w') and player.top - 1 != 0:
            player.move_ip(0, -1)
            current_pixel_count  += 1
            for x in targetObjects:
                if (x.collidepoint(player.x, player.y - 1) and x not in collected_targets):
                    collectTarget(x)
                    if len(collected_targets) == 5:
                        run = False
        elif key[pygame.K_s] == True and isOnPath('s') and player.bottom + 2 != 720:
            player.move_ip(0, 1)
            current_pixel_count  += 1
            for x in targetObjects:
                if (x.collidepoint(player.right, player.bottom + 1) and x not in collected_targets):
                    collectTarget(x)
                    if len(collected_targets) == 5:
                        run = False
        for event in ev:
            if event.type==pygame.QUIT:
                run = False
        pygame.display.update()
    
#end screen/play again loop
def end_screen():
    run = True
    while run:
        ev = pygame.event.get()
        background = pygame.image.load("background.webp")
        background_top = screen.get_height() - background.get_height()
        background_left = screen.get_width()/2 - background.get_width()/2
        screen.blit(background, (background_left, background_top))
        scoreFont = pygame.font.SysFont('courier', 23, True)
        scoreText = scoreFont.render('YOUR CHOSEN ROUTE WAS ' + str((int(percent_efficiency))) + "% EFFICIENT!", True, (0,0,0))
        scoreText_rect = scoreText.get_rect(center=(720/2, 720/2))
        screen.blit(scoreText, scoreText_rect)
       
        for event in ev:
            if event.type == pygame.QUIT:
                run = False
                   
        pygame.display.update()

end_sound = pygame.mixer.Sound("good!.mp3")
fail_sound = pygame.mixer.Sound("fail.mp3")
average_sound = pygame.mixer.Sound("average.mp3")

#handles game states
start_screen()
game_loop()
#only calculated percentage if the user collected all targets
if len(collected_targets) == 5:
    shortest_route = find_shortest_route()
    percent_efficiency = ((shortest_route - (total_pixel_count - shortest_route)) / shortest_route) * 100
    if percent_efficiency < 0:
        percent_efficiency = 0
    if percent_efficiency >= 50 and percent_efficiency < 80:
        pygame.mixer.Sound.play(average_sound)
    if (percent_efficiency >= 80):
        pygame.mixer.Sound.play(end_sound)
    elif (percent_efficiency < 50):
        pygame.mixer.Sound.play(fail_sound)

    
    end_screen()

pygame.quit()


