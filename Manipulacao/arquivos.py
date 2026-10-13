with open("Manipulacao/Dados/teste_arquivo.txt","a", encoding="utf-8") as arquivo:
    for i in range(4):
        nome = input("\nDigite o nome do aluno: ")
        arquivo.write(nome + '\n')