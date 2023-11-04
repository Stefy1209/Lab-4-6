import Domain
import Infrastructure
def create_cmp_number_and_add_to_list_position(rl_part, img_part, lst, position):
    '''
    creates a complex number and adds the number to the list to a given position
    :param rl_part: float
    :param img_part: float
    :param lst: list
    :param position: int
    :return: -
    '''
    cmp_number = Domain.create_cmp_number(rl_part, img_part)
    Infrastructure.add_cmp_number_to_list_position(cmp_number, lst, position)

def img_part(lst, start, end):
    '''
    takes a list and prints the imaginary part of the numbers from start to end
    :param lst: list
    :param start: int
    :param end: int
    :return: -
    '''
    Infrastructure.print_img_part_sbq(lst, start, end)

def abs_less(lst, x):
    '''
    takes a list and prints the numbers which their absolute value is less than x
    :param lst: list
    :param x: float
    :return: -
    '''
    Infrastructure.print_abs_less(lst, x)

def abs_equal(lst, x):
    '''
    takes a list and prints the numbers which their absolute values is equal to x
    :param lst: list
    :param x: float
    :return: -
    '''
    Infrastructure.print_abs_equal(lst, x)

def create_complex_numbers_and_change_in_list(rl_part1, img_part1, rl_part2, img_part2, lst):
    '''
    creates 2 complex numbers and changes the first complex number with the second
    :params rl_part1: float
    :params img_part1: float
    :params rl_part2: float
    :params img_part2: float
    :params lst: list
    :returns: -
    '''
    cmp_number1 = Domain.create_cmp_number(rl_part1, img_part1)
    cmp_number2 = Domain.create_cmp_number(rl_part2, img_part2)
    Infrastructure.change_cmp_number(cmp_number1, cmp_number2, lst)

def eliminate_sbq(lst, start, end):
    '''
    eliminates a subsequence from a list
    :param lst: list
    :param start: int
    :param end: int
    :return: -
    '''
    Infrastructure.remove_sbq(lst, start, end)

def eliminate_primes(lst):
    '''
    eliminates the numbers which the real part is prime
    :param lst: list
    :return: -
    '''
    for i in lst:
        r = abs(Domain.get_rl_part(i))
        if r.is_integer() and Domain.x_is_prime(int(r)):
            lst.remove(i)

def eliminate_less(lst, x):
    '''
    eliminates the numbers where the absolute value is less than x
    :param lst: list
    :param x: float
    :return: -
    '''
    i = 0
    l = len(lst)
    while(i < l):
        a = Domain.cmp_abs(i)
        if a < x and abs(a - x) > 0.001:
            lst.remove(i)
            l -= 1
        else: i += 1

def eliminate_equal(lst,x):
    '''
    eliminates the numbers which their absolute value is equal to x
    :param lst: list
    :param x: float
    :return: -
    '''
    i = 0
    l = len(lst)
    while(i < l):
        a = Domain.cmp_abs(i)
        if abs(a - x) < 0.001:
            lst.remove(i)
            l -= 1
        else: i += 1

def eliminate_greater(lst, x):
    '''
    eliminates the numbers which their absolute value is greater than x
    :param lst: list
    :param x: float
    :return: -
    '''
    i = 0
    l = len(lst)
    while(i < l):
        a = Domain.cmp_abs(i)
        if a > x and abs(a - x) > 0.001:
            lst.remove(i)
            l -= 1
        else: i += 1

def print_help_UI():
    print("For every action you want to make you have to type a comand:")
    print(">>> 'add' + 'type complex number' + ('position') to add a complex number to list (at a given position)")
    print(">>> 'modify' + 'type position/subsequence' to remove the number/numbers from position/subsequence")
    print(">>> 'modify' + 'type complex number 1' + 'type complex number 2' to modify every apareance of the first number with the second")
    print(">>> 'search' + 'img_part' + 'type subsequence' to show the imaginary part of the numbers from the subsequence")
    print(">>> 'search' + '<' / '+' to show all the numbers that their absolute value is less/equal than/to 10")
    print(">>> 'filter' + 'prime' to remove all the numbers that the real part is a prime number")
    print(">>> 'filter' + '<' / '=' / '>' + 'type non-complex number' to remove all the numbers that their absolute value is less/equal/greater than/to a number")
    print(">>> 'print' to show your list")
    print(">>> 'exit' to exit the program")