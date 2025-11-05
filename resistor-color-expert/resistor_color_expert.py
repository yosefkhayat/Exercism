def resistor_label(colors):
    values = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    tolarance_values = {"grey" : 0.05, "violet" : 0.1, "blue" : 0.25, "green" : 0.5, "brown" : 1, "red" : 2, "gold" : 5, "silver" : 10}
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
    tolarance = tolarance_values.get(colors[4])
    print(colors[4])
    return f"{int(abs_number)} {prefix}{unit} ±{tolarance}%"