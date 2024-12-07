def area(name):
    name = name.lower()
    pie = 3.1415926
    if (name == 'rectangle'):
        l = int(input("Enter the length of the rectange: "))
        b = int(input("Enter the breadth of the rectange: "))
        a = l * b
        print("Area of the rectangle is ", a)
    elif (name == 'square'):
        s = int(input("Enter the side of the square: "))
        a = s*s
        print("Area of the square is ", a)
    elif (name == 'circle'):
        r = int(input("Enter the radius of the circle: "))
        a = pie * r**2
        print("Area of the circle is ", a)
    elif (name == 'cone'):
        r = int(input("Enter the radius of the cone: "))
        h = int(input("Enter the height of the cone: "))
        a = 1/3 * (pie * r**2 * h)
        print("Area of the cone is ", a)
    elif (name == 'cylinder'):
        r = int(input("Enter the radius of the cylinder: "))
        h = int(input("Enter the height of the cylinder: "))
        a = pie * r**2 * h
        print("Area of the cylinder is ", a)
    elif (name == 'sphere'):
        r = int(input("Enter the radius of the cylinder: "))
        a = 4 * pie * r**2
        print("Area of the sphere is ", a)
    else:
        print("Shape is currently not available")

print("Shape Area Calculator")
while(1):
    shape = input("Enter the name of the shape: ")
    area(shape)
    for i in range(101):
'''if (i <= 100):
    print('out of loop', i)
    i += 1'''
