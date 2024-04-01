# [Solução B]
# pythonSnake's solution
# https://exercism.org/tracks/python/exercises/forth/solutions/pythonSnake

class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message = message


def evaluate(input_data):
    result = []
    custom = {}

    if len(input_data) == 1:
        if input_data[0].split()[0] == ':':
            if input_data[0].split()[1].isalpha() == False:
                raise ValueError("illegal operation")
        for elem in input_data[0].split():
            if elem == '+':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                sum = 0
                for elem2 in result:
                    sum += elem2
                result = [sum]
            elif elem == '-':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result = [result[0]-result[1]]
            elif elem == '*':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result = [result[0]*result[1]]
            elif elem == '/':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                if result[1] == 0:
                    raise ZeroDivisionError("divide by zero")
                result = [result[0]//result[1]]
            elif elem.lower() == 'dup':
                if len(result) < 1:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result.append(result[-1])
            elif elem.lower() == 'drop':
                if len(result) < 1:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result.pop(-1)
            elif elem.lower() == 'swap':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                temp = result[-1]
                result[-1] = result[-2]
                result[-2] = temp
            elif elem.lower() == 'over':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result.append(result[-2])
            else:
                try:
                    result.append(int(elem))
                except:
                    raise ValueError("undefined operation")
    elif len(input_data) >= 2:
        for strings in input_data:
            if strings.split()[0] == ':':
                defined = strings.lower().split()[1:-1]
                variable = defined[0]
                other = defined[1:]
                if len(other) == 1 and other[0] in custom.keys():
                    custom[variable] = custom[other[0]]
                elif other[0] in custom.keys():
                    custom[variable].extend(other[1:])
                else:
                    custom[variable] = other

            
        analyze = []

        for elem in input_data[-1].lower().split():
            if elem in custom.keys():
                analyze.extend(custom[elem])
            else:
                analyze.append(elem)

        for elem in analyze:
            if elem == '+':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                sum = 0
                for elem2 in result:
                    sum += elem2
                result = [sum]
            elif elem == '-':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result = [result[0]-result[1]]
            elif elem == '*':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result = [result[0]*result[1]]
            elif elem == '/':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                if result[1] == 0:
                    raise ZeroDivisionError("divide by zero")
                result = [result[0]//result[1]]
            elif elem == 'dup':
                if len(result) < 1:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result.append(result[-1])
            elif elem == 'drop':
                if len(result) < 1:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result.pop(-1)
            elif elem == 'swap':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                temp = result[-1]
                result[-1] = result[-2]
                result[-2] = temp
            elif elem == 'over':
                if len(result) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                result.append(result[-2])
            else:
                result.append(int(elem))

    
    return result