# Problem Statement
# Write a function that takes a list of numbers and returns the sum of those numbers.

def add_number(lst):
    total = 0
    for number in lst:
        total+=number
    return total

def main():
    lst = [1,3,3,4,5,6]
    sum = add_number(lst)
    print(f"The sum of all number is {sum}")
    
  
 
main()