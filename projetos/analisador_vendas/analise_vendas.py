import pandas as pd


def carregar_dados_csv(caminho):
    return pd.read_csv(caminho)

def lista_produtos(df):
    return set(df['produto'].unique())

def faturamento_total(df):
    return (df['preco'] * df['quantidade']).sum()

def maior_venda(df):
    idx = (df['preco'] * df['quantidade']).idxmax()
    return df.loc[idx]

def main():
    caminho = input("digite o nome da base de dados: ")
    df = carregar_dados_csv(caminho)


    while True:
        print("\n---MENU---")
        print("lista de produtos - [1]")
        print("maior venda - [2]")
        print("faturamento total - [3]")
        print("Fechar programa - [4]")

        try:
            opcao = int(input("digite o numero da opção desejada: "))
        except ValueError:
            print("Entrada invalida. Digite um número.")
        
        if opcao == 1:
            print(f"Os produtos vendidos são : {lista_produtos(df)}")

        elif opcao == 2:
            print(f"A maior vendas foi de {maior_venda['produto']},"
                  f"com {maior_venda['quantidade']} unidades,"
                  f"totalizando {maior_venda['preco'] * maior_venda['quantidade']}")

        elif opcao == 3:
            print(f"O faturamento total foi de {faturamento_total(df)} reais.")

        elif opcao == 4:
            break

        else:
            print("Opção invalida, tente novamente: ")
            continue


if __name__ == "__main__":
    main()
