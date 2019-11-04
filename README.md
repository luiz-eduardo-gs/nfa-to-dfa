# NFA-to-DFA

Aluno: Luiz Eduardo Gonçalves Silva

Data: 04/11/2019

Trabalho 01 - LFA 

# Requisitos do sistema:

Sistema operacional: Windows (x86) / Windows (x64) / Mac OS / Linux (Qualquer sistema operacional que tenha suporte ao Python)

Python: --version 2.x/3.x/Superior

# Como usar o programa:

0) No diretório onde está contido o arquivo 'main.py', abra o prompt de comando (Windows) / linux shell (Linux), e digite o seguinte comando:

```
    $ python main.py
```

1) Digite o nome do arquivo teste (incluindo .txt), cujo esquema está detalhado abaixo, e o programa fará a conversão de NFA para DFA e essa será a saída do programa.

# ENTRADA:

O arquivo de teste deve estar no seguinte formato:
quantidade de estados

simbolos

conjunto de estados finais

estado inicial

transição 1

transição 2

transição n

Ex.:

    3 
    ab 
    q1 q2 
    >q0 
    q0 a q0
    q0 b q0
    q0 a q1
    q1 b q2

OBS:

    Pode ser usado qualquer símbolo, porém os estados devem ser declarados como acima. Do contrário, o programa não irá funcionar.