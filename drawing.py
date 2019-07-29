'''
Author: Siddhant Bhardwaj
Date: Today
Class: ISTA 130
Section Leader: Erica Cohen

Description:
The given program draws a polygon and 
draws with the help of a main shape and function 
and helper functions. The program draws the 
polygon in different sizes, colors and shapes in multiple 
locations.
'''

import turtle

def shape(sidd,radius):
    '''
    Here, we use shape function to 
    create a polygon with 2 parameters
    - sidd making the drawing and radius denoting the 
    numerical value of the side of the polygon.
    '''
    sidd.circle(radius,60)
    sidd.right(120)
    sidd.circle(radius,60)
    sidd.right(120)
    sidd.circle(radius,60)
    sidd.right(120)
    sidd.circle(radius,60)
    sidd.right(120)
    sidd.circle(radius,60)
    sidd.right(120)
    sidd.circle(radius,60)
    
    
def extra_walk1(sidd,distance):
    '''
    This is a helper function 
    used to make the polygon in 
    a different location. It has 2 
    parameters - sidd, which is used 
    for drawing and distance, which is 
    the numerical value of the distance 
    between the old shape and the news shape.
    '''
    sidd.penup()
    sidd.left(40)
    sidd.forward(distance)
    sidd.pendown()
    
def extra_walk2(sidd,distance):
    '''
    This is a helper function 
    used to make the polygon in 
    a different location. It has 2 
    parameters - sidd, which is used 
    for drawing and distance, which is 
    the numerical value of the distance 
    between the old shape and the news shape.
    '''
    sidd.penup()
    sidd.left(270)
    sidd.forward(distance)
    sidd.pendown()
    
def extra_walk3(sidd,distance):
    '''
    This is a helper function 
    used to make the polygon in 
    a different location. It has 2 
    parameters - sidd, which is used 
    for drawing and distance, which is 
    the numerical value of the distance 
    between the old shape and the news shape.
    ''' 
    sidd.penup()
    sidd.left(90)
    sidd.forward(distance)
    sidd.pendown()
    
def extra_walk4(sidd,distance):
    '''
    This is a helper function 
    used to make the polygon in 
    a different location. It has 2 
    parameters - sidd, which is used 
    for drawing and distance, which is 
    the numerical value of the distance 
    between the old shape and the news shape.
    ''' 
    sidd.penup()
    sidd.left(90)
    sidd.forward(distance)
    sidd.pendown()
    
def extra_walk5(sidd,distance):
    '''
    This is a helper function 
    used to make the polygon in 
    a different location. It has 2 
    parameters - sidd, which is used 
    for drawing and distance, which is 
    the numerical value of the distance 
    between the old shape and the news shape.
    ''' 
    sidd.penup()
    sidd.right(260)
    sidd.forward(distance)
    sidd.pendown()
    

    


#==========================================================
def main():
    '''
    Here, we draw the polygon with the 
    help of the helper function and the
    shape function. We specify the color, size
    and turtle name.
    '''
    
    sidd = turtle.Turtle()
    sidd.shape('turtle')
    sidd.speed(0)
    sidd.pensize(5)
   
    
    
    # Draw shape
    sidd.color('blue')
    shape(sidd,100)
    
    extra_walk2(sidd,150)
    
    sidd.color('pink')
    shape(sidd,50)
    
    extra_walk1(sidd,200)
    
    sidd.color('crimson')
    shape(sidd,75)
    
    extra_walk3(sidd,100)
    sidd.color('yellow')
    shape(sidd,60)
    
    extra_walk3(sidd,200)
    sidd.color('orange')
    shape(sidd,70)
    
    extra_walk4(sidd,270)
    sidd.color('darkgreen')
    shape(sidd,45)
    
    extra_walk5(sidd,425)
    sidd.color('purple')
    shape(sidd,70)
    
    
    
    
    
    
    sidd.hideturtle()
    turtle.getscreen().exitonclick()  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
