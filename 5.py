# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def lcm(a, b):
    if a > b:
        larger = a
        smallr = b
    else:
        larger = b
        smallr = a

    i = 1
    while larger*i % smallr != 0:
        i += 1

    return (larger*i)


best = lcm(1, 2)
for i in range(3, 20+1):
    best = lcm(best, i)

print(best)
