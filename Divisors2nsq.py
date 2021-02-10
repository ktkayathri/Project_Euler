

def finddivisor(num):
    count = 0
    num1 = 2 * (num**2)
    for i in range(1,num+1):
        if (num1 % i == 0):
            count = count + 1
            # print (i)
    # print ("Count is ", count)
    return count

if __name__ == "__main__":
    arg = 10**12
    sum = 15066
    for i in range(1001,arg+1):
        count = finddivisor(i)
        sum = sum + count
    print("Final count is ", sum)