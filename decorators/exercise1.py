import random
import functools

def before_and_after(func):
    def wrapper(*args, **kwargs):
        print("BEFORE")
        func(*args, **kwargs)
        print("AFTER")
    return wrapper

@before_and_after
def greet(name, printer=print):
    printer(f"Hi {name}!")
    
def do_twice(func):
    def wrapper(*args, **kwargs):
        
        return (func(*args, **kwargs), func(*args, **kwargs))
    return wrapper


@do_twice
@do_twice
def roll_dice():
    return random.randint(1,6)

FUNCTIONS = {}

def register(func):
    FUNCTIONS[func.__name__] = func
    return func
@register
def roll_dice():
    return random.randint(1,6)

def retry(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        while(True):
            try:
                return func(*args, **kwargs)
                break
            except Exception as e:
                print (f"Retrying {e}")
    return wrapper
    
@retry
def only_roll_sixes():
    number = random.randint(1,6)
    if number != 6:
        raise ValueError(number)
    return number

def retry(exception):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            while(True):
                try:
                    return func(*args, **kwargs)
                    break
                except Exception as e:
                    print (f"Retrying {e}")
        return wrapper
    return decorator

@retry(ValueError)
def calculation():
    number = random.randint(-5, 5)
    if abs(1/number) > 0.2:
        raise ValueError(number)
    return number

def retry(max_retries):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            tries = 1
            while(tries < max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print (f"Retrying {e}")
            raise Exception("Max tries exhasted")
        return wrapper
    return decorator

retry(3)
def calculation():
    number = random.randint(-5, 5)
    if abs(1/number) > 0.2:
        raise ValueError(number)
    return number

class Retry:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.tries = 0
    
    def __call__(self, *args, **kwargs):
        while True:
            try:
                return self.func(*args, **kwargs)
            except Exception as e:
                
                self.tries += 1
                print (f"Retries {self.tries}")

@Retry
def only_roll_sixes():
    number = random.randint(1,6)
    if number != 6:
        raise ValueError(number)
    return number