# Calculadora 

#Funções das operações

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

# Menu usuário

print("\nSelecione a operação desejada:\n") 
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# loop while

while True:

	escolha = input("Digite 1/2/3/4: ")

	if escolha in ("1", "2", "3", "4"):
		num1 = float(input("Digite o primeiro número: "))
		num2 = float(input("Digite o segundo número: "))

		if escolha == "1":

			print(num1, "+", num2, "=", add(num1, num2))

		elif escolha == "2":
		
			print(num1, "-", num2, "=", subtract(num1, num2))

		elif escolha == "3":
		
			print(num1, "*", num2, "=", multiply(num1, num2))

		elif escolha = "4":
		
			print(num1, "/", num2, "=", divide(num1, num2))


# checa se o usuário quer calcular novamente
# acaba o loop while se a resposta for negativa

prox_calculo = input("Deseja calcular novamente? (S/N): ")

if prox_calculo == "N":
	break

else:
	print("Opção Inválida.")	
