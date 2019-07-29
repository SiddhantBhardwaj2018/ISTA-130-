'''
Author: Siddhant Bhardwaj
Date: Today
Class: ISTA 130
Section Leader: Erica Cohen

Description:

The given program draws a snake and 
draws each shape with the help of a function.
Each shape begins in a manner that will assist in 
the drawing of the next shape after it is done so as to
draw the figure of the snake.
'''

# put all of your import statements below this line and then delete this comment
import turtle
# put all of your function definitions below this line and then delete this comment

def pentagon(sidd,length_side):
    '''
    Here we draw a pentagon by starting from the 
    lower left corner and finishes in position to 
    complete the snake. The function has 2 parameters,
    sidd, which draws the shape and the numerical value 
    giving the lengths of the pentagon sides.    
    '''
    sidd.left(180)
    sidd.right(108)
    sidd.forward(length_side)
    sidd.left(180)
    sidd.right(108)
    sidd.forward(length_side)
    sidd.left(180)
    sidd.right(108)
    sidd.forward(length_side)
    sidd.left(180)
    sidd.right(108)
    sidd.forward(length_side)
    sidd.left(180)
    sidd.right(108)
    sidd.forward(length_side)
    
    
    
def extra_walk(sidd,length_side):
    '''
    This is a helper function . It has two parameters, sidd,
    which draws the figure and the numerical value which 
    speicifies the required length of the figure.
    '''
    sidd.left(120)
    sidd.forward(2*length_side)
    sidd.left(120)
    sidd.forward(length_side)
    sidd.left(120)
    sidd.forward(2*length_side)
    sidd.right(60)
    sidd.forward(2*length_side)
    sidd.left(120)
    sidd.forward(length_side)
    sidd.left(120)
    sidd.forward(2*length_side)
    sidd.right(120)
    sidd.forward(length_side)
    sidd.penup()
    sidd.left(60)
    sidd.forward(length_side)
    sidd.left(60)
    sidd.forward(length_side)
    sidd.right(120)
    sidd.left(90)
    sidd.pendown()
    

def hexagon(sidd,length_side):
    '''
    Here we draw a hexagon by starting from the 
    lower left corner and finishes in position to 
    draw the next shape. The function has 2 parameters,
    sidd, which draws the shape and the numerical value 
    giving the lengths of the hexagon sides.
    
    '''
    sidd.left(120)
    sidd.forward(length_side)
    sidd.left(60)
    sidd.forward(length_side)
    sidd.left(60)
    sidd.forward(length_side)
    sidd.left(60)
    sidd.forward(length_side)
    sidd.left(60)
    sidd.forward(length_side)
    sidd.left(60)
    sidd.forward(length_side)
    sidd.left(60)
    sidd.forward(length_side)
    sidd.left(60)
    sidd.forward(length_side)
    sidd.right(60)
    sidd.forward(length_side)
    sidd.left(60)
    sidd.forward(length_side)
    sidd.left(60)
    sidd.forward(length_side)
    sidd.left(60)
    sidd.forward(length_side)
    sidd.left(60)
    sidd.forward(length_side)
    
def square(sidd,length_side):
    '''
    Here we draw a hexagon by starting from the 
    upper right corner and finishes in position to 
    draw the next shape. The function has 2 parameters,
    sidd, which draws the shape and the numerical value 
    giving the length of the square sides.
    '''
    sidd.forward(length_side)
    sidd.left(90)
    sidd.forward(length_side)
    sidd.left(90)
    sidd.forward(length_side)
    sidd.left(90)
    sidd.forward(length_side)
    sidd.left(90)
    sidd.forward(length_side)
    
def triangle(sidd,length_side):
    '''
    Here we draw a triangle by starting from the 
    upper right corner and finishes in position to 
    draw the next shape. The function has 2 parameters,
    sidd, which draws the shape and the numerical value 
    giving the lengths of the triangle sides.
    '''
    sidd.left(30)
    sidd.forward(length_side)
    sidd.left(120)
    sidd.forward(length_side)
    sidd.left(120)
    sidd.forward(length_side)
    sidd.penup()
    sidd.right(90)
    sidd.forward(length_side)
    sidd.left(30)
    sidd.forward(length_side)
    sidd.right(60)
    sidd.forward(length_side)
    sidd.left(60)
    sidd.forward(length_side)
    sidd.right(60)
    sidd.forward(length_side)
    sidd.right(60)
    sidd.forward(length_side)
    sidd.pendown()
    
    
    
    
    
    


#==========================================================
def main():
    '''
    here, we draw a snake by using all 
    the previously specified functions to 
    put together this snake figure. We specify the 
    turtle name, color, pensize and shape.
    '''
    # put main code here, make sure each line is indented one level, and delete this comment
    
    sidd = turtle.Turtle()
    sidd.shape('turtle')
    sidd.speed(0)
    sidd.pensize(10)
    sidd.penup()
    sidd.left(30)  
    sidd.pendown()
    
    # Draw Snake
    
    sidd.color('blue')
    hexagon(sidd,50)
    
    sidd.color('crimson')
    extra_walk(sidd,50)
    
    sidd.color('purple')
    square(sidd,50)
    
    sidd.color('green')
    triangle(sidd,50)
    
    sidd.color('darkred')
    pentagon(sidd,50)
    
    
    
   
    
    
    
    
    
    
    sidd.hideturtle()
    
    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
