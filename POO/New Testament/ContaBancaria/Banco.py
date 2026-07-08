import tkinter as tk
from tkinter import messagebox, simpledialog
from Classes import Cliente, ContaBancaria, Endereço, ContaCorrente, ContaPoupanca, ContaSalario

class BancoApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema Bancário - POO em Python")
        self.janela.geometry("1080x700")

        endereço1 = Endereço("Enfermaria", 3, "Esquerda superior", "Skeld")
        endereço2 = Endereço("Laboratório", 4, "Direita superior", "Polus outpost")
        
        cliente1  = Cliente("Ciano", "004.045", endereço1)
        cliente2 = Cliente("Lima", "023.450", endereço2)        

        self.contas = [
            ContaCorrente(cliente1, 1001, 500, 1000, 100),
            ContaPoupanca(cliente2, 1002, 1000, 0.1)
        ]

        # messagebox.showinfo("Sucesso", "Depósito realizado.")

        self.criar_interface()

    def criar_interface(self):
        titulo = tk.Label(
            self.janela,
            text="Banco Python - Contas Bancárias",
            font=("Arial", 18, "bold"),
        )
        titulo.pack(pady=15)

        btn_criar = tk.Button(
            janela,
            text="Pesquisar clientes",
            width=15,
            command=lambda: self.get_cliente()
        )
         # btn_depositar.config(state="disabled")
        btn_criar.pack(pady=2)

        btn_criar = tk.Button(
            janela,
            text="Criar conta",
            width=15,
            command=lambda: self.criar_conta()
        )
         # btn_depositar.config(state="disabled")
        btn_criar.pack(pady=2)

        self.frame_contas = tk.Frame(self.janela)
        self.frame_contas.pack()

        self.atualizar_tela()

    def atualizar_tela(self):
        for widget in self.frame_contas.winfo_children():
            widget.destroy()

        for conta in self.contas:
            frame = tk.Frame(
                self.frame_contas,
                borderwidth=2,
                relief="groove",
                padx=10,
                pady=10
            )
            frame.pack(side="left", padx=10, pady=10)

            lbl_titular = tk.Label(
                frame,
                text=conta.get_titular(),
                font=("Arial", 14, "bold")
            )
            lbl_titular.pack()

            lbl_numero = tk.Label(
                frame,
                text=f"Conta: {conta.get_numero()}",
                font=("Arial", 14, "bold")
            )
            lbl_numero.pack()

            lbl_tipo = tk.Label(
                frame,
                text=f"Conta: {conta.get_tipo_conta()}",
                font=("Arial", 14, "bold"),
            )
            lbl_tipo.pack()


            lbl_saldo = tk.Label(
                frame,
                text=f"Saldo: R$ {conta.get_saldo():.2f}",
                font=("Arial", 12)
            )
            lbl_saldo.pack(pady=5)

            btn_depositar = tk.Button(
                frame,
                text="Depositar",
                width=15,
                command=lambda c=conta: self.depositar(c)
            )
            # btn_depositar.config(state="disabled")
            btn_depositar.pack(pady=2)

            btn_sacar = tk.Button(
                frame,
                text="Sacar",
                width=15,
                command=lambda c=conta: self.sacar(c)
            )
            # btn_sacar.config(state="disabled")
            btn_sacar.pack(pady=2)

            btn_transferir = tk.Button(
                frame,
                text="Transferir",
                width=15,
                command=lambda c=conta: self.transferir(c)
            )
            # btn_transferir.config(state="disabled")
            btn_transferir.pack(pady=2)

            btn_dados = tk.Button(
                frame,
                text="Exibir Dados",
                width=15,
                command=lambda c=conta: self.exibir_dados(c)
            )
            # btn_dados.config(state="disabled")
            btn_dados.pack(pady=2)

            btn_rendimento = tk.Button(
                frame,
                text="Render Juros",
                width=15,
                command=lambda c=conta: self.render_juros(c)
            )
           # btn_rendimento.config(state="disabled")
            btn_rendimento.pack(pady=2)

            btn_taxa = tk.Button(
                frame,
                text="Cobrar Taxa",
                width=15,
                command=lambda c=conta: self.cobrar_taxa(c)
            )
            #btn_taxa.config(state="disabled")
            btn_taxa.pack(pady=2)

    def criar_conta(self):
        janela_cadastro = tk.Toplevel(self.janela)
        janela_cadastro.title("Criar nova conta")
        janela_cadastro.geometry("300x490")
        janela_cadastro.resizable(False, False)

        tk.Label(janela_cadastro, text="Titular:").pack(pady=5)
        entrada_titular = tk.Entry(janela_cadastro)
        entrada_titular.pack()

        tk.Label(janela_cadastro, text="CPF:").pack(pady=5)
        entrada_cpf = tk.Entry(janela_cadastro)
        entrada_cpf.pack()

        tk.Label(janela_cadastro, text="Número da conta:").pack(pady=5)
        entrada_numero = tk.Entry(janela_cadastro)
        entrada_numero.pack()

        tk.Label(janela_cadastro, text="Saldo inicial:").pack(pady=5)
        entrada_saldo = tk.Entry(janela_cadastro)
        entrada_saldo.pack()

        tk.Label(janela_cadastro, text="Rua:").pack(pady=5)
        entrada_rua = tk.Entry(janela_cadastro)
        entrada_rua.pack()

        tk.Label(janela_cadastro, text="Número da residência:").pack(pady=5)
        entrada_numero_rua = tk.Entry(janela_cadastro)
        entrada_numero_rua.pack()

        tk.Label(janela_cadastro, text="Bairro:").pack(pady=5)
        entrada_bairro = tk.Entry(janela_cadastro)
        entrada_bairro.pack()

        tk.Label(janela_cadastro, text="Cidade:").pack(pady=5)
        entrada_cidade = tk.Entry(janela_cadastro)
        entrada_cidade.pack()

        def salvar_conta():
            titular = entrada_titular.get()
            cpf = entrada_cpf.get()
            numero = entrada_numero.get()
            saldo = entrada_saldo.get()
            rua = entrada_rua.get()
            numero_residencia = entrada_numero_rua.get()
            bairro = entrada_bairro.get()
            cidade = entrada_cidade.get()

            if titular == "" or numero == "" or saldo == "" or rua == "" or numero_residencia == "" or cpf == "" or bairro == "" or cidade == "":
                messagebox.showerror("Erro", "Preencha todos os campos.")
                return

            try:
                numero = int(numero)
                saldo = float(saldo)
                numero_residencia = int(numero_residencia)
                cpf = float(cpf)
            except ValueError:
                messagebox.showerror("Erro", "Cpf, número da conta, saldo e número de residência devem ser valores numéricos.")
                return

            cliente = Cliente(titular, cpf, Endereço(rua, numero_residencia, bairro, cidade))
            nova_conta = ContaBancaria(cliente, numero, saldo)
            self.contas.append(nova_conta)

            messagebox.showinfo("Sucesso", "Conta criada com sucesso.")

            janela_cadastro.destroy()
            self.atualizar_tela()

        btn_salvar = tk.Button(
            janela_cadastro,
            text="Salvar conta",
            width=15,
            command=salvar_conta
        )
        btn_salvar.pack(pady=15)
    def depositar(self, conta):
        valor = simpledialog.askfloat("Depósito", "Digite o valor do depósito:")

        if valor is not None:
            if conta.depositar(valor):
                messagebox.showinfo("Sucesso", "Depósito realizado.")
            else:
                messagebox.showerror("Erro", "Valor inválido.")

        self.atualizar_tela()

    def sacar(self, conta):
        valor = simpledialog.askfloat("Saque", "Digite o valor do saque:")

        if valor is not None:
            if conta.sacar(valor):
                messagebox.showinfo("Sucesso", "Saque realizado.")
            else:
                messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido.")

        self.atualizar_tela()

    def transferir(self, conta_origem):
        valor = simpledialog.askfloat("Transferência", "Digite o valor:")

        if valor is None:
            return

        numero_destino = simpledialog.askinteger(
            "Transferência",
            "Digite o número da conta destino:"
        )

        conta_destino = None

        for conta in self.contas:
            if conta.get_numero() == numero_destino:
                conta_destino = conta
                break

        if conta_destino is None:
            messagebox.showerror("Erro", "Conta destino não encontrada.")
            return

        if conta_origem == conta_destino:
            messagebox.showerror("Erro", "Não é possível transferir para a mesma conta.")
            return

        if conta_origem.transferir(valor, conta_destino):
            messagebox.showinfo("Sucesso", "Transferência realizada.")
        else:
            messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido.")

        self.atualizar_tela()

    def exibir_dados(self, conta):
        messagebox.showinfo("Dados da Conta", conta.exibir_dados())

    def render_juros(self, conta):
        if(conta.get_tipo_conta() == "Conta Poupança"):
            conta.render_juros()
            messagebox.showerror("Sucesso", "Rendimento efetuado.")
        else:
            messagebox.showerror("Erro", "Conta não disponibiliza rendimento")
    
    def cobrar_taxa(self, conta):
        if(conta.get_tipo_conta() == "Conta Corrente"):
            conta.cobrar_taxa()
            messagebox.showerror("Sucesso", "Rendimento efetuado.")
        else:
            messagebox.showerror("Erro", "Cobrança invalida para essa conta")
        self.atualizar_tela()



janela = tk.Tk()
app = BancoApp(janela)
janela.mainloop()