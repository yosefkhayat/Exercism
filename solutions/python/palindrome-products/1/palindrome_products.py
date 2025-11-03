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
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    all_factors = tuple((0, []))
    for index in range(min_factor, max_factor+1):
        for index1 in range(index, max_factor+1):
            temp = index*index1
            if check_palindrome(temp):
                if temp == all_factors[0]:
                    all_factors[1].append([index, index1])
                elif temp > all_factors[0]:
                    all_factors = tuple((temp, [[index, index1]]))
    if all_factors[1] == []:
        return [None, []]
    return all_factors


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """

    if min_factor >= max_factor:
        raise ValueError("min must be <= max")
    all_factors = tuple((max_factor*max_factor, []))
    for index in range(min_factor, max_factor+1):
        for index1 in range(index, max_factor+1):
            temp = index*index1
            if check_palindrome(temp):
                if temp == all_factors[0]:
                    all_factors[1].append([index, index1])
                elif temp < all_factors[0]:
                    all_factors = tuple((temp, [[index, index1]]))
    if all_factors[1] == []:
        return [None, []]
    return all_factors
