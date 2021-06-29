import Permutation as P
import Combination as C

def Permi():

    print("You have chosen Permutation Calculator!")
    choice = 'Y'
    while choice == 'Y':

        input_N = int(input("Enter N:"))
        input_R = int(input("Enter R:"))

        P.Permutation(input_N,input_R)
    
        user_choice = input("Would you like to try again? [Y] / [N]")
        if user_choice.casefold() == 'y':
            choice = 'Y'
        elif user_choice.casefold() == 'n':
            print("Thank you!")
            break

def Combi():

    print("You have chosen Comination Calculator!")
    choice = 'Y'
    while choice == 'Y':

        input_N = int(input("Enter N:"))
        input_R = int(input("Enter R:"))

        C.Combination(input_N,input_R)
    
        user_choice = input("Would you like to try again? [Y] / [N]:")
        if user_choice.casefold() == 'y':
            choice = 'Y'
        elif user_choice.casefold() == 'n':
            print("Thank you!")
            break

def Main():
    print("Welcome to Permutation and Combiantion Calcu!")
    print("[1]Permutation Calculator \n[2]Combination Calculator")
    user = int(input("Enter number of choice:"))
    if user == 1:
        Permi()
    elif user == 2:
        Combi()
        


Main()