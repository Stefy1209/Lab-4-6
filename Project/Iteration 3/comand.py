def get_real_part(number):
    '''
    takes a string complex number and gets the rela part
    :param number: string
    :return: float
    '''
    pass

def get_imaginary_part(number):
    '''
    takes a string complex number and gets the imaginary part
    :param number: string
    :return: float
    '''
    pass

def is_number(number):
    '''
    verifies if the string number can be interpreted as a complex number
    :param number: string
    :return: bool
    '''
    pass

def is_good_position(position, list):
    '''
    verifies if a number can be added to a list at the given string position
    :param position: string
    :param list: list
    :return: bool
    '''
    p = int(position)

    if p < 0 or len(list) < p:
        return False

    return True

def get_action(comand):
    '''
    takes a comand and returns the action in it
    :param comand: string
    :return: string
    '''
    comand = comand.strip().split()
    return comand[0]

def get_parameters(comand):
    '''
    takes a comand and returns the parameters in it
    :param comand: string
    :return: string
    '''
    comand = comand.strip().split()
    return comand[1:]