# 10001 st Prime Number
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import sys
sys.path.append("/Users/kayathriprabakaran/Desktop/Tools/Python/")
from utils.prime import gen_prime

if __name__ == "__main__":
   
    count = 0
    n = 1
    for n in gen_prime():
        count += 1
        if (count == 10001):
            break
    
    print ("10001st Prime number is  ", n)

    