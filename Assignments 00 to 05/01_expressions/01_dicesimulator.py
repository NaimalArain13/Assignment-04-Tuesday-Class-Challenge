import random 
# Program: dicesimulator
# ----------------------
# Simulate rolling two dice, three times.  Prints
# the results of each die roll.  This program is used
# to show how variable scope works.


Num = 6
def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    num1:int = random.randint(1,Num)
    num2:int = random.randint(1,Num)
    total:int = num1+num2
    print(f"Total of 2 dice {total}")
    
    
def main():
    die1:int = 10
        
    print("die1 in main() in starts as ", str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is ", str(die1))
    
main()
    
    