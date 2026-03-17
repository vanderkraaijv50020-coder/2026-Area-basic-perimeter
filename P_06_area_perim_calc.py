# Ask the user for their width and height
# (assumer they put in the valid data)
width = float(input("Width: "))
height = float(input("Height:"))

# calculate the area / perimeter
area = width * height
perimeter = 2 * (width + height)

# Output the area and perimeter
print()
print(f"Perimeter: {perimeter} units")
print(f"Area: {area} square units")