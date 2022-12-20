import turtle
try:
    score_a=0
    score_b=0
    Win=turtle.Screen()
    Win.setup(800,600)
    Win.bgcolor('aqua')
    Win.title("Pong")
    Win.tracer(0)
    #pen
    pen=turtle.Turtle() #object pen to write details
    pen.speed(0)
    pen.color("red")
    pen.up()
    pen.hideturtle()
    pen.goto(-10,235)
    pen.write("Player A : 0 \t  \t Player B : 0",align="center",font=("ariel",20,"bold"),)

    #pad
    cp="gold"
    # left
    lepad=turtle.Turtle()
    lepad.speed(0)
    lepad.shape("square")
    lepad.color(cp)
    lepad.shapesize(stretch_wid=5,stretch_len=1)
    lepad.penup()
    lepad.goto(-380,0)
    #right
    repad=turtle.Turtle()
    repad.speed(0)
    repad.shape("square")
    repad.color(cp)
    repad.shapesize(stretch_wid=5,stretch_len=1)
    repad.penup()
    repad.goto(380,0)

    #box
    cb="purple"
    #left box
    lbox=turtle.Turtle()
    lbox.speed(0)
    lbox.shape("square")
    lbox.color(cb)
    lbox.shapesize(stretch_wid=29.5,stretch_len=0.4)
    lbox.penup()
    lbox.goto(-395,0)
    #right box
    rbox=turtle.Turtle()
    rbox.speed(0)
    rbox.shape("square")
    rbox.color(cb)
    rbox.shapesize(stretch_wid=29.5,stretch_len=0.4)
    rbox.penup()
    rbox.goto(389,0)
    #top box
    tbox=turtle.Turtle()
    tbox.speed(0)
    tbox.shape("square")
    tbox.color(cb)
    tbox.shapesize(stretch_wid=0.3,stretch_len=39)
    tbox.penup()
    tbox.goto(0,292)
    #bottom box
    bbox=turtle.Turtle()
    bbox.speed(0)
    bbox.shape("square")
    bbox.color(cb)
    bbox.shapesize(stretch_wid=0.3,stretch_len=39)
    bbox.penup()
    bbox.goto(0,-292)

    #ball
    ball=turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("black")
    ball.penup()
    while True:
        a=int(input("Enter speed level: 1.slow,2.medium,3.fast: "))
        win_pts=int(input("Enter winning point: "))
        playerA=input("Enter your name player A: ")
        playerB=input("Enter your name player B: ")
        if a==1:
            ball.dx=0.6;ball.dy=0.7
        elif a==2:
            ball.dx=1.2;ball.dy=1.3
        elif a==3:
            ball.dx=1.8;ball.dy=1.9
        else:
            print("1 or 2 or 3 only")
        spdx=ball.dx;spdy=ball.dy;break
       
    is_paused = False
    is_quit = False
    #Functions
    def lepadup():
        lepad.sety(lepad.ycor()+80)
        if (lepad.ycor()>300):
            lepad.goto(-380,-300)
    def lepaddown():
        lepad.sety(lepad.ycor()-80)
        if (lepad.ycor()<-300):
            lepad.goto(-380,300)
    def repadup():
        repad.sety(repad.ycor()+80)
        if (repad.ycor()>300):
            repad.goto(380,-300)
    def repaddown():
        repad.sety(repad.ycor()-80)
        if (repad.ycor()<-300):
            repad.goto(380,300)
    def score_write():
        global score_a, score_b
        pen.goto(-10,235)
        pen.write(playerA+" : {}".format(score_a)+" \t  \t "+playerB+" : {}".format(score_b),align="center",font=("ariel",20,"bold"))

    def pause():
        global is_paused,score_a, score_b
        if is_paused == False:
            is_paused = True
            pen.goto(0,0)
            pen.write("Paused",align="center",font=("ariel",30,"normal"))
        else:
            is_paused = False
            pen.clear()
            score_write()
    def start():
        global is_paused,score_a, score_b
        if is_paused == False:
            is_paused = True
            pen.goto(0,0)
            pen.write("Press Space To start",align="center",font=("ariel",30,"normal"))
        else:
            is_paused = False
            pen.clear()
            score_write()
    def quit():
        global is_quit
        is_quit = not is_quit
        pen.write("Exited",align="center",font=("ariel",30,"normal"))
        return
    #to get command from keyboard      
    Win.listen()
    Win.onkeypress(lepadup,"w")
    Win.onkeypress(lepaddown,"s")
    Win.onkeypress(repadup,"Up")
    Win.onkeypress(repaddown,"Down")
    Win.onkeypress(pause,"p")
    Win.onkeypress(pause,"space")
    Win.onkeypress(pause,"space")
    Win.onkeypress(quit,"q")

    #to be paused when starting
    start()
    while True:
        if is_quit:
            turtle.bye()
            print("Exited the program midway")
            break
        #pause
        if not is_paused:
            Win.update()
            ball.setx(ball.xcor()+ball.dx)
            ball.sety(ball.ycor()+ball.dy)
        else:
            Win.update()
           
        #collison
        if ball.ycor()>290:
            ball.sety(290)
            ball.dy*=-1
        if ball.ycor()<-290:
            ball.sety(-290)
            ball.dy*=-1
           
        #player A(Left)
        if ball.xcor()>390:
            ball.setx(390)
            ball.dx*=-1
            score_a+=1
            pen.clear()
            pen.goto(-320,200)
            pen.write("+1",align="left",font=("calbri",16,"normal"),)
            score_write()   #function to write score
            ball.dx,ball.dy=-spdx,-spdy#change direction of ball
            #ball.goto(0,0)
           
        #player B(Right)
        if ball.xcor()<-390:
            ball.setx(-390)
            ball.dx*=-1
            score_b+=1
            pen.clear()
            pen.goto(320,200)
            pen.write("+1",align="right",font=("calbri",16,"normal"),)
            score_write()   #function to write score
            ball.dx,ball.dy=spdx,spdy#change direction of ball
            #ball.goto(0,0)
           
        #hits
        if ball.xcor()>370 and ball.ycor()>repad.ycor()-50 and ball.ycor()<repad.ycor()+50:
            ball.setx(360)
            ball.dx*=-1.15 #increase speed x after each hits on pad
            ball.dy*=1.09  #increase speed y after each hits on pad
           
        if ball.xcor()<-370 and ball.ycor()>lepad.ycor()-50 and ball.ycor()<lepad.ycor()+50:
            ball.setx(-360)
            ball.dx*=-1.15 #increase speed x after each hits on pad
            ball.dy*=1.09  #increase speed y after each hits on pad
           
        if ball.dx>4.5 or ball.dx>4:
            ball.dx*=0.7   #decrease speed x after each hits on pad
            ball.dy*=0.75  #decrease speed y after each hits on pad
           
        #win determination
        if score_a==win_pts:
            print(playerA+" wins")
            pen.goto(0,0)
            pen.write(playerA+" wins",align="center",font=("ariel",30,"normal"));break
           
        if score_b==win_pts:
            print(playerB+" wins")
            pen.goto(0,0)
            pen.write(playerB+" wins",align="center",font=("ariel",30,"normal"));break
    turtle.bye()
except:
    print("Exited the program midway")


