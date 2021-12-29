from turtle import Turtle, Screen
from guessing_engine import StateGuess
from scoreboard import ScoreBoard

turtle = Turtle()
turtle.hideturtle()
turtle.penup()
screen = Screen()
screen.title('U.S. Map Game')
screen.bgpic('blank_states_img.gif')
guess_engine = StateGuess()
scoreboard = ScoreBoard()

already_correct = []

game_is_on = True
while game_is_on:
    state_guess = screen.textinput('US State Game', 'Type in a state name.').title()
    if state_guess not in guess_engine.states:
        continue

    elif state_guess in already_correct:
        continue

    elif state_guess in guess_engine.states:
        label_coord = guess_engine.user_guess(state_guess)
        turtle.goto(label_coord)
        turtle.write(state_guess, font=('Arial', 14, 'bold'))
        scoreboard.score_tracker()
        already_correct.append(state_guess)
        if scoreboard.score == 50:
            game_is_on = False

screen.exitonclick()
