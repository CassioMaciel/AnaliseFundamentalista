import pandas as pd
from openpyxl import Workbook, load_workbook
from datetime import datetime
from logging import debug, warning
from logging import basicConfig, DEBUG, WARNING

basicConfig(level=WARNING)


dados_fundamentalistas_df = pd.read_csv("./.BancoDados/RelatoriosContabeis",
                                        index_col=0)

planilha = load_workbook(
    r"C:\Users\EVKB\OneDrive - PETROBRAS\Documentos\Python\ProgBolsa\ROA.xlsx")

aba_inativa = planilha["ROA"]
aba_ativa = planilha["Data_Base"]

aba_ativa[f"A1"] = "Ticker"
aba_ativa[f"B1"] = "Cotação"
aba_ativa[f"C1"] = "Nro. Ações"
aba_ativa[f"D1"] = "Ativos"
aba_ativa[f"E1"] = "Pat.Liq."
aba_ativa[f"F1"] = "Lucro"
aba_ativa[f"G1"] = "Ultmo Balanço"
aba_ativa[f"H1"] = "Volume"
aba_ativa[f"I1"] = "Ultima Cotação"
aba_ativa[f"J1"] = "Cres. Rec. 5a"
aba_ativa[f"K1"] = "Ebitda"
aba_ativa[f"L1"] = "ROIC"

index = 2

for ticker in dados_fundamentalistas_df.index:
    linha = index
    debug(ticker)
    aba_ativa[f"A{linha}"] = ticker
    aba_ativa[f"B{linha}"] = \
        dados_fundamentalistas_df.loc[ticker, "Cotacao"]

    aba_ativa[f"C{linha}"] = \
        dados_fundamentalistas_df.loc[ticker, "Nro_Acoes"]

    aba_ativa[f"D{linha}"] = \
        dados_fundamentalistas_df.loc[ticker, "Ativo"]

    aba_ativa[f"E{linha}"] = \
        dados_fundamentalistas_df.loc[ticker, "Patrim_Liq"]

    aba_ativa[f"F{linha}"] = \
        dados_fundamentalistas_df.loc[ticker, "Lucro_Liquido_12m"]

    aba_ativa[f"G{linha}"] = \
        datetime.strptime(
            dados_fundamentalistas_df.loc[ticker, "Ult_balanco_processado"],
            "%Y-%m-%d"
        )

    aba_ativa[f"H{linha}"] = \
        dados_fundamentalistas_df.loc[ticker, "Vol_med_2m"]

    debug(dados_fundamentalistas_df.loc[ticker, "Data_ult_cot"])

    debug(type(dados_fundamentalistas_df.loc[ticker, "Data_ult_cot"]))

    try:
        aba_ativa[f"I{linha}"] = datetime.strptime(
            dados_fundamentalistas_df.loc[ticker, "Data_ult_cot"],
            "%Y-%m-%d"
        )
    except TypeError as e:
        debug(f"Erro ao converter a data: {e}")
        aba_ativa[f"I{linha}"] = \
            dados_fundamentalistas_df.loc[ticker, "Data_ult_cot"]

    index += 1

    cres_rec_5a = dados_fundamentalistas_df.loc[ticker, "Cres_Rec_5a"]
    if cres_rec_5a != '-':
        cres_rec_5a = cres_rec_5a.split('%')
        aba_ativa[f"J{linha}"] = float(cres_rec_5a[0]) / 100
    else:
        aba_ativa[f"J{linha}"] = ""

    aba_ativa[f"K{linha}"] = \
        dados_fundamentalistas_df.loc[ticker, 'EBIT_12m']

    roic = dados_fundamentalistas_df.loc[ticker, 'ROIC']
    if roic != '-':
        roic = roic.split('%')
        aba_ativa[f"L{linha}"] = float(roic[0]) / 100
    else:
        aba_ativa[f"L{linha}"] = ""



# TODO: Colocar para salvar o excel em uma pasta escolhida pelo usuario
# print(dados_fundamentalistas_df.keys())

planilha.save(
    r"C:\Users\EVKB\OneDrive - PETROBRAS\Documentos\Python\ProgBolsa\ROA.xlsx")
