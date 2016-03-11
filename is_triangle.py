def is_triangle(a, b, c):
    if a > (b + c):
        print("No")
    elif b > (a + c):
        print("No")
    elif c > (a + b):
        print("No")
    else:
        print("Yes")

def three_sticks():
    s1 = int(input("please enter a stick length: "))
    s2 = int(input("please enter a second stick length: "))
    s3 = int(input("please enter a third stick length: "))
    is_triangle(s1, s2, s3)
    
