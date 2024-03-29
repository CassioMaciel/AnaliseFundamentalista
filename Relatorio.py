import pandas as pd
from openpyxl import Workbook, load_workbook
from openpyxl.styles import NamedStyle
from datetime import datetime

dados_fundamentalistas_df = pd.read_csv("./.BancoDados/RelatoriosContabeis",
                                        index_col=0)

planilha = load_workbook(r"C:\Users\EVKB\OneDrive - PETROBRAS\Documentos\Python\ProgBolsa\ROA.xlsx")

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

index = 2

for ticker in dados_fundamentalistas_df.index:
    linha = index
    aba_ativa[f"A{linha}"] = ticker
    aba_ativa[f"B{linha}"] = dados_fundamentalistas_df.loc[ticker, "Cotacao"]
    aba_ativa[f"C{linha}"] = dados_fundamentalistas_df.loc[ticker, "Nro_Acoes"]
    aba_ativa[f"D{linha}"] = dados_fundamentalistas_df.loc[ticker, "Ativo"]
    aba_ativa[f"E{linha}"] = dados_fundamentalistas_df.loc[ticker, "Patrim_Liq"]
    aba_ativa[f"F{linha}"] = dados_fundamentalistas_df.loc[ticker, "Lucro_Liquido_12m"]
    aba_ativa[f"G{linha}"] = datetime.strptime(dados_fundamentalistas_df.loc[ticker, "Ult_balanco_processado"], "%Y-%m-%d")
    aba_ativa[f"H{linha}"] = dados_fundamentalistas_df.loc[ticker, "Vol_med_2m"]

    index += 1

# TODO: Colocar para salvar o excel em uma pasta escolhida pelo usuario
# print(dados_fundamentalistas_df.keys())

planilha.save(r"C:\Users\EVKB\OneDrive - PETROBRAS\Documentos\Python\ProgBolsa\ROA.xlsx")
