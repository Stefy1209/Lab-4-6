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
    string = [*number]

    if string[0] != '-' and string[0] != '+':
        string.insert(0,'+')

    i = 1
    cnt_dot = 0
    cnt_digit = 0
    while i < len(string) and string[i] != '-' and string[i] != '+':
        if not string[i].isdigit():
            if string[i] != '.':
                return False
            cnt_dot += 1
            if cnt_dot > 1:
                return False

        cnt_digit += 1
        i += 1

    if cnt_digit == 0:
        return False

    if i == len(string):
        return False

    i += 1
    cnt_dot = 0
    cnt_digit = 0
    while i < len(string) and string[i] != 'i':
        if not string[i].isdigit():
            if string[i] != '.':
                return False
            cnt_dot += 1
            if cnt_dot > 1:
                return False

        cnt_digit += 1
        i += 1

    if cnt_digit == 0:
        return False

    if i == len(string):
        return False

    return True

def is_integer(position):
    '''
    verifies if position is an integer
    :param position: string
    :return: bool
    '''
    if not position.isdecimal():
        return False

    return True

def is_subsequence(subsequence):
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