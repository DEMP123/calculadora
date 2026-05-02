def multiplicacao(a: float, b: float) -> float:

   return a * b

def divisao(a: float, b: float) -> float:

   return a / b

def soma(a: float, b: float) -> float:

   return a + b

def subtracacao(a: float, b: float) -> float:

    return a - b

def exponenciacao(a: float, b: float) -> float:

    return a ** b

#print("divisao" divisao())

def menu() -> None:

    print("--- MENU ---")
    print("(1) Multiplicacao")
    print("(2) Divisao")
    print("(3) Soma")
    print("(4) Subtracao")
    print("(5) exponenciacao")

while True:

    menu()

    option = input("Informe uma opção:")

    if option == "1":

       a = float(input("Informe um valor de (a):"))
       b = float(input("Informe um valor de (b):"))

       print("Saída de multiplicar:", multiplicacao(a, b))

    elif option == "2":
        a = float(input("Informe um valor de (a):"))
        b = float(input("Infomre um valor de (b):"))

        print("Saida de dividir:", divisao(a, b))

    elif option == "3":
        a = float(input("Informe um valor de (a):"))
        b = float(input("Informe um valor de (b):"))

        print("saide de somar", soma(a, b))

    elif option == "4":
        a = float(input("Informe um valor de (a):"))
        b = float(input("Informe um valor de (b):"))

        print("saida de subtração", subtracacao(a, b))

    elif option == "5":
        a = float(input("Informe um valor de (a):"))
        b = float(input("informe um valor de (b):"))

        print("exponenciação", exponenciacao(a, b))

    else:
        print("Opção inválida")







