import pygame
import time
import random
square = 60
pac = [0,0]
graph = []
graph_fog = []
vision_bool = []
run = [1]
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)
orange = (255,69,0)
color_light = (170,170,170)
color_dark = (100,100,100)
no_color = (255,255,255)
dark = (0,0,0)
score = [0]
height,width = [0],[0]
ghost_array = []  #IndexColor,(x_now,y_now),(x_start,y_start),IndexAlgorithm
pacman1 = pygame.image.load('pacman1.png')
pacman2 = pygame.image.load('pacman2.png')
pacman3 = pygame.image.load('pacman3.png')
pacman4 = pygame.image.load('pacman4.png')
pacman = [pacman1]

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('PACMAN')

def input_level():
    click_AI = False
    font2 = pygame.font.SysFont("arial", 36)
    AI_level = font2.render('AI', True, no_color)
    HUMAN_level = font2.render('Human', True, no_color)
    LV1 = font2.render('LV1', True, no_color)
    LV2 = font2.render('LV2', True, no_color)
    LV3 = font2.render('LV3', True, no_color)
    LV4 = font2.render('LV4', True, no_color)
    pygame.display.update()
    while True:
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get(): 
            if ev.type == pygame.QUIT: 
                pygame.quit() 
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 10 <= mouse[0] <= 10 + 50 and 100 <= mouse[1] <= 100 +40:
                    click_AI = True
                if 10 <= mouse[0] <= 10 + 140 and 300 <= mouse[1] <= 300 +40:
                    return (0,4)
                if click_AI == True:
                    if 80 <= mouse[0] <= 80 + 70 and 100 <= mouse[1] <= 100 +40:
                        return (1,1)
                    if 170 <= mouse[0] <= 170 + 70 and 100 <= mouse[1] <= 100 +40:
                        return (1,2)
                    if 260 <= mouse[0] <= 260 + 70 and 100 <= mouse[1] <= 100 +40:
                        return (1,3)
                    if 350 <= mouse[0] <= 350 + 70 and 100 <= mouse[1] <= 100 +40:
                        return (1,4)
                    
        if (10 <= mouse[0] <= 10 + 50 and 100 <= mouse[1] <= 100 +40) or click_AI == True: 
            pygame.draw.rect(screen,color_light,[10,100,50,40])  
        else: 
            pygame.draw.rect(screen,color_dark,[10,100,50,40])
        screen.blit(AI_level , (10+10,100))

        if 10 <= mouse[0] <= 10 + 140 and 300 <= mouse[1] <= 300 +40: 
            pygame.draw.rect(screen,color_light,[10,300,140,40])  
        else: 
            pygame.draw.rect(screen,color_dark,[10,300,140,40])
        screen.blit(HUMAN_level , (10 + 10,300))
        
        if click_AI == True:
            if 80 <= mouse[0] <= 80 + 70 and 100 <= mouse[1] <= 100 +40: 
                pygame.draw.rect(screen,color_light,[80,100,70,40])  
            else: 
                pygame.draw.rect(screen,color_dark,[80,100,70,40])
            screen.blit(LV1 , (70 + 10, 100))
            if 170 <= mouse[0] <= 170 + 70 and 100 <= mouse[1] <= 100 +40: 
                pygame.draw.rect(screen,color_light,[170,100,70,40])  
            else: 
                pygame.draw.rect(screen,color_dark,[170,100,70,40])
            screen.blit(LV2 , (170 + 10, 100))
            if 260 <= mouse[0] <= 260 + 70 and 100 <= mouse[1] <= 100 +40: 
                pygame.draw.rect(screen,color_light,[260,100,70,40])  
            else: 
                pygame.draw.rect(screen,color_dark,[260,100,70,40])
            screen.blit(LV3 , (260 + 10, 100))
            if 350 <= mouse[0] <= 350 + 70 and 100 <= mouse[1] <= 100 +40: 
                pygame.draw.rect(screen,color_light,[350,100,70,40])  
            else: 
                pygame.draw.rect(screen,color_dark,[350,100,70,40])
            screen.blit(LV4 , (350 + 10, 100))
        
        pygame.display.update()

def input_matrix():
    file = open("input.txt","r")
    temp = list(map(int,file.readline().split()))
    height[0],width[0] = temp[0],temp[1]
    for i in range(height[0]):
        temp = list(map(int,file.readline().split()))
        row = []
        for i in temp:
            temp1 = []
            temp1.append(i)
            row.append(temp1)
        graph.append(row)
    temp = list(map(int,file.readline().split()))
    pac[0] = temp[0]
    pac[1] = temp[1]
    screen = pygame.display.set_mode((width[0] * square,(height[0] + 2) * square))
    screen.fill(dark)
    pygame.display.flip()

def Human():
    ff = False
    x_ = pac[0]
    y_ = pac[1]
    pygame.event.clear()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == 97 or event.key == pygame.K_LEFT:
                        x_ = x_ - 1
                        pacman[0] = pacman3
                    if event.key == 119 or event.key == pygame.K_UP:
                        y_ = y_ - 1
                        pacman[0] = pacman2
                    if event.key == 115 or event.key == pygame.K_DOWN:
                        y_ = y_ + 1
                        pacman[0] = pacman4
                    if event.key == 100 or event.key == pygame.K_RIGHT:
                        x_ = x_ + 1
                        pacman[0] = pacman1
                    if event.key == pygame.K_SPACE:
                        return pac[0],pac[1],ff
                    if event.key == pygame.K_ESCAPE:
                        run[0] = 0
                        ff = True
                if x_ != pac[0] or y_ != pac[1] or ff == True:
                    return x_,y_,ff
    
def AI(level):
    #print(graph_fog)
    ff = False
    x_ = pac[0]
    y_ = pac[1]
    pygame.event.clear()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == 97 or event.key == pygame.K_LEFT:
                        x_ = x_ - 1
                        pacman[0] = pacman3
                    if event.key == 119 or event.key == pygame.K_UP:
                        y_ = y_ - 1
                        pacman[0] = pacman2
                    if event.key == 115 or event.key == pygame.K_DOWN:
                        y_ = y_ + 1
                        pacman[0] = pacman4
                    if event.key == 100 or event.key == pygame.K_RIGHT:
                        x_ = x_ + 1
                        pacman[0] = pacman1
                    if event.key == pygame.K_SPACE:
                        return pac[0],pac[1],ff
                    if event.key == pygame.K_ESCAPE:
                        run[0] = 0
                        ff = True
                if x_ != pac[0] or y_ != pac[1] or ff == True:
                    return x_,y_,ff
    return 0,0,True

def canSee(x,y):
    if x >= width[0] or x < 0:
        return False
    if y >= height[0] or y < 0:
        return False
    return True

def canMove(x,y):
    if x >= width[0] or x < 0:
        return False
    if y >= height[0] or y < 0:
        return False
    if graph[y][x][0] == 1:
        return False
    return True

def return_h(node):
    return node[1]
def Mahattan(x_now,y_now):
    return abs(pac[0] - x_now) + abs(pac[1] - y_now)
def AlgorithmGhostIndex0(ghost_node):
    x_now,y_now = ghost_node[1][0],ghost_node[1][1]
    fqueue = [([(x_now,y_now)],Mahattan(x_now,y_now))]
    while len(fqueue) > 0:
        fqueue = sorted(fqueue,key = return_h)
        node = fqueue.pop(0)
        if node[0][-1][0] == pac[0] and node[0][-1][1] == pac[1]:
            ghost_node[1] = node[0][1]
            break
        if canMove(node[0][-1][0] + 1,node[0][-1][1])  and (node[0][-1][0] + 1,node[0][-1][1]) not in node[0]:
            temp = []
            temp = node[0].copy()
            temp.append((node[0][-1][0] + 1,node[0][-1][1]))
            node1 = (temp,Mahattan(node[0][-1][0] + 1,node[0][-1][1]))
            fqueue.append(node1)
        if canMove(node[0][-1][0] - 1,node[0][-1][1])  and (node[0][-1][0]  - 1,node[0][-1][1]) not in node[0]:
            temp = []
            temp = node[0].copy()
            temp.append((node[0][-1][0] - 1,node[0][-1][1]))
            node1 = (temp,Mahattan(node[0][-1][0] - 1,node[0][-1][1]))
            fqueue.append(node1)
        if canMove(node[0][-1][0],node[0][-1][1] + 1)  and (node[0][-1][0],node[0][-1][1] + 1) not in node[0]:
            temp = []
            temp = node[0].copy()
            temp.append((node[0][-1][0],node[0][-1][1] + 1))
            node1 = (temp,Mahattan(node[0][-1][0],node[0][-1][1] + 1))
            fqueue.append(node1)
        if canMove(node[0][-1][0],node[0][-1][1] - 1) and (node[0][-1][0],node[0][-1][1] - 1) not in node[0]:
            temp = []
            temp = node[0].copy()
            temp.append((node[0][-1][0],node[0][-1][1] - 1))
            node1 = (temp,Mahattan(node[0][-1][0],node[0][-1][1] - 1))
            fqueue.append(node1)
    return ghost_node

def Ghost_play(level):
    if level <= 2:
        return
    if level == 3:
        for i in range(0,len(ghost_array)):
            x_now,y_now = ghost_array[i][1][0],ghost_array[i][1][1]
            x_start,y_start = ghost_array[i][2][0],ghost_array[i][2][1]
            if x_now == x_start and y_now == y_start:
                list_ = [(x_start - 1,y_start),(x_start + 1,y_start),(x_start,y_start - 1),(x_start,y_start + 1)]
                flag = False
                while len(list_) > 0:
                    temp = list_.pop(random.randint(0,len(list_)-1))
                    x_now = temp[0]
                    y_now = temp[1]
                    flag = canMove(x_now,y_now)
                    if flag == True:
                        break
                if flag == False:
                    continue
                graph[y_start][x_start].remove(i+3)
                graph[y_now][x_now].append(i+3)
                ghost_array[i][1] = (x_now,y_now)
            else:
                graph[y_now][x_now].remove(i+3)
                graph[y_start][x_start].append(i+3)
                ghost_array[i][1] = (ghost_array[i][2][0],ghost_array[i][2][1])
    if level == 4:
        for i in range(0,len(ghost_array)):
            if ghost_array[i][4] == 0:
                x_now,y_now = ghost_array[i][1][0],ghost_array[i][1][1]
                graph[y_now][x_now].remove(i+3)
                ghost_array[i] = AlgorithmGhostIndex0(ghost_array[i])
                x_now,y_now = ghost_array[i][1][0],ghost_array[i][1][1]
                graph[y_now][x_now].append(i+3)
    return
def vision():
    vision_bool = []
    for i in range(len(graph)):
        vision_bool.append([])
        for j in range(len(graph[0])):
            vision_bool[i].append(False)
    fqueue = [((pac[0],pac[1]),0)]
    explored = []
    while len(fqueue) > 0:
        fqueue = sorted(fqueue,key = return_h)
        node = fqueue.pop(0)
        vision_bool[node[0][1]][node[0][0]] = True
        explored.append(node[0])
        depth = node[1]
        if depth == 4:
            continue
        if depth < 3:
            buffer = [(node[0][0]+1,node[0][1]),(node[0][0]-1,node[0][1]),(node[0][0],node[0][1]+1),(node[0][0],node[0][1]-1)]
        else:
            buffer = [(node[0][0]+1,node[0][1]),(node[0][0]-1,node[0][1]),(node[0][0],node[0][1]+1),(node[0][0],node[0][1]-1),(node[0][0]-1,node[0][1]+1),(node[0][0]+1,node[0][1]-1),(node[0][0]-1,node[0][1]-1),(node[0][0]+1,node[0][1]+1)]
        while len(buffer) > 0:
            temp = buffer.pop(random.randint(0,len(buffer) - 1))
            if canSee(temp[0],temp[1])  and temp not in explored:
                node1 = (temp,depth + 1)
                fqueue.append(node1)
    return vision_bool
    
    
def renderBoard(Fog = False):
    screen.fill((0,0,0))
    ghost1 = pygame.image.load('ghost.png')
    ghost2 = pygame.image.load('ghost1.png')
    ghost3 = pygame.image.load('ghost2.png')
    ghost4 = pygame.image.load('ghost3.png')
    ghost = [ghost1,ghost2,ghost3,ghost4]
    wall = pygame.image.load('wall.png')
    food = pygame.image.load('food.png')
    land = pygame.image.load('land_no_fog.png')
    food_fog = pygame.image.load('food_fog.png')
    wall_fog = pygame.image.load('wall_fog.png')
    vision_bool = vision()
    if Fog == True:
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if vision_bool[i][j] == True:
                    screen.blit(land, (j* square,i * square))
                if len(graph[i][j]) > 1 and vision_bool[i][j] == True:
                    graph_fog[i][j] = graph[i][j]
                    ghost_node = ghost_array[graph[i][j][-1] - 3]
                    screen.blit(ghost[ghost_node[0]], (j* square,i * square))
                    continue
                if graph[i][j][0] == 1:
                    if vision_bool[i][j] == True:
                        graph_fog[i][j] = [1]
                        screen.blit(wall, (j* square,i * square))
                    elif graph_fog[i][j][0] == 1:
                        screen.blit(wall_fog, (j* square,i * square))
                if graph[i][j][0] == 2:
                    if vision_bool[i][j] == True:
                        graph_fog[i][j] = [2]
                        screen.blit(food, (j* square,i * square))
                    elif graph_fog[i][j][0] == 2:
                        screen.blit(food_fog, (j* square,i * square))
    else:
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                screen.blit(land, (j* square,i * square))
                if graph[i][j][0] == 1:
                    screen.blit(wall, (j* square,i * square))
                if graph[i][j][0] == 2:
                    screen.blit(food, (j* square,i * square))
                if len(graph[i][j]) > 1:
                    ghost_node = ghost_array[graph[i][j][-1] - 3]
                    screen.blit(ghost[ghost_node[0]], (j* square,i * square))
    screen.blit(pacman[0], (pac[0] * square,pac[1] * square))
    pygame.draw.line(screen,orange,(0, height[0]  * square),(width[0] * square, height[0] * square),width=2)
    font1 = pygame.font.SysFont("arial", 36)
    text1 = font1.render("SCORE: " + str(score[0]), True, green, blue)
    textRect1 = text1.get_rect()
    textRect1.center = (0, height[0] * square + 3)
    screen.blit(text1, textRect1.center)
    pygame.display.update()

def play(choose):
    level = choose[1]
    number_food = 0
    Fog = False
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j][0] == 2:
                number_food += 1
            if graph[i][j][0] == 3:
                graph[i][j][0] = 0
                if level != 1:
                    index = len(ghost_array) + 3
                    graph[i][j].append(index)
                    ghost_node = [random.randint(0, 3),(j , i) ,(j , i),index,0]
                    ghost_array.append(ghost_node)
    if level >= 3:
        for i in range(len(graph)):
            graph_fog.append([])
            for j in range(len(graph[0])):
                graph_fog[i].append([0])
        Fog = True
    while run[0] == 1:
        renderBoard(Fog)
        x = pac[0]
        y = pac[1]
        flag = False
        ff = False
        while flag == False and ff == False:
            if choose[0] == 0:
                x,y,ff = Human()
            else:
                x,y,ff = AI(level)
            flag = canMove(x,y)
        if ff == True:
            font = pygame.font.SysFont("arial", 36)
            text = font.render('SURRENDER', True, green, blue)
            textRect = text.get_rect()
            textRect.center = (0, (height[0] + 1) * square + 3)
            screen.blit(text, textRect.center)
            pygame.display.update()
            time.sleep(1)
            exit(0)
        pac[0],pac[1] = x,y
        score[0] -=1
        if graph[pac[1]][pac[0]][-1] >= 3:
            renderBoard(Fog)
            font = pygame.font.SysFont("arial", 36)
            text = font.render('GAME OVER', True, green, blue)
            textRect = text.get_rect()
            textRect.center = (0, (height[0] + 1) * square + 3)
            screen.blit(text, textRect.center)
            pygame.display.update()
            time.sleep(2)
            exit(0)
        #ghost play
        Ghost_play(level)
        if graph[pac[1]][pac[0]][-1] >= 3:
            renderBoard(Fog)
            font = pygame.font.SysFont("arial", 36)
            text = font.render('GAME OVER', True, green, blue)
            textRect = text.get_rect()
            textRect.center = (0, (height[0] + 1) * square + 3)
            screen.blit(text, textRect.center)
            pygame.display.update()
            time.sleep(2)
            exit(0)
        if graph[pac[1]][pac[0]][0] == 2:
            score[0] += 20
            graph[pac[1]][pac[0]][0] = 0
            number_food -= 1
            if number_food == 0:
                renderBoard(Fog)
                font = pygame.font.SysFont("arial", 36)
                text = font.render('YOU WIN', True, green, blue)
                textRect = text.get_rect()
                textRect.center = (0, (height[0] + 1) * square + 3)
                screen.blit(text, textRect.center)
                pygame.display.update()
                time.sleep(2)
                exit(0)

if __name__ == '__main__':
    choose = input_level()
    input_matrix()
    play(choose)

