num = int(input("Please input a number:(Should be greater than 1)"))

square_num = int(num ** 0.5)
for i in range(2, (square_num+1)):
    if (num % i) == 0:
        print('%d is NOT prime.' % num)
        print("%d = %d * %d" % (num, i, num / i))
        break
else:
    print("%d is prime." % num)
