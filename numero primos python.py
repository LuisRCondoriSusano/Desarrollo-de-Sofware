def es_primo(n):

    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def busca_primos(n):

    primos = []
    for i in range(1, n + 1):
        if n % i == 0:
            primos.append(i)
    return primos

def main():
    num = int(input("da un numero: "))
    primos = busca_primos(num)
    if es_primo(num):
        print(f"el numero primo es {num}.")
    else:
        print(f"los numeros primos son: {primos}")

if __name__ == "__main__":
    main()