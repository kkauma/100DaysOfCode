import math

test_h = int(input("Enter the height: "))
test_w = int(input("Enter the width: "))
coverage = 5

def paint_calc(height, width):
    num_cans = math.ceil((height * width) / coverage)
    print(num_cans)

paint_calc(height=test_h, width=test_w)