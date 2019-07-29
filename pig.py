'''
Author: Sriharsha Madhira
Collab: Siddhant Bhardwaj
Date: Today
Class: ISTA 130
Section Leader: Erica Cohen

Description:
The given program is a 2 player game of pig. the players roll a 
dice and get values between 1 and 6. Ech player starts with a score of 0
and each dice roll other than 1 is added to the players' score. The first player to get a score of 50
wins the game.
'''

import random

def print_scores(first_name,first_score,second_name,second_score):
    '''
    This function will print the name of the first player, the score of the second player
    the score of the first player, and the name of the second player.
    '''
    print()
    print('--- SCORES\t' + first_name + ': ' + str(first_score) +'\t' + second_name + ': ' + str(second_score) + ' ---')
    
    

    
def check_for_winner(name,score):
    '''
    This function will check whether the said person has won the game. If the person 
    has received a score of 50 or above, then he is the winner and the function returns True.
    Else, the function returns false.
    '''
    if score >= 50:
        print('THE WINNER IS:',name +'!!!!!')
        return True
    else:
        return False

def roll_again(name):
    '''
    This function will ask the player to roll again. If the player answers with a Y or a y, the 
    function returns True, else if player submits N, it returns False. If the player enters something else,
    the function asks the player to resubmit since it could not be understood.
    '''
    while True:
        choice = input('Roll again, {}? (Y/N) '.format(name))
        if choice == 'y' or choice == 'Y':
            return True
        elif choice == 'n' or choice == 'N' :
            return False
        else:
            print("I don't understand:",'"'+choice+'". Please enter either "Y" or "N".')
            continue

def play_turn(name):
    '''
    This function takes a player's name and beginning with a score of 0,
    adds the score with the dice roll if the the roll is not 1.
    Otherwise, it adds 0 to score and asks the user to enter to continue    
    '''
    print('---------- '+ name+"'s turn",'----------')
    score = 0

    while True:
        x = random.randint(1,6)
        print('\t<<< {} rolls a {} >>>'.format(name,x))
        if x == 1:  
            print('\t!!! PIG! No points earned, sorry {} !!!'.format(name))
            score = 0
            continue_code = input('(enter to continue)')
            return score
            
            
            
        else:
            score += x  
            print('\tPoints:',score)
            wish = roll_again(name)
            if wish == False:
                return score
        
def main():
    '''
    This main function runs the final function
    and executes the code.
    '''
    seed1 = int(input('Enter seed value: '))
    random.seed(seed1)
    print()
    print()
    print("Pig Dice")
    player_1 = input("Enter name for player 1: ")
    player_2 = input("Enter name for player 2: ")
    print('\tHello',player_1,'and',player_2+', '+'welcome to Pig Dice!')
    score_1 = 0
    score_2 = 0
    
    print_scores(player_1,score_1,player_2,score_2)
    while True:
        score_1+= play_turn(player_1)
        print_scores(player_1,score_1,player_2,score_2)
        if check_for_winner(player_1,score_1) == True:
            break
        else:
            score_2 += play_turn(player_2)
            print_scores(player_1,score_1,player_2,score_2)
            if check_for_winner(player_2,score_2) == True:
               break
            
                
                
               
        




    

    


#==========================================================
