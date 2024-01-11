import fundamentus
import warnings


get_resultado = fundamentus.get_resultado()

# FIXME: Está puxando de 28/12/2023, e não atualizado.
# TODO: Colocar no Código que ao iniciar deve apagar o arquivo http_cache_sqlite

index = 0

resultados = fundamentus.get_papel('WEGE3')

resultados = resultados.drop("WEGE3")  # exclui a linha WEGE3

for acao in get_resultado.index:
    with warnings.catch_warnings(): #https://docs.python.org/3/library/warnings.html
        warnings.simplefilter("ignore")
        resultados = resultados._append(fundamentus.get_papel(acao))
    index += index
    print(acao)

resultados.to_csv('./.BancoDados/RelatoriosContabeis')

# TODO: Exportar os Dados Históricos
