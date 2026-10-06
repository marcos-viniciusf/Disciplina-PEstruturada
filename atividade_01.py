import random

## Q1
# nome = input("Digite seu nome: ")
# idade = int(input("\nDigite sua idade: "))
# cidade = input("\nDigite sua cidade: ")

# print(f"\n\n{nome} possuí {idade} anos e mora na cidade de {cidade}")


# # Q2
# num1, num2 = input("Digite dois números, separados por espaço, para ser realizados operações matématicas: ").split(" ")

# num1 = float(num1)
# num2 = float(num2)

# if num1 == 0 or num2 == 0:
#     print("\nNão é possível realizar divisão por ZERO")
#     exit
# print(f"\nOperações envolvendo os números {num1} e {num2}")
# print(f"\nSoma: {num1} + {num2} = {num1+num2}")
# print(f"\nSubtração: {num1} - {num2} = {num1-num2}")
# print(f"\nMultiplicação: {num1} x {num2} = {num1*num2}")
# print(f"\nDivisão: {num1} / {num2} = {num1/num2}")

## Q3

# idade = int(input("Digite sua idade: "))

# if idade < 12:
#     print("Classificação: CRIANÇA")
# elif idade <= 17:
#     print("Classificação: ADOLESCENTE")
# elif idade <=59:
#     print("Classificação: ADULTO")
# else:
#     print("Classificação: IDOSO")

# ##Q4
# def num_maior (num1, num2, num3):

#     if num1 == num2 and num1 == num3:
#         return num1
#     if num1 > num2 and num1 > num3:
#         return num1
#     elif num2 > num1 and num2 > num3:
#         return num2
#     else:
#         return num3 

    
# num1, num2, num3 = input("Digite três números separados por espaço: ").split(" ")
# num1 = float(num1)
# num2 = float(num2)
# num3 = float(num3)

# print(f"\n\nO maior número é: ", num_maior(num1, num2, num3))


# #Q5

# numero = int(input("Digite um número para ser exibido sua tabuada: "))
# print("\n---------------------- Tabuada ----------------------\n")
# for i in range(1,10):
#     print(f"{numero} x {i} = {numero*i}\n")

#Q6

# numero = int(input("Digite um número N positivo: "))

# soma = 0
# contador  = numero
# while contador != 0:
#     soma+=contador
#     contador -= 1

# print(f"Valor da soma de 1 até {numero}: {soma}")

#Q7

# senha = input("Digite a senha: ")

# while senha != "python123":
#     senha = input("\nSenha incorreta.\nDigite novamente a senha: ")
    
# print("\nAcesso Permitido!")

    
# #Q8

# def calcular_media(nota1, nota2, nota3):
#     return ((nota1 + nota2 + nota3)/3)

# n1, n2, n3 = input("Digite três notas sendo separadas por espaço: ").split(" ")
# n1 = float(n1)
# n2 = float(n2)
# n3 = float(n3)

# print(f"\nMédia do aluno é: {calcular_media(n1, n2, n3):.2f}")

#Q9

# def verificar_situacao(media):
#     if media < 5:
#         print("\nReprovado")
#     elif media < 7:
#         print("\n Recuperação")
#     else:
#         print("\nAprovado")

# media = float(input("Digite a média do aluno: "))
# while media < 0 or media > 10:
#     media = float(input("Média inválida! Digite novamente: "))

# verificar_situacao(media)


#Q10

# numeros = []

# for i in range(10):
#     num = int(input(f"\nDigite um valor para o {i+1} da lista: "))
#     numeros.append(num)

# maior = numeros[0]
# menor = numeros[0]
# soma = 0

# for num in numeros:
#     soma += num

#     if num > maior:
#         maior = num
    
#     if num < menor:
#         menor = num
    
# print("\n----------------------------------\n")
# print(f"Todos os números: {numeros}\n")
# print(f"Maior número: {maior}\n")
# print(f"Menor número: {menor}\n")
# print(f"Soma de todos os números: {soma}")

#Q11

# numeros = []
# par = []
# impar = []

# for i in range(10):
#     num = int(input(f"\nDigite um valor para o {i+1}º da lista: "))
#     numeros.append(num)

# for j in numeros:
#     if j % 2 == 0:
#         par.append(j)
#     else:
#         impar.append(j)

# print("\n--------------------------------------------\n")
# print(f"{numeros}\n")
# print(f"{par}\n")
# print(f"{impar}")

# #Q12
# def contar_maior(lista, limite):
#     contador = 0    
#     for i in lista:
#         if i > limite:
#             contador += 1
    
#     return contador

# lista = []
# for i in range(random.randint(1,20)):
#     lista.append(random.randint(1,100))

# limite = random.randint(1,100)
# qnt_maior = contar_maior(lista, limite)

# print("\n", lista)
# print(f"\nQuantidade de números maior que {limite}: ", qnt_maior)

# #Q13
# def somar_lista(lista):
#     soma = 0
#     for i in lista:
#         soma += i
    
#     return soma


# lista = []
# for i in range(random.randint(1,20)):
#     lista.append(random.randint(1,100))

# valor_soma = somar_lista(lista)

# print(f"\nSoma dos valores da lista {lista}: ", valor_soma)

# #Q14
# def buscar_valor(lista, valor):
#     indices = []
#     for posicao, num in enumerate(lista):
#         if num == valor:
#             indices.append(posicao)

#     if len(indices) > 0:
#         return True, indices
#     else:
#         return False, None

# lista = []
# #tam_lista = int(input("\nDigite o tamanho da lista: "))
# tam_lista = random.randint(1,20)
# for i in range(tam_lista):
#     #num = int(input(f"\nDigite um valor para o {i+1}º da lista: "))
#     num = random.randint(1,100)
#     lista.append(num)

# print(lista)
# valor = int(input("\nDigite um valor a ser buscado na lista: "))

# busca, indice = buscar_valor(lista, valor)
# if busca == True:
#     print(f"\nValor {valor} encontrado na lista no(s) indíce(s) {indice}")

#Q15

# lista = []
# tam_lista = random.randint(1,10)
# for i in range(tam_lista):
#     num = random.randint(1,100)
#     lista.append(num)

# nova_lista = []

# print("Lista original: ", lista)

# for num in lista:
#     n_existe = True
#     for comparado in nova_lista:
#         if comparado == num:
#             n_existe = False
#             break
#     if n_existe:
#         nova_lista.append(num)

# print("\nNova lista: ", nova_lista)

#Q16

# frase = input("Digite uma frase: ")

# print("\nFrase sem espaço no início e fim: ", frase.strip())
# print("\nFrase em maiúsculo: ", frase.upper())
# print("\nFrase em minúsculo: ", frase.lower())
# print("\nTroca a palavra 'Python' por 'Programação': ", frase.replace("Python", "Programação"))

#Q17

# palavra = input("Digite uma palavra: ")

# print("\nPrimeiro caractere: ", palavra[0])
# print("\nÚltimo caractere: ", palavra[-1])
# print("\nTrês primeiros caracteres: ", palavra[:3])
# print("\nTrês últimos caracteres: ", palavra[3:])

#Q19
def menu():
    print("\n----------------------------------------------------\n")
    print('''1 -  Cadastrar aluno
2 - Listar alunos
3 - Buscar alunos
4 - Remover aluno
5 - Sair''')
    print("\n----------------------------------------------------\n")
    
    opc = int(input("Digite uma opção: \n"))    
    while opc <= 0 or opc > 5:
        opc = int(input("\nDigite uma opção válida! Opção: "))

    return opc

def cadastro_aluno(alunos):
    nome = input("\nDigite o nome do aluno: ")
    alunos.append(nome)
    print("\n", alunos)

def listar_alunos(alunos):
    print("\n", alunos)

def buscar_aluno(alunos):
    nome_buscado = input("\nDigite o nome do aluno a ser buscado: ")
    for posicao, nome_lista in enumerate(alunos):
        if nome_lista == nome_buscado:
            print(f"\n n{nome_buscado} está na posição {posicao+1}")
            break

def remover_aluno(alunos):
    nome_buscado = input("\nDigite o nome do aluno a ser removido: ")
    for nome in alunos:
        if nome_buscado == nome:
            alunos.remove(nome_buscado)        
    print("\n", alunos)
###############
###############
alunos = []
opc = menu()

match opc:
    case 1:
        cadastro_aluno(alunos)
    case 2:   
        listar_alunos(alunos)  
    case 3:
        buscar_aluno(alunos)
    case 4:
        remover_aluno(alunos)
    case _:
        print("\nErro!")


