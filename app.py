# app.py

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Não pode dividir por zero")
    return a / b

def saudacao(nome):
    return f"Olá, {nome}!"
