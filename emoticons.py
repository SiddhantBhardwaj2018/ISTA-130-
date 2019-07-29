'''
Name: Siddhant Bhardwaj
Contributors: Siddhant Bhardwaj, Sriharsha Madhira
'''

def load_twitter_dicts_from_file(filename,emoticons_to_ids,ids_to_emoticons):
    '''
    This functions takes two empty dictionaries and reads file 
    'twitter_emoticons.dat' to them and makes emoticons the key and 
    the user ids the values in one dictionary and vice versa in the 
    other.
    '''
    file = open(filename,'r')
    
    
    for line in file:
        line = line.split()
        line[0] = line[0].replace('"','')
        line[2] = line[2].replace('"','')
        emoticon_key = line[0]
        id_key = line[2]
        if emoticon_key not in emoticons_to_ids:
           emoticons_to_ids[emoticon_key] = []
        emoticons_to_ids[emoticon_key].append(line[2])
        if id_key not in ids_to_emoticons:
           ids_to_emoticons[id_key] = []
        ids_to_emoticons[id_key].append(line[0])
        
def find_most_common(dict1):
    '''
    This function finds the key in the dictionary whose list valu has the most 
    length and prints it and returns it.
    '''
    max_len = 0
    max_key = None
    for key in dict1:
        if len(dict1[key]) >= max_len:
           max_len = len(dict1[key])
           max_key = key
           
    a = max_key.ljust(21)
    b = str(max_len).rjust(9)
    print(a+'occurs'+b+' times')
    return max_key
    
def main():
    '''
    This main function prints the length of the emoticons_to_ids
    and ids_to_emoticons dictionaries and then finds the 5 most
    common emoticons.
    '''
    emoticons_to_ids = {}
    ids_to_emoticons = {}
    load_twitter_dicts_from_file('twitter_emoticons.dat',emoticons_to_ids,ids_to_emoticons)
    s = str(len(emoticons_to_ids))
    w = str(len(ids_to_emoticons))
    print('Emoticons: '+s)
    print('UserIDs:   '+w)
    for i in range(5):
        
        y = find_most_common(emoticons_to_ids)
        emoticons_to_ids.pop(y)
        
        
        
            
    
   
        
            