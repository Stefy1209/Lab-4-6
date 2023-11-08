import cmpnumber
import comand
import infrastructure
import validate

def main():
    list = []
    finished = False
    history = []

    while not finished:
        cmd = input(">>> ")
        cmd = cmd.lower()
        action = comand.get_action(cmd)
        parameters = comand.get_parameters(cmd)

        validAction = True

        try:
            validate.action(action)
        except SyntaxError as se:
            print(se, end = '')
            validAction = False

        match action:
            case 'add':
                ok = True

                try:
                    validate.parameters_add(parameters, list)
                except SyntaxError as se:
                    print(se, end = '')
                    ok = False

                if ok:
                    realPart = 0
                    imaginaryPart = 0
                    position = len(list)+1

                    realPart = comand.get_real_part(parameters[0])
                    imaginaryPart = comand.get_imaginary_part(parameters[0])

                    number = cmpnumber.create_complex_number(realPart,imaginaryPart)

                    if len(parameters) > 1:
                        position = comand.get_position(parameters[1])

                    infrastructure.add_number_to_list_position(number, list, position - 1)

            case 'modify':
                ok = True

                try:
                    validate.parameters_modify(parameters)
                except SyntaxError as es:
                    print(se, end = '')
                    ok = False

                if ok:
                    if len(parameters) == 1:
                        start = comand.get_start(parameters[0])
                        end = comand.get_end(parameters[0])

                        infrastructure.eliminate_from_list(list, start-1, end-1)

                    if len(parameters) == 2:
                        realPart1 = comand.get_real_part(parameters[0])
                        imaginaryPart1 = comand.get_imaginary_part(parameters[0])
                        number1 = cmpnumber.create_complex_number(realPart1, imaginaryPart1)

                        realPart2 = comand.get_real_part(parameters[1])
                        imaginaryPart2 = comand.get_imaginary_part(parameters[1])
                        number2 = cmpnumber.create_complex_number(realPart2, imaginaryPart2)

                        infrastructure.replace_number1_with_number2_list(number1, number2, list)

            case 'search':
                ok = True

                try:
                    validate.parameters_search(parameters)
                except SyntaxError as se:
                    print(se, end = '')
                    ok = false

                if ok:
                    if parameters[0][0].isdigit():
                        start = comand.get_start(parameters[0])
                        end = comand.get_end(parameters[0])

                        imaginaryList = infrastructure.get_imaginary_parts(list, start-1, end-1)

                        print(imaginaryList)

                    if parameters[0] == '<':
                        newList = infrastructure.get_less(list)

                        print(newList)

                    if parameters[0] == '=':
                        newList = infrastructure.get_equal(list)

                        print(newList)

            case 'operate':
                ok = True

                try:
                    validate.parameters_operate(parameters)
                except SyntaxError as es:
                    print(es)
                    ok = False

                if ok:
                    if parameters[0] == 'sum':
                        start = comand.get_start(parameters[1])
                        end = comand.get_end(parameters[1])

                        sum = infrastructure.get_sum_subsequence(list, start-1, end-1)

                        print(sum)

                    if parameters[0] == 'product':
                        start = comand.get_start(parameters[1])
                        end = comand.get_end(parameters[1])

                        product = infrastructure.get_product_subsequence(list, start-1, end-1)

                        print(product)

                    if parameters[0] == 'descent':
                        newList = list.copy()

                        infrastructure.sort_descent_imaginary(newList)

                        print(newList)
            case 'filter':
                 ok = True

                 try:
                     validate.parameters_filter(parameters)
                 except SyntaxError as se:
                     print(se, end = '')
                     ok = False

                 if ok:
                     if parameters[0] == 'primes':
                         newList = list.copy()

                         infrastructure.eliminate_primes(newList)

                         print(newList)

                     if parameters[0] == '<':
                         pass

            case 'undo':
                pass
            case 'print':
                print(list)
            case 'exit':
                finished = True