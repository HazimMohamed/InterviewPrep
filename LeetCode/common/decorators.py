from common.runtime import run_and_time
from typing import Callable


def print_time_func(func: Callable[[any], any]):
    def wrapper(*args, **kwargs):
        runtime = run_and_time(func, args, kwargs)
        print(f'Took {runtime}ns seconds to run {func.__name__}', end='')
        if args:
            print(' with args {}'.format(str(args)))
    return wrapper
