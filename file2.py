# returns true if n is even, else odd
def isEvenOdd(n) :
    #XOR with 1 equal n+1
    if (n ^ 1 == n+1) :
        return True;
    else :
        return False;

number = int(input("enter your number :"))

if