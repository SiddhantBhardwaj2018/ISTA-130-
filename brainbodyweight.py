'''
Author: Siddhant Bhardwaj
Class: ISTA 130
Section Leader: Cedric Vicera
Collaborator: SriHarsha Madhira
'''
def find_insert_position(name,list1):
    '''
    This function takes two parameters, first one is a string
    showing mammal's name and the second is a list which is used in 
    the function such that it returns an integer so that the name entered in
    the list still remains in an alphabetical order.
    '''
    list1.insert(0,name)
    list1.sort()
    for i in range(len(list1)):
        if list1[i] == name:
            list1.remove(name)
            return (i)
            
def populate_lists(name,body,brain):
    '''
    This functions opens BrainBodyWeightKilos.csv file and
    populates 3 lists such that the name list contains names of animals,
    body contains body weights and brain list contains brain weights.
    '''
    f1 = open('BrainBodyWeightKilos.csv','r')
    for line in f1:
        x = line.split(',')
        y = x[0].title()
        z = float(x[1])
        a = float(x[2])
        name.append(y)
        body.append(z)
        brain.append(a)
    f1.close()     
    return None
     
    
def write_converted_csv(file,name,body_weights,brain_weights):
    '''
    The function writes a new file with the names of the mammals,
    their brain aweight and body weight. It has 4 parameters.
    '''
    f2 = open(file,'w')
    new_wt = []
    new_brain = []
    for element in body_weights:
        x = element * 2.205
        new_wt.append(round(x,2))
    for item in brain_weights:
        y = item * 0.0022
        new_brain.append(round(y,2))
   
    for a,b,c in zip(name,new_wt,new_brain):
        f2.write(a+','+str(b)+','+str(c)+'\n')
    f2.close()            
        
def main():
	'''
	This function asks user for input regarding animal name and checks if there is the animal
    in the list. If not, it asks the user to enter or not to enter it in the list.
    Otherwise, if the user wants to leave, it writes a new file with the data in it.
	'''
	names = []
	body_weights = []
	brain_weights = []
	populate_lists(names, body_weights, brain_weights)

	while True:
		print()
		animal = input('Enter animal name (or "q" to quit): ')
		if (animal == 'q'):
			write_converted_csv('BrainBodyWeightPounds.csv', names, body_weights, brain_weights)
			return None

		animal_name = animal.title()

		if animal_name in names:
			index = find_insert_position(animal_name, names)
			body = body_weights[index]
			brain = brain_weights[index]
			print(animal_name+': body = '+str(body)+', brain = '+str(brain))
			del_line = 'Delete \"'+animal_name+'\"? (y|n) '
			del_answer = input(del_line)
			if (del_answer == 'n'):
				continue
			if (del_answer == 'y'):
				names.pop(index)
				body_weights.pop(index)
				brain_weights.pop(index)
		else:
			print('File does not contain \"'+animal_name+'\".')
			name_add = input('Add \"'+animal_name+'\" to file? (y|n) ')
			if name_add == 'n':
				continue
			if name_add == 'y':
				body_weight = float(input('Enter body weight for \"'+animal_name+'\" in kilograms: '))
				brain_weight = float(input('Enter brain weight for \"'+animal_name+'\" in grams: '))
				index = find_insert_position(animal_name, names)
				names.insert(index, animal_name)
				body_weights.insert(index, body_weight)
				brain_weights.insert(index, brain_weight)

if __name__ == '__main__':
	main()