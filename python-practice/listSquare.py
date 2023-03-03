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
