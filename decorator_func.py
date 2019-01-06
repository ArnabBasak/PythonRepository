"""decorators"""
import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__+"took"+str((end-start)*1000) + "mil second")
        return result
    return wrapper
@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result
@time_it          
def cal_cube(numbers):
    result = []
    for number in numbers:
          result.append(number * number * number)
    return result
        
