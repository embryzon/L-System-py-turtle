# Based on Daniel Shiffman's Coding Challenge #16
import turtle
from rules import TREE

def main():
    axiom = 'F'
    iterations = 5

    width = 775
    height = 775
    padding = 25
    turtle.Screen().screensize(width+padding, height+padding)
    turtle.hideturtle()
    
    # Set the turtle to be at the center bottom of the screen facing up
    turtle.penup()
    turtle.goto(0,-height/2)
    turtle.pendown()
    turtle.left(90)
    turtle.speed(0)
    
    # Draw the Lsystem
    TURTLE(GENERATE_L_SYSTEM(axiom, TREE, iterations))
    
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
    length = 100
    stack = []
    for char in sentence:
        match char:
            case 'F':
                turtle.forward(length)
                length *= 0.99
                if length < 2:
                    break
            case '+':
                turtle.left(15)
            case '-':
                turtle.right(15)
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