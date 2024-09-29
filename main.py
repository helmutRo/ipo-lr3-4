import math
print ("Введите x:", end = " ")
x = float(input()) #запришивается x
if x < 0:
    result = x ** 2
    print(f"{x} = {result}")
else:
    result = math.sqrt(x)
    print(f"{x} = {result}")