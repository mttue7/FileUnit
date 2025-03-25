import pandas as pd
import os

def juntar_arquivos_excel(caminho_pasta):
    arquivos = os.listdir(caminho_pasta)
    arquivos_excel = [arquivo for arquivo in arquivos if arquivo.endswith('.xlsx')]
    print(arquivos_excel)

    lista_df = []

    for arquivo in arquivos_excel:
        caminho_arquivo = os.path.join(caminho_pasta, arquivo)
        df = pd.read_excel(caminho_arquivo)
        lista_df.append(df)
    
    resultado = pd.concat(lista_df, ignore_index=True)
    resultado.to_excel(os.path.join(caminho_pasta, 'resultado.xlsx'), index = False)

    print('Arquivos unidos com sucesso!')
    print(resultado)

caminho = 'coloque_aqui_o_caminho_da_sua_pasta'
juntar_arquivos_excel(caminho)