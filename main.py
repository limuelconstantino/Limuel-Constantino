def get_length():
    return float(input("Enter the length of the triangle: "))

def get_width():
    return float(input("Enter the width of the triangle: "))

def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

def main():
    length = get_length()
    width = get_width()
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)

    print(f"The area of the triangle is {area} square units.")
    print(f"The perimeter of the triangle is {perimeter} units.")

    if length == width:
        print("The triangle is a square.")
    else:
        print("The triangle is not a square.")
        
    if length > width:
        print("The triangle is longer than it is wide.")
    elif length < width:
        print("The triangle is wider than it is long.")
    else:
        print("The triangle is a square with equal length and width.")
main()