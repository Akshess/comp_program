# functions
def prime_func(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")

    else:
        print(num, "is not a prime number")


# User defined function to find square root
def sqrt(n):
    return n ** 0.5


def square_func(num):
    root = sqrt(num)
    if int(root) ** 2 == number:
        print(number, "is a perfect square")
    else:
        print(number, "is not a perfect square")


# User defined function for cube root
def curt_func(n):
    return n ** (1 / 3)


def cube_func(num):
    cube_1 = curt_func(num)
    if cube_1 * cube_1 * cube_1 == num:
        print(number, " is a perfect cube number")
        return
    else:
        print(number, 'is not a perfect cube number')
        return


def fact_func(num):
    fact = 1
    if num < 0:
        print("Factorial doesn't exist for negative number")
    elif num == 0:
        print('factorial of zero is one')
    else:
        for i in range(1, num + 1):
            fact = fact * i
        print('The factorial of', num, "is", fact)
        # return n * fact_func(n - 1)


def pal_func(num):
    reverse = 0
    if num >= 10:
        while num > 0:
            rem = num % 10
            reverse = (reverse * 10) + rem
            num = num // 10
        if number == reverse:
            print("%d is a Palindrome Number" % number)
        else:
            print("%d is not a Palindrome Number" % number)
    else:
        print("Not a palindrome.Enter 2+ digit number ")


def neon_func(num):
    sqr = num * num
    sumOfDigit = 0
    while sqr > 0:
        sumOfDigit = sumOfDigit + sqr % 10
        sqr = sqr // 10
    if num == sumOfDigit:
        return print("It is a neon number")
    else:
        return print("It is not a neon number")


def fib_func(num):
    print("calculating fibonacci series......")
    a, b = 0, 1
    while a < num:
        print(a, end=' ')
        a, b = b, a + b
    print()


def armstrong_func(num):
    sum_1 = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_1 += digit ** 3
        temp //= 10
    if number == sum_1:
        print(number, "is an Armstrong number")
    else:
        print(number, "is not an Armstrong number")


def di_func(num):
    dig = len(str(num))
    temp = num
    sum_1 = 0
    while temp > 0:
        du = temp % 10
        sum_1 += (du ** dig)
        temp = temp // 10
        dig = dig - 1
    if sum_1 == num:
        print("It is Disarium number")
    else:
        print("It is not a Disarium number")


def hd_func(num):
    total = 0

    while num > 0:
        total = total + num % 10
        num //= 10

    if number % total == 0:
        print(number, "is harshad number")
    else:
        print(number, "is not a harshad number")


# List containing text and function
choices = [
    {
        "text": "0.Prime number",
        "func": prime_func
    },
    {
        "text": "1.Square number",
        "func": square_func
    },
    {
        "text": "2.Cube number",
        "func": cube_func
    },
    {
        "text": "3.Factorial ",
        "func": fact_func
    },
    {
        "text": "4.Palindrome number ",
        "func": pal_func
    },
    {
        "text": "5.Neon number",
        "func": neon_func
    },
    {
        "text": "6.Fibonacci series",
        "func": fib_func
    },
    {
        "text": "7.Armstrong number",
        "func": armstrong_func
    },
    {
        "text": "8.Disarium number",
        "func": di_func
    },
    {
        "text": "9.Harshad number",
        "func": hd_func
    },
    {
        "text": "Enter the choice index within range(0-9)"
    }
]
# print(choices["one"]["func"]())
# print(choices["two"]["func"]())
# print(choices.keys())
number = int(input("ENTER THE NUMBER : "))
# print(number)
for item in choices:
    print(item["text"])
your_choice = int(input("ENTER YOUR CHOICE:"))
# print(your_choice)
your = choices[your_choice]
var1 = your["func"]
var1(number)
