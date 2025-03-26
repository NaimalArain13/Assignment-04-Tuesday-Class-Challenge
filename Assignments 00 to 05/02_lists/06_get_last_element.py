# Problem Statement
# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_first_element(lst):
    if not lst:
        return "List must be non-empty"
    print(lst[-1])
   
    
def main():
        lst = []
        try:
           length = int(input("How many element are there in your list? "))
           if length == 0:
               print("Your list is empty")
           for _ in range(length):
            num = input("Enter an element: ")
            lst.append(num)
        except ValueError:
            print("Please enter a valid integer.")
            
        print(lst)
        get_first_element(lst)
        
        
main()