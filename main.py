from operaciones import suma, resta, multiplicacion, division

def main():
    a = 10
    b = 5
    print("Suma:", suma.sumar(a, b))
    print("Resta:", resta.restar(a, b))
    print("Multiplicación:", multiplicacion.multiplicar(a, b))
    print("División:", division.dividir(a, b))

if __name__ == "__main__":
    main()
