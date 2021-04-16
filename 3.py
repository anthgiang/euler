# Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?
#


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
