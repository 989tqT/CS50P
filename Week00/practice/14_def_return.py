# functions returning a value (squaring a number)
def main():
    x = int(input("what's x? "))
    print("x squared is", square(x))


def square(n):
    return pow(n, 2)
    # return n ** 2
    # return n * n

main()