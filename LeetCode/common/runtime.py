import matplotlib.pyplot as plt
import time
from math import floor


def run_and_time(func, args, kwargs):
    start = time.process_time_ns()
    func(*args, **kwargs)
    end = time.process_time_ns()
    return floor(end - start)


def plot_runtime(func, input_generator, max_range, increment):
    run_times = []
    in_gen = input_generator(max_range, increment)
    for new_input in in_gen:
        runtime = run_and_time(func, args=(*new_input,), kwargs=None)
        run_times.append(runtime)
    plt.plot(range(0, max_range, increment), run_times)
    plt.show()
