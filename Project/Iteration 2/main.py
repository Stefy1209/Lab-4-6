import Test
import Validation
import Business
def run_main():
    print("Feel stuck? Try help")
    finished = False
    lst = []
    while not finished:
        cmd = input("<<< ")
        cmd = cmd.strip()
        cmd = cmd.lower()
        parts = cmd.split(' ')
        cmd_name = parts[0]
        params = parts[1:]

        try:
            Validation.validate_cmd(cmd_name)
        except SyntaxError as se:
            print(se, end='')

        match cmd_name:
            case 'add':
                ok = True

                try:
                    Validation.validate_params_add(params, len(lst))
                except SyntaxError as se:
                    print(se, end='')
                    ok = False

                if ok:
                    number = params[0]
                    number = number.strip('i')
                    position = len(lst) + 1

                    if number.__contains__('+'):
                        number = number.split('+')
                        rl_part = float(number[0])
                        img_part = float(number[1])
                    else:
                        number = number.split('-')
                        rl_part = float(number[0])
                        img_part = -float(number[1])

                    if len(params) == 2:
                        position = int(params[1])
                    Business.create_cmp_number_and_add_to_list_position(rl_part, img_part, lst, position-1)

            case 'modify':
                ok = True

                try:
                    Validation.validate_params_modify(params, lst)
                except SyntaxError as se:
                    print(se, end='')
                    ok = False

                if ok:
                    if len(params) == 1:
                        borders = params[0].split('-')
                        start = int(borders[0])
                        end = int(borders[len(borders)-1])
                        Business.eliminate_sbq(lst, start-1, end-1)

                    if len(params) == 2:
                        number1 = params[0]
                        number1 = number1.strip('i')

                        number2 = params[1]
                        number2 = number2.strip('i')

                        if number1.__contains__('+'):
                            number1 = number1.split('+')
                            rl_part1 = float(number1[0])
                            img_part1 = float(number1[1])
                        else:
                            number1 = number1.split('-')
                            rl_part1 = float(number1[0])
                            img_part1 = -float(number1[1])

                        if number2.__contains__('+'):
                            number2 = number2.split('+')
                            rl_part2 = float(number2[0])
                            img_part2 = float(number2[1])
                        else:
                            number2 = number2.split('-')
                            rl_part2 = float(number2[0])
                            img_part2 = -float(number2[1])

                        Business.create_complex_numbers_and_change_in_list(rl_part1, img_part1, rl_part2, img_part2, lst)

            case 'search':
                ok = True

                try:
                    Validation.validate_params_search(params, lst)
                except SyntaxError as se:
                    print(se, end='')
                    ok = False

                if ok:
                    if len(params) == 2:
                        borders = params[1].split('-')
                        start = int(borders[0])
                        end = int(borders[1])
                        Business.img_part(lst, start-1, end-1)

                    if len(params) == 1:
                        if params[0] == '<':
                            Business.abs_less(lst, 10)
                        else:
                            Business.abs_equal(lst, 10)

            case 'operate':
                pass

            case 'filter':
                ok = True

                try:
                    Validation.validate_params_filter(params)
                except SyntaxError as se:
                    print(se, end = '')
                    ok = False

                if ok:
                    if len(params) == 1:
                        Business.eliminate_primes(lst)

                    if len(params) == 2:
                        x = float(params[1])

                        if params[0] == '<':
                            Business.eliminate_less(lst,x)

                        if params[0] == '=':
                            Business.eliminate_equal(lst,x)

                        if params[0] == '>':
                            Business.eliminate_greater(lst,x)


            case 'undo':
                pass

            case 'help':
                Business.print_help_UI()

            case 'print':
                print(lst)

            case 'exit':
                finished = True

Test.run_tests()
run_main()


