# creating 2d list
x = [[1,2,3,0], [4,5,6,0], [7,8,9,0]]

print (x)

# no of rows
print (len(x))

# no of columns
print (len(x[0]))

# accessing element in 2d list
print ("The 2nd element of 3rd row : ",x[1][1])

# looping through values in 2d list
for i in range (0, len(x)):
    for j in range (0, len(x[0])) :
        print (x[i][j], end = " ")
    print ("\n")

# take an input for a matrix and print the elements
row = int(input ("Enter no. of rows = "))
col = int(input ("Enter no. of columns = "))
x = []
for i in range (row):
    temp = []
    for j in range (col):
        el = int (input ("Enter your element : "))
        temp.append (el)
    x.append (temp)
print (x)   
