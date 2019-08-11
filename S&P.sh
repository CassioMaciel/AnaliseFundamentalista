#!/bin/bash

trap "rm /tmp/$$_* 2> /dev/null ;  exit" 0 1 2 3 15

echo "Ticker;P/B;Roa" > SeP.csv

for ticker in `cat "/home/cassio/Documentos/Balanços/.BancoDados/Ativos S&P"`
do

lynx --dump -reload https://finviz.com/quote.ashx?t=$ticker > /tmp/$$_dump_fundamentus

Preco=`cat /tmp/$$_dump_fundamentus | grep "Book/sh" | sed "s/.*P\/B//" | sed "s/EPS.*//" | sed "s/\./,/"`
Roa=`cat /tmp/$$_dump_fundamentus | grep "ROA" | sed "s/.*ROA//" | sed "s/Target.*//" | sed "s/\./,/"`

echo "$ticker;$Preco;$Roa" >> SeP.csv

echo "$ticker"

done

exit 0
