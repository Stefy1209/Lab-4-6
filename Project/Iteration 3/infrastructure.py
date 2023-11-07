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