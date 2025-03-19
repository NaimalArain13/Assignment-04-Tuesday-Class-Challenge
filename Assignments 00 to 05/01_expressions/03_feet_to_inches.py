# Problem Statement
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

def main():
    Inches_In_Feet = 12
    
    feet = float(input("Enter number of feet: "))
    inches = feet * Inches_In_Feet
    print(f"That is {inches} inches")
    
main()