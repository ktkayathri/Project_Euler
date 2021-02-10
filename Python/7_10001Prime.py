# 10001 st Prime Number
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math

def isprime(num):
    flag = 0
    sq = math.ceil(math.sqrt(num))
    for i in range(2,sq+1):
        flag = 1
        if (num % i == 0):
            flag = 0
            break
    if (num==2):
        flag = 1
    
    if (flag == 1):
        return 1
    else:
        return 0


if __name__ == "__main__":
    count = 0
    num = 1
    while (count < 10001):
        num = num + 1
        ret = isprime(num)
        if (ret == 1):
            print (str(num) + " is Prime")
            count += 1
        
    print (str(count) + "st Prime number is " + str(num))
    