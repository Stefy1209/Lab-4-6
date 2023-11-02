import math
def create_cmp_number(rl_part, img_part):
    '''
    creates a complex number
    :param rl_part: float
    :param img_part: float
    :return: list
    '''
    return [rl_part, img_part]

def get_rl_part(cmp_number):
    '''
    gets the real part of a complex number
    :param cmp_number: list
    :return: float
    '''
    return cmp_number[0]

def get_img_part(cmp_number):
    '''
    gets the imaginary part of a complex number
    :param cmp_number: list
    :return: float
    '''
    return cmp_number[1]

def set_rl_part(cmp_number, value):
    '''
    change the real part of a complex number
    :param cmp_number: list
    :param value: float
    :return: -
    '''
    cmp_number[0] = value

def set_img_part(cmp_number, value):
    '''
    change the imaginary part of a complex number
    :param cmp_number: list
    :param value: float
    :return: -
    '''
    cmp_number[1] = value

def cmp_abs(cmp_number):
    '''
    finds the absolute value of a number
    :param cmp_number: list
    :return: float
    '''
    a = get_rl_part(cmp_number)
    b = get_img_part(cmp_number)
    return math.sqrt(a*a + b*b)

def x_is_prime(x):
    '''
    tests if x is prime
    :param x: int
    :return: bool
    '''
    if x < 2:
        return False

    if x == 2:
        return True

    if x % 2 == 0:
        return False

    d = 3
    while d*d <= x:
        if x % d == 0:
            return False
        d += 2

    return True