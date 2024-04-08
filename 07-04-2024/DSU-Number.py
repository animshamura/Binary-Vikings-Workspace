p=list(x for x in range(1,21))
def find(x):
	if(p[x]==x): return x
	else:
      res = find(p[x])
      p[x] = res
      return res

def union(a, b):
	  p[find(b)] = find(a)
	
def unifier(src, sub): 
     for s in sub: union(src,s)

def finder(src):
	print("Subordinates under source (src): ")
	for j in range(len(p)):
		if(p[j]==src): print(j,end="")
		print()

print(f"Initial state: {p}")
while(True):
	print("Enter :\n1 to change subordinates\n2 to see subordinates\n3 to exit")
	c = int(input("Enter here: "))
	if(c==1 ):
		s = int(input("Enter source: "))
		sub = list(map(int, input("Enter subordinates list: ").split()))
		unifier(s,sub)
		print(f"After change: {p}")
	elif(c==2):
    	s1 = int(input("Enter source: "))
    	finder (s1)
    elif(c==3): break
    else: print("Wrong Input!")
