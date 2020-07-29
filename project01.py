import pygame
import time
square = 60
pac = [0,0]
graph = []
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
                    return (0,0)
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
        row = list(map(int,file.readline().split()))
        graph.append(row)
    screen = pygame.display.set_mode((width[0] * square,(height[0] + 1) * square))
    screen.fill(dark)
    pygame.display.flip()

def Human():
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
                    if event.key == ord ( "e" ):
                        run[0] = 0
                if x_ != pac[0] or y_ != pac[1]:
                    return x_,y_
    
        
def canMove(x,y):
    if pac[0] == x and pac[1] == y:
        return False
    if x >= width[0] or x < 0:
        return False
    if y >= height[0] or y < 0:
        return False
    if graph[y][x] == 1:
        return False
    return True

def renderBoard():
    screen.fill((0,0,0))
    ghost = pygame.image.load('ghost.png')
    wall = pygame.image.load('wall.png')
    food = pygame.image.load('food.png')
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 1:
                screen.blit(wall, (j* square,i * square))
            if graph[i][j] == 2:
                screen.blit(food, (j* square,i * square))
            if graph[i][j] == 3:
                screen.blit(ghost, (j* square,i * square))
    screen.blit(pacman[0], (pac[0] * square,pac[1] * square))
    pygame.draw.line(screen,orange,(0, height[0]  * square),(width[0] * square, height[0] * square),width=2)
    font1 = pygame.font.SysFont("arial", 36)
    text1 = font1.render("SCORE: " + str(score[0]), True, green, blue)
    textRect1 = text1.get_rect()
    textRect1.center = (0, height[0] * square + 3)
    screen.blit(text1, textRect1.center)
    pygame.display.update()

def play():
    while run[0] == 1:
        x = pac[0]
        y = pac[1]
        flag = False
        while flag == False:
            x,y = Human()
            flag = canMove(x,y)
        pac[0],pac[1] = x,y
        score[0] -=1
        if graph[pac[1]][pac[0]] == 2:
            score[0] += 20
            graph[pac[1]][pac[0]] = 0
        if graph[pac[1]][pac[0]] == 3:
            renderBoard()
            font = pygame.font.SysFont("arial", 36)
            text = font.render('GAME OVER', True, green, blue)
            textRect = text.get_rect()
            textRect.center = (0, height[0] * square + 3)
            screen.blit(text, textRect.center)
            pygame.display.update()
            time.sleep(2)
            exit(0)
        renderBoard()

if __name__ == '__main__':
    input_level()
    input_matrix()
    renderBoard()
    play()

