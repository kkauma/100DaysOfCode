import math

def paint_calc(height, width, cover):
    num_cans = math.ceil((height * width) / cover)
    print(f"You'll need {num_cans} cans of paint!")

test_h = int(input("Enter the height: "))
test_w = int(input("Enter the width: "))
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)