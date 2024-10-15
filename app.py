# Função para calcular o valor de x na equação do 1º grau
def calcular_x(a, b):
    if a == 0:
        return "A equação não é de 1º grau (a não pode ser zero)."
    return -b / a

# Solicitando os valores de "a" e "b" do usuário
a = float(input("Digite o valor de a (coeficiente de x): "))
b = float(input("Digite o valor de b (termo constante): "))

# Calculando o valor de x
x = calcular_x(a, b)

# Exibindo o valor de x
print(f"O valor de x é: {x}")
