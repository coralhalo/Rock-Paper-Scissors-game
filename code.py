# Rock-Paper-Scissors-game
# Rock - paper - Scissors game using python. Computer vs human game. 

# generates random number on behalf of the computer 
import random
def generateComputerChoice(): 
    computerinput= random.randint(1,3) 
    if computerinput==1 : 
        return 'r'
    elif computerinput==2: 
        return 'p'
    elif computerinput ==3: 
        return 's' 
    
#generateComputerChoice() testing to see if this function works or not 

#includes conditions for all cases where the user wins. excluding these cases, the computer wins 
def determineWinner(userChoice, computerinput): 
    if userChoice=='r' and computerinput =='s': 
        return 'user'
    elif userChoice=='s' and computerinput =='p': 
        return 'user'
    elif userChoice =='p' and computerinput =='r':
        return 'user' 
    elif userChoice == 'r' and computerinput =='r': 
        return 'tie' 
    elif userChoice =='s' and computerinput == 's': 
        return 'tie' 
    elif userChoice =='p' and computerinput=='p': 
        return 'tie' 
    else: 
        return 'computer' 

      #main function 
def main () :
    userChoice= input("Enter your choice among r,p,s): ")
    computerinput=generateComputerChoice()
    if userChoice=='r' or userChoice =='s' or userChoice=='p':
        final_winner= determineWinner(userChoice, computerinput)
        if final_winner=='user':
            print("You won!")
            return 'user' 
        elif final_winner =='computer': 
            print("Too bad,you lost.")
            return 'computer'
        else: 
            print("It's a tie!")
            return 'tie'
    else: 
        return "Error"      
