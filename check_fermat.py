def check_fermat():
    a = input("Enter value for 'a': ")
    b = input("Enter value for 'b': ")
    c = input("Enter value for 'c': ")
    n = input("Enter value for 'n': ")
    if n > 2 and (a^n + b^n == c^n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

check_fermat()
