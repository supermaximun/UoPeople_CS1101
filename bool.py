#prompt user for integer inputs, alpha and beta
alpha = input("Please enter a number:  ")
beta = input("Please enter a second number:  ")

# compare function compares the values of two numbers
def compare(a, b):
# if a > b, then return 1
    if a > b:
        return 1
# else if a == b, then return 0
    elif a == b:
        return 0
# else if a < b, then return -1
    else:
        return -1

# print out the result of the user's compare function
print('Result: ', compare(alpha, beta))

# print out the results of every possible condition
print('Testing a > b:', compare(5, 2))
print('Testing a < b:',compare(2, 5))
print('Testing a == b:',compare(3, 3))
