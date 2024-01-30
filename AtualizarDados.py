import fundamentus
import warnings
import os
import pandas as pd
import datetime

dados_atuais_path = './.BancoDados/RelatoriosContabeis'
dados_historicos_path = './.BancoDados/historicas'

if os.path.exists("http_cache.sqlite"):
    os.remove("http_cache.sqlite")

get_resultado = fundamentus.get_resultado()

index = 0
resultados = pd.DataFrame()

for acao in get_resultado.index:
    print(acao)
    with warnings.catch_warnings():
        # https://docs.python.org/3/library/warnings.html
        warnings.simplefilter("ignore")
        resultados = resultados._append(fundamentus.get_papel(acao))
    index += index
    print(acao)

resultados = resultados.set_index('Papel')
resultados.to_csv(dados_atuais_path)

today = datetime.datetime.now()
string_today = today.strftime('%Y-%m-%d-%H-%M')
resultados.to_csv(dados_historicos_path + '/' + string_today)
