import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
score = 0
states = pandas.read_csv("50_states.csv")
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 Guess The State", prompt="What's another state's name?").capitalize()
    print(answer_state)

    if answer_state in states.state.values:
        score += 1
        #screen.write(states.state.values, align = "state.x.values")
    else:
        game_is_on = False
