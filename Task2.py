import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        koch_curve(t, order-1, size/3)
        t.left(60)
        koch_curve(t, order-1, size/3)
        t.right(120)
        koch_curve(t, order-1, size/3)
        t.left(60)
        koch_curve(t, order-1, size/3)

def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

# Вікно та об'єкт turtle
window = turtle.Screen()
t = turtle.Turtle()
t.speed(0)

# Рекурсія та розмір сніжинки
order = int(input("Введіть рівень рекурсії: "))
size = 300  # Задана довжина сторони трикутника

koch_snowflake(t, order, size)

window.mainloop()


