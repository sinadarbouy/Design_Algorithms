import time

def timer_decorator(original_function):
    def wrapper_function(*args, **kwargs):
        start_time = time.time()
        result = original_function(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{original_function.__name__} ran in: {elapsed_time} sec")
        return result
    return wrapper_function

@timer_decorator
def example_function():
    time.sleep(2)  # Simulate a delay
    print("Function completed.")

example_function()
