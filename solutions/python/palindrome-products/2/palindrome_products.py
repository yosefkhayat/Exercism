def check_palindrome(number):
    """Given a number return true if the number is palindrome and false otherwise 

    :param number: int
    :return: Bool
    """

    return str(number) == str(number)[::-1]

def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    factors_list = []
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    for x in range(max_factor ** 2, min_factor ** 2 - 1, -1):
        if check_palindrome(x):
            for y in range(min_factor, max_factor + 1):
                if x % y == 0 and min_factor <= x / y <= max_factor:
                    factors_list.append([y, int(x / y)])
        if factors_list:
            return x, factors_list
    return None, factors_list 
   

def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    factors_list = []
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    for x in range(min_factor ** 2, (max_factor+1) ** 2):
        if check_palindrome(x):
            for y in range(min_factor, max_factor + 1):
                if x % y == 0 and min_factor <= x / y <= max_factor:
                    factors_list.append([y, int(x / y)])
        if factors_list:
            return x, factors_list
    return None, factors_list
    