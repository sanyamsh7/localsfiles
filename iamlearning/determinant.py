#finding determinant of a matrix

def matrix(a,b):
    row = []
    
    for i in range(a):
        row.extend(input().split())
        
    if len(row) == a*b:
        return row
    else:
        print("Enter the matrix again.")
        return matrix(a,b)
    

dimension = input("Enter the dimensions of the matrix in the form axb: ") #axb

print(matrix(int(dimension[0]), int(dimension[2])))
    
        
    
