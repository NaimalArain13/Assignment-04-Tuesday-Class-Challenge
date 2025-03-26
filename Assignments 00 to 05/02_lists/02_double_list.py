# Problem Statement
# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

def double_number(lst):
    double_numbered = []
    for num in lst:
        num+=num
        double_numbered.append(num)
    return double_numbered

def main():
    lst = [2,3,1,4,5]  
    double = double_number(lst)
    print(double)
    

main()