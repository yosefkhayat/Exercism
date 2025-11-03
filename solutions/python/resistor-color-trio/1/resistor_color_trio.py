def label(colors):
    values = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    prefixes = {0:"ohms",3: "kiloohms",6:"megaohms",9:"gigaohms"}
    res = (values.index(colors[0])*10 + values.index(colors[1])) * (10 ** values.index(colors[2]))
    exponent = 0
    abs_number = abs(res)
    unit=""
    if res == 0:
        return f"0 ohms"
    while abs_number >= 1000 and exponent < 24:
        abs_number /= 1000
        exponent += 3
    while abs_number < 1 and exponent > -24:
        abs_number *= 1000
        exponent -= 3

    prefix = prefixes.get(exponent, "")
    return f"{int(abs_number)} {prefix}{unit}"