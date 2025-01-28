import turtle

# Disciplina: introdução a programação
# Componentes: Maria Clara Fonsêca e Kauanny Lorena Gomes
# Bandeira do Senegal 


screen = turtle.Screen()
screen.title("Bandeira do Senegal")
screen.bgcolor("white")


t = turtle.Turtle()
t.speed(0)
t.hideturtle()


def retangulo(color, x, y, width, height):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()


def estrela(color, x, y, size):
    t.penup()
    t.goto(x, y)
    t.setheading(0)  
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()


flag_width = 300
flag_height = 180
stripe_width = flag_width / 3
star_size = 50
pentagon_size = 60  


x_start = -flag_width // 2
y_start = flag_height // 2


retangulo("green", x_start, y_start, stripe_width, flag_height)
retangulo("yellow", x_start + stripe_width, y_start, stripe_width, flag_height)
retangulo("red", x_start + 2 * stripe_width, y_start, stripe_width, flag_height)


star_x = x_start + 250 / 2
star_y = y_start - 83  
estrela("green", star_x, star_y, star_size)



turtle.done()