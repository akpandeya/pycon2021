import functools
import time
from functools import lru_cache
import random
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
        value = func(*args, **kwargs)
        print("AFTER")
        return value
    return wrapper

@before_and_after
def adder(num1, num2):
    return num1 + num2

adder(3, 10)

def define(func):
    print(f"Defining {func.__name__}") # Runs only at the definintion of the function
    return func

@define
def roll_dice():
    return random.randint(1,6)

# How to ensure that name of the function is not changed by decorator
def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        
        return (func(*args, **kwargs), func(*args, **kwargs))
    return wrapper
FUNCTIONS = {}
@define
@do_twice
def roll_dice():
    return random.randint(1,6)

# Order may matter

# State in decorator

class BeforeAndAfter:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
    
    def __call__(self, *args, **kwargs):
        print("Before")
        value = self.func(*args, **kwargs)
        print ("After")
        
        return value
    
@BeforeAndAfter
def greet(name):
    print(name)
greet("akp")