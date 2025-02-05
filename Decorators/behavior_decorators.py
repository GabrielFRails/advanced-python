from functools import wraps

def env_log(tipo):
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if tipo == "debug":
                print(f"Debug: {func.__name__}() with {args} and {kwargs}")
            elif tipo == "production":
                pass
            return func(*args, **kwargs)
        return wrapper
    return decorador

@env_log("debug")
def add(x, y):
    return x + y

print(add(1, 2))

@env_log("production")
def mult(x, y):
    return x * y

print(mult(3, 4))