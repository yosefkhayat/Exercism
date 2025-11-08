def is_paired(input_string):
    queue = []
    brackets = {'}':'{',')':'(',']':'['}
    for charecter in input_string:
        if charecter in brackets.values():
            queue.append(charecter)
            continue
        if charecter in brackets.keys():
            if len(queue) == 0 or queue[-1] != brackets.get(charecter) :
                return False
            queue.pop()
    if len(queue) != 0: 
        return False
    return True
            