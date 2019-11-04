import sys
from finite_automata import NFA, DFA


if sys.version_info >= (3, 0):
    filename = input('Entre com o nome do arquivo NFA: ')
elif sys.version_info >= (2, 0):
    filename = raw_input('Entre com o nome do arquivo NFA: ')
else:
    print("Por favor, utilize uma versão do python superior a 2.x")
    quit()

file = open(filename, 'r')
lines = file.readlines()
file.close()

nfa = NFA()
dfa = DFA()

nfa.construct_nfa_from_file(lines)
dfa.convert_from_nfa(nfa)
print('NFA to DFA:')
dfa.print_dfa()