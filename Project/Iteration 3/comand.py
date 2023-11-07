def get_real_part(number):
    '''
    takes a string complex number and gets the rela part
    :param number: string
    :return: float
    '''
    number = number.strip()
    if '+' in number[1:]:
        number = number.split('+')

    elif '-' in number[1:]:
        number = number.split('-')

    if number[0] == '':
        return -float(number[1])

    return float(number[0])

def get_imaginary_part(number):
    '''
    takes a string complex number and gets the imaginary part
    :param number: string
    :return: float
    '''
    number = number.strip().strip('i')
    if '+' in number:
        number = number.split('+')
        return float(number[1])

    elif '-' in number:
        number = number.split('-')
        if number[0] == '':
            return -float(number[2])
        return -float(number[1])

def is_number(number):
    '''
    verifies if the string number can be interpreted as a complex number
    :param number: string
    :return: bool
    '''
    pass

def get_position(position):
    '''
    verifies if a number can be added to a list at the given string position
    :param position: string
    :param list: list
    :return: int
    '''
    p = int(position)
    return p

def get_action(cmd):
    '''
    takes a comand and returns the action in it
    :param comand: string
    :return: string
    '''
    cmd = cmd.strip().split()
    return cmd[0]

def get_parameters(cmd):
    '''
    takes a comand and returns the parameters in it
    :param comand: string
    :return: string
    '''
    cmd = cmd.strip().split()
    return cmd[1:]

def get_start(subsequence):
    '''
    gets a subsequence and returns the start of it
    :param subsequence: string
    :return: int
    '''
    subsequence = subsequence.strip().split('-')
    start = int(subsequence[0])
    return start

def get_end(subsequence):
    '''
    gets a subsequence and returns the end of it
    :param subsequence: list
    :return: int
    '''
    subsequence = subsequence.strip().split('-')
    if len(subsequence) == 1:
        end = int(subsequence[0])
    else:
        end = int(subsequence[1])
    return end