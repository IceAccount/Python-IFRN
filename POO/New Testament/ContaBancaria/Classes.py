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
    
    def possui_contas(self):
        return len(self.__contas) > 0
        
    def buscar_conta(self,numero):
        for n in self.__contas:
            if n.get_numero() == numero:
                return f"{n.get_cliente().get_nome()} tem a conta {n.get_numero()}"
        return None
        
    def consultar_saldo_total(self):
        saldo_total = 0 
        for n in self.__contas:
            saldo_total += n.get_saldo()
        return saldo_total
    

class ContaBancaria:
    numeros_contas = []
    contas_duplicada = []
    def __init__(self,cliente,numero,saldo):
        self.__cliente = cliente 
        self.__numero =  numero
        self.__saldo = saldo
        ContaBancaria.numeros_contas.append(self.__numero)
    @classmethod
    def existe_conta_duplicada(cls):
        return len(cls.numeros_contas) != len(set(cls.numeros_contas))
        
    @classmethod
    def contas_duplicadas(cls):
        vistos = set()
        for numero in cls.numeros_contas:
            if numero in vistos:
                cls.contas_duplicada.append(numero)
            else:
                vistos.add(numero)
        return cls.contas_duplicada
        
    def get_cliente(self):
        return self.__cliente
    
    def get_numero(self):
        return self.__numero

    def get_saldo(self):
        return self.__saldo
        
    def set_saldo(self,valor):
        self.__saldo = valor 
        
    def get_tipo_conta(self):
        return "Conta Bancária"
        
    def depositar(self,valor):
        self.__saldo += valor
        return True
        
    def sacar(self,valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            return True
        else:
            return False
            
    def transferir(self,valor,destino):
            if self.sacar(valor):
                destino.depositar(valor)
                return True
            else:
                return False

    def exibir_dados(self):
        return (f"{self.__cliente.exibir_dados()}\n"
                f"=== CONTA ===\n"
                f"Número: {self.get_numero()}\n"
                f"Saldo: {self.get_saldo():.2f}R$")
    
class ContaCorrente(ContaBancaria):
    def __init__(self, cliente, numero, saldo,limite,tarifa_mensal):
        super().__init__(cliente, numero, saldo)
        self.__limite = limite
        self.__tarifa_mensal = tarifa_mensal
        
    def sacar(self,valor:float) -> float: 
        if valor <= (self.__limite + self._ContaBancaria__saldo) and self._ContaBancaria__saldo >= -(self.__limite):
            self._ContaBancaria__saldo -= valor
            return True
        else:
            return False
            
    def cobrar_taxa(self):
        self.sacar(self.__tarifa_mensal)
        
    def get_tipo_conta(self):
        return "Conta Corrente"
        
    def exibir_dados(self):
        return f'{super().exibir_dados()}\nLimite:{self.__limite:.2f}R$\nTarifa:{self.__tarifa_mensal:.2f}R$'
    
class ContaPoupanca(ContaBancaria):
    def __init__(self, cliente, numero, saldo,taxa_rendimento):
        super().__init__(cliente, numero, saldo)
        self.__taxa_rendimento = taxa_rendimento
    def get_tipo_conta(self):
        return 'Conta Poupança'
    def render_juros(self):
        self._ContaBancaria__saldo += self.__taxa_rendimento * self._ContaBancaria__saldo
        return None
    def exibir_dados(self):
         return f"{super().exibir_dados()}\nTaxa:{self.__taxa_rendimento}"
    
class ContaSalario(ContaBancaria):
    def __init__(self, cliente, numero, saldo,empresa,saques_realizados,limite_saques):
        super().__init__(cliente, numero, saldo)
        self.__empresa = empresa
        self.__saques_realizados = saques_realizados
        self.__limite_saques = limite_saques

    def get_tipo_conta(self):
        return "Conta Salário"
