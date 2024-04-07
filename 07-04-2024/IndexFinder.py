import math 
g = int(input("Enter grid size : "))
n = int(input("Enter number to be checked : "))
if(g*g>=n): 
    r = int(math.ceil(n/g))-1
    c = n-(r*g+1)
    print(f"{n} is in ({r},{c}) in {g} x {g} matrix")
else: print("Out of range!")
