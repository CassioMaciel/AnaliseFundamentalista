import logging
import requests_cache
import warnings
import pandas as pd
import datetime
logging.basicConfig(level=logging.CRITICAL)
import fundamentus

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

for acao in get_resultado.index:
    # logger_main.info(acao)
    # if os.path.exists("http_cache.sqlite"):
    #     os.remove("http_cache.sqlite")
    # with warnings.catch_warnings():
        # https://docs.python.org/3/library/warnings.html
        # warnings.simplefilter("ignore")
    resultados_acao = fundamentus.get_papel(acao)
    print(  'Ticker: ',
            acao,
            ' Data Ult. Cot.: ',
            str(
                resultados_acao["Data_ult_cot"].to_string(index=False)
            ))
    # resultados = resultados._append(resultados_acao)
    resultados = pd.concat([resultados, resultados_acao])
    index += index
    logger_main.debug('saida', acao)

resultados = resultados.set_index('Papel')
resultados.to_csv(dados_atuais_path)

today = datetime.datetime.now()
string_today = today.strftime('%Y-%m-%d-%H-%M')
resultados.to_csv(dados_historicos_path + '/' + string_today)

requests_cache.clear()
