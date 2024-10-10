import math

#Definição das funções
def cateto_oposto(hipo, ca):
    return (hipo ** 2 - ca ** 2) ** (1/2)

def cateto_adjacente(hipo, co):
    return (hipo ** 2 - co ** 2) ** (1/2)

def hipotenusa(co, ca):
    return (co ** 2 + ca ** 2) ** (1/2)

#Função exibir menu
def menu():
    print("TRIGOTEC - CALCULADORA TRIGONOMÉTRICA")
    print("Menu de Opções {Triângulo Retângulo}:")
    print("1. Teorema de Pitágoras")
    print("2. Seno")
    print("3. Cosseno")
    print("4. Tangente")
    print("5. Sair")
    escolha = int(input("Escolha uma opção: "))
    return escolha

def menu_pitagoras():
    print("\n[MENU DE OPÇÕES PITÁGORAS]")
    print("1. Descobrir cateto oposto.")
    print("2. Descobrir cateto adjacente.")
    print("3. Descobrir hipotenusa.")
    escolha = int(input("Escolha uma opção: "))
    return escolha

#Declaração de Variável
opção = 0
hipo = 0
co = 0
ca = 0

def teorema_pitagoras(escolha):
    if escolha == 1:
        hipo = int(input("Informe a hipotenusa: "))
        ca = int(input("Informe o cateto adjacente: "))
        print(f"O CATETO OPOSTO É: {cateto_oposto(hipo, ca)}\n")

    elif escolha == 2:
        hipo = int(input("Informe a hipotenusa: "))
        co = int(input("Informe o cateto adjacente: "))
        print(f"O CATETO ADJACENTE É: {cateto_adjacente(hipo, co)}\n")

    elif escolha == 3:
        co = int(input("Informe o cateto oposto: "))
        ca = int(input("Informe o cateto adjacente: "))
        print(f"A HIPOTENUSA É: {hipotenusa(co, ca)}\n")
    else:
        print("Opção inválida :(")

def calcular_seno():
    angulo = float(input("Informe o ângulo em graus: "))
    seno = math.sin(math.radians(angulo))
    print(f"SENO de {angulo}°: {seno:.2f}")

def calcular_cosseno():
    angulo = float(input("Informe o ângulo em graus: "))
    cosseno = math.cos(math.radians(angulo))
    print(f"COSSENO de {angulo}°: {cosseno:.2f}")

def calcular_tangente():
    angulo = float(input("Informe o ângulo em graus: "))
    tangente = math.tan(math.radians(angulo))
    print(f"TANGENTE de {angulo}°: {tangente:.2f}")

while True:
    escolha_principal = menu()

    if escolha_principal == 1:
        escolha_pitagoras = menu_pitagoras()
        teorema_pitagoras(escolha_pitagoras)

    elif escolha_principal == 2:
        calcular_seno()

    elif escolha_principal == 3:
        calcular_cosseno()

    elif escolha_principal == 4:
        calcular_tangente()

    elif escolha_principal == 5:
        print("Saindo...")
        break

    else:
        print("Opção inválida :(")

