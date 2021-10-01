#!/bin/bash

trap "rm /tmp/$$_* 2> /dev/null ;  exit" 0 1 2 3 15

Ticker=TKNO4

echo "Data;Cotacao;VPA;LPA;Roic;Graham;Porcentagem" > /tmp/$$_Ativo.csv

for Data in `cat ./.BancoDados/historicas/$Ticker | cut -d ";" -f 1 | sort | uniq`
do
	PatrLiq=`cat ./.BancoDados/historicas/$Ticker | grep ^$Data | sort | uniq | cut -d ";" -f 5`
	LucroLiq=`cat ./.BancoDados/historicas/$Ticker | grep ^$Data | sort | uniq | cut -d ";" -f 7`
	NroAcoes=`cat ./.BancoDados/historicas/$Ticker | grep ^$Data | sort | uniq | cut -d ";" -f 3`
	Cotacao=`cat ./.BancoDados/historicas/$Ticker | grep ^$Data | sort | uniq | cut -d ";" -f 2`
	echo "$Data;$Cotacao;=$PatrLiq/$NroAcoes;=$LucroLiq/$NroAcoes" >> /tmp/$$_Ativo.csv
done

unoconv -i FilterOptions=59,34,utf-8,1,5/1/1/1/1/1/1/1 -f ods --output "./$Ticker.ods" "/tmp/$$_Ativo.csv"

