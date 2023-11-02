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

    :param lst:
    :param start:
    :param end:
    :return:
    '''
    Infrastructure.print_img_part_sbq(lst, start, end)

def abs_less(lst, x):
    '''

    :param lst:
    :param x:
    :return:
    '''
    Infrastructure.print_abs_less(lst, x)

def abs_equal(lst, x):
    '''

    :param lst:
    :param x:
    :return:
    '''
    Infrastructure.print_abs_equal(lst, x)

def create_complex_numbers_and_change_in_list(rl_part1, img_part1, rl_part2, img_part2, lst):
    cmp_number1 = Domain.create_cmp_number(rl_part1, img_part1)
    cmp_number2 = Domain.create_cmp_number(rl_part2, img_part2)
    Infrastructure.change_cmp_number(cmp_number1, cmp_number2, lst)

def eliminate_sbq(lst, start, end):
    '''

    :param lst:
    :param start:
    :param end:
    :return:
    '''
    Infrastructure.remove_sbq(lst, start, end)

def eliminate_primes(lst):
    '''

    :param lst:
    :return:
    '''
    for i in lst:
        r = abs(Domain.get_rl_part(i))
        if r.is_integer() and Domain.x_is_prime(int(r)):
            lst.remove(i)

def eliminate_less(lst, x):
    '''

    :param lst:
    :param x:
    :return:
    '''
    for i in lst:
        a = Domain.cmp_abs(i)
        if a < x and abs(a - x) > 0.001:
            lst.remove(i)

def eliminate_equal(lst,x):
    '''

    :param lst:
    :param x:
    :return:
    '''
    for i in lst:
        a = Domain.cmp_abs(i)
        if abs(a - x) < 0.001:
            lst.remove(i)

def eliminate_greater(lst, x):
    '''

    :param lst: list
    :param x: float
    :return: -
    '''
    for i in lst:
        a = Domain.cmp_abs(i)
        if a > x and abs(a - x) > 0.001:
            lst.remove(i)

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