def prime_checker(num):
    if num < 2:
        return False 
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True
