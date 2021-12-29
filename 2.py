# Find the sum of even Fibonacci numbers not exceeding 4 million

def next_fib(arr):
    arr.append(arr[-2]+arr[-1])


fib = [1, 2]

sum = 2
while fib[-2]+fib[-1] < 4000000:
    next_fib(fib)
    if fib[-1] % 2 == 0:
        sum += fib[-1]

print(sum)
