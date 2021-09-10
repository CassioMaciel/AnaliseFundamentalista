#!/bin/bash

trap "rm /tmp/$$_* 2> /dev/null ;  exit" 0 1 2 3 15

echo "Ticker;Setor;Qtd;;Cotação;LPA;VPA;;Valor Merc.;Lucro;Patrimonio Liq.;;Valuation"> /tmp/$$_carteira.csv

for Ticker in `cat ./.BancoDados/carteira | cut -d ";" -f 1`

do
	Qtd=`cat ./.BancoDados/carteira | grep $Ticker | cut -d ";" -f 2`
	PatrLiq=`cat ./.BancoDados/RelatoriosContabeis | grep $Ticker | cut -d ";" -f 6`
	LucroLiq=`cat ./.BancoDados/RelatoriosContabeis | grep $Ticker | cut -d ";" -f 8`
	NroAcoes=`cat ./.BancoDados/RelatoriosContabeis | grep $Ticker | cut -d ";" -f 4`
	Cotacao=`cat ./.BancoDados/RelatoriosContabeis | grep $Ticker | cut -d ";" -f 3`
	Setor=`cat ./.BancoDados/RelatoriosContabeis | grep $Ticker | cut -d ";" -f 10`
	SubSetor=`cat ./.BancoDados/RelatoriosContabeis | grep $Ticker | cut -d ";" -f 11`
	echo "$Ticker;$Setor;$Qtd;;$Cotacao;=$LucroLiq/$NroAcoes;=$PatrLiq/$NroAcoes" >> /tmp/$$_carteira.csv
done
unoconv -i FilterOptions=59,34,utf-8,1,1/1/1/1/1 -f ods --output './Carteira.ods' "/tmp/$$_carteira.csv"
