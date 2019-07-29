def word_length(a_string,integer):
    '''
    This is a function taking 2 parameters
    a_string and an integer, and prints 
    a message about the relationship between the
    length of the word and the integer, such as if the word is
    longer than, shorter than or exactly the same.
    '''
    if len(a_string) == integer:
       print('Exactly',integer,'characters:',a_string)
    elif len(a_string) > integer:
       print('Longer than',integer,'characters:',a_string)
    else:
       print('Shorter than',integer,'characters:',a_string)
       
       
def stop_light(current_color,time):
    '''
    This is a function that takes 2 parameters, one for color of light 
    and second for length of light's duration.It then changes color based on 
    2 parameters, current color and time.    
    '''
    if current_color == 'green' and time > 60:
        return "yellow"
    elif current_color == 'yellow' and time > 5:
        return "red"
    elif current_color == 'yellow' and time <= 5:
        return "yellow"
    elif current_color == 'red' and time > 55:
        return "green"
    elif current_color == 'green' or current_color == 'red' and time < 55:
        return current_color
        
def is_normal_blood_pressure(systolic_pressure,diastolic_pressure):
    '''
    This function takes 2 parameters, systolic pressure and diastolic 
    pressure, and returns respective boolean considering what values are
    entered for 2 parameters.
    '''
    if systolic_pressure < 120 and diastolic_pressure < 80:
        return True
    
    return False
    
def doctor():
    '''
    This function has no parameters and takes 2 inputs for systolic 
    pressure and diastolic pressure, and calls the previous function
    to generate output of whether bllod pressure is normal or high.
    '''
    systolic_reading = int(input('Enter your systolic reading:'))
    diastolic_reading = int(input('Enter your diastolic reading:'))
    if is_normal_blood_pressure(systolic_reading,diastolic_reading) == True:
        print('Your blood pressure is normal.')
    else:
        print('Your blood pressure is high.')
    
def pants_size(integer):
    '''
    This function has one parameter that determines
    if the pant size is large small or
    medium
    '''
    if integer >= 34:
        return "large"
    elif integer >= 30 and integer < 34:
        return "medium"
    else:
        return "small"
        
def pants_fitter():
    '''
    This function has no parameter and prints
    the details of the customer such as cost of dress and takes inputs
    such as name , number of dresses, waist size and pant type.
    '''
    name = input('Enter your name:')
    print('Greetings',name,'welcome to Pants-R-Us')
    waist_size = int(input('Enter your waist size in inches:'))
    boogie = (pants_size(waist_size))
    pair_num = input('How many pairs of pants would you like:')
    pant_type = input('Would you like regular or fancy pants:')
    if pant_type == 'regular':
        cost = 40 * int(pair_num)
    elif pant_type == 'fancy':
        cost = 100 * int(pair_num)
    
    print(pair_num,'pairs of',boogie,pant_type,'pants: $',cost)
        
        
def species_height(species,height):
    '''
    This function takes 2 parameters - species and height
    and prints whether the height is average or below average 
    depending on if the species is klingon or human.    
    '''
    if species == "Klingon" and height == 71:
        print('Average')
    elif species == "Human" and height == 67:
        print('Average')
    elif species == "Klingon" and height < 71:
        print('Below Average')
    elif species == "Klingon" and height > 71:
        print('Above Average')
    elif species == "Human" and height > 67:
        print('Above Average')
    elif species == "Human" and height < 67:
        print('Below Average')
        
        
def beef_type(percent_lean):
    '''
    This function takes 1 parameter - percent_lean 
    and returns different types of cuts depending on 
    what percent is lean.
    '''
    if percent_lean < 78:
        return "Hamburger"
    elif percent_lean >= 78 and percent_lean < 85:
        return "Chuck"
    elif percent_lean >= 85 and percent_lean < 90:
        return "Round"
    elif percent_lean >= 90 and percent_lean <= 95:
        return "Sirloin"
    else:
        return "Unknown"
        
def digdug(integer):
    '''
    This function has a single parameter, integer and 
    prints the phrases 'dig','dug' and 'digdug' depending 
    whether the integer was evenly divisible by 3,5 or both
    '''
    i = 0
    while i < integer:
        i = i + 1
        if i%3 == 0 and i%5 != 0:
            print(i,": dig")
        elif i%5 == 0 and i%3 != 0:
            print(i,": dug")
        elif i%3 == 0 and i%5 == 0:
            print(i,": digdug")
        
        
def sooner_date(month_1,day_1,month_2,day_2):
    '''
    This function is a 4 parameter function takes in 
    2 different months and days and prints the dat that is earlier 
    than the other one.
    '''
    if month_1 > month_2:
        print(month_2,'/',day_2)
    elif month_1 < month_2:
        print(month_1,'/',day_1)
    elif month_1 == month_2:
        if day_1 > day_2:
            print(month_1,'/',day_2)
        elif day_1 < day_2:
            print(month_1,'/',day_1)
        else:
            print(month_1,'/',day_1)
        

        
