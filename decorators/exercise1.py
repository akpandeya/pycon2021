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