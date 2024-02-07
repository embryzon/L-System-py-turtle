# Based on Daniel Shiffman's Coding Challenge #16
import turtle
from rules import *
from colorsys import hsv_to_rgb

def main():
    axiom = 'F'
    rule = TREE
    iterations = 7 # do not set this to anything higher

    width = 800
    height = 800
    padding = 25
    turtle.Screen().setup(width=0.8, height=0.8)
    turtle.Screen().bgcolor('black')
    turtle.Screen().screensize(width+padding, height+padding)
    turtle.hideturtle()
    
    # Set the turtle to be at the center bottom of the screen facing up
    turtle.penup()
    turtle.goto(width/2,-height/2)
    turtle.pendown()
    turtle.left(90)
    # turtle.speed(0)
    turtle.tracer(75)

    # Draw the Lsystem
    TURTLE(GENERATE_L_SYSTEM(axiom, rule, iterations))
    
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
    for i in range(1, iterations + 1):
        axiom = apply_rules(axiom, rules)
    return axiom

def TURTLE(sentence):
    length = 69
    stack = []
    angle = 10
    hue = 0.0
    for char in sentence:
        # Add more instructions for different chars
        match char:
            case 'F':
                turtle.color(hsv_to_rgb(hue, 0.3, 0.7))
                hue += 0.01
                if hue > 1.0:
                    hue = 0

                turtle.forward(length)
                length -= 0.1
                if length < 1:
                    break
            case '+':
                turtle.left(angle)
            case '-':
                turtle.right(angle)
            case '[':
                stack.append((turtle.pos(), turtle.heading()))
            case ']':
                position, heading = stack.pop()
                turtle.penup()
                turtle.goto(position)
                turtle.setheading(heading)
                turtle.pendown()
            case _:
                print(f'{char} not found in the rules')
        


if __name__ == '__main__':
    main()