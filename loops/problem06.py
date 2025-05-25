# prime number checker

is_prime = True
number =20
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break
    print(is_prime)
