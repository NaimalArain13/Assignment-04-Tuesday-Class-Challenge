# Problem Statement
# In this program we show an example of using dictionaries to keep track of information in a phonebook.


def read_number():
    phonebook={}
    while True:
        name =input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        if number == "":
            break
        phonebook[name]=number
    return phonebook

def print_number(phonebook):
    for name in phonebook:
        print(f"{name} => {phonebook[name]}")
        
def lookup_number(phonebook):
    while True:
        name=input("Enter name: ")
        if name=="":
            break;
        if name not in phonebook:
            print(f"{name} is not in phonebook")
        else:
            print(phonebook[name])
def main():
   phonebook= read_number()
   print_number(phonebook)
   lookup_number(phonebook)
main()