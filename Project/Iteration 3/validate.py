import comand
def action(action):
    '''
    verifies if the action is valid
    :param action: string
    :return: -
    '''
    listAction = ['add', 'modify', 'search', 'operate', 'filter', 'undo', 'print', 'exit', 'help']
    errors = ''

    if not action in listAction:
        errors += 'invalid action!\n'

    if len(errors) > 0:
        raise SyntaxError(errors)

def parameters_add(parameters, list):
    '''
    verifies if the parameters are valid for the action add
    :param parameters: string
    :param list: list
    :return: -
    '''
    errors = ''

    if len(parameters) == 0:
        errors += 'there are no parameters!\n'

    if len(parameters) == 1:
        if not comand.is_number(parameters[0]):
            errors += 'invalid number!\n'

    if len(parameters) == 2:
        if not comand.is_number(parameters[0]):
            errors += 'invalid number!\n'

        if not parameters[1].isdigit():
            errors += parameters[1]
            errors += ' is not a position!\n'

    if len(errors) > 0:
        raise SyntaxError(errors)

def parameters_modify(parameters, list):
    errors = ''

    if list == []:
        raise SyntaxError('there is no list!\n')

    if len(parameters) == 0:
        errors += 'there are no parameters!\n'

    if len(parameters) == 1:
        subsequence = parameters.split('-')
        if len(subsequence) == 1:
            if not comand.is_integer(subsequence[0]):
                errors += 'invalid position!\n'
            else:
                p = int(subsequence[0])
                if p < 1 and len(list) < p:
                    errors += 'invalid position!\n'

        if len(subsequence) == 2:
            ok1 = True
            ok2 = True
            if not subsequence[0].isdecimal():
                errors += 'invalid subsequence!\n'
                ok1 = False
            else:
                p1 = int(subsequence[0])
                if p1 < 1 or len(list) < p1:
                    errors += 'invalid subsequence!\n'
                    ok1 = False

            if not subsequence[1].isdecimal():
                errors += 'invalid subsequence!\n'
                ok2 = False
            else:
                p2 = int(subsequence[1])
                if p2 < 1 or len(list) < p2:
                    errors += 'invalid subsequence!\n'
                    ok2 = False

            if ok1 and ok2 and p1 > p2:
                errors += 'invalid subsequence!\n'

    if len(parameters) == 2:
        if not comand.is_number(parameters[0]) or not comand.is_number(parameters[1]):
            errors += 'invalid numbers!\n'

    if len(errors) > 0:
        raise SyntaxError(errors)


def parameters_search(parameters, list):
    errors = ''

    if list == []:
        raise SyntaxError('there is no list!\n')

    if len(parameters) == 0:
        errors += 'there are no parameters!\n'

    if len(parameters) == 1:
        if parameters[0][0].isdigit():
            ok1 = True
            ok2 = True

            subsequence = parameters[0].split('-')
            if len(subsequence) == 1:
                errors += 'invalid subsequence!\n'

            if len(subsequence) == 2:
                ok1 = True
                ok2 = True
                if not subsequence[0].isdecimal():
                    errors += 'invalid subsequence!\n'
                    ok1 = False
                else:
                    p1 = int(subsequence[0])
                    if p1 < 1 or len(list) < p1:
                        errors += 'invalid subsequence!\n'
                        ok1 = False

                if not subsequence[1].isdecimal():
                    errors += 'invalid subsequence!\n'
                    ok2 = False
                else:
                    p2 = int(subsequence[1])
                    if p2 < 1 or len(list) < p2:
                        errors += 'invalid subsequence!\n'
                        ok2 = False

                if ok1 and ok2 and p1 > p2:
                    errors += 'invalid subsequence!\n'

        elif parameters[0] != '<' and parameters[0] != '=':
            errors += 'invalid operator!\n'

    if len(errors) > 0:
        raise SyntaxError(errors)

def parameters_operate(parameters):
    errors = ''

    if len(parameters) == 0:
        errors += 'there are no parameters!\n'

    if len(parameters) == 1 and not parameters[0] in ['sum', 'product', 'descent']:
        errors += 'invalid parameter!\n'

    if len(errors) > 0:
        raise SyntaxError(errors)

def parameters_filter(parameters):
    errors = ''

    if len(parameters) == 0:
        errors += 'there are no parameters!\n'

    if len(parameters) == 1:
        if parameters[0] != 'primes':
            errors += parameters[0]
            errors += ' does not exist!\n'

    if len(parameters) == 2:
        if not parameters[0] in ['<', '=', '<']:
            errors += 'invalid operater!\n'

        if not parameters[1].isdecimal():
            errors += 'invalid number!\n'

    if len(errors) > 0:
        raise SyntaxError(errors)