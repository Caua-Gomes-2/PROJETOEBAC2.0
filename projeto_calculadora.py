# -*- coding: utf-8 -*-
"""projeto calculadora

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17Oqw-3BqDBBN84WwdkcH6QZzWlN9Br6U
"""

def calculadora():
    while True:
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número: "))
        print("Selecione a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")
        opcao = int(input("Digite o número da operação: "))

        if opcao == 1:
            resultado = num1 + num2
            print("Resultado da soma:", resultado)
        elif opcao == 2:
            resultado = num1 - num2
            print("Resultado da subtração:", resultado)
        elif opcao == 3:
            resultado = num1 * num2
            print("Resultado da multiplicação:", resultado)
        elif opcao == 4:
            if num2 == 0:
                print("Erro: Divisão por zero!")
            else:
                resultado = num1 / num2
                print("Resultado da divisão:", resultado)
        elif opcao == 5:
            print("Saindo da calculadora...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamando a função para iniciar a calculadora
calculadora()