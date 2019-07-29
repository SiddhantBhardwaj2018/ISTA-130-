'''
Author: Siddhant Bhardwaj
Date: Today
Class: ISTA 130
Section Leader: Erica Cohen

Description:
The given program draws the name 'SIDDHANT' and 
draws each letter with the help of a function.
Each letter starts from the lower-left corner 
and finishes in position to start the next letter.
'''
# put all of your import statements below this line and then delete this comment
import turtle
# put all of your function definitions below this line and then delete this comment
def draw_S(sidd):
    '''
    Draws the letter 'S' starting in the lower-left corner and 
    finishes in position to start the next letter.The function 
    has one turtle parameter, sidd , which draws the letter.
    It returns None.
    '''
    sidd.forward(15)
    sidd.left(90)
    sidd.forward(15)
    sidd.left(90)
    sidd.forward(15)
    sidd.right(90)
    sidd.forward(15)
    sidd.right(90)
    sidd.forward(15)
    sidd.penup()
    sidd.right(90)
    sidd.forward(30)
    sidd.left(90)
    sidd.pendown()
    return None
    
def draw_I(sidd):
    '''
    Draws the letter 'I' starting in the lower-left corner and 
    finishes in position to start the next letter.The function 
    has one turtle parameter, sidd , which draws the letter.
    It returns None.
    '''
    sidd.left(90)
    sidd.forward(30)
    sidd.penup()
    sidd.backward(30)
    sidd.pendown()
    sidd.right(90)
    return None
    
def draw_D(sidd):
    '''
    Draws the letter 'D' starting in the lower-left corner and 
    finishes in position to start the next letter.The function 
    has one turtle parameter, sidd , which draws the letter.
    It returns None.
    '''
    sidd.circle(15,180)
    sidd.left(90)
    sidd.forward(30)
    sidd.left(90)
    return None
    
def draw_H(sidd):
    '''
    Draws the letter 'H' starting in the lower-left corner and 
    finishes in position to start the next letter.The function 
    has one turtle parameter, sidd , which draws the letter.
    It returns None.
    '''
    sidd.left(90)
    sidd.forward(30)
    sidd.penup()
    sidd.backward(15)
    sidd.right(90)
    sidd.pendown()
    sidd.forward(15)
    sidd.penup()
    sidd.left(90)
    sidd.forward(15)
    sidd.pendown()
    sidd.backward(30)
    sidd.right(90)
    return None
     
def draw_A(sidd):
    '''
    Draws the letter 'A' starting in the lower-left corner and 
    finishes in position to start the next letter.The function 
    has one turtle parameter, sidd , which draws the letter.
    It returns None.
    '''
    sidd.left(90)
    sidd.forward(30)
    sidd.right(90)
    sidd.forward(15)
    sidd.right(90)
    sidd.forward(30)
    sidd.penup()
    sidd.backward(15)
    sidd.right(90)
    sidd.pendown()
    sidd.forward(15)
    sidd.penup()
    sidd.backward(15)
    sidd.left(90)
    sidd.forward(15)
    sidd.left(90)
    sidd.pendown()
    return None
    
def draw_N(sidd):
    '''
    Draws the letter 'N' starting in the lower-left corner and 
    finishes in position to start the next letter.The function 
    has one turtle parameter, sidd , which draws the letter.
    It returns None.
    '''
    sidd.left(90)
    sidd.forward(30)
    sidd.right(145)
    sidd.forward(36)
    sidd.left(145)
    sidd.forward(30)
    sidd.penup()
    sidd.backward(30)
    sidd.right(90)
    sidd.pendown()
    return None

def draw_T(sidd):
    '''
    Draws the letter 'T' starting in the lower-left corner and 
    finishes in position to start the next letter.The function 
    has one turtle parameter, sidd , which draws the letter.
    It returns None.
    '''
    sidd.left(90)
    sidd.forward(30)
    sidd.left(90)
    sidd.forward(15)
    sidd.penup()
    sidd.backward(15)
    sidd.pendown()
    sidd.backward(15)
    sidd.penup()
    sidd.forward(15)
    sidd.left(90)
    sidd.forward(30)
    sidd.pendown()
    sidd.left(90)
    return None
    
def walk(sidd,what_distance):
    sidd.penup()
    sidd.forward(what_distance)
    sidd.pendown()

#==========================================================
def main():
    '''
    Here, we draw the name SIDDHANT. We use all 
    the previous functions used to draw individual
    letters and use them to draw the name. We specify 
    the turtle name, color, pensize and shape.
    
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    sidd = turtle.Turtle()
    sidd.shape('turtle')
    sidd.speed(0)
    sidd.pensize(5)
    sidd.penup()
    sidd.backward(200)
    sidd.pendown()
    turtle.bgcolor('black')
    
    # Draw SIDDHANT
    sidd.color('darkmagenta')
    draw_S(sidd)
    
    walk(sidd,15)
    
    sidd.color('red')
    draw_I(sidd)
    
    walk(sidd,15)
    
    sidd.color('blue')
    draw_D(sidd)
    
    walk(sidd,30)
    
    sidd.color('deeppink')
    draw_D(sidd)
    
    walk(sidd,30)
    
    sidd.color('crimson')
    draw_H(sidd)
    
    walk(sidd,15)
    
    sidd.color('darkseagreen')
    draw_A(sidd)
    
    walk(sidd,15)
    
    sidd.color('darkslateblue')
    draw_N(sidd)
    
    walk(sidd,25)
    
    sidd.color('white')
    draw_T(sidd)
    
    sidd.hideturtle()
  
    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
