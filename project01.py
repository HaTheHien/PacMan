import pygame
import time
import random
import sys
import copy
import operator
square = 30
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

#Use if you need
graph_temp = []
path_temp = []
check = False
list_temp = []
node_temp = []
black_list = []
not_centre = []
danger = []
old = []
number_ = 0

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
def Move(x_now, y_now, max_expand_move):
    if max_expand_move == 'a':
        x_now -= 1
    if max_expand_move == 'w':
        y_now -= 1
    if max_expand_move == 's':
        y_now += 1
    if max_expand_move == 'd':
        x_now += 1
    return x_now, y_now
def Mahattan(x_now,y_now,x_end = pac[0],y_end = pac[1]):
    return abs(x_end - x_now) + abs(y_end - y_now)
def mahatan_node_temp(node_food):
    return Mahattan(node_temp[0],node_temp[1],node_food[0],node_food[1])
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
    
def vision(x,y,vision_bool1 = []):
    if len(vision_bool1) == 0:
        for i in range(len(graph)):
            vision_bool1.append([])
            for j in range(len(graph[0])):
                vision_bool1[i].append(False)
    fqueue = [((x,y),0)]
    explored = []
    number = 0
    while len(fqueue) > 0:
        node = fqueue.pop(0)
        if vision_bool1[node[0][1]][node[0][0]] == False:
            vision_bool1[node[0][1]][node[0][0]] = True
            number+=1
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
    return vision_bool1,number

def vision_4_direct():
    global vision_bool
    vision_bool2 = copy.deepcopy(vision_bool)
    number = 0
    for i in range(len(graph_fog)):
        for j in range(len(graph_fog[0])):
            if graph_fog[i][j][0] != -1:
                vision_bool2[i][j] = True
                number+=1
            else:
                vision_bool2[i][j] = False
    x,y = pac[0],pac[1]
    temp = [('d',0),('a',0),('s',0),('w',0)]
    n = 0
    buffer = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
    while len(buffer)>0:
        node = buffer.pop(0)
        if canMove(node[0],node[1]) and len(graph[node[1]][node[0]]) == 1:
            temp2,number_ = vision(node[0],node[1],copy.deepcopy(vision_bool2))
            temp[n] = (temp[n][0],number_)
        n+=1
    return temp
def change_direct(x,y):
    if x < pac[0]:
        pacman[0] = pacman3
    if x > pac[0]:
        pacman[0] = pacman1
    if y > pac[1]:
        pacman[0] = pacman4
    if y < pac[1]:
        pacman[0] = pacman2
        
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
                
def return_index_1(node):
    return node[1]
def return_len_path(node):
    return len(node[0])
def return_index_2(node):
    return node[2]
def PacMan_A_star(x_now,y_now,x_end,y_end,food_list,explored = []):
    global node_temp
    check= False
    if len(explored) > 0 or len(node_temp) > 0:
        check = True
    fqueue = [([(x_now,y_now)],Mahattan(x_end,y_end),0,food_list)]
    while len(fqueue) > 0:
        fqueue = sorted(fqueue,key = return_index_1)
        node = fqueue.pop(0)
        last_node = node[0][-1]
        food_l = node[3]
        explored.append(last_node)
        f = node[1]
        g = node[2]
        if last_node in food_l:
            food_l.remove(last_node)
            if check == True:
                return node[0],food_l,explored
            else:
                g-=1
        if last_node[0] == x_end and last_node[1] == y_end:
            return node[0],food_l,explored
        buffer = [(last_node[0]+1,last_node[1]),(last_node[0]-1,last_node[1]),(last_node[0],last_node[1]+1),(last_node[0],last_node[1]-1)]
        while len(buffer) > 0:
            path = node[0].copy()
            temp = buffer.pop(random.randint(0,len(buffer) - 1))
            path.append(temp)
            if canMove(temp[0],temp[1]) and len(graph[last_node[1]][last_node[0]]) == 1 and temp not in explored:
                node1 = (path,Mahattan(temp[0],temp[1],x_end,y_end)+g,g+1,food_l.copy())
                fqueue.append(node1)
    return [],food_list,explored

def AI(level,number_food):
    global check
    global path_temp
    global node_temp
    global black_list
    global danger
    global not_centre
    global number_
    if level == 1 or level == 2:
        if check == False:
            check = True
            # remove food can't go
            explored = []
            food_list = []
            for i in range(len(graph)):
                graph_temp.append([])
                for j in range(len(graph[0])):
                    graph_temp[i].append([0])
            fqueue = [(pac[0],pac[1])]
            all_explored = []
            while len(fqueue) > 0:
                fqueue = sorted(fqueue,key = return_index_1)
                node = fqueue.pop(0)
                x,y = node[0],node[1]
                graph_temp[y][x] = graph[y][x]
                if graph_temp[y][x][0] == 2 and node not in all_explored:
                    food_list.append(node)
                all_explored.append(node)
                buffer = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
                while len(buffer) > 0:
                    temp = buffer.pop(random.randint(0,len(buffer) - 1))
                    if canMove(temp[0],temp[1]) and len(graph[temp[1]][temp[0]]) == 1 and temp not in all_explored:
                        fqueue.append(temp)
            n = len(food_list)
            #search
            max_path = []
            max_score = 0
            fqueue = [([(pac[0],pac[1])],food_list,0)]
            number = 0
            depth = 99999
            while len(fqueue) > 0:
                fqueue = sorted(fqueue,key = return_index_2)
                node = fqueue.pop(0)
                last_node = node[0][-1]
                food_l1 = node[1]
                score = node[2]
                if score > max_score:
                    max_score = score
                    max_path = node[0]
                if len(node[0]) > depth:
                    continue
                if len(food_l1) == 0:
                    depth = len(node[0])
                    continue
                #A_star
                node_temp = last_node
                food_l2 = sorted(food_l1,key = mahatan_node_temp)
                food_near = food_l2.pop(0)
                path_,food_l4,explored = PacMan_A_star(last_node[0],last_node[1],food_near[0],food_near[1],food_l1.copy(),[])
                path_.remove(last_node)
                path = node[0] + path_
                score_ = (n - len(food_l4))*20 - len(path)
                fqueue.append((path,food_l4,score_))
                node_temp = food_near
                path_ = []
                while len(food_l2) > 0:
                    food_near = food_l2.pop(0)
                    path_1,food_l4,explored = PacMan_A_star(last_node[0],last_node[1],food_near[0],food_near[1],food_l1.copy(),path_)
                    if len(path_1) == 0:
                        break
                    path_1.remove(last_node)
                    path = node[0] + path_1
                    score_ = (n - len(food_l4))*20 - len(path)
                    fqueue.append((path,food_l4,score_))
                    path_ = path_ + path_1
                    node_temp = []
            path_temp = max_path
            if len(path_temp) == 0:
                return 0,0,True
            temp = path_temp.pop(0)
            return temp[0],temp[1],False
        else:
            if len(path_temp) == 0:
                return 0,0,True
            temp = path_temp.pop(0)
            time.sleep(0.2)
            return temp[0],temp[1],False
    if level == 3:
        time.sleep(0.5)
        ghost_arr = []
        for i in range(0,len(graph_fog)):
            for j in range(0,len(graph_fog[0])):
                if len(graph_fog[i][j]) > 1:
                    ghost_arr.append((j,i))
        food_arr = []
        for i in range(len(graph)):
            graph_temp.append([])
            for j in range(len(graph[0])):
                graph_temp[i].append([0])
        fqueue = [(pac[0],pac[1])]
        danger2 = []
        for j,i in ghost_arr:
            if (j,i) not in danger:
                danger.append((j,i))
            buffer = [(j+1,i),(j-1,i),(j,i+1),(j,i-1),(j,i)]
            while len(buffer) > 0:
                temp = buffer.pop(0)
                if canMove(temp[0],temp[1]):
                    danger2.append(temp)
                    if temp in danger:
                        if temp not in black_list and temp not in not_centre:
                            if graph_fog[i][j][0] != -1:
                                black_list.append(temp)
                    else:
                        if temp in black_list:
                            black_list.remove(temp)
                            not_centre.append(temp)
                            if temp not in food_arr:
                                food_arr.append(temp)
        flag = False
        vision_bool1,n = vision(pac[0],pac[1],[])
        for i in danger:
            if i not in danger2:
                if i in not_centre:
                    continue
                buffer = [(i[0]+1,i[1]),(i[0]-1,i[1]),(i[0],i[1]+1),(i[0],i[1]-1),(i[0],i[1])]
                while len(buffer) > 0:
                    temp = buffer.pop(0)
                    if canMove(temp[0],temp[1]) and vision_bool1[temp[1]][temp[0]] == False:
                        flag = True
                        break
                if flag == False:
                    not_centre.append(i)
                    if i in black_list:
                        black_list.remove(i)
        flag = False
        all_explored = []
        while len(fqueue) > 0:
            number = -1
            fqueue = sorted(fqueue,key = return_index_1)
            node = fqueue.pop(0)
            x,y = node[0],node[1]
            graph_temp[y][x] = graph_fog[y][x]
            if graph_temp[y][x][0] == 2 and node not in all_explored:
                number = 0
                food_arr.append(node)
            all_explored.append(node)
            buffer = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            if node in black_list:
                number = -1
            while len(buffer) > 0:
                temp = buffer.pop(random.randint(0,len(buffer) - 1))
                if canMove(temp[0],temp[1]) and vision_bool1[temp[1]][temp[0]] == True:
                    if number != -1 :
                        if len(graph_temp[temp[1]][temp[0]]) > 1:
                            number+=1
                        else:
                            if len(graph_temp[temp[1]][temp[0]]) == 1:
                                number-=1
                    if number >= 2 and node in food_arr:
                       black_list.append(node)
                       food_arr.remove(node)
                    if number >= 0 and number < 2:
                        if node in black_list:
                            black_list.remove(node)
                if canMove(temp[0],temp[1]) and temp not in all_explored:
                    if temp not in black_list:
                        fqueue.append(temp)
        
        if len(food_arr) == 0:
            expand_size = vision_4_direct()
            expand_size = sorted(expand_size, key = operator.itemgetter(1))
            max_expand_move = expand_size[-1][0]
            if expand_size[1] == 0:
                flag = True
            if max_expand_move == 'a' and canMove(pac[0]-1,pac[1]):
                pac[0] -= 1
            if max_expand_move == 'w' and canMove(pac[0],pac[1]-1):
                pac[1] -= 1
            if max_expand_move == 's' and canMove(pac[0]+1,pac[1]):
                pac[1] += 1
            if max_expand_move == 'd' and canMove(pac[0],pac[1] + 1):
                pac[0] += 1

        #print(black_list)
        #print(danger,'\n')
        #BFS
        max_score = 0
        max_path = []
        min_path_explore = []
        explored = []
        fqueue = [([(pac[0],pac[1])],food_arr,0)]
        while len(fqueue) > 0:
            node = fqueue.pop(0)
            last_node = node[0][-1]
            food_l1 = node[1]
            score = node[2]
            x,y = last_node[0],last_node[1]
            if graph_fog[y][x][0] == -1:
                min_path_explore = node[0]
                if flag == True:
                    max_path = node[0]
                    break
            if graph_fog[y][x][0] == 2 and (x,y) not in black_list and (x,y) in food_l1:
                food_l1.remove((x,y))
                score+=20
            if score > max_score:
                max_score = score
                max_path = node[0]
            buffer = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
            while len(buffer) > 0:
                path = node[0].copy()
                temp = buffer.pop(0)
                if canMove(temp[0],temp[1]) and graph_fog[temp[1]][temp[0]][0] != -1 and temp not in explored and temp not in black_list:
                    path.append(temp)
                    if temp in danger:
                        fqueue.append((path,food_l1.copy(),score - 10))
                    else:
                        fqueue.append((path,food_l1.copy(),score - 1))
                    explored.append(temp)
        if len(max_path) != 0:
            x,y = max_path[1][0],max_path[1][1]
            flag2 = False
            if len(graph_fog[y][x]) == 1:
                buffer = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
                while len(buffer) > 0:
                    temp = buffer.pop(0)
                    if canMove(temp[0],temp[1]) and len(graph_fog[temp[1]][temp[0]]) > 1:
                        flag2 = True
                        break
                if flag2 == False and flag != True and (x,y) != pac:
                    number_ = 0
                    return max_path[1][0],max_path[1][1],False
        number_ += 1
        if number_ >= 3 and len(max_path) == 0:
            return pac[0],pac[1],True
        if number_ >= 10 and len(max_path) != 0:
            return pac[0],pac[1],True
        x,y = pac[0],pac[1]
        buffer = [(x,y),(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
        while len(buffer) > 0:
            temp = buffer.pop(0)
            if canMove(temp[0],temp[1]) and temp not in danger:
                return temp[0],temp[1],False
        return pac[0],pac[1],False
            
    if level == 4:    
        time.sleep(0.05)
        ghost_arr = []
        food_arr = []
        for i in range(0,len(graph_fog)):
            for j in range(0,len(graph_fog[0])):
                if graph_fog[i][j][0] == 2:
                    food_arr.append((j,i))
                if len(graph_fog[i][j]) > 1:
                    ghost_arr.append((j,i))
                    continue
        expand_size = vision_4_direct()
        expand_size = sorted(expand_size, key = operator.itemgetter(1))
        max_expand_move = expand_size[-1][0]
        if len(food_arr) == 0 and len(ghost_arr) == 0:
            pac[0], pac[1] = Move(pac[0], pac[1], max_expand_move)
            return pac[0], pac[1], False
<<<<<<< HEAD
        if len(food_arr) != 0 and len(ghost_arr) == 0:
            if check == False:
                check = True
                # remove food can't go
                explored = []
                food_list = []
                for i in range(len(graph)):
                    graph_temp.append([])
                    for j in range(len(graph[0])):
                        graph_temp[i].append([0])
                fqueue = [(pac[0], pac[1])]
                all_explored = []
                while len(fqueue) > 0:
                    fqueue = sorted(fqueue, key=return_index_1)
                    node = fqueue.pop(0)
                    x, y = node[0], node[1]
                    graph_temp[y][x] = graph[y][x]
                    if graph_temp[y][x][0] == 2 and node not in all_explored:
                        food_list.append(node)
                    all_explored.append(node)
                    buffer = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
                    while len(buffer) > 0:
                        temp = buffer.pop(random.randint(0, len(buffer) - 1))
                        if canMove(temp[0], temp[1]) and len(graph[temp[1]][temp[0]]) == 1 and temp not in all_explored:
                            fqueue.append(temp)
                n = len(food_list)
                # search
                max_path = []
                max_score = 0
                fqueue = [([(pac[0], pac[1])], food_list, 0)]
                flag = True
                number = 0
                depth = 99999
                while len(fqueue) > 0:
                    fqueue = sorted(fqueue, key=return_index_2)
                    if flag == True:
                        node = fqueue.pop(0)
                    else:
                        node = fqueue.pop(-1)
                    last_node = node[0][-1]
                    food_l1 = node[1]
                    score = node[2]
                    if score > max_score:
                        max_score = score
                        max_path = node[0]
                    if len(node[0]) > depth:
                        continue
                    if len(food_l1) == 0:
                        depth = len(node[0])
                        continue
                    # A_star
                    node_temp = last_node
                    food_l2 = sorted(food_l1, key=mahatan_node_temp)
                    food_near = food_l2.pop(0)
                    path_, food_l4, explored = PacMan_A_star(last_node[0], last_node[1], food_near[0], food_near[1],
                                                             food_l1.copy(), [])
                    path_.remove(last_node)
                    path = node[0] + path_
                    score_ = (n - len(food_l4)) * 20 - len(path)
                    fqueue.append((path, food_l4, score_))
                    node_temp = food_near
                    explored = []
                    while len(food_l2) > 0:
                        food_near = food_l2.pop(0)
                        path_1, food_l4, explored = PacMan_A_star(last_node[0], last_node[1], food_near[0],
                                                                  food_near[1], food_l1.copy(), path_)
                        if len(path_1) == 0:
                            break
                        path_1.remove(last_node)
                        path = node[0] + path_1
                        score_ = (n - len(food_l4)) * 20 - len(path)
                        fqueue.append((path, food_l4, score_))
                        path_ = path_ + path_1
                        node_temp = []
                path_temp = max_path
                if len(path_temp) == 0:
                    return 0, 0, True
                temp = path_temp.pop(0)
                return temp[0], temp[1], False
            else:
                if len(path_temp) == 0:
                    return 0, 0, True
                temp = path_temp.pop(0)
                time.sleep(0.2)
                return temp[0], temp[1], False
=======
        
<<<<<<< HEAD
=======
>>>>>>> eb1f3f98a2ec24b51d7bf7ab7517d226d77e67be
            
        
                
                    
            
        
        
>>>>>>> 3f6fac13d2ce8df7911008dd88f6f7745d9df5cd
    if True:   #test
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
    return pac[0],pac[1],True

def AlgorithmGhostIndex0(ghost_node):
    x_now,y_now = ghost_node[1][0],ghost_node[1][1]
    fqueue = [([(x_now,y_now)],Mahattan(x_now,y_now),0)]
    explored = []
    while len(fqueue) > 0:
        fqueue = sorted(fqueue,key = return_index_1)
        node = fqueue.pop(0)
        last_node = node[0][-1]
        if last_node[0] == pac[0] and last_node[1] == pac[1]:
            ghost_node[1] = node[0][1]
            break   
        explored.append(last_node)
        f = node[1]
        g = node[2]
        buffer = [(last_node[0]+1,last_node[1]),(last_node[0]-1,last_node[1]),(last_node[0],last_node[1]+1),(last_node[0],last_node[1]-1)]
        while len(buffer) > 0:
            path = node[0].copy()
            temp = buffer.pop(random.randint(0,len(buffer) - 1))
            path.append(temp)
            if canMove(temp[0],temp[1]) and temp not in explored:
                node1 = (path,Mahattan(temp[0],temp[1])+g,g+1)
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
    
def renderBoard(Fog = False):
    global vision_bool
    global graph_fog
    screen.fill((0,0,0))
    ghost1 = pygame.image.load('ghost.png')
    ghost2 = pygame.image.load('ghost1.png')
    ghost3 = pygame.image.load('ghost2.png')
    ghost4 = pygame.image.load('ghost3.png')
    ghost = [ghost1,ghost2,ghost3,ghost4]
    wall = pygame.image.load('wall.png')
    food = pygame.image.load('food.png')
    land_no_fog = pygame.image.load('land_no_fog.png')
    land_fog = pygame.image.load('land_fog.png')
    food_fog = pygame.image.load('food_fog.png')
    wall_fog = pygame.image.load('wall_fog.png')
    vision_bool,number = vision(pac[0],pac[1],[])
    if Fog == True:
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                if vision_bool[i][j] == True:
                    screen.blit(land_no_fog, (j* square,i * square))
                else:
                    if graph_fog[i][j][0] != -1:
                        screen.blit(land_fog, (j* square,i * square))
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
                if graph[i][j][0] == 0 and vision_bool[i][j] == True:
                    graph_fog[i][j] = [0]
    else:
        for i in range(len(graph)):
            for j in range(len(graph[0])):
                screen.blit(land_no_fog, (j* square,i * square))
                if graph[i][j][0] == 1:
                    screen.blit(wall, (j* square,i * square))
                if graph[i][j][0] == 2:
                    screen.blit(food, (j* square,i * square))
                if len(graph[i][j]) > 1:
                    ghost_node = ghost_array[graph[i][j][-1] - 3]
                    screen.blit(ghost[ghost_node[0]], (j* square,i * square))
    screen.blit(pacman[0], (pac[0] * square,pac[1] * square))
    #pygame.draw.line(screen,orange,(0, height[0]  * square),(width[0] * square, height[0] * square),width=2)
    font1 = pygame.font.SysFont("arial", 26)
    text1 = font1.render("SCORE: " + str(score[0]), True, green, blue)
    textRect1 = text1.get_rect()
    textRect1.center = (0, height[0] * square + 3)
    screen.blit(text1, textRect1.center)
    pygame.display.update()

def play(choose):
    global graph_fog
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
                graph_fog[i].append([-1])
        Fog = True
    #level = 5
    path = []
    explored = []
    a = 0
    TimeStart = time.time()
    while run[0] == 1:
        renderBoard(Fog)
        if graph[pac[1]][pac[0]][0] == 2:
            score[0] += 20
            graph[pac[1]][pac[0]][0] = 0
            if level >= 3:
                graph_fog[pac[1]][pac[0]][0] = 0
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
                return path,a
        x = pac[0]
        y = pac[1]
        flag = False
        ff = False
        explored_ = []
        while flag == False and ff == False:
            if choose[0] == 0:
                x,y,ff = Human()
            else:
                x,y,ff = AI(level,number_food)
            flag = canMove(x,y)
            if len(explored_) > 0:
                explored = explored_
        a = time.time() - TimeStart
        change_direct(x,y)
        path.append((x,y))
        if ff == True:
            renderBoard(Fog)
            font = pygame.font.SysFont("arial", 36)
            text = font.render('SURRENDER', True, green, blue)
            textRect = text.get_rect()
            textRect.center = (0, (height[0] + 1) * square + 3)
            screen.blit(text, textRect.center)
            pygame.display.update()
            time.sleep(1)
            return path,a
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
            return path,a
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
            return path,a
        
def write_file(path,time):
    file = open('output.txt','w')
    file.write('Path:')
    for i in path:
        file.write('('+ str(i[0]) +',' + str(i[1]) +') ')
    file.write('\nLen path:' + str(len(path)))
    file.write('\nTime:'+str(time))
    file.close()
    
if __name__ == '__main__':
    choose = input_level()
    input_matrix()
    path,time = play(choose)
    write_file(path,time)
    exit(0)
