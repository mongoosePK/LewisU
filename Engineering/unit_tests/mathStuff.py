class Math:
    def is_prime(self, num):
        if num < 0:
            raise(ValueError())
        if num == 0:
            return False

        if num <=3:
            return True

        for i in range(2, num):
            if num % i == 0:
                return False

        return True

    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        return a/b

    def multiply(self, a, b):
        return a * b

    def power(self, a, b):
        '''calculates a ^ b'''
        prod = 1
        for i in range(abs(b)):
            prod *= a

        return prod

    def factorial(self, n):
        '''calculates n! = 1 * 2 * 3 * ... * n'''
        prod = 1
        for i in range(1, n):
            prod *= i

        return prod


    def is_even(self, a):
        return a // 2 == 0


    def sub_and_print(self, a, b):
        print('result is : {}'.format(a-b))

