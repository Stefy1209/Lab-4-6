def validate_cmd(cmd):
    errors = ""
    if cmd != "add" and cmd != "modify" and cmd != "search" and cmd != "operate" and cmd != "filter" and cmd != "undo" and cmd != "print" and cmd != "help" and cmd != "exit":
        errors += cmd + " invalid comand!\n"
    if len(errors) > 0:
        raise SyntaxError(errors)
def validate_params_add(params, l):
    errors = ""
    if not 1 <= len(params) <= 2:
        errors += "invalid parameters!\n"
    if len(params) == 1 and not params[0].__contains__('i'):
        errors += "invalid complex number!\n"
    if len(params) == 2:
        if not params[0].__contains__('i'):
            errors += "invalid complex number!\n"
        if not 0 <= int(params[1]) <= l+1:
            errors += "invalid position!\n"
    if len(errors) != 0:
        raise SyntaxError(errors)

def validate_params_modify(params, lst):
    errors = ""
    if len(params) > 2 or len(params) < 1:
        errors += "invalid parameters!\n"
    elif len(params) == 1 and not params[0].__contains__('i'):
        borders = params[0].split('-')
        if len(borders) == 2:
            start = int(borders[0])
            end = int(borders[1])
            if start < 1 or len(lst) < end or start > end:
                errors += "invalid subsquence!\n"
        if len(borders) == 1:
            position = int(borders[0])
            if position < 1 or len(lst) < position:
                errors += "invalid position!\n"
    elif len(params) == 2 and (not params[0].__contains__('i') or not params[1].__contains__('i')):
        errors += "invalid complex numbers!\n"
    elif len(params) == 1 and params[0].__contains__('i'):
        errors += "invalid second complex number!\n"

    if len(errors) > 0:
        raise SyntaxError(errors)

def validate_params_search(params, lst):
    errors = ""
    if not 1 <= len(params) <= 2:
        errors += "invalid parameters!\n"
    if len(params) == 1 and (params[0] != "<" and params[0] != "="):
        errors += "invalid operator!\n"
    if len(params) == 2:
        if params[0] != "img_part":
            errors += "invalid operator!\n"
        borders = params[1].split('-')
        start = int(borders[0])
        end = int(borders[1])
        if start < 1 or len(lst) < end  or start > end:
            errors += "invalid subsequence!\n"
    if len(errors) > 0:
        raise SyntaxError(errors)

def validate_params_filter(params):
    errors = ""

    if not 1 <= len(params) <= 2:
        errors += "invalid parameters!\n"

    if len(params) == 1 and params[0] != "prime":
        errors += "invalid parameter!\n"

    if len(params) == 2 and not(params[0] == '<' or params[0] == '=' or params[0] == '>'):
        errors += "invalid operator!\n"

    if len(errors) > 0:
        raise SyntaxError(errors)