from snake_body import *
from food import *
from score_board import *

snake = Snake()
food = Food()
scoreboard = Scoreboard()

def game_func(): 
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down,"Down")
    screen.onkey(snake.right,"Right")
    screen.onkey(snake.left,"Left")

game_func()
game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move() 

    # Detecting collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.update()

    # Detect Collision with wall
    if snake.head.xcor() > 390 or snake.head.xcor() <-390 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        #  game_is_on = False
         scoreboard.game_over()
         should_continue = screen.textinput(title="Restart Game",prompt ="write yes to restart otherwise no : ").lower()
         if should_continue == 'yes':
            screen.reset()
            snake.__init__()
            food.__init__()
            scoreboard.__init__()
            game_func()
         else :
            game_is_on = False

    # Detect Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10 :
            scoreboard.game_over()
            should_continue = screen.textinput(title="Restart Game",prompt ="write yes to restart otherwise no : ").lower()
            if should_continue == 'yes':
                screen.reset()
                snake.__init__()
                food.__init__()
                scoreboard.__init__()
                game_func()
            else :
                game_is_on = False
   
t.exitonclick()