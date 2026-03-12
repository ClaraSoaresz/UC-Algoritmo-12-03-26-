# Sem função
print("OLá, mundo!")
print("OLá, mundo!")
print("OLá, mundo!")

# Com função
def exibirMensagem():
    print("Olá, mundo!")

exibirMensagem()
exibirMensagem()
exibirMensagem()

# Função com parâmetro
def saudar(nome): 
    print(f"Olá {nome}!")

saudar("Gaby!")

# Parâmetros obrigatórios
def exibirBoasVindas(pessoa, mensagem):
    print(f"{mensagem}, {pessoa}")

exibirBoasVindas("Ana", "Bom dia")

def exibirBoasMensagens(mensagem = "Olá", pessoa = "João"):
    print(f"{mensagem}, {pessoa}")


# Função que retorna um valor
def calcularMedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

resultado = calcularMedia(8.0, 9.0)
print(f"Média: {resultado}")


# Função que retorna multiplos valores 
def obterMaiorMenor(a, b, c):
    maior = max(a, b, c)
    menor = min(a, b, c)
    return maior, menor

maxValor, minValor = obterMaiorMenor(10, 5, 8)
print(f"Maior: {maxValor} e Menor: {minValor}")