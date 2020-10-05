def print_something():
    print("someting")

def function_that_returns_a_function():
    def a_function_that_is_returned():
        print("I have been returned from another function")
    return a_function_that_is_returned

def function_that_calls_a_func_that_is_an_arg(func):
    func()

print_something()
x = function_that_returns_a_function()
print(x)
x()

# This is effectively what happens with a decorator
# https://realpython.com/primer-on-python-decorators/
function_that_calls_a_func_that_is_an_arg(print_something)
