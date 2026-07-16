# marcos-randtools

Biblioteca para geração de listas numéricas aleatórias, desenvolvida com foco em aplicações matemáticas, testes lógicos e ensino de programação.

---

## Sobre o Projeto
A biblioteca `marcos_randtools` oferece uma interface simples para encapsular lógicas de sorteio, validações estruturais e laços de repetição. O objetivo é fornecer uma ferramenta leve para gerar conjuntos de dados aleatórios, mantendo a integridade matemática das operações, sem a necessidade de reescrever funções de validação em cada novo projeto.

## Como Utilizar (Parâmetros e Exemplos)

A função principal da biblioteca é a `randlist`, que aceita até quatro parâmetros para personalizar a sua lista de números:

### Parâmetros:
* size (int): A quantidade de números que você deseja gerar na lista.
* max_val(int ou float)*: O valor máximo que um número sorteado pode atingir (o sorteio ocorre sempre de 1 até `max_val`).
* allow_duplicates(bool, opcional, padrão=False): Se definido como `True`, permite que os números se repitam na lista.
*  Se `False`, garante exclusividade total (todos os números serão diferentes).
* use_floats (bool, opcional, padrão=False)*: Se definido como `True`, gera números reais (com casas decimais). Se `False`, gera apenas números inteiros.

---

### Exemplos Práticos

Abaixo, veja 4 cenários de uso, do mais básico até o tratamento de exceções matemáticas:

#### 1. Uso Básico (Sorteio Simples)
Gera uma lista de inteiros exclusivos. Excelente para sorteios estilo "loteria" ou amostragem de dados únicos.
```python
from marcos_randtools import randlist

# Gerando 6 números únicos entre 1 e 60
sorteio = randlist(size=6, max_val=60) ou sorteio = randlist(6,60)

print(sorteio)
# Possível saída: [12, 45, 7, 58, 23, 31]
---------------------------------------------------------------------------
from marcos_randtools import randlist

# Simulando 10 lançamentos de um dado de 6 faces
lancamentos = randlist(size=10, max_val=6, allow_duplicates=True) ou lancamentos = randlist(10,6,True)

print(lancamentos)
# Possível saída: [3, 6, 1, 3, 2, 6, 5, 1, 4, 3]
----------------------------------------------------------------------------
from marcos_randtools import randlist

# Gerando 3 valores reais entre 1 e 10
valores_reais = randlist(size=3, max_val=10, use_floats=True) ou valores_reais = randlist(3,10,False,True)

print(valores_reais)
# Possível saída: [7.34512, 1.98345, 4.56789]
-----------------------------------------------------------------------------
from marcos_randtools import randlist

# Tentando gerar 10 números ÚNICOS entre 1 e 5 (Impossível na matemática)
try:
    erro_matematico = randlist(size=10, max_val=5)
except ValueError as erro:
    print("Erro capturado:", erro)

# Saída garantida: 
# Erro capturado: Impossible to generate 10 unique integers within a limit of 5.
---------------------------------------------------------------------------------
## Instalação
Para instalar a biblioteca em seu ambiente de desenvolvimento, utilize o gerenciador de pacotes padrão do Python:

```bash
pip install marcos-randtools
