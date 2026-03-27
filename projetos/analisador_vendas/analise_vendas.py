import pandas as pd


def carregar_dados_csv(caminho):
    return pd.read_csv(caminho)

def lista_produtos(df):
    return list(df['produto'].unique())

def faturamento_total(df):
    return (df['preco'] * df['quantidade']).sum()

def maior_venda(df):
    idx = (df['preco'] * df['quantidade']).idxmax()
    return df.loc[idx]
    
def protudo_mais_lucrativo(df):
    total_por_protudo = (df['preco'] * df['quantidade']).groupby(df['produto']).sum()
    produto = total_por_produto.idxmax()
    valor = total_por_produto.max()
    return produto, valor
    
def ranking_produtos(df):
    agrupar = df.groupby("produto")['quantidade'].sum()
    ordena = agrupar.sort_values(ascending=False)
    return ordena

def filtro_por_valor(df):
    corte = float(input("digite um valor mínimo: "))
    filtro = (df['preco'] * df['quantidade']) >= corte
    resultado = df[filtro]
    return resultado

def main():
    caminho = input("digite o nome da base de dados: ")
    df = carregar_dados_csv(caminho)


    while True:
        print("\n---MENU---")
        print("lista de produtos - [1]")
        print("maior venda - [2]")
        print("faturamento total - [3]")
        print("Ranking de vendas - [4]")
        print("maior lucro - [5]")
        print("Filtrar vendas por valor - [6]")
        print("Encerrar programa - [0]")

        try:
            opcao = int(input("digite o numero da opção desejada: "))
        except ValueError:
            print("Entrada invalida. Digite um número.")
            continue
        
        if opcao == 1:
            print(f"\nOs produtos vendidos são: }")
            for produtos in lista_produtos(df):
                print(f"- {produto}")

        elif opcao == 2:
            maior = maior_venda(df)
            valor_total = maior['peco'] * maior['quantidade']
            print(f"\nA maior venda foi de {maior_venda['produto']},"
                  f"com {maior_venda['quantidade']} unidades,"
                  f"totalizando {valor_total}")

        elif opcao == 3:
            print(f"\nO faturamento total foi de {faturamento_total(df)} reais.")

        elif opcao == 4: 
            for indice, (produto, quantidade) in enumerate(ranking_produtos(df).items(), start=1):
                print(f"{indice}º {produto} - {quantidade} unidades")

        elif opcao == 5:
            produto, valor = produto_mais_lucrativo(df)
            print(f"\nProduto mais lucrativo: {produto}\n"
                  f"Faturamento total: {valor:,.2f}")
            
        elif opcao ==6:
            filtrados = filtro_por_valor(df)
            print("\n Vendas acima do valor informado:\n")
            for _, linha in filtrados.iterrows():
                total = linha['preco'] * linha['quantidade']
                print(f"Produto: {linha['produto']}\n"
                      f"Quantidade: {linha['quantidade']}\n"
                      f"Total: {total:,.2f}\n")
                
        elif opcao == 0:
            print("\nEncerrando programa...")
            break
            
        else:
            print("\nOpção invalida, tente novamente: ")
            continue


if __name__ == "__main__":
    main()
