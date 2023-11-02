import math
def get_real_part(complex_number):
    '''
    gets the real part of a complex number
    :param complex_number: tuple
    :return: float
    '''
    return float(complex_number[0])
def get_imaginary_part(complex_number):
    '''
    gets the imaginary part of a complex number
    :param complex_number: tuple
    :return: float
    '''
    return float(complex_number[1])
def add_number_to_list(complex_number, list):
    '''
    adds the complex number to the list
    :param complex_number: tuple (real_part, imaginary_part)
    :param list: list of complex numbers
    :return: -
    '''
    list.append(complex_number)
def test_create_complex_number():
    real_part = 3.14
    imaginary_part = 0.159
    complex_number = create_complex_number(real_part, imaginary_part)
    assert get_real_part(complex_number) == real_part
    assert get_imaginary_part(complex_number) == imaginary_part

def test_add_number_to_list():
    real_part = 3.14
    imaginary_part = 0.159
    complex_number = create_complex_number(real_part, imaginary_part)

    list = []
    assert list == []

    add_number_to_list(complex_number, list)
    assert list == [complex_number]

    add_number_to_list((1, 0), list)
    assert list == [complex_number, (1, 0)]

def test_validate_position():
    list = [(0,0), (1,1), (2,2)]
    validate_position(1, list)
    try:
        validate_position(3, list)
    except Exception as ex: assert str(ex) == "Position doesn't exist!"
def test_add_number_to_list_position():
    list = []
    add_number_to_list_position((0,0), list, 0)
    assert list == [(0,0)]

    list = [(0,1), (23,87), (34, 87), (23, 567)]
    add_number_to_list_position((1,2), list, 1)
    assert list == [(0,1), (1,2), (23,87), (34, 87), (23, 567)]

def run_test_add():
    test_create_complex_number()
    test_add_number_to_list()
    test_validate_position()
    test_add_number_to_list_position()

def validate_position(position, list):
    '''
    validates if it can add an element in the list at the given position
    :param position: int
    :param list: list
    :return: -
    :raise: IndexError("Position doesn't exist!")
    '''
    l = len(list)
    if position < 0 or l < position:
        raise IndexError("Position doesn't exist!")
def create_complex_number(real_part, imaginary_part):
    '''
    creates a complex number
    :param real_part: float
    :param imaginary_part: float
    :return: tuple
    '''
    return (real_part, imaginary_part)
def add_number_to_list_position(complex_number, list, position):
    '''
    adds a number to a given position in a list
    :param complex_number: tuple
    :param list: list
    :param position: int
    :return: -
    '''
    list.insert(position, complex_number)

def service_add_number(list):
    print_UI_add()
    action = int(input())
    print("Please enter your number x = a + bi, where:")
    real_part = float(input("The real part is a: "))
    imaginary_part = float(input("The imaginary part is b: "))
    complex_number = create_complex_number(real_part, imaginary_part)

    match action:
        case 1:
            add_number_to_list(complex_number, list)
        case 2:
            position = int(input("Enter position: "))
            validate_position(position, list)
            add_number_to_list_position(complex_number, list, position)
    print(list,'\n')
def print_UI_add():
    print("1.Add number in the list")
    print("2.Add number at a given position")
def print_UI():
    print("Select your next action: ")
    print("1.Add number")
    print("3.Search numbers")
    print("5.Filter numbers")
    print("7.Exit")

def validate_subsequence(list, start, end):
    '''
    validates if the subsequence from the list is correctly define by start and end
    :param list: list
    :param start: int
    :param end: int
    :return: -
    :raise: "Invalid subsequence!"
    '''
    if not 0 <= start <= end <= len(list)-1:
        raise IndexError("Invalid subsequence!")

def test_validate_subsequence():
    list = [(0,0) , (1,1), (2,2), (3, 3)]
    start_valid = 1
    end_valid = 3
    start_invalid = -1
    end_invalid = 10

    validate_subsequence(list, start_valid, end_valid)

    try:
        validate_subsequence(list, start_invalid, end_invalid)
    except Exception as ex:
        assert str(ex) == "Invalid subsequence!"

    end_invalid = 2
    try:
        validate_subsequence(list, start_invalid, end_invalid)
    except Exception as ex:
        assert str(ex) == "Invalid subsequence!"

def abs_value(complex_number) -> float:
    '''
    gives the absolute value of a complex number
    :param complex_number: tuple
    :return: float
    '''
    a = math.sqrt(get_real_part(complex_number) ** 2 + get_imaginary_part(complex_number) ** 2)
    return round(a, 3)
def test_abs_value():
    complex_number = (1, 3)
    eps = 0.001

    result = 3.162 - abs_value(complex_number)
    assert abs(result) < eps

def create_imaginary_list(list, start, end, im_list):
    '''
    creates a list where each element is the imaginary part of the subsequence from start to fins
    :param list:
    :param start:
    :param end:
    :param im_list:
    :return:
    '''
    for i in range(start, end+1):
        im_list.append(get_imaginary_part(list[i]))
def test_create_imaginary_list():
    list = [(0, 0), (1, 43), (-4, 0.135), (-4,96)]
    start = 1
    end = 3
    im_list = []
    create_imaginary_list(list, start, end, im_list)
    assert im_list == [43, 0.135, 96]
def run_test_search():
    test_validate_subsequence()
    test_abs_value()
    test_create_imaginary_list()

def test_generate_sieve_of_eratosthenes():
    sieve = []
    generate_sieve_of_eratosthenes(sieve)
    assert sieve[0] == 1
    assert sieve[1] == 1
    assert sieve[2] == 0
    assert sieve[121] == 1

def test_eliminate_primes():
    sieve = []
    generate_sieve_of_eratosthenes(sieve)

    list = []
    eliminate_primes(list, sieve)
    assert list == []

    list = [(-2.12, 4.5), (5.0, 0.2) ,(4.0, 2.1) ,(-7.0, 12) ,(41.0, 1)]
    eliminate_primes(list, sieve)
    assert list == [(-2.12, 4.5), (4, 2.1)]
def run_test_filter():
    test_generate_sieve_of_eratosthenes()
    test_eliminate_primes()
def run_test():
    run_test_add()
    run_test_search()
    run_test_filter()

def print_UI_search():
    print("1.Print the imaginary part of the numbers from a subsequence")
    print("2.Print all the numbers which abs(x) < 10")
    print("3.Print all the numbers which abs(x) == 10")
def service_search_number(list):
    print_UI_search()
    action = int(input())
    match action:
        case 1:
            start, end = [int(item) for item in input("Enter the start and the end of your subsequence: ").split()]
            validate_subsequence(list, start, end)
            im_list = []
            create_imaginary_list(list, start, end, im_list)
            print(im_list)
        case 2:
            eps = 0.0001
            for i in list:
                if abs_value(i) < 10 and abs(abs_value(i) -10) > eps:
                    print(i, end=' ')
            print('\n')
        case 3:
            eps = 0.0001
            for i in list:
                if abs(abs_value(i) -10) < eps:
                    print(i, end=' ')
            print('\n')

def eliminate_primes(list, sieve):
    '''
    removes from list the numbers where the real part is prime
    :param list: list
    :param sieve: sieve
    :return: -
    '''
    l = len(list)
    i = 0
    while i < l:
        if get_real_part(list[i]) - math.trunc(get_real_part(list[i])) == 0 and sieve[abs(math.trunc(get_real_part(list[i])))] == 0:
            list.remove(list[i])
            l -= 1
        else: i += 1
def print_UI_filter():
    print("1.Eliminate the complex numbers where the real part is prime")
    print("2.Eliminate the complex numbers that their absolute value is <, = or > than a given number")
def service_filter(list, sieve):
    print_UI_filter()
    action = int(input())
    match action:
        case 1:
            eliminate_primes(list, sieve)
        case 2:
            pass
    print(list, '\n')

def generate_sieve_of_eratosthenes(sieve):
    '''
    generates in sieve the sieve of eratosthenes
    :param sieve: list
    :return: -
    '''
    for i in range(1000001):
        sieve.append(0)
    sieve[0] = sieve[1] = 1
    for i in range(2, 1000001):
        if sieve[i] == 0:
            for j in range(2*i, 1000001, i):
                sieve[j] = 1
def run():
    finished = False
    list = []
    sieve_of_eratosthenes = []
    generate_sieve_of_eratosthenes(sieve_of_eratosthenes)
    while not finished:
        print_UI()
        action = int(input())
        match action:
            case 1:
                service_add_number(list)
            case 3:
                service_search_number(list)
            case 5:
                service_filter(list, sieve_of_eratosthenes)
            case 7:
                finished = True

run_test()
run()