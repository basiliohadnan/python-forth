import inspect, re

operations = {
    '+':    lambda x, y: [y + x],
    '-':    lambda x, y: [y - x],
    '*':    lambda x, y: [y * x],
    '/':    lambda x, y: [y // x],
    'dup':  lambda x:    [x, x],
    'drop': lambda _:    [],
    'swap': lambda x, y: [x, y],
    'over': lambda x, y: [y, x, y],
}

class StackUnderflowError(Exception):
    def __init__(self):
        super().__init__('Insufficient number of items in stack')
        
#removed DivisionByZero's custom exception.
        
def is_number(elem):
#preferred to use regex | accepts integer or float
    return bool(re.match(r'^-?\d+(\.\d+)?$', elem))

def apply(stack, element):
    if is_number(element):
        stack.append(int(element))
    elif element in operations:
        operation = operations[element]
        parameters_count = len(inspect.signature(operation).parameters)
        if len(stack) < parameters_count:
            #removed unnecessary print
            raise StackUnderflowError
        stack.extend(operation(*(stack.pop() for x in range(parameters_count))))
    else:
        raise ValueError('undefined operation')


def substitute(custom_operations, elements):
#used list comprehension instead of generator expression inside chain 
#(removed chain, as well)
#then avoided multiple dictionary lookups. 
    result = []
    for x in elements:
        if x in custom_operations:
            result.extend(custom_operations[x])
        else:
            result.append(x)
    return result

def evaluate(input_data):
    stack = []
    custom_operations = {}
    try:
        for line in input_data:
            elements = line.lower().split()
            if elements[0] == ':':
                assert elements[-1] == ';'
                op = elements[1]
                if is_number(op):
                    raise ValueError('illegal operation')
                custom_operations[op] = substitute(custom_operations, elements[2:-1])
            else:
                elements = substitute(custom_operations, elements)
                for element in elements:
                    apply(stack, element)
        return stack
    except ZeroDivisionError:
        raise ZeroDivisionError('divide by zero') 