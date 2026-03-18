from dados_vendas import vendas

#funções:
#Lista de produtos
def lista_produtos(vendas):

    produtos = set(venda['produto'] for venda in vendas)

    return produtos

def maior_venda (vendas):

    return max(vendas, key=lambda venda: venda["preco"] * venda["quantidade"] )

def faturamento_total(vendas):

    return sum(iten['preco'] * iten['quantidade'] for iten in vendas)


lista_de_produtos = lista_produtos(vendas)

print(f"Os produtos vendidos são : {lista_de_produtos}")

faturamento = faturamento_total(vendas)

print(f"O faturamento total foi {faturamento} reais")

maior_venda = maior_venda(vendas)

print(f"A maior venda foi de um {maior_venda['produto']}, que vendeu {maior_venda['quantidade']} unidades e custou {maior_venda['preco']} reais." )


if __name__ == "__main__":
    main()
