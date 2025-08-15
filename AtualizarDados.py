import logging
import requests_cache
import warnings
import pandas as pd
import datetime
logging.basicConfig(level=logging.CRITICAL)
import fundamentus
from math import log, ceil

logger_main = logging.getLogger("minha_funcao_main")
logger_main.setLevel(logging.INFO)

requests_cache.install_cache("http_cache")
requests_cache.clear()

dados_atuais_path = './.BancoDados/RelatoriosContabeis'
dados_historicos_path = './.BancoDados/historicas'

warnings.simplefilter(action='ignore', category=FutureWarning)

get_resultado = fundamentus.get_resultado()
get_resultado = get_resultado.sort_values(by='liq2m', ascending=False)
get_resultado = get_resultado[get_resultado['liq2m'] > 10]

index = 0
resultados = pd.DataFrame()
quantidade_itens: int = len(get_resultado.index)
precision: int = ceil(log(quantidade_itens, 10))  # essa variável calcula a
# quantidade de digitos que tem no número de itens. Por exemplo, se o número
# de itens for 400 a variável terá valor 3, se for 3_000, a variável terá
# valor 4, se for 45_000 a variável terá valor 5

for acao in get_resultado.index:
    # logger_main.info(acao)
    # if os.path.exists("http_cache.sqlite"):
    #     os.remove("http_cache.sqlite")
    # with warnings.catch_warnings():
    #     https://docs.python.org/3/library/warnings.html
    #     warnings.simplefilter("ignore")
    resultados_acao = fundamentus.get_papel(acao)

    print(f'Ticker: {acao:6}', end=" ")
    print('Data Ult. Cot.:', end=" ")
    print(str(resultados_acao["Data_ult_cot"].to_string(index=False)), end=" ")
    print(f'resultado {index+1:{precision}.0f} de {quantidade_itens}', end=" ")
    print(f'concluido: {(index+1)/quantidade_itens:3.0%}')
    resultados = pd.concat([resultados, resultados_acao])
    index += 1
    logger_main.debug('saida', acao)

resultados = resultados.set_index('Papel')
resultados.to_csv(dados_atuais_path)

today = datetime.datetime.now()
string_today = today.strftime('%Y-%m-%d-%H-%M')
resultados.to_csv(dados_historicos_path + '/' + string_today)

requests_cache.clear()
