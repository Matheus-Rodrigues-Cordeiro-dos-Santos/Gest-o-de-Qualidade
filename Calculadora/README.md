# Calculadora Matemática

## 1. Sobre o projeto

Este projeto foi desenvolvido para a disciplina de Gestão da Qualidade. Consiste em uma calculadora matemática simples, capaz de realizar as quatro operações básicas: adição, subtração, multiplicação e divisão.

O objetivo é aplicar conceitos de qualidade de software por meio da implementação de testes automatizados.

## 2. Tecnologias utilizadas

- **Linguagem:** Python
- **Framework de testes:** Pytest
- **Editor de código:** Visual Studio Code

## 3. Funcionalidades

- Adição de dois números.
- Subtração de dois números.
- Multiplicação de dois números.
- Divisão de dois números.
- Tratamento de erro para divisão por zero.

## 4. Testes automatizados

O projeto possui 8 testes automatizados, distribuídos entre as quatro operações matemáticas.

Os testes verificam:
- Resultados de operações com números positivos.
- Operações envolvendo números negativos.
- Multiplicação por zero.
- Resultado decimal da divisão.
- Tratamento de divisão por zero.

## 5. Como executar o projeto

### Instalar o Pytest

```bash
python -m pip install pytest
```

### Executar os testes

Dentro da pasta do projeto, execute:

```bash
python -m pytest -v
```

O resultado esperado é a aprovação dos 8 testes automatizados.

## 6. Estrutura do projeto

```text
Calculadora/
├── Calculadora.py
├── test_calculadora.py
├── README.md
└── .gitignore
```

## 7. Considerações finais

O projeto demonstra a aplicação de testes automatizados para verificar o funcionamento de operações matemáticas, identificar possíveis erros e contribuir para a qualidade do software.