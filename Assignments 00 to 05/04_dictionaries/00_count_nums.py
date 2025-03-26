# Problem Statement
# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):
# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.

def get_num_lst():
    num_lst=[]
    while True:
        num = input("Enter a number: ")
        if(num==""):
            break
        num=int(num)
        num_lst.append(num)
    return num_lst



def count_num(num_list):
    num_dict={}
    for num in num_list:
        if num not in num_dict:
            num_dict[num]=1
        else:
            num_dict[num] += 1
    return num_dict

def print_count(num_dict):
    for num in num_dict:
        print(f"{str(num)} appears {str(num_dict[num])} times")

def main():
    lst = get_num_lst()
    count = count_num(lst)
    print_count(count)
    
main()