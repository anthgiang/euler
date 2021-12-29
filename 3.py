# Find the largest prime factor of 600851475143

def factor(num):
    for i in range(2, num+1):
        if num % i == 0:
            return i


curr = 600851475143
largest = 0
while curr != 1:
    temp = factor(curr)
    if temp > largest:
        largest = temp
    curr = curr // temp

print(largest)
