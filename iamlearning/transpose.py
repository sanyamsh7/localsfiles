#WAP to transpose a matrix
# # [[1,2,3],
#    [4,5,6],
#    [7,8,9]]

image = [[1,2,3],
        [4,5,6],
        [7,8,9]]
rows = len(image)
columns = len(image[0])
new_matrix = [[0,0,0],[0,0,0],[0,0,0]]

for r in range(rows):
    for c in range(columns):
        new_matrix[c][r] = image[r][c]

print(new_matrix)
