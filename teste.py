"""Funcoes matematicas basicas e uma calculadora interativa de terminal."""


def soma(a: float, b: float) -> float:
    """Retorna a soma de dois numeros."""
    return a + b


def subtracao(a: float, b: float) -> float:
    """Retorna a diferenca entre dois numeros."""
    return a - b


def multiplicacao(a: float, b: float) -> float:
    """Retorna o produto de dois numeros."""
    return a * b


def divisao(a: float, b: float) -> float:
    """Retorna o quociente de dois numeros.

    Raises:
        ZeroDivisionError: Quando o divisor for zero.
    """
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b


def main() -> None:
    """Executa o menu interativo da calculadora no terminal."""
    print("Calculadora")
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")

    while True:
        try:
            opcao: str = input("Escolha uma operacao (1-4) ou 's' para sair: ").strip().lower()
            if opcao == "s":
                print("Encerrando a calculadora.")
                break

            if opcao not in ("1", "2", "3", "4"):
                print("Opcao invalida.")
                continue

            a: float = float(input("Digite o primeiro numero: "))
            b: float = float(input("Digite o segundo numero: "))
            resultado: float

            if opcao == "1":
                resultado = soma(a, b)
            elif opcao == "2":
                resultado = subtracao(a, b)
            elif opcao == "3":
                resultado = multiplicacao(a, b)
            else:
                resultado = divisao(a, b)

            print(f"Resultado: {resultado}")
        except ZeroDivisionError as erro:
            print(erro)
        except ValueError:
            print("Digite apenas numeros validos.")


if __name__ == "__main__":
    main()
