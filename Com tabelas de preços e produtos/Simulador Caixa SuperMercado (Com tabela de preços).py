from time import sleep
print("="*50)
print("{:^50}".format("SUPERMERCADO SANTOS ARAUJO"))
produtos = ("BANANA",
            "TOMATE",
            "CARNE DE FRANGO",
            "CARNE DE PORCO",
            "MELÂNCIA",
            "FEIJÃO",
            "ARROZ",
            "MACARRÃO")
preços = (3.50,5.80,13,12.80,8.50,7.80,6.30,8)
print("=" * 50)
print("{:^50}".format("LISTA DE PRODUTOS E PREÇOS(Por KG)"))
print("=" * 50)
for tabela in range(0,len(produtos)):
    print(f"{produtos[tabela]:.<40}R${preços[tabela]:8.2f}")
print("="*50)
custo = 0
print("="*50)
print(f"{'FAÇA AQUI SUAS COMPRAS':^50}")
while True:
    print("=" * 50)
    nome = str(input("Nome do produto: ")).strip().upper()
    if nome in produtos:
        pos = produtos.index(nome)
        preço = preços[pos]
        print(f"R${preço}")
        custo += preço
    else:
        print("Produto não disponivel")
    print("="*50)
    resposta = " "
    while not resposta in "SN":
        resposta = str(input("Quer continuar?[S/N]:")).upper().strip()[0]
    if resposta == "N":
        break
print("="*50)
print("Calculando...")
sleep(2)
print("Valor total das compras: R${:.2f}".format(custo))
while True:
    print("="*50)
    print("{:^50}".format("FORMAS DE PAGAMENTOS"))
    print("="*50)
    opcao = int(input('''[1] A vista dinheiro/cheque (10% de Desconto)
[2] Cartão com parcela (5X ou mais, juros de 15%)
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
            juros = custo + (custo*15/100)
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
print('='*50)
print("Tenha um bom dia!!\nVolte sempre a SUPERMERCADO SANTOS ARAUJO")
