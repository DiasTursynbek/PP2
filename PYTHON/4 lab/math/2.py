def trapezoid_area(height, base1, base2):
    return 0.5 * (base1 + base2) * height

height = 5
base1 = 5
base2 = 6
print(f"\nHeight: {height}")
print(f"Base, first value: {base1}")
print(f"Base, second value: {base2}")
print(f"Expected Output: {trapezoid_area(height, base1, base2)}")