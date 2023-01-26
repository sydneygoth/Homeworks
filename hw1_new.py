import os
import math
state = 0
wins = 0
losses = 0
guesses = 0
my_list = []
correct_answer = 0
leftover_list = []
new_list = []
correct_ans = []
hint = str

import random
#blah blah
while(True):
  #  try:
        #initialize grid               
        if(state==0):
            my_list.clear()
            num1 = random.randint(0, 5)
            num2 = random.randint(0, 5)
            num3 = random.randint(0, 5)
            num4 = random.randint(0, 5)

            correct_answer = int( str(num1) + str(num2) + str(num3) + str(num4))
            correct_dig = 0
            other_dig = 0
            notrightspot = 0
            
            #print(correct_answer)
            guesses = 0
            print('Mastermind! Try to break the code. Only integers')
            print('wins:  ',wins)
            print('losses:',losses)
            
            if guesses < 12:
                for i in range(12-guesses):
                    print("+−−−+−−−+−−−+−−−+")
                    print ("|   |   |   |   |")
            print("+−−−+−−−+−−−+−−−+")
            
            state = 1
            
        #wait for user
        elif(state==1):
            
            my_input = input('Enter a guess: ')
            #converts to string to check each indiv size of number to be <= 5
            my_guess = str(my_input)
            state = 3
                           
            #checks length of guess
            if (len(my_input) != 4):
                state = 2
            else:
                state = 3
                
            #checks if between 0-5
            for d in range (-1, len(my_guess)):
                i = my_guess[d]
                if (int(i)>=6):
                    state = 2
                elif(int(i)<6):
                    state = 3
                else:
                    state = 2
            
        #error
        elif(state==2):
            print ('Digits outside of range')
            state = 1
            
        #display guess
        elif(state==3):
            state = 1
            
            correct_dig = 0
            notrightspot = 0
            
            my_list.insert(guesses, my_input)
            str_input = str(my_input)
            str_ans = str(correct_answer)
            hint = ""
            correct_ans = [x for x in str(str_ans)]
            
            #print(correct_ans)
            #this splits the string into individual spots :)
            new_list = [x for x in str(my_input)]
            
            #check if number is in right spot
            for d in range (0, len(str_input)):
                if new_list[d] in correct_ans:
                    if new_list[d] == correct_ans[d]:
                        hint = hint + "+"
                        
                       # hint = str(hint + '+')
                        correct_dig +=1
                        
                    else:
                        hint = hint + "-"
                        notrightspot +=1
            leftover_list.insert(guesses, hint)
            #print(leftover_list)
            #should add new input to the array
            if (guesses < 11):
                for i in range(11-guesses):
                    print("+−−−+−−−+−−−+−−−+")
                    print ("|   |   |   |   |")
                print("+−−−+−−−+−−−+−−−+")
                
                #FIGURE OUT HOW TO ADD + and -
                for my_item in reversed(my_list):
                    
                    print ("| " + " | ".join(my_item) + " |" + hint)
                    print("+−−−+−−−+−−−+−−−+")   
 
                state = 1    #return to state 1 for new input
                
                #you win yay! :D (make sure to be comparing the same type of number (integer type))
                int_input = int(my_input)
                if (int_input == correct_answer):
                    state = 4  
                    
            #you lose... :(
            elif(guesses>=11):
                state = 5
                print("+−−−+−−−+−−−+−−−+")
                for my_item in reversed(my_list):
                    print ("| " + " | ".join(my_item) + " |")
                    print("+−−−+−−−+−−−+−−−+")
                
            guesses+=1
            
        #win
        elif(state==4):
            print('you win')
            play_again = input('play again? [y]: ')
            if (play_again == 'y'):
                state = 0
            else:
                break
            wins +=1

        
        #lose
        elif(state==5):
            print('you lose')
            play_again = input('play again? [y]: ')
            if (play_again == 'y'):
                state = 0
            elif():
                break
            losses +=1
