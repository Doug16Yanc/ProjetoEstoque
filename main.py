def main():

    descricao = ["arroz", "feijão", "carnes", "ovos", "macarrão", "biscoitos", "bebidas", "frutas", "legumes", "doces"]

    codigo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    quantidade = [100, 80, 90, 120, 110, 50, 60, 40, 90, 100]

    valor = True


    print("Bem-vindo ao nosso supermercado, faça suas compras e sejas feliz!")


    print("Descrição:", "Código:" ,"Estoque")

    for i in range (0, 10):
        print(" ", descricao[i], codigo[i], quantidade[i])


    while(valor):
        opcao = int(input("Digite uma das opções:\n1-Efetuar retirada de produto\n2-Mostrar estoque atual\n3-Encerrar programa\n"))

        if opcao == 1:
            print("Você escolheu efetuar retirada de produto\n")

            codigoProduto = int(input("Digite o código do produto:"))

            if codigoProduto > codigo[9]:
                print("Código inexistente, tente novamente!")
            else:
                print(f"Produto encontrado com sucesso e o produto é {descricao[codigoProduto - 1]}")

                quant = int(input("Digite a quantidade que desejas retirar:"))

                if quant <= quantidade[codigoProduto - 1]:
                    print("Pedido atendido com sucesso.")

                    quantidade[codigoProduto - 1] -= quant

                else:
                    print("Não temos estoque suficiente dessa mercadoria.")

        elif opcao == 2:

            print("Você escolheu mostrar estoque atualizado.\n")

            print("Descrição", "")
            for i in range(0, 10):
                print(" ", descricao[i], codigo[i], quantidade[i])

        elif opcao == 3:

            print("Você escolheu encerrar a operação. O nosso sistema distribuidor de mercadorias agradece sua interação conosco.")

            break
if __name__:
    main()