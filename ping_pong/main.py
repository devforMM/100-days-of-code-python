from turtle import Screen, Turtle
from padle import Padle
from ball import Ball
from score_board import Scoreboard


# Configurer l'écran
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.bgcolor("black")
screen.tracer(0)  # Désactiver la mise à jour automatique

# Créer les paddles
paddle = Padle(-350, 0)
score1=Scoreboard(50,270)
paddle_2 = Padle(350, 0)
score2=Scoreboard(-50,270)
# Mettre à jour l'écran pour afficher les paddles
screen.update()

# Définir les fonctions de mouvement pour les paddles
def p1_forward():
    paddle.sety(paddle.ycor() + 30)

def p1_backward():
    paddle.sety(paddle.ycor() - 15)

def p2_forward():
    paddle_2.sety(paddle_2.ycor() + 15)

def p2_backward():
    paddle_2.sety(paddle_2.ycor() - 15)

# Configurer les écouteurs de clavier
screen.listen()
screen.onkey(p1_forward, "z")
screen.onkey(p1_backward, "s")
screen.onkey(p2_forward, "p")
screen.onkey(p2_backward, "m")

# Dessiner les carrés
x = -290
while x <= 290:  # Utiliser <= pour s'assurer que la boucle inclut 290
    carre = Turtle()
    carre.shape("square")
    carre.shapesize(0.5, 0.5)
    carre.penup()
    carre.color("white")
    carre.goto(0, x)
    x += 20

ballon=Ball()
screen.update() 
screen.tracer(1)
ballon.random_move()
while True:
    if ballon.distance(paddle)<20 :
        ballon.move_right()
    elif ballon.distance(paddle_2)<20:
        ballon.move_left()
    elif ballon.xcor()<=-350:
            score1.increase()
            ballon.home()
            ballon.random_move()
    elif ballon.xcor()>=350:
            score2.increase()
            ballon.home()
            ballon.random_move()
    if score1.score>=10 or score2.score>=10:
        break
     
         
         
      
       


     
screen.exitonclick()
