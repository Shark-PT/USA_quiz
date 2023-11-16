import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
answers = []


while len(answers) < 50:
    answer_state = (screen.textinput(title=f"{score}/50 Guess The State", prompt="What's another state's name?")
                    .capitalize())

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        score += 1
        answers.append(answer_state)

        # Tentativa para escrever a resposta no mapa. Não conseguida !!
        # print(answers)
        # x = states[states.state.values == states.x.values]
        # print(x)
        # # y = states.y.values
        # # map.goto(x, y)
        # map.write(arg="Home = ", move=True, align="center")
        # Map.write_name()
