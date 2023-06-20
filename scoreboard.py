from turtle import Turtle
FONT_TEXT = ("Serif", 30, "bold")
FONT_GAME_OVER = ("Serif", 50, "bold")


class Scoreboard:
    def __init__(self):
        self.lives = 3
        self.score = 0

        self.lives_t = Turtle(visible=False)
        self.lives_t.color("white")
        self.lives_t.penup()
        self.lives_t.goto(-370, 200)

        self.score_t = Turtle.clone(self.lives_t)
        self.score_t.goto(370, 200)

        self.update_score()
        self.update_lives()

    def update_lives(self):
        self.lives_t.clear()
        self.lives_t.write(f"Lives: {self.lives}", align="left", font=FONT_TEXT)

    def update_score(self):
        self.score_t.clear()
        self.score_t.write(f"Score: {self.score}", align="right", font=FONT_TEXT)

    def increase_score(self, block_score: int):
        self.score += block_score
        self.update_score()

    def lose_life(self):
        self.lives -= 1
        self.update_lives()

    def game_over(self, win: bool):
        self.lives_t.goto(0, 0)
        if win:
            self.lives_t.write("YOU WIN!", align="center", font=FONT_GAME_OVER)
        else:
            self.lives_t.write("GAME OVER", align="center", font=FONT_GAME_OVER)
