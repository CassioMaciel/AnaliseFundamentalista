#!/bin/bash

trap "rm /tmp/$$_* 2> /dev/null ;  exit" 0 1 2 3 15

echo "Papel;Setor;Subsetor;Cotação;Ativo;Patrimonio Liquido;Lucro Anual;Lucro Trimestral;ROIC" > "/home/cassio/Documentos/Balanços/Balanços.csv"

for acao in `cat ativos | sed "s/ //" | sort | uniq  | tr "\n" " "`

do
lynx --dump -reload http://www.fundamentus.com.br/detalhes.php?papel=$acao > /tmp/$$_dump_fundamentus 2>> .erros.txt



Papel=`cat /tmp/$$_dump_fundamentus | grep "?Papel" | sed "s/?Cotação.*$//g" | sed "s/?Papel //g" | sed "s/ //g"`
Cotacao=`cat /tmp/$$_dump_fundamentus | grep "?Cotação" | sed "s/.*?Cotação//g"`
NroAcoes=`cat /tmp/$$_dump_fundamentus | grep "?Nro. Ações" | sed "s/.*?Nro. Ações//g"`
Ativo=`cat /tmp/$$_dump_fundamentus | grep "?Dív. Bruta" | sed "s/\?Dív\. Bruta.*$//g" | sed "s/?Ativo //g"`
PatrLiq=`cat /tmp/$$_dump_fundamentus | grep "?Patrim. Líq" | sed "s/^.*?Patrim. Líq//g"`
LucroTrimestral=`cat /tmp/$$_dump_fundamentus | grep "?Lucro Líquido" | sed "s/.*?Lucro Líquido//g"`
LucroAnual=`cat /tmp/$$_dump_fundamentus | grep "?Lucro Líquido" | sed  -r "s/\?Lucro Líquido(.*)\?Lucro Líquido.*/\1/g"`
Setor=`cat /tmp/$$_dump_fundamentus | grep "?Setor" | sed "s/ *?Max 52 sem.*//g" | sed "s/.*]//g"`
SubSetor=`cat /tmp/$$_dump_fundamentus | grep "?Subsetor" | sed "s/ *?Vol.*//g" | sed "s/.*]//g"`
Roic=`cat /tmp/$$_dump_fundamentus | grep "?ROIC" | sed "s/.*?ROIC//g"`

echo "$acao -- $Setor"

financeiro=`echo "$Cotacao;=$Ativo/$NroAcoes;=$PatrLiq/$NroAcoes;=$LucroAnual/$NroAcoes;=$LucroTrimestral/$NroAcoes;$Roic" | sed "s/ //g" | sed "s/\.//g"`

echo "$Papel;$Setor;$SubSetor;$financeiro" >> "/home/cassio/Documentos/Balanços/Balanços.csv"

sleep 1

done
