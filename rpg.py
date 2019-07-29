'''
Name: Siddhant Bhardwaj
Contributors: Siddhant Bhardwaj, SriHarsha Madhira
'''

import random


class Fighter:
    def __init__(self,name):
        '''
        The init method initializes the fighter class and sets the name
        and hit_points parameter to name and 10 points respectively.
        '''
        self.name = name
        self.hit_points = 10
        
    def __repr__(self):
        '''
        The repr method prints the name of the player and the hit points
        and returns it.
        '''
        result  = self.name + ' (HP: '+ str(self.hit_points) + ')'
        return result
        
    def take_damage(self,damage_amount):
        '''
        The take_damage method calculates the hit points of 
        the players and if it is equal to or less than zero,
        the player falls or if not, the player continues to play with 
        reduced points.        
        '''

        self.hit_points = self.hit_points - damage_amount
        
        if self.hit_points <= 0:
           print('\tAlas, '+ self.name + ' has fallen!')
        else:
           print('\t'+self.name+ ' has '+str(self.hit_points)+ ' hit points remaining.')
           
    def attack(self,other):
        '''
        The attack method calculates an attack value and
        prints it. If attack value is greater than or equal 
        to 12, then the other player takes damage else it misses.
        '''
        print(self.name +' attacks ' + other.name+'!')
        attack_value = random.randrange(1,21)
        if attack_value >= 12:
           damageamount = random.randrange(1,7)
           print('\tHits for '+ str(damageamount) + ' hit points!')
           other.take_damage(damageamount)
        else:
            print('\tMisses!')
           
    def is_alive(self):
        '''
        The is_alive method checks if hit_points are greater than 0
        and returns True.If not, returns false.
        '''
        if self.hit_points > 0:
           return True
        return False

def combat_round(fighter1,fighter2):
    '''
    This  function takes 2 parameters and generates 2 attack values
    and then decides the order in which the fighters attack each other.
    '''
    attack1 = random.randrange(1,7)
    attack2 = random.randrange(1,7)
    if attack1 == attack2:
       print('Simultaneous!')
       fighter1.attack(fighter2)
       fighter2.attack(fighter1)
    elif attack1 > attack2:
       fighter1.attack(fighter2)
       if fighter2.is_alive():
          fighter2.attack(fighter1)
    elif attack1 < attack2:
        fighter2.attack(fighter1)
        if fighter1.is_alive():
           fighter1.attack(fighter2)
             
def main():
    '''
    This main function plays the game and prints the combat rounds 
    until one fighter is slain.
    '''
    Death_Mongrel = Fighter('Death_Mongrel')
    Hurt_then_Pain = Fighter('Hurt_then_Pain')
    c_round = 0
    while Death_Mongrel.is_alive() and Hurt_then_Pain.is_alive():
        c_round += 1  
        print('=================== ROUND '+str(c_round)+' ===================')
        print(Death_Mongrel.__repr__())
        print(Hurt_then_Pain.__repr__())
        pause = input('Enter to Fight!')
        if pause == '':
           continue
        combat_round(Death_Mongrel,Hurt_then_Pain)
    print()
    print('The battle is over!')
    print(Death_Mongrel.__repr__())
    print(Hurt_then_Pain.__repr__())
    
           
           
           
    
          


        