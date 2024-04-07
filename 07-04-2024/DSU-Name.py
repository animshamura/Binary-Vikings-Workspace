p = list(x for x in range(11))
name = ['Kenn','Bard','Muse','Seff','Matt','Jazz','Tart','Dew','Skar','Padd','Ross']
# Serial  0......1......2......3......4......5......6......7.....8......9......10     

def find(x):
    if(p[x]==x): return x
    else: 
        res = find(p[x])
        p[x] = res
        return res

def union(a,b):
    p[find(b)] = find(a)

def unifier(s,sub): 
    for j in sub: union(s,j)
    
def finder(s):
    print(f"{name[s]} owns : ",end="")
    for j in range(len(p)):
        if(p[j]==s): print(name[j],end=" ")
    print()
    
def show():
    print("Current State : ")
    for j in range(len(p)): print(f"{name[p[j]]} owns {name[j]}")
    print()

show()
while(True):
     q = int(input("Enter:\n1 to Change\n2 to Show\n3 to Exit\nEnter here: "))
     if(q==1):
         s = int(input("Enter source : "))
         sub = list(map(int, input("Enter subordinates list : ").split()))
         unifier(s,sub)
         show()
     elif(q==2):
         n = int(input("Enter:\n1 for whole list\n2 for subordinates\nEnter here : "))
         if(n==1): show()
         elif(n==2):
             s = int(input("Enter source : "))
             finder(s)
         else: print("Wrong Input!")
     elif(q==3): break
     else: print("Wrong Input!")  
     print()  
