#!/usr/bin/python3
import random
rand_int = random.randint(-3,3)
print(f"The number is {rand_int}",end=" ")
if rand_int > 0:
    print("positive")
elif rand_int == 0:
    print("zero")
else:
    print("negative")
