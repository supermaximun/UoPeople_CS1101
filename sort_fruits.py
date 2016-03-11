## reads in the fruits from the file unsorted_fruits.txt
infile = open("unsorted_fruits.txt", "r")
## writes fruits out in alphabetical order to a file named sorted_fruits.txt.
outfile=open("sorted_fruits.txt","w")
fruit=infile.read(50)

lst = list()
def make_list():
    for line in fruit:
        line.strip()
        lst.append(line)
        lst.sort()
print("printing list", lst)
make_list()

def print_list():
    for item in lst:
        print(item + '\n')

print_list()


outfile.write(fruit)
print (fruit)
infile.close()
outfile.close()

