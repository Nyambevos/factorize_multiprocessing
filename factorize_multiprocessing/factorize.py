import logging
from multiprocessing import Pool, cpu_count
from time import time

def time_measurement(func):
    def inner(*args, **kwargs):
        start_t = time()
        result = func(*args, *kwargs)
        end_t = time()
        logging.debug(f'time: {end_t-start_t}')
        return result
    return inner

def find_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

@time_measurement
def factorize(*number):
    with Pool(processes=cpu_count()) as pool:
        return pool.map(find_factors, number)