class Endereço:
    def __init__(self, rua, numero, bairro, cidade):
        self.__rua = rua
        self.__numero = int(numero)
        self.__bairro = bairro
        self.__cidade = cidade
    
    def get_rua(self):
        return self.__rua
    
    def get_numero(self):
        return self.__numero

    def get_bairro(self):
        return self.__bairro
    
    def get_cidade(self):
        return self.__cidade

    def exibir_dados(self):
        return f'Rua: {self.__rua}, numero: {self.__numero}; \nBairro: {self.__bairro} \nCidade {self.__cidade}'


class Cliente:
    def __init__(self, nome, cpf, endereço):
        self.__nome = nome
        self.__cpf = cpf
        self.__endereço = endereço
        self.__contas = []
    
    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_endereco(self):
        return self.__endereço
    
    def adicionar_conta(self, cnt):
        self.__contas.append(cnt)
    
    def exibir_dados(self):
        return f'Nome: {self.__nome} \nCPF: {self.__cpf} \nEndereço: {self.__endereço}'

class ContaBancaria:
    numeros_contas = []
    def __init__(self, titular, numero, saldo):
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo

        ContaBancaria.numeros_contas.append()
    def get_titular(self):
        return self.__titular.get_nome()
    
    def get_numero(self):
        return self.__numero
    
    def get_saldo(self):
        return self.__saldo
    
    def exibir_dados(self):
        return f"CONTA:\nTitular: {self.__titular.get_nome()}\nNumero da conta: {self.__numero}\nSaldo: R$ {self.__saldo}\nCpf: {self.__titular.get_cpf()} \n\nENDEREÇO:\n{self.__titular.get_endereco().exibir_dados()}"
    
    def depositar(self, value):
        if value <= 0:
            return False
        self.__saldo += value                                            
        return True

    def sacar(self, value):
        if value <= 0:
            return False
        self.__saldo -= value
        return True
    def transferir(self, valor, conta_destino):
        if valor > 0:
            self.__saldo -= valor
            conta_destino.depositar(valor)
            return True
        else:
            return False       
    @classmethod
    def contas_duplicadas(cls):
        repetidos = set()
        n_repetidos = []
        for x in cls.numeros_contas:
            if ContaBancaria.numeros_contas.count(x) > 1:
                repetidos.add(x)
            else:
                n_repetidos.append(x)
        return f'{repetidos}'
    @classmethod
    def verificar_conta_duplicada(cls):
        return len(cls.numeros_contas) != len(set(cls.numeros_contas))
    
class ContaCorrente(ContaBancaria):
    def __init__(self, titular, numero, saldo, limite, tarifa_mensal):
        super().__init__(titular, numero, saldo)
        self.__limite = limite
        self.__tarifa_mental = tarifa_mensal
    def exibir_dados(self):
        return f"{self.__titular}\n{self.__numero}\n{self.__saldo}\n{self.__limite}\n{self.__tarifa_mental}"
    def sacar(self, value: float):
        super.sacar(self.__limite)
        if value <= 0:
            return False
        self.__saldo -= value
        return True
    
class contapoupança(ContaBancaria):
    def __init__(self, titular, numero, saldo, taxa_rendimento):
        super().__init__(titular, numero, saldo)
        self.__taxa_rendimento = taxa_rendimento
    def exibir_dados(self):
        return f"{self.__titular}\n{self.__numero}\n{self.__saldo}\n{self.__taxa_rendimento}"
