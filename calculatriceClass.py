class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    def subtract(self, num1, num2):
        return num1 - num2
    def multiply(self, num1, num2):
        return num1 * num2
    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Division par zéro impossible"

Calculator = Calculator()

num1 = float(input("Entrez le premier nombre : "))
num2 = float(input("Entrez le deuxième nombre : "))


print("Opérations disponibles :")
print("1. Addition")
print("2. Soustraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choisissez une opération (1/2/3/4) : ")

if choice == '1':
    result = Calculator.add(num1, num2)
    operation = "+"
elif choice == '2':
    result = Calculator.subtract(num1, num2)
    operation = "-"
elif choice == '3':
    result = Calculator.multiply(num1, num2)
    operation = "*"
elif choice == '4':
    result = Calculator.divide(num1, num2)
    operation = "/"
else:
    result = "Choix invalide"
    operation = ""

if operation:
    print(f"Résultat : {num1} {operation} {num2} = {result}")
else:
    print(result)