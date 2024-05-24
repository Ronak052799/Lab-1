import sys

def calculate_area(radius):
    # Area of a circle formula: πr^2
    pi = 3.14159
    return pi * (float(radius) ** 2)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python calculate_area.py <radius>")
        sys.exit(1)
    radius = sys.argv[1]
    result = calculate_area(radius)
    print(result)
