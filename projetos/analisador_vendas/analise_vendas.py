import pandas as pd
import matplotlib.pyplot as plt

COLUNAS_NECESSARIAS = ['produto', 'preco', 'quntidade']

def carregar_dados_csv(caminho):

    try:
        df = pd.read)csv(caminho)
        if not all(col in df.columns for col in COLUNAS_NECESSARIAS):
            print("\nErro: O arquivo não possui as colunas necessárias.")
            print(f"\nColunas necessarias: {COLUNAS_NECESSARIAS}")
            return None
        return df
    except FileNotFuoundError:
        print("\nErro: Arquivo não encontrado.")
        return None
    except pd.errors.EmptyDataError:
        print("\nErro: O arquivo está vazio.")
        return None
    except Exception as erro:
        print("\nErro aos carregar o arquivo.")
        return None
        
    return pd.read_csv(caminho)
    
def carrega_novo_arquivo():
    colunas_necessarias = ['produto'], ['preco'], ['quantidade']
    caminho = input("digite o nome do novo arquivo.CSV: ")
                    
    try: 
        df.read_csv(caminho)
        
        if not all(col indf.columns for col in COLUNAS_NECESSARIAS):
            print("\n Erro: O arquivo não posssui as colunas necessárias.")
            print(f"\n colunas esperadas: {COLUNAS_NECESSARIAS}")
            return None
            
        print("\nArquivo carregado com sucesso.")
        return df
    except FileNotFoundErro:
        print(f"\n Erro: Arquivo não encontrado")

    except Exception as e:
        print(f"\nErro ao carregar arquivo: {e}")
        return None

    except pd.errors.EmptyDataError:
        print("\nErro: O Arquivo está vazio.")
        return None

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

def grafico_faturamento(df):
    faturamento = (df['produto'] * df['quantidade']).groupby(df['produto']).sum()

    plt.bar(faturamento.index, faturamneto.values)

    plt.title("Faturaento por produto")
    plt.xlabel("Produto")
    plt.ylabel("Faturamento R$")

return plt.show()

def grafico_quantidade(df):

    quantidade = df.groupby('produto')['quantidade'].sum()
    quantidade = quantidade.sort_values(ascending=False)

    plt.bar(quantidade.index, quantidade.values)

    plt.xlabel('Produto')
    plt.xticks(rotation=45)

    plt.ylabel('Quantidade')
    plt.tight_layout()

    plt.grid(axis='y', linestyle='--', alpha=0.7

    return plt.show()

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
        print("Mostra Gráfico Faturamento X Produto" - [7]) 
        print("Mostra Gráfico Quantidade X Produto: - [8]")
        print("Carregar novo arquivo csv - [9]")
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
                
        elif opcao == 7:
            print(f"\nMontando o gráfico")
            grafico_faturmento(df)

        elif opcao == 8:
            print(f"\nGerando gráfico: ")
            grafico_quantidade(df)

        elif opcao == 9:
            print("Preparando")
            novo_df = carrega_novo_arquivo()
            if novo_df is not None:
                df = novo_df
            
        elif opcao == 0:
            print("\nEncerrando programa...")
            break
            
        else:
            print("\nOpção invalida, tente novamente: ")
            continue


if __name__ == "__main__":
    main()
