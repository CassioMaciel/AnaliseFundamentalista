from bs4 import BeautifulSoup
import requests
import fundamentus
import pandas as pd
from pathlib import Path

get_resultado = fundamentus.get_resultado()

index=0

resultados = fundamentus.get_papel('WEGE3')

resultados = resultados.drop("WEGE3") #exclui alinha WEGE3

for acao in get_resultado.index:
    resultados = resultados._append(fundamentus.get_papel(acao))
    index += index
    print(acao)

resultados.to_csv('./.BancoDados/RelatoriosContabeis')

#TODO: Exportar os Dados Históricos