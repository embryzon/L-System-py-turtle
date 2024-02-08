# Based on Daniel Shiffman's Coding Challenge #16
import turtle
from rules import *
from colorsys import hsv_to_rgb

def main():
    width = 800
    height = 800
    padding = 25
    
    # Set the screen dimensions
    setScreen(width, height, padding)

    # Set Speed of drawing
    turtle.tracer(75)
    
    # Fractal binary tree
    axiom, rule, iterations, length, angle, startX, startY, dec = fractal_binary_tree(width, height)

    # Set initial position and heading of the turtle
    setStartPos(startX, startY)

    # Draw the Lsystem
    sentence = GENERATE_L_SYSTEM(axiom, rule, iterations)
    TURTLE(sentence, length, angle, dec)

    # # TREE
    # axiom, rule, iterations, length, angle, startX, startY = broom_stick(width, height)
    
    # # Set initial position and heading of the turtle
    # setStartPos(startX, startY)
    
    # # Draw the Lsystem
    # sentence = GENERATE_L_SYSTEM(axiom, rule, iterations)
    # TURTLE(sentence, length, angle)

    
    turtle.done()

def apply_rules(sentence, rules): 
    nextGen = ''
    for char in sentence:
        found = False
        for rule in rules:
            if char == rule['a']:
                found = True
                nextGen += rule['b']
                break
        if not found:
            nextGen += char

    return nextGen

def GENERATE_L_SYSTEM(axiom, rules, iterations):
    for _ in range(1, iterations + 1):
        axiom = apply_rules(axiom, rules)
    return axiom

def TURTLE(sentence, length, angle, dec = 0.1):
    stack = []
    hue = 0.0
    for char in sentence:
        # Add more instructions for different chars
        match char:
            case 'F' | 'G': # Draw Forward
                turtle.color(hsv_to_rgb(hue, 0.3, 0.7))
                hue += 0.01
                if hue > 1.0:
                    hue = 0

                turtle.forward(length)
                length -= dec
                if length < 1:
                    break

            case 'H': # move forward
                turtle.penup()
                turtle.forward(length)
                turtle.pendown()

            case '+': # turn left
                turtle.left(angle)

            case '-': # turn right
                turtle.right(angle)

            case '[': # save state
                stack.append((turtle.pos(), turtle.heading()))

            case ']': # load state
                position, heading = stack.pop()
                turtle.penup()
                turtle.goto(position)
                turtle.setheading(heading)
                turtle.pendown()

            case _:
                print(f'{char} not found in the rules')
        
def fractal_binary_tree(width, height):
    axiom = 'G'
    rule = FRACTAL_BINARY_TREE
    iterations = 8
    length = 3
    angle = 45
    x = 0
    y = -height/2
    dec = 0.001
    return (axiom, rule, iterations, length, angle, x, y, dec)

def broom_stick(width, height):
    axiom = 'F'
    rule = TREE
    iterations = 7
    length = 69
    angle = 9
    x = width/2
    y = -height/2

    return (axiom, rule, iterations, length, angle, x, y)

def setScreen(width, height, padding, bgcolor='black'):
    turtle.Screen().setup(width=0.8, height=0.8)
    turtle.Screen().bgcolor(bgcolor)
    turtle.Screen().screensize(width+padding, height+padding)
    turtle.hideturtle()

def setStartPos(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.left(90)

if __name__ == '__main__':
    main()