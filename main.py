import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")

answer_state = screen.textinput(title="Guess The State", prompt="What's another state's name?").capitalize()
print(answer_state)

if answer_state in states.state.values:
    screen.write(align = "state.x.values")
