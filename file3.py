#program to find the number of bits present in a number

#functions taking our number as input
def numberOfBits(n):

    #count variable set as 0
    count = 0

    #right shift the number till it becomes 0
    while (n):
        count += 1
        n >>= 1

    return count

number = int(input("enter your number :"))  
print("total bits : ",numberOfBits(number))
  