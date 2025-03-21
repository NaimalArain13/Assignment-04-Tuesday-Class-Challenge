# Problem Statement
# Simulate rolling two dice, and prints results of each roll as well as the total.
import random 
Num = 6
def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    num1:int = random.randint(1,Num)
    num2:int = random.randint(1,Num)
    total:int = num1+num2
    
    # Print out the results
    print("Dice have", Num, "sides each.")
    print("First die:", num1)
    print("Second die:", num2)
    print(f"Total of 2 dice {total}")
    
   
roll_dice()