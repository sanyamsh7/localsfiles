# Write a Python function that accpets a hyphen-seperated sequence of colors
# as input and returns the colors in a hyphen-separated sequence after sorting them
# alphabetically.
#
# constraint: all the colors will be completely in either lower case or upper case

def sort_colors(list_of_colors):
    list_of_colors.sort()
    return "-".join(list_of_colors)

colors = input("enter colors(hyphen separated): ").split("-")
colors = sort_colors(colors)
print(colors)
