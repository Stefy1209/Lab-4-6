import math

import cmpnumber

def add_number_to_list_position(number, list, position):
    '''
    insert a number in a list at a given position
    :param number: almost everything
    :param list: list
    :param position: int
    :return: -
    '''
    list.insert(position, number)

def eliminate_from_list(list, start, end):
    '''
    elimibates from the list the numbers between start and end
    :param list: list
    :param start: int
    :param end: int
    :return: -
    '''
    n = end - start + 1
    for i in range(n):
        list.remove(list[start])

def replace_number1_with_number2_list(number1, number2, list):
    '''
    replace the number 1 from list with number 2
    :param number1: dictionary
    :param number2: dictionary
    :param list: list
    :return: -
    '''
    for i in list:
        realPart_i = cmpnumber.get_real_part(i)
        imaginaryPart_i = cmpnumber.get_imaginary_part(i)

        realPart1 = cmpnumber.get_real_part(number1)
        imaginaryPart1 =cmpnumber.get_imaginary_part(number1)

        realPart2 = cmpnumber.get_real_part(number2)
        imaginaryPart2 = cmpnumber.get_imaginary_part(number2)

        if realPart_i == realPart1 and imaginaryPart_i == imaginaryPart1:
            cmpnumber.set_real_part(i, realPart2)
            cmpnumber.set_imaginary_part(i, imaginaryPart2)

def get_imaginary_parts(list, start, end):
    '''
    gets the imagianry part of the numbers form start to end from the list
    :param list: list
    :param start: int
    :param end: int
    :return: list
    '''
    newList = []

    for i in range(start, end+1):
        imaginaryPart = cmpnumber.get_imaginary_part(list[i])
        newList.append(imaginaryPart)

    return newList

def get_less(list):
    '''
    gets the numbers from the list that the absolute value is less than 10
    :param list: list
    :return: list
    '''
    newList = []

    for i in list:
        if cmpnumber.is_less(i, 10):
            newList.append(i)

    return newList

def get_equal(list):
    '''
    gets the numbers from the list that the absolute value is equal to 10
    :param list: list
    :return: list
    '''
    newList = []

    for i in list:
        if cmpnumber.is_equal(i, 10):
            newList.append(i)

    return newList

def get_sum_subsequence(list, start, end):
    '''
    gets the sum of the numbers from start to end
    :param list: list
    :param start: start
    :param end: end
    :return: dictionary
    '''
    sum = cmpnumber.create_complex_number(0, 0)

    for i in range(start, end+1):
        a = cmpnumber.get_real_part(sum)
        b = cmpnumber.get_imaginary_part(sum)

        a += cmpnumber.get_real_part(list [i])
        b += cmpnumber.get_imaginary_part(list [i])

        cmpnumber.set_real_part(sum, a)
        cmpnumber.set_imaginary_part(sum, b)

    return sum

def get_product_subsequence(list, start, end):
    '''
    gets the product of the numbers from start to end
    :param list: list
    :param start: int
    :param end: int
    :return: dictionary
    '''
    product = cmpnumber.create_complex_number(1, 0)

    for i in range(start, end+1):
        a = cmpnumber.get_real_part(product)
        b = cmpnumber.get_imaginary_part(product)

        c = cmpnumber.get_real_part(list [i])
        d = cmpnumber.get_imaginary_part(list [i])

        cmpnumber.set_real_part(product, a*c - b*d)
        cmpnumber.set_imaginary_part(product, b*d + a*d)

    return product

def sort_descent_imaginary(list):
    '''
    sort list descent by imaginary part
    :param list: list
    :return: list
    '''
    newList = []
    for number in list:
        newList.append(cmpnumber.get_imaginary_part(number))

    length = len(list)
    for i in range(length - 1):
        max = newList[i]
        Pmax = i

        for j in range(i+1, length):
            item = newList[j]

            if item > max:
                max = item
                Pmax = j

        newList[i], newList[Pmax] = newList[Pmax], newList[i]
        list[i], list[Pmax] = list[Pmax], list[i]

    return list

def is_prime(a):
    '''
    verifies if a is prime
    :param a: float
    :return: bool
    '''
    if a - math.floor(a) != 0:
        return False

    if a < 2:
        return False

    if a == 2:
        return True

    if a%2 == 0:
        return False

    d = 3
    while(d*d <= a):
        if a%d == 0:
            return False
        d += 1

    return True

def eliminate_primes(list):
    '''
    eliminates the numbers that the real part is prime
    :param list: list
    :return: list
    '''
    i = 0
    while i < len(list):
        number = list[i]
        realPart = cmpnumber.get_real_part(number)

        if is_prime(realPart):
            list.remove(number)

        else:
            i += 1

    return list