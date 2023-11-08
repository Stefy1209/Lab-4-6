import cmpnumber
import infrastructure
import comand

def test_get_abs_value():
    realPart = 2.456
    imaginaryPart = -0.124
    cmp = cmpnumber.create_complex_number(realPart, imaginaryPart)
    a = cmpnumber.get_abs_value(cmp)

    assert abs(a - 2.459) < 0.0001

def test_is_less():
    realPart = 2.456
    imaginaryPart = -0.124
    cmp = cmpnumber.create_complex_number(realPart, imaginaryPart)

    value = 2.458
    assert cmpnumber.is_less(cmp, value) == False

    value = 2.459
    assert cmpnumber.is_less(cmp, value) == False

    value = 2.46
    assert cmpnumber.is_less(cmp, value) == True

def test_is_equal():
    realPart = 2.456
    imaginaryPart = -0.124
    cmp = cmpnumber.create_complex_number(realPart, imaginaryPart)

    value = 2.458
    assert cmpnumber.is_equal(cmp, value) == False

    value = 2.459
    assert cmpnumber.is_equal(cmp, value) == True

    value = 2.46
    assert cmpnumber.is_equal(cmp, value) == False

def test_is_greater():
    realPart = 2.456
    imaginaryPart = -0.124
    cmp = cmpnumber.create_complex_number(realPart, imaginaryPart)

    value = 2.458
    assert cmpnumber.is_greater(cmp, value) == True

    value = 2.459
    assert cmpnumber.is_greater(cmp, value) == False

    value = 2.46
    assert cmpnumber.is_greater(cmp, value) == False

def test_add_number_to_list_position():
    l = []

    realPart1 = 1
    imaginaryPart1 = 2
    num1 = cmpnumber.create_complex_number(realPart1, imaginaryPart1)

    realPart2 = 2.5
    imaginaryPart2 = 7.5
    num2 = cmpnumber.create_complex_number(realPart2, imaginaryPart2)

    infrastructure.add_number_to_list_position(num1, l, 0)
    assert l == [num1]

    infrastructure.add_number_to_list_position(num2, l, 0)
    assert l == [num2, num1]

    infrastructure.add_number_to_list_position(num2, l, 2)
    assert l == [num2, num1, num2]

def test_eliminate_from_list():
    realPart1 = 3.43
    imaginaryPart1 = 234.45
    number1 = cmpnumber.create_complex_number(realPart1, imaginaryPart1)

    realPart2 = 0.1237
    imaginaryPart2 = -345.090
    number2 = cmpnumber.create_complex_number(realPart2, imaginaryPart2)

    list = [number1, number2, number2, number2, number1, number2]

    start = 1
    end = 1
    infrastructure.eliminate_from_list(list, start, end)
    assert list == [number1, number2, number2, number1, number2]

    start = 0
    end = 3
    infrastructure.eliminate_from_list(list, start, end)
    assert list == [number2]

def test_get_action():
    cmd = "a fost o data ca niciodata un programator"
    action = comand.get_action(cmd)

    assert action == "a"

def test_get_parameters():
    cmd = "a fost o data ca niciodata un programator"
    parameters = comand.get_parameters(cmd)

    assert parameters == ['fost', 'o', 'data', 'ca', 'niciodata', 'un', 'programator']

def test_get_start():
    subsequence = '1'
    start = comand.get_start(subsequence)
    assert start == 1

    subsequence = '1-6'
    start = comand.get_start(subsequence)
    assert start == 1

    subsequence = '23-24'
    start = comand.get_start(subsequence)
    assert start == 23

def test_get_end():
    subsequence = '1'
    end = comand.get_end(subsequence)
    assert end == 1

    subsequence = '1-6'
    end = comand.get_end(subsequence)
    assert end == 6

    subsequence = '23-24'
    end = comand.get_end(subsequence)
    assert end == 24

def test_replace_number1_with_number2_list():
    realPart1 = 2342.435
    imaginaryPart1 = 85.934
    number1 = cmpnumber.create_complex_number(realPart1, imaginaryPart1)

    realPart2 = -4576
    imaginaryPart2 = -495.650
    number2 = cmpnumber.create_complex_number(realPart2, imaginaryPart2)

    realPart3 = 3475.86
    imaginaryPart3 = -0.345
    number3 = cmpnumber.create_complex_number(realPart3, imaginaryPart3)

    list = [number1, number2, number2, number1, number1, number2]
    infrastructure.replace_number1_with_number2_list(number1, number3, list)
    assert list == [number3, number2, number2, number3, number3, number2]

def test_is_prime():
    a = 1
    assert infrastructure.is_prime(a) == False

    a = 2
    assert infrastructure.is_prime(a) == True

    a = 2.0
    assert infrastructure.is_prime(a) == True

    a = -2
    assert infrastructure.is_prime(a) == False

def test_get_real_part():
    """number = '3'
    realPart = comand.get_real_part(number)
    assert realPart == 3

    number = '-3'
    number = comand.get_real_part(number)
    assert realPart == -3

    number = '2i'
    realPart = comand.get_real_part(number)
    assert realPart == 0

    number = '-3i'
    realPart = comand.get_real_part(number)
    assert realPart == 0"""

    number = '-2.243+3.90i'
    realPart = comand.get_real_part(number)
    assert realPart == -2.243

def test_get_imaginaty_part():
    """number = '3'
    imaginaryPart = comand.get_imaginary_part(number)
    assert imaginaryPart == 0

    number = '-2.3'
    imaginaryPart = comand.get_imaginary_part(number)
    assert imaginaryPart == 0

    number = '2i'
    imaginaryPart = comand.get_imaginary_part(number)
    assert imaginaryPart == 2

    number = '-3.01i'
    imaginaryPart = comand.get_imaginary_part(number)
    assert imaginaryPart == -3.01"""

    number = '2-3i'
    imaginaryPart = comand.get_imaginary_part(number)
    assert imaginaryPart == -3.0

def test_is_number():
    """number = '2'
    assert comand.is_number(number) == True

    number= '-3.2'
    assert comand.is_number(number) == True

    number = '2i'
    assert comand.is_number(number) == True

    number = '-2.5i'
    assert comand.is_number(number) == True"""

    number = '2+3i'
    assert comand.is_number(number) == True

def test_cmpnumber():
    test_get_abs_value()
    test_is_equal()
    test_is_less()
    test_is_greater()

def test_infrastructure():
    test_add_number_to_list_position()
    test_eliminate_from_list()

def test_comand():
    test_get_real_part()
    test_get_imaginaty_part()
    #test_is_number()
    test_get_action()
    test_get_parameters()
    test_get_start()
    test_get_end()
    test_replace_number1_with_number2_list()
    test_is_prime()

def run_tests():
    test_cmpnumber()
    test_infrastructure()
    test_comand()