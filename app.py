import turtle

# draw a square by repeating the two statments
# inside the for loop
def draw_square(width):
    for i in range(4):
        shap.fd(width)
        shap.rt(90)

# create a turtle object
shap = turtle.Turtle()


draw_square(100)


# keep the turtle window open
turtle.done()