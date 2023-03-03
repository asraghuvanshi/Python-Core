#program to calculate square of list items

square = 0
squares = []
def findSquare(list):
    for i in list:
        square = i**2
        squares.append(square)
    print(squares)

list = [5, 6, 7, 8 , 9 ,10]
p = findSquare(list)

string = "Welcome to the world of python"
counter = 0
print(len(string))
for i in range(0 , len(string)):
    if string[i] == 'o':
        counter += 1
print(counter)

