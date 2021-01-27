from turtle import *
from freegames import line
from random import randint
import time

turns = {'yellow' : 'red', 'red' : 'yellow'}

state = {'player' : 'yellow' , 'grid' : [[] for _ in range(8)],
         'player2' : 'human' , 'board' : 'start'}

def grid():
    "Draw Connect Four grid."
    clear()

    bgcolor('light blue')
    color('white')

    for x in range(-150,200,50):
        line(x,-200,x,200)

    for x in range(-175,200,50):
        for y in range(-175,200,50):
            up()
            goto(x,y)
            dot(40,'white')


    update()

def start():
    clear()
    color('red')
    up()
    goto(-200,90)
    down()
    time.sleep(2)

    begin_fill()
    forward(400)
    left(90)
    forward(80)
    left(90)
    forward(400)
    left(90)
    forward(80)
    left(90)
    time.sleep(1)
    end_fill()
    up()

    goto(-180,-110)
    down()
    begin_fill()
    forward(360)
    left(90)
    forward(80)
    left(90)
    forward(360)
    left(90)
    forward(80)
    left(90)
    end_fill()
    up()

    goto(0,100)
    
    color('black')
    write("Player vs Player " ,font=('Arial' , 30,'bold') , align="center")
    goto(0,-100)
    
    write("Player vs PC",font=('Arial' , 30,'bold') , align="center")
    update()

def act(x,y):
    if(state['board'] == 'start'):
        if(y<0):
            state['player2'] = 'pc'

        grid()
        state['board'] = 'play'

    else:
        tap(x,y)


def tap(x,y):
    "Draw red or yellow circle in tapped col"

    player = state['player']
    grid = state['grid']

    col = int((x+200)//50)
    count = len(grid[col])
    if count ==8:
        return

    x = ((x+200)//50)*50-200+25
    y = count * 50-200+25

    up()
    goto(x,y)
    dot(40,player)
    update()

    if player =='yellow':
        grid[col].append(1)
    else:
        grid[col].append(2)

    if(checkgame()):
        gameover()
        return
    state['player'] = turns[player]

    if(state['player2'] !='human' and player=='yellow'):
        ontimer(tap(randint(-4,3)*50,0),500)

def checkgame():
    grid = state['grid']

    "vertical check"

    for i in grid:
        if len(i)>3:
            if(any(w==x==y==z for w,x,y,z in zip(i,i[1:],i[2:],i[3:]))):
               return True


    "horizontal check"

    for i in range(len(grid)-3):
        minh = min(len(j) for j in grid[i:i+4])
        for j in range(minh):
            if(grid[i][j] == grid[i+1][j] == grid[i+2][j] == grid[i+3][j]):
                return True
    
    "Diagonal check"

    for i in range(len(grid)-3):
        maxh = max(len(j) for j in grid[i:i+4])

        if maxh>3:
            for j in range(maxh-3):
                if(len(grid[i]) > j and len(grid[i+1]) > j+1 and len(grid[i+2]) > j+2 and len(grid[i+3]) > j+3):
                    if(grid[i][j]==grid[i+1][j+1]==grid[i+2][j+2]==grid[i+3][j+3]):
                       return True

                if(len(grid[i]) > j+3 and len(grid[i+1]) > j+2 and len(grid[i+2]) > j+1 and len(grid[i+3]) >j):
                    if(grid[i][j+3]==grid[i+1][j+2]==grid[i+2][j+1]==grid[i+3][j]):
                       return True

def gameover():
    clear()
    up()
    goto(0,-10)
    color(state['player'])
    if(state['player2'] == 'pc' and state['player'] == 'red'):
        write("{} Wins".format(state['player'].capitalize()),font=('Arial' , 30,'normal') ,align ="center")
    else:
        write("{} Wins".format(state['player'].capitalize()),font=('Arial' , 30,'normal') ,align ="center")

    update()



setup(420,420,370,0)

hideturtle()
tracer(False)
start()

onscreenclick(act)
done()






    
                    














            

















    
        
       





























    






    
    











    
