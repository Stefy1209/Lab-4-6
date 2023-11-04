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

def test_get_action():
    comand = "a fost o data ca niciodata un programator"
    action = comand.get_action(comand)

    assert action == "a"

def test_get_parameters():
    comand = "a fost o data ca niciodata un programator"
    parameters = comand.get_parameters(comand)

    assert parameters == ['fost', 'o', 'data', 'ca', 'niciodata', 'un', 'programator']

def test_get_real_part():
    number = '3'
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
    assert realPart == 0

    number = '-2.243+3.90i'
    realPart = comand.get_real_part(number)
    assert realPart == -2.243

def test_get_imaginaty_part():
    number = '3'
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
    assert imaginaryPart == -3.01

    number = '2-3i'
    imaginaryPart = comand.get_imaginary_part(number)
    assert imaginaryPart == -3

def test_is_number():
    number = '2'
    assert comand.is_number(number) == True

    number= '-3.2'
    assert comand.is_number(number) == True

    number = '2i'
    assert comand.is_number(number) == True

    number = '-2.5i'
    assert comand.is_number(number) == True

    number = '2+3i'
    assert comand.is_number(number) == True

def test_is_good_position():
    position = '0'
    list = []
    assert comand.is_good_position(position, list) == True

    position = '1'
    list = [None, None]
    assert comand.is_good_position(position, list) == True

    position = '1'
    list = [None, None, None]
    assert comand.is_good_position(position, list) == True

def test_cmpnumber():
    test_get_abs_value()
    test_is_equal()
    test_is_less()
    test_is_greater()

def test_infrastructure():
    test_add_number_to_list_position()

def test_comand():
    test_get_real_part()
    test_get_imaginaty_part()
    test_is_number()
    test_is_good_position()
    test_get_action()
    test_get_parameters()

def run_tests():
    test_cmpnumber()
    test_infrastructure()
    test_comand()