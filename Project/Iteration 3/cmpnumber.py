import math

def create_complex_number(realPart, imaginaryPart):
    '''
    creates a complex number
    :param realPart: float
    :param imaginaryPart: float
    :return: dictionary
    '''
    return {"real part": realPart, "imaginary part": imaginaryPart}

def get_real_part(cmpNumber):
    '''
    gets the real part of a complex number
    :param cmpNumber: dictionary
    :return: float
    '''
    return cmpNumber["real part"]

def get_imaginary_part(cmpNumber):
    '''
    gets the imaginary part of a complex number
    :param cmpNumber: dictionary
    :return: float
    '''
    return cmpNumber["imaginary part"]

def set_real_part(cmpNumber, value):
    '''
    sets the real part of a complex number with a value
    :param cmpNumber: dictionary
    :param value: float
    :return: -
    '''
    cmpNumber["real part"] = value

def set_imaginary_part(cmpNumber, value):
    '''
    sets the imaginary part of a complex number with a value
    :param cmpNumber: dictionary
    :param value: float
    :return: -
    '''
    cmpNumber["imaginary part"] = value

def get_abs_value(cmpNumber):
    '''
    gets the absolute value of a complex number
    :param cmpNumber: dictionary
    :return: float
    '''
    x = get_real_part(cmpNumber) ** 2
    y = get_imaginary_part(cmpNumber) ** 2
    abs = math.sqrt(x + y)
    return round(abs, 3)

def is_less(cmpNumber, value):
    '''
    checks if the absolute value of a complex number is less than a value
    :param cmpNumber:
    :param value:
    :return:
    '''
    x = get_abs_value(cmpNumber)
    return x < value and not is_equal(cmpNumber, value)

def is_equal(cmpNumber, value):
    '''
    checks if the absolute value of a complex number is equal to a value
    :param cmpNumber: dictionary
    :param value: float
    :return: bool
    '''
    x = get_abs_value(cmpNumber)
    return abs(x - value) < 0.0001

def is_greater(cmpNumber, value):
    '''
    checks if the absolute value of a complex number is greater than a value
    :param cmpNumber: dictionary
    :param value: float
    :return: bool
    '''
    x = get_abs_value(cmpNumber)
    return x > value and not is_equal(cmpNumber, value)
