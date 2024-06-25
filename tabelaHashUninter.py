# Criação das classes
class ElementoDaListaSimples:
    def __init__(self, chave=None, dado=None):
        self.chave = chave
        self.dado = dado
        self.proximo = None

class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None

    def inserir(self, chave, dado):
        nodo = ElementoDaListaSimples(chave, dado)
        if self.head is None:
            self.head = nodo
        else:
            nodo.proximo = self.head
            self.head = nodo

    def remover(self, chave):
        temp = self.head
        prev = None
        while temp is not None and temp.chave != chave:
            prev = temp
            temp = temp.proximo
        if temp is None:
            return False
        if prev is None:
            self.head = temp.proximo
        else:
            prev.proximo = temp.proximo
        return True

    def imprimir(self):
        temp = self.head
        while temp:
            print(f"{temp.chave}\t{temp.dado}")
            temp = temp.proximo

class TabelaHash:
    def __init__(self):
        self.tam = 10
        self.length = 0
        self.h = [ListaEncadeadaSimples() for _ in range(self.tam)]

    def hashFunc(self, k):
        if k == "DF":
            return 7
        return (ord(k[0]) + ord(k[1])) % self.tam

    def inserir(self, chave, dado):
        pos = self.hashFunc(chave)
        self.h[pos].inserir(chave, dado)

    def remover(self, chave):
        pos = self.hashFunc(chave)
        return self.h[pos].remover(chave)

    def imprimir(self):
        for i in range(self.tam):
            print(f"Posição {i}:", end="")
            if self.h[i].head is None:
                print("None")
            else:
                self.h[i].imprimir()
                print()




# Lista de estados com siglas e nomes
estados = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
    ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
    ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
    ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
    ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins"),
]

# Estado fictício
estado_ficticio = ("JR", "José Rech")

# Criando a tabela hash e inserindo estados
Teste = TabelaHash()
for sigla, nome in estados:
    Teste.inserir(sigla, nome)

# Inserindo o estado fictício na tabela hash
Teste.inserir(estado_ficticio[0], estado_ficticio[1])

# Programa principal interativo
while True:
    print('1 - Inserir na tabela hash')
    print('2 - Remover na tabela hash')
    print('3 - Listar a tabela hash')
    print('4 - Sair')

    op = int(input("Escolha uma opção: "))
    if op == 1:
        chave = input('Digite a sigla de um estado: ')
        dado = input('Digite o nome do estado: ')
        Teste.inserir(chave, dado)
    elif op == 2:
        chave = input('Digite a sigla que deseja remover: ')
        if Teste.remover(chave):
            print(f'{chave} removido com sucesso.')
        else:
            print(f'{chave} não encontrado.')
    elif op == 3:
        Teste.imprimir()
    elif op == 4:
        print('Encerrando...')
        break
    else:
        print("Selecione outra opção!\n")

