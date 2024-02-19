import turtle

# Настройка экрана
screen = turtle.Screen()
screen.title("Рисунок Цветка с использованием Turtle")
screen.bgcolor("sky blue")

# Настройка "черепашки"
flower = turtle.Turtle()
flower.speed(10)  # Установка средней скорости рисования

flower.color("red")
flower.pensize(2)

# Функция для рисования окружности с заданным радиусом и цветом
def draw_circle(radius, color):
    flower.color(color)
    flower.begin_fill()
    flower.circle(radius)
    flower.end_fill()

# Функция для рисования лепестков цветка
def draw_flower_petals(radius, color, petals):
    for _ in range(petals):
        draw_circle(radius, color)
        flower.right(360 / petals)

# Перемещение черепашки в начальную позицию
flower.penup()
flower.goto(0, -100)
flower.pendown()

# Рисование цветка
draw_flower_petals(50, "red", 12)

# Рисование стебля
flower.color("green")
flower.right(90)
flower.penup()
flower.forward(100)
flower.pendown()
flower.forward(200)

# Рисование листьев
def draw_leaf(distance, angle):
    flower.penup()
    flower.forward(distance)
    flower.left(angle)
    flower.pendown()
    draw_circle(40, "light green")
    flower.right(angle)
    flower.penup()
    flower.backward(distance)
    flower.pendown()

draw_leaf(50, 45)
draw_leaf(50, -45)

flower.hideturtle()  # Скрыть черепашку после завершения рисунка

turtle.done()
