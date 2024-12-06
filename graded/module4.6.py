import random

points = int(input("Enter the number of random points to generate: "))

count = 0
inside_A = 0

while count < points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        inside_A += 1
    count += 1

estimatePi = 4 * inside_A / points
print (f"PI is approximately {estimatePi}")