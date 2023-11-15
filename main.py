
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
map = turtle.Turtle
screen.addshape(image)
turtle.shape(image)
score = 0
states = pandas.read_csv("50_states.csv")
answers = []
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 Guess The State", prompt="What's another state's name?").capitalize()
    print(answer_state)

    if answer_state in states.state.values:
        score += 1
        answers.append(answer_state)

        # Tentativa para escrever a resposta no mapa. Não conseguida !!
        # print(answers)
        # x = states[states.state.values == states.x.values]
        # print(x)
        # # y = states.y.values
        # # map.goto(x, y)
        # #screen.write(states.state.values, align = "left")
    else:
        game_is_on = False
