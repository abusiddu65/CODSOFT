def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Additon")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

while True:
    user_input= input("Enter choice(1/2/3/4): ")
    if user_input in ('1', '2', '3', '4'):
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        if user_input == '1':
            print(number1, "+", number2, "=", add(number1, number2))
        elif user_input== '2':
            print(number1, "-", number2, "=", subtract(number1, number2))
        elif user_input == '3':
            print(number1, "*", number2, "=", multiply(number1, number2))
        elif user_input == '4':
            print(number1, "/", number2, "=", divide(number1, number2))
        next_calculation = input("Calculate or Not ? (Y/N): ")
        if next_calculation == "N":
          break
    else:
        print("Invalid Input")
 