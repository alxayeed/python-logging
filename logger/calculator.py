import logging

# logger configuration
logging.basicConfig(level=logging.DEBUG)


def add(x, y):
    """adds 2 numbers"""
    logging.debug(f'adding {x} and {y}')
    return x + y

def substract(x, y):
    """substraction between 2 numbers"""
    logging.debug(f'subtracting {y} from {x}')
    return x - y

def multiply(x, y):
    """multiplication of 2 numbers"""
    return x * y


result = add(10, 5)
print(result)
print(substract(20, 7))