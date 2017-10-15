
import time


def seconds(x):
    return f'{x} Seconds.'


def profile(*args, unit=seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            print(f'The function {func.__name__} has taken: {unit(time.time() - start_time)} to run.')
            return result
        return wrapper

    if args:
        return decorator(args[0])

    return decorator


@profile
def fast_algorithm(gap):
    time.sleep(gap)


@profile(unit=lambda x: f'{x / 60} Minutes.')
def lazy_algorithm(gap):
    time.sleep(gap)

if __name__ == '__main__':
    fast_algorithm(1.4)
    lazy_algorithm(5)
