#coding conway's game of life



from random import randint

import pygame


pygame.init()

N = 100
WIDTH, HEIGHT = 700,700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BLACK = (0,0,0)
WHITE=(255, 255, 255)
BLUE = (0,14,71)


FPS = 60


pygame.display.set_caption("Conway's Game of Life")


world = {}

for i in range(N):
    world[i]=[]
    for j in range(N):
        world[i].append(randint(0,1))


def show():
    global world
    for i in range(N):
        for j in range(N):
            if(world[i][j]==1):
                pygame.draw.rect(WIN, BLUE, (7*i, 7*j, 6, 6))
            else:
                pygame.draw.rect(WIN, WHITE, (7*i,7*j, 6, 6))


#count neighbors
def Neighbors(x,y):

    dx=[1,1,1,0,0,-1,-1,-1]
    dy=[1,-1,0,1,-1,1,-1,0]

    ret = 0

    for i in range(8):
        X=(x+dx[i]+N)%N
        Y=(y+dy[i]+N)%N
        if X<0 or Y<0 or X>=N or Y>=N:
            continue
        global world
        ret+=world[X][Y]
    
    return ret


'''
From wikipedia:
Any live cell with two or three live neighbours survives.
Any dead cell with three live neighbours becomes a live cell. 
All other live cells die in the next generation. 
Similarly, all other dead cells stay dead.
'''

#process a day
def process():

    global N, world

    G = {}

    for i in range(N):
        G[i]=[]
        for j in range(N):
          G[i].append(Neighbors(i,j))


    for i in range(N):
        for j in range(N):
            if(world[i][j]==1):
                if(G[i][j]<=1 or G[i][j]>3):world[i][j]=0
            elif(world[i][j]==0):
                if(G[i][j]==3):world[i][j]=1



run = True

while run:

    execute = False
    #time delay
    pygame.time.delay(10)

    for event in pygame.event.get():
        if (event.type==pygame.QUIT): run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        execute = True
    
    if(execute == False):
        WIN.fill((0,0,0))
        show()
        pygame.display.update()
    else:
        process()
        WIN.fill((0,0,0))
        show()
        pygame.time.delay(60)
        pygame.display.update()
    


pygame.quit()





