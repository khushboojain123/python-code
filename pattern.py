# Function to demonstrate printing pattern
def pyramid(n):
    #outer loop to handle no. of rows
    for i in range (0,n):

    #inner loop to handle no. of columns

        for j in range (0,i+1):

         print("*",end='')