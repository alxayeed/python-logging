import logging

# logger configuration
logging.basicConfig(filename='logfile.log' ,level=logging.DEBUG)


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

def division(x, y):
    """divide a number with another"""
    try:
        return x / y
    except ZeroDivisionError as e:
        logging.error(f'dividing {x} by {y}')


# result = add(10, 5)
# print(result)
print(division(21, 0))