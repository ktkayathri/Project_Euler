# # The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

def dectobinary(num):
    return bin(num).replace("0b", "") 

def ispalindrome(x):
    num = str(x)
    revnum = ''.join(reversed(num))

    if (num == revnum):
        return 1
    else:
        # print ("Not palindrome")
        return 0

if __name__ == "__main__":
    sum = 0
    for i in range(1,1000000):
        retval = ispalindrome(i)
        if (retval == 1):
            binary = dectobinary(i)
            if (ispalindrome(binary) == 1):
                print (i, " - Number is palindrome")
                print (binary, " also is palindrome")
                sum = sum + i
    print ("Final sum of palindromes is ", sum)

    # dectobinary(decimal)

