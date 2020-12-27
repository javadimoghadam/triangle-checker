from os import system
from colorama import Fore
from time import sleep as s

# Define for Check Triangle
# Param
# Side1 = First side of Triangle
# Side2 = Second side of Triangle
# Side1 = Third side of Triangle
#
def IsTriangleOK(side1:int,side2:int,side3:int):
    a = side1
    b = side2
    c = side3
    # Check Triangle Side 
    if b>(a/2) and c>(a/2):
        # Check Can create Triangle ?
        if (b+c)>a and (a+b)>c and (a+c)>b:
            # Yes ! , Sides a,b,c Can Creste a Triangle
            return True
        else:
            # No ! , Can't Create Triangle with Sides a,b,c
            return False    
    else:
        # No ! , Can't Create Triangle with Sides a,b,c
        return False

# Start A Software
if __name__ == "__main__":
    while True:
        # Set Deafult data
        system("title Triangle Checker - Side 1")
        system('mode con: cols=50 lines=20')
        system("clear")
        try:
            # Get Sides
            a = int(input(Fore.CYAN + "side 1 => "))
            system("title Triangle Checker - Side 2")
            b = int(input("side 2 => "))
            system("title Triangle Checker - Side 3")
            c = int(input("side 3 => "))
            # Check Side not Empty
            if (a and b and c) != "":
                # Check Triangle With Define IsTriangaleOK() with Parameter a,b,c
                if(IsTriangleOK(a,b,c)):
                    # True
                    system("title Triangle Checker - True")
                    print(Fore.GREEN + "===================================")
                    print(str("You Can Create a Triangle with this Side"))
                    print("===================================" + Fore.RESET)
                    s(2)
                else:
                    system("title Triangle Checker - False")
                    print(Fore.RED + "===================================")
                    # False
                    print("You Can't Create a Triangle with this Side" )
                    print("===================================" + + Fore.RESET)
                    s(2)
        except ValueError as V:
            system("title Triangle Checker - Int Error")
            s(.5)
            print(Fore.RED + "Please Enter Valid Number ." + Fore.RESET)
            s(1)
        except KeyboardInterrupt as ki:
            system("clear")
            system('mode con: cols=20 lines=3')
            print()
            print(str(Fore.GREEN + "      GoodBye !"))
            s(.6)
            exit()

            
        
