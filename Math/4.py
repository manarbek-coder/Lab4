def parallelogram_area(base_length, height):
    return base_length * height

base_length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = parallelogram_area(base_length, height)

print("Area of the parallelogram:", area)
