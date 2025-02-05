def meu_decorador(funcao):
    def wrapper():
        print("Algo está acontecendo antes da função ser chamada.")
        funcao()
        print("Algo está acontecendo após a função ser chamada.")
    return wrapper

@meu_decorador
def diz_oi():
    print("Oi!")

diz_oi()

from functools import wraps

def decorador_com_parametros(*decor_args, **decor_kwargs):
    def decorador(funcao):
        @wraps(funcao)
        def wrapper(*args, **kwargs):
            print(f"Parâmetros do decorador: {decor_args}, {decor_kwargs}")
            return funcao(*args, **kwargs)
        return wrapper
    return decorador

@decorador_com_parametros("foo", "bar", baz="qux")
def soma(x, y):
    return x + y

# Chamando a função decorada:
print(soma(2, 3))