import math

def print_word(integer,a_string):
    '''
    This function prints a string the number of times as specified by the integer.
    To do this, it uses the for loop statement.
    '''
    for i in range(integer):
        print(i+1,'-->',a_string)
      

def bacteria(num_min,num_gen):
    '''
    This function calculates the time it takes for a bacteria to calculate the number of 
    bacteria in a petri dish. It uses 2 parameters denoting the number of minutes and
    the number of generations and uses this to print out the population of the bacteria 
    after a given point of time.
    '''
    min = 0
    for i in range(num_gen):
        min = min + num_min
        print('after',min,'minutes: ',2**(i+1),'bacteria')
        
def convert_to_copper(num_gold,num_silver,num_copper):
    '''
    This function is a 3 parameter function which calculates the equivalent number of copper coins
    coins that a given number of gold,silver and copper  is equal to.
    '''
    total_copper = num_gold * 50 + num_silver * 5 + num_copper
    print(num_gold,'gp,',num_silver,'sp,',num_copper,'cp converted to copper is:',total_copper,'cp')
    
def convert_from_copper(num_copper):
    '''
    This function is a 1 parameter function which calculates the equivalent number
    of gold,silver and copper coins that a given number of copper coins is equal to.
    '''
    num_gold = num_copper//50
    remain_copper = num_copper - (num_gold*50)
    num_silver = remain_copper//5
    remain_copper1 = remain_copper - (num_silver*5)
    print(num_copper,'copper pieces is:',num_gold,'gp,',num_silver,'sp,',remain_copper1,'cp')
    
def repeat_word(a_string,num_rows,num_columns):
    '''
    This is a 3 parameter function which prints a string
    along a given number of columns and rows using the for loop.
    '''
    for i in range(num_rows):
        print(a_string*num_columns)
        
        
def text_triangle(integer):
    '''
    This is a 1 parameter function which prints a text triangle using the for loop
    and if the integer is not greater than 0, it prints a blank space. It uses the
    if else statement to complete the task.
    '''
    if integer > 0:
        for i in range(integer):
            print('X' * (i+1))
    else:
        print('X' * 0)
    
def surface_area_of_cylinder(radius,height):
    '''
    This is a 2 parameter function which calculates 
    the surface area of a cylinder using the radius and the height.
    It uses the math.pi function and imports math module to help solve the problem.
    '''
    result = 2*math.pi*(radius**2)+ 2*math.pi*radius*height
    print('The surface area of a cylinder with radius',radius,'and height',height,'is',result)
    
    
def tree_height(base,length):
    '''
    This function uses 2 parameters to determine the 
    height of the tree described in the problem. It uses 
    math.sqrt function in order to solve the problem
    '''
    height = math.sqrt((length**2)-(base**2))
    print('Kite string:',length)
    print('Distance:',base)
    print('Height:',height)
