#importing turtle module
import turtle

#setting up the game's window
Window = turtle.Screen() #initialize screen
Window.title("Ping Pong Game") #setting window title
Window.bgcolor("black") #background color
Window.setup(width = 1000, height = 800) #window coordinates 
Window.tracer(0) #stops automatic updates for the window

#game rackets

#racket1
racket1 = turtle.Turtle()   #generating an obj using the turtle module
racket1.speed(0)            #setting the speed of the obj
racket1.shape("circle")     #setting the shape of the obj
racket1.color("yellow")     #setting the color of the obj
racket1.shapesize(stretch_wid = 5, stretch_len = 2)     #reshaping the obj
racket1.penup()             #removing the trace drawing the obj leaves behined
racket1.goto(-460, 0)       #setting the posetion of the obj


#racket2
racket2 = turtle.Turtle()
racket2.speed(0)
racket2.shape("circle")
racket2.color("blue")
racket2.shapesize(stretch_wid = 5, stretch_len = 2)
racket2.penup()
racket2.goto(460, 0)


#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)         #the stating postion of the ball is in the mid of the screen
ball.dx = 0.6           #Coefficient of variation for the x axis
ball.dy = 0.6           #Coefficient of variation for the y axis


#setting the score
player_1_score = 0
player_2_score = 0
score = turtle.Turtle()
score.speed(0)
score.penup()
score.color("white")
score.hideturtle()
score.goto(0, 360)
score.write("player 1: 0 || player 2: 0", align = "center", font = ("courier", 24, "normal"))


#racket movement
def racket1_up():   #racket 1 moving up
    y = racket1.ycor()      #get the y coordinate of the racket
    y += 30                 #the y coordinate increases by 30 pixels
    racket1.sety(y)         #set the y of the racket to the new y (the increased y)
       
def racket1_down(): #racket 1 moving down
    y = racket1.ycor()      #get the y coordinate of the racket
    y -= 30                 #the y coordinate decreases by 20 pixels
    racket1.sety(y)         #set the y of the racket to the new y (the decreased y)
    
def racket2_up():   #racket 2 moving up
    y = racket2.ycor()
    y += 30
    racket2.sety(y)
       
def racket2_down(): #racket 2 moving down
    y = racket2.ycor()
    y -= 30
    racket2.sety(y)
    

#Keyboard bindings (keys that move the rackets)
Window.listen()         #notify the window to expect an input

Window.onkeypress(racket1_up, "w")          #when pressing w the function racket1_up is invoked (called)
Window.onkeypress(racket1_down, "s")

Window.onkeypress(racket2_up, "Up")
Window.onkeypress(racket2_down, "Down")


#main game loop
while True:
    Window.update() #updates the screen everytime the loop runs
    
    #ball movement
    ball.setx(ball.xcor() + ball.dx)    #ball starts at 0 then starts moving according to dx
    ball.sety(ball.ycor() + ball.dy)    #ball starts at 0 then starts moving according to dy
    
    #border check  "when the ball touch any border of the screen it pounces back"
    #border coordinates [top = +400px, bottom = -400px,right is at +500px,left at -500px, ball size is 20px]
    if ball.ycor() > 390:       #if ball is at the top
        ball.sety(390)          #set new y to +390
        ball.dy *= -1           #reverse the direction of the ball
        
    if ball.ycor() < -390:      #if ball is at the bottom
        ball.sety(-390)
        ball.dy *= -1
    
    if ball.xcor() > 490:       #if the ball touches the right border
        ball.goto(0, 0)         #set ball back to center
        ball.dx *= -1           #reverse the x direction
        
    if ball.xcor() < -490:      #if the ball touches the right border
        ball.goto(0, 0)
        ball.dx *= -1
        
    
    #------------------------------------------------------------------------
    #ball collision with racket 
    if (ball.xcor() > 440 and ball.xcor() < 470) and (ball.ycor() < racket2.ycor() + 40 and ball.ycor() > racket2.ycor() - 40):
        ball.setx(440)
        ball.dx *= -1
        player_1_score += 1
        score.clear()
        score.write("player 1: {} || player 2: {}".format(player_1_score, player_2_score), align = "center", font = ("courier", 24, "normal"))
        
    if (ball.xcor() < -440 and ball.xcor() > -470) and (ball.ycor() < racket1.ycor() + 40 and ball.ycor() > racket1.ycor() - 40):
        ball.setx(-440)
        ball.dx *= -1
        player_2_score += 1
        score.clear()
        score.write("player 1: {} || player 2: {}".format(player_1_score, player_2_score), align = "center", font = ("courier", 24, "normal"))
    