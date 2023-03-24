import math

def solve_sine_law(side_a, angle_A, angle_B):
    angle_C = 180 - angle_A - angle_B
    side_b = (side_a * math.sin(math.radians(angle_B))) / math.sin(math.radians(angle_A))
    side_c = (side_a * math.sin(math.radians(angle_C))) / math.sin(math.radians(angle_A))
    return side_b, side_c
