import time
from functools import lru_cache

# Example of use of decorator
@lru_cache()
def slow_square(number):
    print(f"Sleeping for {number} seconds")
    
    time.sleep(number)
    return number **2
# Functions can be passed around as arguments
def greet(name, printer=print):
    printer(f"Hi {name}!")


def tnirp(text):
    print(text[::-1])

# Create function at runtime
def prefix_factory(prefix):
    def prefix_printer(text):
        print(f"{prefix} : {text}")
    
    return prefix_printer

debug = prefix_factory("DEBUG")

#Example of a decorator
def reverse_factory(func):
    def reverse_caller(text):
        func(text[::-1])
    return reverse_caller
reverse_print = reverse_factory(print)
reverse_print("Hell Akp")

reverse_tnirp = reverse_factory(tnirp)
reverse_tnirp("Hello")

reverse_debug = reverse_factory(debug)

reverse_debug("Hello")

# This can be achieved with syntactic sugar: 
# greet = reverse_factory(greet)
@reverse_factory
def greet(name, printer=print):
    printer(f"Hi {name}!")
greet("Hello")

def params(*args, **kwargs):
    print(f"args = {args}")
    print(f"kwargs = {kwargs}")
    


def before_and_after(func):
    def wrapper(*args, **kwargs):
        print("BEFORE")
        func(*args, **kwargs)
        print("AFTER")
    return wrapper
@before_and_after
def adder(num1, num2):
    return num1 + num2

adder(3, 10)