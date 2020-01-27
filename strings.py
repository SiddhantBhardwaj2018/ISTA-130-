'''
Name: Siddhant Bhardwaj
'''

def US_to_EU(date):
    '''
    This code converts dates from the U.S. format of mm/dd/yyyy to E.U.
    format of dd/mm/yyyy/ The function uses the find function and slicing to 
    solve the given problem.
    
    This code was partly inspired by worksheet problem solution 
    taught in lecture for week 10. 
    '''
    len_1 = len(date) 
    x = date.find('/')
    y = date.find('/',x + 1)
    month = str(date[:x])
    day = str(date[x + 1 : y])
    year = str(date[y + 1: len_1])
    return day +'.' + month + '.' + year
    
def is_phone_num(number):
    '''
    This code checks if a given string is a phone number.
    It uses slicing and isdigit function in order to 
    check if the string is a phone number.
    '''
    x = number.find('-')
    y = number.find('-',x + 1)
    len_1 = len(number)
    num1 = str(number[:x])
    num2 = str(number[x + 1: y])
    num3 = str(number[y + 1: len_1])
    if num1.isdigit() == True and num2.isdigit() == True and num3.isdigit() == True:
        if len(num1) == 3 and len(num2) == 3 and len(num3) == 4:
            return True
        return False
    return False
    
def redact_line(a_string):
    '''
    This function redacts a string if it is a phone number
    and his is done by calling the is_phone_num function, 
    by checking various conditions such as i = 0 or if there is a space 
    or '\n' nearby.
    
    This  code was made with the help of our Professor
    
    '''
    
    x = len(a_string)
    for i in range(x - 12):
        if ((i == 0 or a_string[i-1] == ' ') and (a_string[i+12] == '\n' or a_string[i+12] == ' ') and is_phone_num(a_string[i:i+12]) == True):
            
            a_string = a_string[:i] + a_string[i:].replace(a_string[i:i+12],'XXX-XXX-XXXX',1)
    return a_string     
                    
    
def highlight(fname,word):
    '''
    This function highlights a particular keyword 
    in a file by showing it as -->word<-- and 
    uses replace,ljust and strip functions in order to 
    complete it.
    '''
    file = open(fname,'r')
    i = 1
    for line in file:
        if word in line:
           new_1 = repr(i)+':'
           new_1 = new_1.ljust(5)
           line = line.replace(word,'-->'+word+'<--')
           
           print(new_1 + line.strip())
        i += 1
    file.close()
    
def plagiarism(fname1,fname2):
    '''
    This function checks if a line in 1 file is also 
    present in another file. This is done by using the nested loop and readlines()
    and using if statement in order to check this requirement.
    '''
     
    f1 = open(fname1).readlines()
    
    f2 = open(fname2).readlines()
    for line in f1:
        for line1 in f2:
            if line in f2:
               return  True
    return False
    
    f1.close()
    f2.close()
    
def count_word(fname,word):
    '''
    This function counts the number of instances a particular word
    occurs in a file. It uses the .read() and .count() functions in 
    order to return the number of instances the word occurs in 
    a file.
    '''
    f = open(fname,'r')
    f1 = f.read().count(word)
    return (f1)
    f.close()
      
    
    
def redact_file(fname):
    '''
    This code checks all lines in a file and redacts 
    them if a string is a phone number. This is done by 
    calling redact_line function.    
    
    This code was inspired from  the lecture and worksheet
    problem solution for week 10
    '''
    file = open(fname,'r')
    period = fname.find('.')
    new_file = open(fname[:period] + '_redacted' + fname[period:],'w')
    for line in file:
        new_file.write(redact_line(line))
    new_file.close()
    file.close()    



