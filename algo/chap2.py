# recursion
#
# to understand recursion, we will look at finding the factorial of a given number
# 5! = 5 * 4 * 3 * 2 * 1

# the function, factorial, takes in a given number to use in the calculation
def factorial(n):
    the_product = 1
    # inside the function, we define a variable product and set it to one.
    # we will use this variable to keep track of the product, by multiplying
    # n by the numbers preceding it. The while loop iterates backward while
    # keeping track of the product
    while n > 0:
        the_product *= n
        n = n - 1
    return the_product

# let's do this recursively now
def recurse_factorial(n):
    # The function accepts a number as a parameter. Next comes the base case.
    # The function will call itself repeatedly until n is 0, at which point
    # it will return 1 and will stop calling itself.
    if n == 0:
        return 1
    # Whenever the base case is not satisfied, this line of code executes:
    return n * recurse_factorial(n - 1)
    # python puts this recursive function in a stack, as it does not yet know
    # the result of the function. Once the base case is met in one of the function
    # calls, the whole thing is ran.
    #
    # recurse_factorial(3)
    # return [n * recurse_factorial(n - 1) return n * recurse_factorial( n - 1....

# challenge
# print 1 - 10 recursively

def print_range(n):
    if n > 0:
        print_range(n - 1)
        print(n, " ")

print_range(26)
