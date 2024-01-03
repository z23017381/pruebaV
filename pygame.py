import turtle
import time
import random

posponer = 0.1

score = 0

high_score = 0 

ventana = turtle.Screen()
ventana.title("juego de serpiente")
ventana.bgcolor("black")
ventana.setup(width = 600, height = 600)
ventana.tracer(0)

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"


comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(100,100)


segmentos = []

texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("score: 0      high score:0", align = "center", font = ("courier", 24, "normal"))


def arriba():
	cabeza.direction = "up"
def abajo():
	cabeza.direction = "down"
def derecha():
	cabeza.direction = "right"
def izquierda():
	cabeza.direction = "left"



def mov():
	if cabeza.direction == "up":
		y = cabeza.ycor()
		cabeza.sety(y + 20)

	if cabeza.direction == "down":
		y = cabeza.ycor()
		cabeza.sety(y - 20)

	if cabeza.direction == "left":
		x = cabeza.xcor()
		cabeza.setx(x - 20)

	if cabeza.direction == "right":
		x = cabeza.xcor()
		cabeza.setx(x + 20)


ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

while True:
	ventana.update()

	if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
	 time.sleep(3)
	 cabeza.goto(0,0)
	 cabeza.direction = "stop"


	 for segmento in segmentos:
	 	segmento.goto(1000,1000)

	 segmentos.clear()

	 score = 0
	 texto.clear()
	 texto.write("score: {}   high score: {}".format(score, high_score),
			align = "center", font =("courier", 24, "normal"))







      
	if cabeza.distance(comida) < 20:
		x = random.randint(-280,280)
		y = random.randint(-280,280)
		comida.goto(x,y)

		nuevo_segmento = turtle.Turtle()
		nuevo_segmento.speed(0)
		nuevo_segmento.shape("circle")
		nuevo_segmento.color("green")
		nuevo_segmento.penup()
		segmentos.append(nuevo_segmento)


		score += 10

		if score > high_score:
			high_score = score

		texto.clear()

		texto.write("score: {}   high score: {}".format(score, high_score),
			align = "center", font =("courier", 24, "normal"))


	#mover cuerpo
	totalSeg = len(segmentos)
	for index in range(totalSeg -1, 0, -1):
		x = segmentos[index - 1].xcor()
		y = segmentos[index - 1].ycor()
		segmentos[index].goto(x,y)


	if totalSeg > 0:
		x = cabeza.xcor()
		y = cabeza.ycor()
		segmentos[0].goto(x, y)
	 

	mov()

	for segmento in segmentos:
		if segmento.distance(cabeza) < 20:
			time.sleep(3)
			cabeza.goto(0,0)
			cabeza.direction = "stop"


			for segmento in segmentos:
				segmento.goto(1000,1000)

			segmentos.clear()

			score = 0
			texto.clear()
			texto.write("score: {}   high score: {}".format(score, high_score),align = "center", font =("courier", 24, "normal"))


	time.sleep(posponer)

