from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]


    def create_snake(self):
        for _ in range(3):
            self.snake_body.append(Turtle(shape="square"))
        xpos = 0
        for i in range(3):
            self.snake_body[i].penup()
            self.snake_body[i].color("white")
            self.snake_body[i].goto(x =  xpos, y = 0)
            xpos -= 20

    def add_snake(self):
        self.snake_body.append(Turtle(shape="square"))
        self.snake_body[-1].penup()
        self.snake_body[-1].color("white")
        self.snake_body[-1].goto(self.snake_body[-2].position())


    def move(self):
        for segment_num in range(len(self.snake_body)-1,0,-1):
            x_new = self.snake_body[segment_num-1].xcor()
            y_new = self.snake_body[segment_num-1].ycor()
            self.snake_body[segment_num].goto(x_new,y_new)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # self.move()

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        # self.move()

        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        # self.move()


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        # self.move()    