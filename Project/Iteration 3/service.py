import cmpnumber
import comand
import infrastructure
import validate

def main():
    list = []
    finished = False

    while not finished:
        comand = input(">>> ")
        comand = comand.lower()
        action = comand.get_action(comand)
        parameters = comand.get_parameters(comand)

        validAction = True

        try:
            validate.action(action)
        except SyntaxError as se:
            print(se, end='')
            validAction = False

        match action:
            case 'add':
                ok = True

                try:
                    validate.parameters_add(parameters, list)
                except SyntaxError as se:
                    print(se, end='')
                    ok = False

                if ok:
                    realPart = 0
                    imaginaryPart = 0
                    position = len(list)

                    realPart = comand.get_real_part(parameters[0])
                    imaginaryPart = comand.get_imaginary_part(parameters[0])

                    number = cmpnumber.create_complex_number(realPart,imaginaryPart)

                    infrastructure.add_number_to_list_position(number, list, position)

            case 'modify':
                pass
            case 'search':
                pass
            case 'operate':
                pass
            case 'filter':
                pass
            case 'undo':
                pass
            case 'print':
                print(list)
            case 'exit':
                finished = True