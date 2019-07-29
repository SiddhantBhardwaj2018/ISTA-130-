def print_report(fname):
    '''
    This function will read a given file and 
    count the number of vowels, consonants, whitespace and
    punctuation, their percentage as a part of the total file 
    and presents it in the form of a table.
    '''
    file = open(fname,'r')
    x = file.read().lower()
    v = ['a','e','i','o','u']
    c = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    count_vowel = 0
    count_consonant = 0
    count_space = 0
    count = 0
    for letter in x:
        if letter in v:
           count_vowel += 1
        elif letter in c:
            count_consonant += 1
        elif letter == ' ' or letter == '\n' or letter == ' ':
            count_space += 1
        else:
            count += 1
    sum = count_consonant + count_space + count_vowel + count
    vowel_comp = (count_vowel / sum) * 100
    consonant_comp = (count_consonant/sum) * 100
    space_comp = (count_space/sum) * 100
    punctuation = (count/sum) * 100
    z = '-------'+fname+'------'
    a = 'Vowels:'.ljust(20)
    
    b = 'Consonants:'.ljust(20)
    
    p = 'Whitespace:'.ljust(20)
    
    q = 'Punctuation:'.ljust(20)
   
    w = 'Percent vowels:'.ljust(20)
    
    s = 'Percent consonants:'.ljust(20)
    
    i = 'Percent spaces:'.ljust(20)
    
    j = 'Percent punctuation:'.ljust(20)
   
    k = 'Total:'.ljust(20)
   
    count1 = str(count_consonant).rjust(5)
    count2 = str(count_vowel).rjust(5)
    count3 = str(count_space).rjust(5)
    count = str(count).rjust(5)
    u = str(round(vowel_comp,1)).rjust(5)
    m = str(round(consonant_comp,1)).rjust(5)
    n = str(round(space_comp,1)).rjust(5)
    r = str(round(punctuation,1,)).rjust(5)
    l = str(sum).rjust(5)
    
    print()
    print(z)
    print(a + count2)
    print(b + count1)
    print(p + count3)
    print(q + count)
    print('-------------------------')
    print(k + l)
    print()
    
    print(w + u)
    print(s + m)
    print(i + n)
    print(j + r)
    print('=========================')
    print()

def replace_parts_of_speech(lineinfile,speechpart):
    '''
    This function replaces the parts of speech in a given line.
    The function takes in 2 parameters - lineinfile and speechpart and
    uses the replace function to replace it in a loop.
    '''
    numpart = lineinfile.count(speechpart)
    new1 = lineinfile
    for i in range(numpart):
        askuser = input('Enter '+speechpart.lower()+': ')
        new1 = new1.replace(speechpart,askuser,1)
    return new1
    
def complete_mad_lib(fname):
    '''
    This function calls the replace_parts_of_speech
    uses them to replace it in a file. It uses a loop function
    in order to complete the task.    
    '''
    file = open(fname,'r')
    
    file2 = open('MAD_'+fname,'w')
    
    for line in file:
        line =  replace_parts_of_speech(line,'PLURAL NOUN')
        line = replace_parts_of_speech(line,'VERB PAST')
        line = replace_parts_of_speech(line,'VERB')
        line = replace_parts_of_speech(line,'NOUN')
        line = replace_parts_of_speech(line,'ADJECTIVE')
        file2.write(line)
    




def main():
    '''
    This function takes the filename through 
    input statement and calls the print_report and complete_mad_lib
    function in order to print a table and replaces part of speech
    in a file.
    '''
    userinput = input("Enter file name: ")
    print_report(userinput)
    complete_mad_lib(userinput)    
    
    
    