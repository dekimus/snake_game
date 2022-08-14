from hashlib import new
from turtle import Turtle, Screen
import random, time
from winsound import SND_ALIAS
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


WIDTH = 600
HEIGHT = 600
screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

food = Food()
snake = Snake()
sc = ScoreBoard()
on = True
screen.listen()
screen.onkeypress(key="a", fun=snake.move_left)
screen.onkeypress(key="d", fun=snake.move_right)
screen.onkeypress(key="s", fun=snake.move_down)
screen.onkeypress(key="w", fun=snake.move_up)
screen.update()


while on:
    time.sleep(0.07)
    screen.update()
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extends()
        sc.update_score()
        

    if snake.posX() > 290 or snake.posX() < -298 or snake.posY() > 298 or snake.posY() < -290 :
        sc.reset()
        snake.reset()

    for seg in snake.segments[2:-1]:
        if snake.head.distance(seg) < 10:
            sc.reset()
            snake.reset()
   
    
    


screen.exitonclick()