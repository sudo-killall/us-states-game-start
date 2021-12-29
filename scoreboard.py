from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.penup()
        self.hideturtle()
        self.goto(100, 300)

    def score_tracker(self):
        self.clear()
        self.score += 1
        score_board = f'Score is {self.score}/ 50'
        self.write(score_board, font=('Arial', 30, 'bold'))

    # def highscore(self):
    #     if self.highscore > self.score:
    #         self.highscore = self.score
    #

# have tracker on screen as all time  starting at zero
# create a score board to track all scores
