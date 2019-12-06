terminal = ['piloto', 'oficial1', 'oficial2', 'chefe de servico', 'comissaria1', 'comissaria2', 'policial', 'presidiario']
aviao = []

def terminal_para_aviao(motorista, passageiro):
    print(f'\033[1;33mPessoas no terminal:\033[m \n{terminal}')
    terminal.remove(motorista)
    terminal.remove(passageiro)
    print(f'\033[1;32mO motorista: {motorista}, Passageiro: {passageiro} indo no fortwo para avião\033[m')
    aviao.append(motorista)
    aviao.append(passageiro)
    print(f'\033[1;32mO motorista: {motorista}, passageiro: {passageiro} no avião\033[m')
    print(f'\033[1;33mPessoas que estão no terminal:\033[m \n{terminal}')

def aviao_para_terminal(motorista):
    print(f'\033[1;33mPessoas no avião:\033[m\n{aviao}')
    aviao.remove(motorista)
    print(f'\033[1;32mO motorista: {motorista} saindo do avião...\033[m')
    terminal.append(motorista)

