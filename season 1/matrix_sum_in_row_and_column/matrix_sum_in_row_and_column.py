#global variables and imports
matrix = []


#get matrix from user
def get_matrix():
    global matrix
    for i in range(3):
        while True:
            row = list(map(int, input("please enter 3 digits like(1 2 3),be aware about space between your numbers!!: ").split()))
            if len(row) == 3:
                matrix.append(row)
                break
            else:
                print("Please enter exactly 3 numbers!")
    return matrix

#sum in rows of matrix:
def sum_rows(matrix):
    for i in range(3):
        print(f"sum of row {i+1} is :  {sum(matrix[i])}") 

#sum in columns of matrix:
def sum_columns(matrix):
    for i in range(3):
        total = 0
        for j in range(3):
            total += matrix[j][i]
        print(f"sum of column {i+1} is: {total}")


#run the app
get_matrix()
sum_rows(matrix)
sum_columns(matrix)