def find_factors(number):
    factors = [1]
    i = 2
    while i * i <= number:
        if number % i == 0:
            factors.append(i)
            if i * i != number:  # Avoid adding the same factor twice for perfect squares
                factors.append(number// i)
        i += 1
    return factors

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number<=0:
        raise ValueError("Classification is only possible for positive integers.")
    sum_factors = sum(find_factors(number))
    print(sum_factors ,find_factors(number), number)
    if number == 1 :
        return "deficient"
    if sum_factors == number:
        return "perfect"
    if sum_factors < number:
        return "deficient"
    return "abundant"
