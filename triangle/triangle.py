def valid(sides):
    a, b, c = sorted(sides)
    return a + b > c and all(side > 0 for side in sides)


def equilateral(sides):
    return sides[0] == sides[1] == sides[2] and valid(sides)


def isosceles(sides):
    return not scalene(sides) and valid(sides)


def scalene(sides):
    return sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2] and valid(sides)
