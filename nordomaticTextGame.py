from pyexpat import version_info
import turtle



print("Velkommen til Nordomatic sitt kule tekstspill!!!")


playerName = str(input("Hva heter du? :"))
startSpill = str(input(f"Hei {playerName} er du klar for å spille? :"))

if startSpill == "ja":
    baneValg = str(input("Hvilken bane vil spille på? ørken eller jungel?"))
else:
    print("Det var synd, du suger!")
    quit()
if baneValg == "ørken":
    desert = str(input("Trist valg, han som skal hjelpe deg er død, vil du gå eller kjøre? :"))
if desert == "gå":
    print("Ikke et bra valg, etter en stund blir du bitt av en slange og dør...")
    quit()
driver = str(input("Etter 2 timer med kjøring kommer du til et kryss, kjører du venstre eller høyre? :"))

if driver == "venstre":
    # For å tegne vindu
    vindu = turtle.Screen()
    vindu.title('Ping Pong av Kim')
    vindu.bgcolor('black') # bakgrunnsfarge
    vindu.setup(width=800, height=600) # størrelse på vindu
    vindu.tracer(0)

    # Score
    score_a = 0
    score_b = 0

    # Kontroller A
    kontroller_a = turtle.Turtle()
    kontroller_a.speed(0)
    kontroller_a.shape('square')
    kontroller_a.color('white')
    kontroller_a.shapesize(stretch_wid=5, stretch_len=1)
    kontroller_a.penup()
    kontroller_a.goto(-350, 0)

    # Kontroller B
    kontroller_b = turtle.Turtle()
    kontroller_b.speed(0)
    kontroller_b.shape('square')
    kontroller_b.color('white')
    kontroller_b.shapesize(stretch_wid=5, stretch_len=1)
    kontroller_b.penup()
    kontroller_b.goto(350, 0) # første tall er side av skjerm, andre er center

    # Ball
    ball = turtle.Turtle()
    ball.speed()
    ball.shape('square')
    ball.color('white')
    ball.penup()
    ball.goto(0,0)
    ball.dx = 0.25
    ball.dy = 0.25

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

    def kontroller_a_up():
        y = kontroller_a.ycor()
        y += 20
        kontroller_a.sety(y)

    def kontroller_a_down():
        y = kontroller_a.ycor()
        y -= 20
        kontroller_a.sety(y)

    def kontroller_b_up():
        y = kontroller_b.ycor()
        y += 20
        kontroller_b.sety(y)

    def kontroller_b_down():
        y = kontroller_b.ycor()
        y -= 20
        kontroller_b.sety(y)



    # Keyboard binding
    vindu.listen()
    vindu.onkeypress(kontroller_a_up, "w")
    vindu.onkeypress(kontroller_a_down, "s")
    vindu.onkeypress(kontroller_b_up, "Up")
    vindu.onkeypress(kontroller_b_down, "Down")

    # Main game loop
    while True:
            vindu.update()


            # Move the ball
            ball.setx(ball.xcor()+ ball.dx)
            ball.sety(ball.ycor()+ ball.dy)

            # Border checking

            # Top and bottom
            if ball.ycor() > 290:
                ball.sety(290)
                ball.dy *= -1


            elif ball.ycor() < -290:
                ball.sety(-290)
                ball.dy *= -1


            #kontroller_a.


            # Left and right
            if ball.xcor() > 350:
                score_a += 1
                pen.clear()
                pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                ball.goto(0, 0)
                ball.dx *= -1
                if score_a == 20:
                    break

            elif ball.xcor() < -350:
                score_b += 1
                pen.clear()
                pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                ball.goto(0, 0)
                ball.dx *= -1
                if score_b == 20:
                    break

            # Paddle and ball collisions
            if ball.xcor() < -340 and ball.ycor() < kontroller_a.ycor() + 50 and ball.ycor() > kontroller_a.ycor() - 50:
                ball.dx *= -1 


            elif ball.xcor() > 340 and ball.ycor() < kontroller_b.ycor() + 50 and ball.ycor() > kontroller_b.ycor() - 50:
                ball.dx *= -1

else:
    print("Du valgte høyre og gikk glipp av et bonusspill :( ")