values = ["black", "brown", "red", "orange", "yellow",
          "green", "blue", "violet", "grey", "white"]
prefixes = {0: "ohms", 3: "kiloohms", 6: "megaohms", 9: "gigaohms"}


def convert_float_to_int_if_whole(number):
    if isinstance(number, float) and number == int(number):
        return int(number)
    else:
        return number


def calculate_ohms(colors):
    res = 0
    for color in colors:
        res = (res * 10) + values.index(color)
    return res


def convert_ohms(number):
    exponent = 0
    abs_number = abs(number)
    unit = ""
    if number == 0:
        return f"0 ohms"
    while abs_number >= 1000 and exponent < 24:
        abs_number /= 1000
        exponent += 3
    while abs_number < 1 and exponent > -24:
        abs_number *= 1000
        exponent -= 3
    prefix = prefixes.get(exponent, "")
    return f"{convert_float_to_int_if_whole(abs_number)} {prefix}{unit}"


def resistor_label(colors):
    tolarance_values = {"grey": 0.05, "violet": 0.1, "blue": 0.25,
                        "green": 0.5, "brown": 1, "red": 2, "gold": 5, "silver": 10}
    if len(colors) == 1:
        return convert_ohms(calculate_ohms(colors))
    result = calculate_ohms(colors[:-2]) * (10 ** values.index(colors[-2]))
    result = convert_ohms(result)
    tolarance = tolarance_values.get(colors[-1])
    return f"{result} ±{tolarance}%"
