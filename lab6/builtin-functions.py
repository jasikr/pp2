#ex1
numbers = [1, 2, 3, 4]
print(numbers[0] * (sum(numbers[1:])+1))

#ex2
some_string = "CRistianoRonaldo"
upper = sum(map(lambda x : x.isupper(), some_string))
lower = sum(map(lambda x : x.islower(), some_string))
print(upper, lower)

#ex3
string_input = input()
print(string_input == string_input[::-1])

#ex4
import time
import math
num = int(input("Sample input: "))
ms = int(input("ms: "))
time.sleep(ms / 1000)
print(f"Square root of {num} after {ms} milliseconds is {math.sqrt(num)}")

#ex5
tuple1 = [True, 3 ,343, True]
tuple2 = [True, 3 ,343, True, 0]
print(all(tuple1))
print(all(tuple2))

