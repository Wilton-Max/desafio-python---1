# Faça um programa um programa no qual o usuário prescisa cadastrar
# as informações de um produto: código, nome, quantidade e preço. No final o programa deve mostrar as
# informaçoes cadastradas e exibir o valor total da compra.

codigo_produto= int(input("Digite o código do produto: "))
nome_produto = input("Digite o nome do produto: ")
quantidade = int(input("Informe a quantidade desse produto: "))
preco = float(input("Informe o preço: "))

total = preco * quantidade

print("Segue as informações:", "Produto: ",nome_produto, "Código: ", codigo_produto, "Quantidade: ",quantidade, "Preço: ",preco )
print("Valor da compra: ",total, "R$")
