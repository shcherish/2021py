import turtle
import random
import math
import winsound

#-----------------------------스크린 객체 생성------------------------------
screen=turtle.Screen()

#-----------------------------스크린 배경 지정------------------------------
screen.bgcolor("lightgrey")

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgpic("store.gif")

#----------------------------------사 람---------------------------------------
image1="people.gif"
screen.addshape(image1)
player=turtle.Turtle()
player.shape(image1)
player.penup()
player.speed(0)
screen = player.getscreen()

asteroids=[]
#----------------------------------흰색 보석------------------------------------
screen=turtle.Screen()
image2="jewelry.gif"
screen.addshape(image2)

for i in range(2):
    a1=turtle.Turtle() #a1은 변수이름
    a1.shape(image2)
    a1.penup()
    a1.speed(0)

    a1.left(random.randint(0,360))

    a1.goto(random.randint(-300,300),random.randint(-300,300))
    asteroids.append(a1)

#----------------------------------빨간색 보석-------------------------------------
screen=turtle.Screen()
image3="red.gif"
screen.addshape(image3)
a2=turtle.Turtle()
a2.shape(image3)
a2.penup()
a2.speed(0)
a2.left(random.randint(0,360))

a2.goto(random.randint(-300,300),random.randint(-300,300))
asteroids.append(a2)

#----------------------------------주황색 보석-------------------------------------
screen=turtle.Screen()
image4="orange.gif"
screen.addshape(image4)
a3=turtle.Turtle()
a3.shape(image4)
a3.penup()
a3.speed(0)
a3.left(random.randint(0,360))

a3.goto(random.randint(-300,300),random.randint(-300,300))
asteroids.append(a3)

#----------------------------------노란색 보석--------------------------------------
screen=turtle.Screen()
image5="yellow.gif"
screen.addshape(image5)
a4=turtle.Turtle()
a4.shape(image5)
a4.penup()
a4.speed(0)
a4.left(random.randint(0,360))

a4.goto(random.randint(-300,300),random.randint(-300,300))
asteroids.append(a4)


#-------------------------------------초록색 보석--------------------------------------
screen=turtle.Screen()
image6="green.gif"
screen.addshape(image6)
a5=turtle.Turtle()
a5.shape(image6)
a5.penup()
a5.left(random.randint(0,360))

a5.goto(random.randint(-300,300),random.randint(-300,300))
asteroids.append(a5)

#----------------------------------파란색 보석-------------------------------------
screen=turtle.Screen()
image6="blue.gif"
screen.addshape(image6)
a6=turtle.Turtle()
a6.shape(image6)
a6.penup()
a6.left(random.randint(0,360))

a6.goto(random.randint(-300,300),random.randint(-300,300))
asteroids.append(a6)

#----------------------------------보라색 보석-------------------------------------
screen=turtle.Screen()
image6="purple.gif"
screen.addshape(image6)
a7=turtle.Turtle()
a7.shape(image6)
a7.penup()
a7.left(random.randint(0,360))

a7.goto(random.randint(-300,300),random.randint(-300,300))
asteroids.append(a7)

#----------------------바위--------------------------------
screen=turtle.Screen()
image3="stone1.gif"
screen.addshape(image3)
a8=turtle.Turtle()
a8.shape(image3)
a8.penup()
a8.goto(-200,152)
a8.pendown()

screen=turtle.Screen()
image4="stone2.gif"
screen.addshape(image4)
a9=turtle.Turtle()
a9.shape(image4)
a9.penup()
a9.goto(200,52)
a9.pendown()

screen=turtle.Screen()
image5="stone3.gif"
screen.addshape(image5)
a10=turtle.Turtle()
a10.shape(image5)
a10.penup()
a10.goto(0,-152)
a10.pendown()

#---------------------------------방향키---------------------------------
def turnleft():
    player. lt(30)
def turnright():
    player.rt(30)
def speedup():
    player.fd(10)

screen.onkeypress(turnleft,"Left")
screen.onkeypress(turnright,"Right")
screen.onkeypress(speedup,"space")
screen.listen()

#--------------------------경계선그리기--------------------------------------
def draw_boundary():
    t=turtle.Turtle()
    #t.color("black")
    t.shape(image1)
    t.penup()
    t.goto(-300,-300)
    t.pendown()
    t.left(90)
    for i in range(4):
        t.fd(600)
        t.right(90)
#----------------------------------------충돌---------------------------------------
def collision_boundary(a): #경계선_충돌
    if a.xcor() <= -300+10 or a.xcor() >= 300-10 :
        a.left(180)
    if a.ycor() <= -300+10 or a.ycor() >=300-10:
        a.left(180)

def collided(a): #충돌한
    dist=math.sqrt((player.xcor()-a.xcor())**2 + (player.ycor()-a.ycor())**2)
    if dist<20:
        return True
    else:
        return False

def process_collision(a): #과정_경계선
    player.fd(40)
    winsound.Beep(300, 2000)
#-----------------------------------상품뽑기--------------------------------------
game_list=[]

game_list.append("꽝")
game_list.append("금")
game_list.append("사탕")
game_list.append("보석")
game_list.append("풍선")

print("상품 : ", game_list)

game = random.choice(game_list)

print("게임에서 이긴 사람이 가져갈 상품은? ")
print(game)

#---------------------------------------결과내기----------------------------------------
score=0
def play():
    global score #전역변수=global
    player.forward(5)

    for a in asteroids:
        a.forward(3)

    collision_boundary(player)

    for a in asteroids:
        collision_boundary(a)
        if collided(a):
            process_collision(a)
            score = score+1

    if score ==7:
        player.write("축하합니다.\n보석과의 게임에서 이겼습니다.\n", font=(50))
        player.write("상품을 받아가세요~", font=(50))
        return
    else :
        screen.ontimer(play,10)
    
draw_boundary()

screen.ontimer(play,10)
