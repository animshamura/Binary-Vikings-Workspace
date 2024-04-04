def Rectangle_Perimeter(l,w): return 2*(l+w)
def Rectangle_Area(l,w): return (l*w)

def Circle_Perimeter(r): return (2*3.1416*r)
def Circle_Area(r): return 3.1416*r**2

def Parallelogram_Perimeter(h,b): return 2*(h+b)
def Parallelogram_Area(h,b): return (h*b)

def Trapezoid_Perimeter(a,b,c,d): return a+b+c+d
def Trapezoid_Area(a,b,h): return 0.5*(a+b)*h

def Triangle_Perimeter(a,b,c): return a+b+c 
def Triangle_Area(b,h): return (b*h)/2

def Cylinder_Area(r,h): return (3.1416*r + 2*3.1416*r*h)
def Cylinder_Volume(r,h): return 3.1416*r*h

def Sphere_Area(r): return 4*3.1416*r**2
def Sphere_Volume(r,h): return (4*3.1416*r**3)/3

def Cone_Area(r,s): return (3.1416*r**2 + 3.1416*r*s)
def Cone_Volume(r,h): return (3.1416*r**2*h)/3

def SquareBasedPyramid_Area(b,s): return (b**2 + 0.5*b*s*4)
def SquareBasedPyramid_Volume(b,h): return (b**2*h)/3

def RectangularPrism_Area(l,w,h): return 2*(w*h + l*w + l*h)
def RectangularPrism_Volume(l,w,h): return l*w*h

def TriangularPrism_Area(a,b,c,l,h): return (a*h + b*h + c*h + b*l)
def TriangularPrism_Volume(b,h,l): return (b*h*l)/2


s = int(input("Enter\n1 for Rectangle\n2 for Circle\n3 for Parallelogram\n4 for Trapezoid\n5 for Triangle\n6 for Cylinder\n7 for Sphere\n8 for Cone\n9 for Squre based pyramid\n10 for Rectangular prism\n11 for Triangular prism\n"))
if(s==1): 
    l,w = map(int, input("Enter length and width : ").split())
    print(f"Perimeter of rectangle : {Rectangle_Perimeter(l,w)}")
    print(f"Area of rectangle : {Rectangle_Area(l,w)}")
elif(s==2): 
    r = int(input("Enter radius : "))
    print(f"Perimeter of circle : {Circle_Perimeter(r)}")
    print(f"Area of circle : {Circle_Area(r)}")
elif(s==3): 
    h,b = map(int, input("Enter height and base : ").split())
    print(f"Perimeter of parallelogram : {Parallelogram_Perimeter(h,b)}")
    print(f"Area of parallelogram : {Parallelogram_Area(h,b)}")
elif(s==4): 
    a,b,c,d = map(int, input("Enter 4 side lengths : ").split())
    a,h,b = map(int, input("Enter 2 Parallel side and hight : ").split())
    print(f"Perimeter of trapezoid : {Trapezoid_Perimeter(a,b,c,d)}")
    print(f"Area of trapezoid : {Trapezoid_Area(a,h,b)}")
elif(s==5): 
    a,b,c = map(int, input("Enter 3 side lengths : ").split())
    b,h = map(int, input("Enter ground and hight : ").split())
    print(f"Perimeter of triangle : {Triangle_Perimeter(a,b,c)}")
    print(f"Area of triangle : {Triangle_Area(b,h)}")
if(s==6): 
    r,h = map(int, input("Enter radius and hight : ").split())
    print(f"Area of cylinder : {Cylinder_Area(r,h)}")
    print(f"Volume of cylinder : {Cylinder_Volume(r,h)}")
if(s==7):
    r = map(int, input("Enter radius : ").split())
    r,h = map(int, input("Enter radius and hight : ").split())
    print(f"Area of sphere : {Sphere_Area(r)}")
    print(f"Volume of sphere : {Sphere_Volume(r,h)}")
if(s==8):
    r,s = map(int, input("Enter radius and side : ").split())
    r,h = map(int, input("Enter radius and hight : ").split())
    print(f"Area of cone : {Cone_Area(r,s)}")
    print(f"Volume of cone : {Cone_Volume(r,h)}")
if(s==10):
    b,s = map(int, input("Enter ground and mid of ground : ").split())
    b,h = map(int, input("Enter ground and hight : ").split())
    print(f"Area of Square-based pyramid : {SquareBasedPyramid_Area(b,s)}")
    print(f"Volume of Square-based pyramid : {SquareBasedPyramid_Volume(b,h)}")
if(s==10):
    l,w,h = map(int, input("Enter lenth, width and hight : ").split())
    print(f"Area of rectangular prism : {RectangularPrism_Area(l,w,h)}")
    print(f"Volume of rectangular prism : {RectangularPrism_Volume(l,w,h)}")
if(s==11):
    a,b,c,l,h = map(int, input("Enter 3 side of triangle, mid of triangle and hight : ").split())
    b,l,h = map(int, input("Enter ground of triangle, mid of triangle and hight : ").split())
    print(f"Area of triangular prism : {TriangularPrism_Area(a,b,c,l,h)}")
    print(f"Volume of triangular prism: {TriangularPrism_Volume(b,l,h)}")
