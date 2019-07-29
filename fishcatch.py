'''
Name: Siddhant Bhardwaj
Contributors: Siddhant Bhardwaj, Sriharsha Madhira


'''

def fish_dict_from_file(filename):
    '''
    This function maps numeric species code to english name
    and reads 'fishcatch.dat' file  to create a dictionary of lists
    containing the weights of the fish as values and name of the fish as the key.
    '''
    fishmap = {'1':'Bream','2':'Whitefish','3':'Roach','4':'?','5':'Smelt','6':'Pike','7':'Perch'}
    spec_weight_dict = {}
    file1 = open(filename,'r')
    for line in file1:
        line1 = line.split()
        if line1[2] == 'NA':
            continue    
        key = fishmap[line1[1]]    
        if key not in spec_weight_dict:
           
            spec_weight_dict[key] = []
           
        spec_weight_dict[key].append(float(line1[2]))
                
    return spec_weight_dict
    
def main():
    '''
    The function prints a report containing the frequency of the fish,
    the name of the fish and the mean weight of the fish.
    '''
    x = fish_dict_from_file('fishcatch.dat')
    a = '#'.rjust(4)
    b = 'NAME'.ljust(10)
    c = 'MEAN WT'.rjust(10)
    print(a+' '+b+' '+c)
    for key in sorted(x):
        y  = str(len(x[key])).rjust(4)
        avg = sum(x[key])/len(x[key])
        avg1 = str(round(avg,1)).rjust(10)
        key = key.ljust(10)
        print(y + ' '+key +avg1 +'g')
        
    
                  
            