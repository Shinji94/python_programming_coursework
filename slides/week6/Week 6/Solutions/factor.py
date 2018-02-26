## Printout the factors of a number
## By Leandro Soriano Marcolino
## "Optimized" for clarity. This is not the most efficient implementation
## If you find any bugs, let me know :)

## First I will use a function to let me know whether a number is prime or not
def isPrime(n):
    
    ## Try to find a divisor. If I find one, it is not prime
    ## Again, not the best solution. I don't really need to check all the way to n-1.
    for m in range(2,n):
        if (n % m == 0):
            return False

    ## If I reach here, it is because I could not find any divisor
    return True


def printFactors(n):
    
    ## A simple solution. Again, not the most efficient way.
    ## I will go through all numbers until n - 1.
    for m in range(2,n):
        
        ## Test if m divides n
        if (n % m == 0):

            ## If I am here, I know that m is a divisor. However,
            ## I must still check if it is prime
            if (isPrime(m)):
                print(m)

## I will hard-code the tests of the handout

print("Factors of 8:")
printFactors(8)

print("Factors of 12:")
printFactors(12)

print("Factors of 28:")
printFactors(28)

print("Factors of 818:")
printFactors(818)


