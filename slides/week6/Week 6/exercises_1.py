# Function for exercise 1
def divisable_by_5(num):
    if num % 5 == 0:
        print("%d is divisable by 5." % num)
    else:
        print("%d is NOT divisable by 5." % num)

# Function for exercise 2 & 3
def is_prime(num, flag=0):
    if num > 1:
        square_num = int(num ** 0.5)
        for i in range(2, (square_num+1)):
            if (num % i) == 0:
                if flag == 0:
                    print('%d is NOT prime.' % num)
                    print("%d = %d * %d" % (num, i, num / i))
                    break
                else:
                    return 0
        else:
            if flag == 0:
                print("%d is prime." % num)
            else:
                return num
    else:
        print("The number should be greater than 1.")


if __name__ == "__main__":
    choice = int(input('Please select an excercise:(1, 2 or 3)'))
    print(choice)
    # exercise 1
    if choice == 1:
        num = int(input("Please input a number:"))
        divisable_by_5(num)
    # exercise 2
    elif choice == 2:
        num = int(input("Please input a number:(Should be greater than 1)"))
        is_prime(num)
    # exercise 3
    elif choice == 3:
        prime_elements = [0 for __ in range(100)]
        n = 0
        i = 2
        while n < 100:
            if is_prime(i, flag=1) == 0:
                i += 1
            else:
                prime_elements[n] = is_prime(i, flag=1)
                i += 1
                n += 1
        print("The first 100 prime numbers are:")
        print(prime_elements)
    else:
        print("Input the right exercise number.")
