#ex1
import math
degree = int(input())
print(math.radians(degree))

#ex2
import math
height, base1, base2 = int(input()), int(input()), int(input())
Area = 1/2 * height * (base1 + base2)
print(Area)

#ex3
import math
number_of_sides, length_of_side = int(input()), int(input())
Area = number_of_sides * length_of_side**2 / (4 * math.tan(math.radians(180 / number_of_sides)))
print(Area)

#ex4
import math
base, height = int(input()), int(input())
print(float(base * height))