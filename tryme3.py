#three_lines prints three blank lines
def three_lines():
    print('\n' * 3)

print("now printing 9 lines")

#nine_lines prints three_lines three times 
def nine_lines(line):
    print(line * 3)

# calling nine lines prints out nine blank lines
# I'm calling the function, even though this wasn't part of the assignment
nine_lines(three_lines)

#clear_screen prints out 25 blank lines
print("now printing 25 lines")
def clear_screen():
    print('\n' * 25)

#clear the screen
print(clear_screen())
