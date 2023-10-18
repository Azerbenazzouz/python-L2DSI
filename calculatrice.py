num1 = float(input("Entrez le premier nombre : "))
num2 = float(input("Entrez le deuxième nombre : "))


print("Opérations disponibles :")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choisissez une opération (1/2/3/4) : ")


if(choice == '1'):
    result = num1 + num2
    operation = "+"
elif(choice == '2'):
    result = num1 - num2
    operation = "-"
elif(choice == '3'):
    result = num1 * num2
    operation = "*"
elif(choice == '4'):
    if(num2 != 0):
        result = num1 / num2
        operation = "/"
    else:
        result = "Division par zéro impossible"
        operation = "/"
else:
    result = "Choix invalide"
    operation = ""


if operation:
    print(f"Résultat : {num1} {operation} {num2} = {result}")
else:
    print(result)
