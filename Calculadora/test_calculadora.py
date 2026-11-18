
# ============================================
# TESTES AUTOMATIZADOS - CALCULADORA
# FRAMEWORK: PYTEST
# ============================================

import pytest

from Calculadora import somar, subtrair, multiplicar, dividir


# TESTES DE ADICAO

def test_somar_numeros_positivos():
    assert somar(10, 5) == 15


def test_somar_numero_negativo():
    assert somar(10, -5) == 5


# TESTES DE SUBTRACAO

def test_subtrair_resultado_positivo():
    assert subtrair(10, 5) == 5


def test_subtrair_resultado_negativo():
    assert subtrair(5, 10) == -5


# TESTES DE MULTIPLICACAO

def test_multiplicar_numeros_positivos():
    assert multiplicar(5, 4) == 20


def test_multiplicar_por_zero():
    assert multiplicar(10, 0) == 0


# TESTES DE DIVISAO

def test_dividir_resultado_decimal():
    assert dividir(10, 4) == pytest.approx(2.5)


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)
