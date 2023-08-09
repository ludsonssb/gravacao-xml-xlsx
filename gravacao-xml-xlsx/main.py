import xmltodict
import os
import json
import pandas as pd

def pegar_infos(nome_arquivo, valores):
    print(f"Pegou a nota {nome_arquivo}")
    with open(f"nfs/{nome_arquivo}", "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        #print(json.dumps(dic_arquivo, indent=4))
        infos_nf = dic_arquivo["nfeProc"]["NFe"]["infNFe"]
        numero_nota = infos_nf["@Id"]
        empresa_emissora = infos_nf["emit"]["xNome"]
        print(numero_nota, empresa_emissora, sep="\n")
        valores.append([numero_nota, empresa_emissora])

lista_arquivos = os.listdir("nfs")

colunas = ["numero_nota", "empresa"]
valores = []

for arquivo in lista_arquivos:
    pegar_infos(arquivo, valores)

tabela = pd.DataFrame(columns=colunas, data=valores)
tabela.to_excel("Notas.xlsx", index=False)
