# A - Criação da lista encadeda simples, nodo representando um cartão numerado contendo: número, cor e um ponteiro para o próximo
class ListaEncadeadaSimples:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None
# Ponteiro para a cabeça da lista(head)
class Fila:
    def __init__(self):
        self.head = None


# B - Criação da funcão inserirSemPrioridade()
def inserirSemPrioridade(fila, nodo):
    # Andar pela lista a paritr da cabeça(head) e inserir o nodo no final da lista
    if fila.head is None:
        fila.head = nodo
    else:
        aux = fila.head
        while aux.proximo is not None:
            aux = aux.proximo
        aux.proximo = nodo


# C - Criação da funcão inserirComPrioridade()
def inserirComPrioridade(fila, nodo):
    if fila.head is None or fila.head.cor == nodo.cor:
        nodo.proximo = fila.head
        fila.head = nodo
    else:
        anterior = None
        atual = fila.head
        while atual is not None and atual.cor != nodo.cor:
            anterior = atual
            atual = atual.proximo
        if atual is not None:
            nodo.proximo = atual
            if anterior is not None:
                anterior.proximo = nodo


# D - Criação da função inserir()
def inserir(fila):
    # Solicitando ao usuário a cor e o número do cartão e criando um nodo com os dados fornecidos
    cor = input("Por favor digite a cor do cartão: A(amarelo) ou V(verde): ")
    numero = int(input("Agora digite o número do cartão: "))
    novo_nodo = ListaEncadeadaSimples(numero, cor)
    # Se a lista estiver vazia, o head apontará para o nodo criado, senão se a cor for V chamará a função inserirSemPrioridade(), ou se a cor for A
    # chamará a função inserirComPrioridade()
    if fila.head is None:
        fila.head = novo_nodo
    elif novo_nodo.cor == "V":
        inserirSemPrioridade(fila, novo_nodo)
    else:
        inserirComPrioridade(fila, novo_nodo)


#  E - Criação da função imprimirListaEspera()
def imprimirListaEspera(fila):
    if fila.head is None:
        print("No momento a fila está vazia")
    else:
        aux = fila.head
        while aux is not None:
            print(f"Cartão número: {aux.numero} | Cor: {aux.cor}")
            aux = aux.proximo


# F - Criação da função atenderPaciente()
def atenderPaciente(fila):
    if fila.head is None:
        print("No momente a fila esta vazia")
    else:
        paciente = fila.head
        fila.head = fila.head.proximo
        print(f"Paciente de número: {paciente.numero} com o cartão de cor: {paciente.cor} favor se apresentar para atendimento")


#  G - Função para mostrar o menu principal
def menu():
    while True:
        print("-----------Menu-----------")
        print("1 - Adicionar pacientes à fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")

        opcao = int(input("Por favor digite sua opção: "))

        if opcao == 1:
            inserir(fila)
        elif opcao == 2:
            imprimirListaEspera(fila)
        elif opcao == 3:
            atenderPaciente(fila)
        elif opcao == 4:
            break
        else:
            print("Opção inválida")


# Inicializando a fila e executando o menu
fila = Fila()
menu()


