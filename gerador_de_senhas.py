import random
import string

def gerar_senha(tamanho):
    senha = ""
    for _ in range(tamanho):
        senha += random.choice(string.ascii_letters)
        
    return senha

print("Gerador de Senhas Alatórias!!!")

tamanho = int(input("Qual o Tamanho da Senha?"))

senha = gerar_senha(tamanho)

print("Sua nova senha é: ", senha)