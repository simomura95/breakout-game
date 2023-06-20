# https://en.wikipedia.org/wiki/Breakout_(video_game)
from turtle import Screen
import time
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
from blocks import Blocks

TIME_REFRESH = 0.01
SPEED_UP = [0.01, 0.0075, 0.005, 0.0025]
WIDTH = 800
HEIGHT = 500
START_PAD_POS = (0, -HEIGHT / 2 + 30)
START_BALL_POS = (START_PAD_POS[0], START_PAD_POS[1] + 10)

# create screen
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Breakout Game")

# create elements
paddle = Paddle(START_PAD_POS)
ball = Ball(START_BALL_POS)
blocks = Blocks()
score = Scoreboard()

screen.listen()
screen.onkeypress(paddle.go_right, "d")
screen.onkeypress(paddle.go_left, "a")

# game
screen.tracer(100)
game_is_on = True
hit_count = 0
while game_is_on:
    screen.update()
    ball.move()

    # bounce on right and left walls
    if ball.xcor() > 385 or ball.xcor() < -385:
        ball.bounce_rl()

    # bounce on ceiling (halve paddle size 1st time this happens)
    if ball.ycor() > 245:
        ball.bounce_ud()
        paddle.shrink()

    # bounce on paddle (speed up ball after 4 and 12 hits)
    elif abs(ball.ycor() - START_PAD_POS[1]) < 10 and abs(ball.xcor() - paddle.xcor()) < paddle.shapesize()[1]*10 and ball.heading() in (225.0, 315.0):
        # print(paddle.pos())  # DEBUG
        # print(ball.pos())  # DEBUG
        ball.bounce_ud()
        hit_count += 1
        if hit_count == 4:
            TIME_REFRESH = max(TIME_REFRESH, SPEED_UP[1])
        elif hit_count == 12:
            TIME_REFRESH = max(TIME_REFRESH, SPEED_UP[2])

    # bounce on blocks and remove them.
    # When an orange or red block is hit, the ball accelerates to maximum speed
    elif ball.ycor() > 60:
        for block in blocks.all_blocks:
            if abs(ball.xcor() - block.xcor()) < 26 and abs(ball.ycor()-block.ycor()) < 11:
                # print(block.pos(), ball.pos())  # DEBUG
                # double if instead of if-else possible to handle diagonal bounce
                if abs(ball.ycor() - block.ycor()) > 5:  # and abs(ball.xcor() - block.xcor()) < 27
                    ball.bounce_ud()
                    # print('ud')  # DEBUG
                else:  # elif abs(ball.xcor()-block.xcor()) > 20  # and abs(ball.ycor()-block.ycor()) < 12:
                    ball.bounce_rl()
                    # print('rl')  # DEBUG
                block_score = blocks.remove_block(block)
                score.increase_score(block_score)
                if block_score > 4:
                    TIME_REFRESH = SPEED_UP[3]
                if blocks.still_other_blocks():
                    game_is_on = False
                    score.game_over(win=True)
                break  # to handle case of 2 collision at same time -> only first block is considered

    # ball lost: reset and lose a life
    elif ball.ycor() < -HEIGHT/2:
        paddle.goto(START_PAD_POS)
        ball.reset()
        ball = Ball(START_BALL_POS)
        score.lose_life()
        # TIME_REFRESH = SPEED_UP[0]  # reset speed to minimum when losing a life?
        if score.lives == 0:
            game_is_on = False
            score.game_over(win=False)
    time.sleep(TIME_REFRESH)

screen.exitonclick()
