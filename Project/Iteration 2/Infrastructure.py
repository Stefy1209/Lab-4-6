import Domain
def add_cmp_number_to_list_position(cmp_number, lst, position):
    '''
    adds complex number at a given position
    :param cmp_number: list
    :param lst: list
    :param position: int
    :return: -
    '''
    lst.insert(position, cmp_number)

def print_img_part_sbq(lst, start, end):
    '''
    prints the imaginary part of the numbers from a subsequence
    :param lst: list
    :param start: int
    :param end: int
    :return: -
    '''
    new_lst = []
    for i in lst[start:end+1]:
        new_lst.append(Domain.get_img_part(i))
    print(new_lst)

def print_abs_less(lst, x):
    '''
    prints the numbers which their absolute value is less than x
    :param lst: list
    :param x: float
    :return: -
    '''
    eps = 0.001
    new_lst = []
    for i in range(len(lst)):
        if Domain.cmp_abs(lst[i]) < 10 and abs(Domain.cmp_abs(lst[i]) - x) > eps:
            new_lst.append(lst[i])
    print(new_lst)

def print_abs_equal(lst, x):
    '''
    prints the numbers which their absolute value is equal to x
    :param lst: list
    :param x: float
    :return: -
    '''
    eps = 0.001
    new_lst = []
    for i in range(len(lst)):
        if abs(Domain.cmp_abs(lst[i]) - x) < eps:
            new_lst.append(lst[i])
    print(new_lst)

def remove_sbq(lst, start, end):
    '''
    removes the subsequence from the list
    :param lst: list
    :param start: int
    :param end: int
    :returns: -
    '''
    for i in range(start, end+1):
        lst.remove(lst[start])

def change_cmp_number(cmp_number1, cmp_number2, lst):
    '''
    changes the complex number 1 with complex number 2
    :params cmp_number1: list
    :params cmp_number2: list
    :params lst: list
    :returns: -
    '''
    for i in lst:
        if Domain.get_rl_part(i) == Domain.get_rl_part(cmp_number1) and Domain.get_img_part(i) == Domain.get_img_part(cmp_number1):
            Domain.set_rl_part(i, Domain.get_rl_part(cmp_number2))
            Domain.set_img_part(i, Domain.get_img_part(cmp_number2))