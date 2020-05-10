#WAP to rotate and image to 90 degrees.
#   [[1,2,3],
#    [4,5,6],
#    [7,8,9]]
#  THIS IMPLEMENTATION IS BY USING ANOTHER 2D ARRAY
#   WE ARE USING EXTRA SPACE HERE.
image = [[1,2,3],
        [4,5,6],
        [7,8,9]]
rotate_image = []
for i in image[::-1]:
    if rotate_image == []:
        for j in range(len(i)):
            rotate_image += [[i[j]]]
    else:
        for j in range(len(i)):
            rotate_image[j] += [i[j]]

print(rotate_image)
