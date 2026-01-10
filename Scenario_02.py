#  Logging DecoratorTask: Create a decorator @log_execution_time
# that logs the time taken to execute a function.
# Use it to log the runtime of a sample function calculate_sum(n)
# that returns the sum of numbers from 1 to n.


#####################################    ANSWER     #####################################



import time #imported time package from python Library.
from functools import wraps

def log_execution_time(func):     # This decorator checks how much time a function takes to run.
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()    # here we Store start time.
        result = func(*args, **kwargs)  # Call the original function (line num- 4)
        end_time = time.time()  # Store the end time.

        execution_time = end_time - start_time # Calculate the total time in execution_time variable.
        print(f"Function {func.__name__} executed in {execution_time:.4f} seconds") #4f = we take only 4 decimals only.
        return result   #calls result
    return wrapper  # Calls wrapper

@log_execution_time
def calculate_sum(n):
    return sum(range(1, n + 1)) # This function returns sum of numbers from 1 to n(user)

# Random Example usage and Calling the function to see execution time
print(calculate_sum(100000))  # Logs execution time and returns 5000050000

