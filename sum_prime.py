def prime_checker(num):
    if num < 2:
        return False 
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True
    
def prime_list(num):
    lst = []
    for i in range(1, num+1):
        prime = prime_checker(i)
        if prime == True:
            lst.append(i)
    return lst

def is_a_prime_factor(num):
    factor_list = []
    lst = prime_list(num)
    for i in lst:
        if num % i == 0:
            factor_list.append(i)
    return factor_list
    
def prime_add(num):
    return sum(is_a_prime_factor(num))
