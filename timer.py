from functools import wraps
import time


def timer(func):
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Run time for {func.__name__} in {run_time:.6f} secs")
        return result
    return wrapper_timer