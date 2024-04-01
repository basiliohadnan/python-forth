import inspect, re

OPS = {
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
#preferred to use regex
    return bool(re.match(r'^-?\d+(\.\d+)?$', elem))

def apply(stack, elem):
    if is_number(elem):
        stack.append(int(elem))
    elif elem in OPS:
        op = OPS[elem]
        count = len(inspect.signature(op).parameters)
        if len(stack) < count:
            #removed unnecessary print
            raise StackUnderflowError
        stack.extend(op(*(stack.pop() for x in range(count))))
    else:
        raise ValueError('undefined operation')

#used list comprehension instead of 
#generator expression inside chain and
#avoided multiple dictionary lookups. 
def substitute(custom, elems):
    result = []
    for x in elems:
        if x in custom:
            result.extend(custom[x])
        else:
            result.append(x)
    return result

def evaluate(input_data):
    stack = []
    custom = {}
    try:
        for line in input_data:
            elems = line.lower().split()
            if elems[0] == ':':
                assert elems[-1] == ';'
                op = elems[1]
                if is_number(op):
                    raise ValueError('illegal operation')
                custom[op] = substitute(custom, elems[2:-1])
            else:
                elems = substitute(custom, elems)
                for elem in elems:
                    apply(stack, elem)
        return stack
    except ZeroDivisionError:
        raise ZeroDivisionError('divide by zero') 