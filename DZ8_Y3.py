def type_logger(function):
    def position(*args):
        for item in args:
            print(f'{item}, {type(item)}')
            result = function(*args)
            return result
    return position

@type_logger
def calc_cube(x,z,w):
    return x * z * w


print(calc_cube(2,9,3))
