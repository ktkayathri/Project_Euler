# def dectobinary(num):
#     global bin
#     if (num > 1):
#         dectobinary(num // 2)
#     # print (num % 2, end = '')

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

