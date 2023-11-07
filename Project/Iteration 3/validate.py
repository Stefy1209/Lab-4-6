import comand
def action(action):
    '''
    verifies if the action is valid
    :param action: string
    :return: -
    '''
    listAction = ['add', 'modify', 'search', 'operate', 'filter', 'undo', 'print', 'exit']
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
        """if not comand.is_number(parameters[0]):
            errors += 'invalid number!\n'"""

    if len(parameters) == 2:
        """if not comand.is_number(parameters[0]):
            errors += 'invalid number!\n'"""

        if not parameters[1].isdigit():
            errors += parameters[1]
            errors += ' is not a position!\n'

    if len(errors) > 0:
        raise SyntaxError(errors)

def parameters_modify(parameeters):
    pass