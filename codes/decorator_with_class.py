import functools
import time


def seconds(x):
    return f'{x} Seconds.'


def minutes(x):
    return f'{x / 60} Minutes.'


class Profile:
    def __init__(self, func, unit=seconds):
        self.unit = unit
        self.func = func

    def __call__(self, *args, **kwargs):
        # @functools.wraps(self.func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = self.func(*args, **kwargs)
            print(f'The function {self.func.__name__} has taken: {self.unit(time.time() - start_time)} to run.')
            return result
        return wrapper


@Profile
def fast_algorithm(gap):
    time.sleep(gap)

# @Profile(unit=minutes)
# def lazy_algorithm(gap):
#     time.sleep(gap)


if __name__ == '__main__' :
    fast_algorithm(0.25)
    # lazy_algorithm(5)


