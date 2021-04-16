# Largest palindrome product
#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#

def palindrome(num):
    temp = str(num)
    for i in range(1, len(temp)//2+1):
        if temp[i-1] != temp[-i]:
            return False
    return True


def main():
    largest = 0
    for i in range(100, 1000, 1):
        for j in range(100, 1000, 1):
            if palindrome(i*j) and i*j > largest:
                largest = i*j
                print(i, j, i*j)


main()
