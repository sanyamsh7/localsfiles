#WAP TO ROTATE AN IMAGE 90 DEGREES WITHOUT USING AN EXTRA SPACE.
# # [[1,2,3],
#    [4,5,6],
#    [7,8,9]]

image = [[1,2,3],
        [4,5,6],
        [7,8,9]]
N = len(image)

#tranpose a matrix
for r in range(N):
    for c in range(r, N):
        temp = image[r][c]
        image[r][c] = image[c][r]
        image[c][r] = temp
        #or simply: image[r][c], image[c][r] = image[c][r], image[r][c]

#flip the matrix horizontally
#setting two pointers at beginning and end of each row
for r in range(N):
    for c in range(N//2):
        temp = image[r][c]
        image[r][c] = image[r][N-1-c]
        image[r][N-1-c] = temp
#now the image is rotated to 90 degrees
print(image)
