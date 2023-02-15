from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width = 600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkeypress(key="Up",fun=snake.up)
screen.onkeypress(key="Down",fun=snake.down)
screen.onkeypress(key="Right",fun=snake.right)
screen.onkeypress(key="Left",fun=snake.left)
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect colision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_increase()
        snake.add_snake()
    
    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < - 290 or snake.head.ycor() > 290 or snake.head.ycor() < - 290:
        is_game_on = False
        score.game_over()


    for segment in snake.snake_body:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) <10 :
            is_game_on = False
            score.game_over()
screen.exitonclick()
