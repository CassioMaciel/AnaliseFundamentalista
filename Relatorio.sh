#!/bin/bash

trap "rm /tmp/$$_* 2> /dev/null ;  exit" 0 1 2 3 15

cat ./.BancoDados/RelatoriosContabeis | cut -d ";" -f 1 | sed "1iTicker" > /tmp/$$_Ticker
cat ./.BancoDados/RelatoriosContabeis | cut -d ";" -f 3 | sed "1iCotação" > /tmp/$$_Preço
cat ./.BancoDados/RelatoriosContabeis | cut -d ";" -f 5 | sed "1iAtivos" > /tmp/$$_Ativos
cat ./.BancoDados/RelatoriosContabeis | cut -d ";" -f 6 | sed "1iPatrimônio Liquido" > /tmp/$$_PatLiq
cat ./.BancoDados/RelatoriosContabeis | cut -d ";" -f 8 | sed "1iLucro Liquido" > /tmp/$$_LucroLiq
cat ./.BancoDados/RelatoriosContabeis | cut -d ";" -f 12 | sed "1iData do Ultimo Balanço"  > /tmp/$$_UltBalanco
cat ./.BancoDados/RelatoriosContabeis | cut -d ";" -f 4 | sed "1iNumero de ações" > /tmp/$$_NroAcoes

paste -d "/" /tmp/$$_Ativos /tmp/$$_NroAcoes | sed "s/^/=/" | sed "1cAtivos Por Ação" > /tmp/$$_APA

paste -d "/" /tmp/$$_PatLiq /tmp/$$_NroAcoes | sed "s/^/=/" | sed "1cPatrimônio liq. por ação" > /tmp/$$_PPA

paste -d "/" /tmp/$$_LucroLiq /tmp/$$_NroAcoes | sed "s/^/=/" | sed "1cLucro por ação" > /tmp/$$_LPA

cat -b /tmp/$$_Ticker | cut -f 1 | sed -r "s/^ *(.*)/=E\1\/C\1/" | sed "1cROA"  > /tmp/$$_ROA

cat -b /tmp/$$_Ticker | cut -f 1 | sed -r "s/^ *(.*)/=\(B\1-D\1\)\/B\1/" | sed "1cP/VPA" > /tmp/$$_PVPA

cat -b /tmp/$$_Ticker | cut -f 1 | sed -r "s/^ *(.*)/=COUNTIF(\$F:\$F;\">=\"\&F\1)/" | sed "1cPI1" > /tmp/$$_PI1

cat -b /tmp/$$_Ticker | cut -f 1 | sed -r "s/^ *(.*)/=COUNTIF(\$G:\$G;\"<=\"\&G\1)/" | sed "1cPI2" > /tmp/$$_PI2

cat -b /tmp/$$_Ticker | cut -f 1 | sed -r "s/^ *(.*)/=H\1+I\1/" | sed "1cSoma" > /tmp/$$_Soma

paste -d "@" /tmp/$$_Ticker /tmp/$$_Preço /tmp/$$_APA /tmp/$$_PPA /tmp/$$_LPA /tmp/$$_ROA /tmp/$$_PVPA /tmp/$$_PI1 /tmp/$$_PI2 /tmp/$$_Soma > /tmp/$$_Geral.csv

unoconv -i FilterOptions=64,34,utf-8,1,1 -f ods --output '/home/cassio/Documentos/Balancos/Geral.ods' "/tmp/$$_Geral.csv"

#ssconvert --merge-to=all.ods basico.csv basico2.csv 

#sc
