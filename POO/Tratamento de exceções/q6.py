def divisao_segura(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Erro: Divisão por zero not allowed")
        return None
    except TypeError:
        print("Erro: Os parâmetros sejam números pfv (int ou float).")
        return None

print(f"Teste 1 (10 / 2): {divisao_segura(10, 2)}")      
print(f"Teste 2 (10 / 0): {divisao_segura(10, 0)}")