prime_elements = [0] * 100
n = 0
i = 2
while n < 100:
    square_num = int(i ** 0.5)
    for j in range(2, (square_num+1)):
        if (i % j) == 0:
            i = i + 1
            break
    else:
        prime_elements[n] = i
        i = i + 1
        n = n + 1 
print("The first 100 prime numbers are:")
print(prime_elements)
