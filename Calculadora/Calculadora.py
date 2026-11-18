
# ============================================
# PROJETO: CALCULADORA MATEMATICA
# DISCIPLINA: GESTAO DA QUALIDADE
# ============================================

# Funcao de adicao
def somar(a, b):
    return a + b


# Funcao de subtracao
def subtrair(a, b):
    return a - b


# Funcao de multiplicacao
def multiplicar(a, b):
    return a * b


# Funcao de divisao
def dividir(a, b):
    if b == 0:
        raise ValueError("Nao e permitido dividir por zero.")

    return a / b
