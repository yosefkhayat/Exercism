def square_root(number):
    if number == 1 : 
        return 1
    high = number 
    low = 0
    res = int(number/2)
    while(res ** 2 != number):
        if (res ** 2)>number:
            high = res
            res = int((high+low)/2)
            continue
        low = res
        res = int((high+low)/2)
    return res