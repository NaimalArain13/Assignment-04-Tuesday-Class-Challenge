# Problem Statement
# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

def get_first_element(lst):
    if not lst:
        return "List must be non-empty"
    print(lst[0])
   
    
def main():
        lst = []
        try:
           length = int(input("How many element are there in your list? "))
           for _ in range(length):
            num = input("Enter an element: ")
            lst.append(num)
        except ValueError:
            print("Please enter a valid integer.")
            
        print(lst)
        get_first_element(lst)
        
        
main()

# Another solution:
'''
def get_first_element(lst):
    print(lst[0])
    
def get_lst():
    lst=[]
    element = input("Enter an element of the list or press enter to stop: ")
    while element != "":
        lst.append(element)
        element = input("Enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)
    
main()
'''