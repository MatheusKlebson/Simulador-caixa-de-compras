from time import sleep #Biblioteca para fazer o programa dormir por alguns segundos, quando for pedido
print("="*50)
print("{:^50}".format("SUPERMERCADO SANTOS ARAUJO")) #Cabeçalho do programa
print("="*50)
print("{:^50}".format("PARA COMPRAS ACIMA DE 50R$ PODE SER FEITO")) #Cabeçalho que mostra o que estará disponivel caso as compras fiquem acima de 50 Reais
print("="*50)
print('''[1] A vista dinheiro/cheque (10% de Desconto)
[2] Cartão com parcela (5X ou mais, juros de 10%)
[3] Cartão a vista (8% de Desconto)''') #Mostrando as formas de pagamentos acima de 50 Reais
produtos = ("BANANA",
            "TOMATE",
            "CARNE DE FRANGO",
            "CARNE DE PORCO",
            "MELÂNCIA",
            "FEIJÃO",
            "ARROZ",
            "MACARRÃO") #Produtos disponiveis no mercado
preços = (3.50, 5.80, 13, 12.80, 8.50, 7.80, 6.30, 8) #Respectivos preços
print("=" * 50)
print("{:^50}".format("LISTA DE PRODUTOS E PREÇOS(Por KG)")) #Cabeçalho que inicia a tabela de preços e produtos
print("=" * 50)
for tabela in range(0, len(produtos)): #Laço de repetição que permite formar a tabela
    print(f"{produtos[tabela]:.<40}R${preços[tabela]:8.2f}") #Tabela sendo mostrada na tela
print("=" * 50)
custo = 0
print("=" * 50)
print(f"{'FAÇA AQUI SUAS COMPRAS':^50}") #Cabeçalho que inicia a interatividade com o usuário
while True:
    print("=" * 50)
    nome = str(input("Nome do produto: ")).strip().upper()
    if nome in produtos:
        pos = produtos.index(nome)
        preço = preços[pos]
        unidade = float(input("Quantos quilos?KG"))
        totuni = preço * unidade
        if unidade > 1:
            print(f"Preço;R${preço} X {unidade}KG")
        else:
            print(f"Preço:R${preço}")
        custo += totuni
    else:
        print("Produto não disponivel")
    print("=" * 50)
    resposta = " "
    while not resposta in "SN":
        resposta = str(input("Quer continuar?[S/N]:")).upper().strip()[0]
    if resposta == "N":
        break
print("=" * 50)
print("Calculando...")
sleep(2)
print("Valor total das compras: R${:.2f}".format(custo))
if custo > 50:
    while True:
        print("="*50)
        print("{:^50}".format("FORMAS DE PAGAMENTOS"))
        print("="*50)
        opcao = int(input('''[1] A vista dinheiro/cheque (10% de Desconto)
[2] Cartão com parcela (5X ou mais, juros de 10%)
[3] Cartão a vista (8% de Desconto) 
Digite: '''))
        print("Analisando...")
        sleep(2)
        print("="*50)
        if opcao == 1:
            print("Desconto: 10%")
            novo = custo - (custo*10/100)
            print("Total a pagar: R${:.2f}".format(novo))
        elif opcao == 2:
            totparcela = int(input("Quantas parcelas? "))
            if totparcela >= 5:
                juros = custo + (custo*10/100)
                novo = juros/totparcela
                print("Juros: 15%")
                print("Total a pagar será: R${:.2f}".format(juros))
            else:
                novo = custo/totparcela
            print("Prestação: R${:.2f}".format(novo))
        elif opcao == 3:
            print("Desconto: 8%")
            novo = custo - (custo * 8 / 100)
            print("Total a pagar: R${:.2f}".format(novo))
        else:
            print("Opção errada!!")
        resposta = ' '
        resposta = str(input("Confirmar compras[S/N]: ")).upper().strip()[0]
        while not resposta in "SN":
            resposta = str(input("Digite corretamente. Confirmar compras[S/N]: ")).upper().strip()[0]
        if resposta == "S":
            break
else:
    print("="*30)
    print("{:^30}".format("COMPRAS DE 50R$ OU MENOS"))
    while True:
        print("="*30)
        opcao = int(input('''[1] A vista dinheiro
[2] Cartão no maximo 2 parcelas 
Digite: '''))
        if opcao == 1:
            print("Compras confirma!")
            print("Total a pagar: R${:.2f}".format(custo))
            break
        elif opcao == 2:
            print("Total de Parcelas: 2X")
            print(f"Prestação: {custo/2}")
            resposta = ' '
            resposta = str(input("Confirmar compras[S/N]: ")).upper().strip()[0]
            while not resposta in "SN":
                resposta = str(input("Digite corretamente. Confirmar compras[S/N]: ")).upper().strip()[0]
            if resposta == "S":
                break
        else:
            print("Opção errada!!!")
print('='*50)
print("Tenha um bom dia!!\nVolte sempre a SUPERMERCADO SANTOS ARAUJO")
