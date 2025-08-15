"""

"""
import csv


def baixa_arquivos(ticker, delta_tempo=365):
    import datetime
    import yfinance
    date_end = datetime.date.today()
    delta = datetime.timedelta(days=delta_tempo)
    date_ini = date_end - delta

    dados_brutos_df = yfinance.download(ticker, start=date_ini,
                                        end=date_end)[["Adj Close"]]
    return dados_brutos_df


def calcula_media_movel(precos_df, periodo=14):
    import numpy as np
    precos_df[['change',
               'positive_change',
               'negative_change',
               'moving_average_positive_change',
               'moving_average_negative_change']] = 0
    precos_df['change'] = precos_df['Adj Close'].diff()
    precos_df['positive_change'] = np.where(precos_df['change'] > 0,
                                            abs(precos_df['change']),
                                            0)
    precos_df['negative_change'] = np.where(precos_df['change'] < 0,
                                            abs(precos_df['change']),
                                            0)
    for i in range(1, len(precos_df)):
        precos_df.iloc[i, 4] = (precos_df.iloc[i - 1, 4] * (periodo - 1) +
                                precos_df.iloc[i, 2])/periodo
        precos_df.iloc[i, 5] = (precos_df.iloc[i - 1, 5] * (periodo - 1) +
                                precos_df.iloc[i, 3]) / periodo
    return precos_df


def ultima_media_movel(precos_df):
    i = len(precos_df)
    return [
            float(precos_df.iloc[i-1, 0]),
            float(precos_df.iloc[i-1, 4]),
            float(precos_df.iloc[i-1, 5])
            ]


def IFR_preditivo(IFR_esperado, ultima_media_movel):
    FR_atual = ultima_media_movel[1] / ultima_media_movel[2]
    IFR_atual = 100 - 100/(1+FR_atual)
    FR_esperado = IFR_esperado/(100 - IFR_esperado)
    if IFR_atual >= IFR_esperado:
        moving_average_positive_change = ultima_media_movel[1] * 13 / 14
        moving_average_negative_change = moving_average_positive_change / \
                                        FR_esperado
        variacao_do_preco = moving_average_negative_change * 14 - \
                            ultima_media_movel[2] * 13
        preco_esperado = ultima_media_movel[0] - variacao_do_preco
        return preco_esperado
    elif IFR_atual < IFR_esperado:
        moving_average_negative_change = ultima_media_movel[2] * 13 / 14
        moving_average_positive_change = FR_esperado * moving_average_negative_change
        variacao_do_preco = moving_average_positive_change * 14 - \
                            ultima_media_movel[1] * 13
        preco_esperado = ultima_media_movel[0] + variacao_do_preco
        return preco_esperado

def calcula_ifr():
    import pandas as pd
    import datetime
    saida_path = './.BancoDados/ifr_banco_de_dados'
    df_saida = pd.DataFrame()
    df_acao = pd.DataFrame()
    with open("Radar.txt", "r") as Radar:
        for acao in Radar :
            # print(acao)
            dados_brutos = baixa_arquivos(acao)
            media_movel = calcula_media_movel(dados_brutos)
            umm = ultima_media_movel(media_movel)
            preco_atual = umm[0]
            ifr_atual = 100 - (100/(1 + umm[1]/umm[2]))
            ifr85 = IFR_preditivo(85, umm)
            ifr35 = IFR_preditivo(35, umm)
            df_acao = pd.DataFrame({
                'Ticker': [acao.replace('\n', '')],
                'Preço de fechamento': [preco_atual],
                'IFR atual': [ifr_atual],
                'Preço IFR 85': [ifr85],
                'Preço IFR 35': [ifr35],
                'Data': [datetime.date.today()]
            })
            df_saida = pd.concat([df_saida, df_acao])
    df_saida.set_index('Ticker', inplace=True)
    df_saida.to_csv(saida_path)


if __name__ == '__main__':
    # calcula_ifr()
    dados_brutos = baixa_arquivos('PETR4.SA')
    print(dados_brutos)
    # media_movel = calcula_media_movel(dados_brutos)
    # umm = ultima_media_movel(media_movel)
    # print(umm)
    # preco = IFR_preditivo(85, umm)
    # print(preco)
    # preco = IFR_preditivo(35, umm)
    # print(preco)
