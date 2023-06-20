from turtle import Turtle

COLORS = ['red', 'red', 'orange', 'orange', 'green', 'green', 'yellow', 'yellow']
COLOR_SCORE = {'red': 7, 'orange': 5, 'green': 3, 'yellow': 1}
ROWS_Y = range(190, 80, -15)


class Blocks:
    def __init__(self):
        self.all_blocks = []
        self.create_blocks()

    def create_blocks(self):
        for row in range(8):
            first_block = Turtle(shape='square')
            first_block.goto(-350, ROWS_Y[row])
            first_block.color(COLORS[row])
            first_block.penup()
            first_block.shapesize(stretch_wid=0.5, stretch_len=2)
            self.all_blocks.append(first_block)
            for n in range(1, 15):
                block = Turtle.clone(first_block)
                block.forward(50 * n)
                self.all_blocks.append(block)

    def remove_block(self, block):
        block_score = COLOR_SCORE[block.color()[0]]
        self.all_blocks.remove(block)
        block.reset()
        return block_score

    def still_other_blocks(self):
        return self.all_blocks == []
