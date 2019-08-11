#!/bin/bash

trap "rm /tmp/$$_* 2> /dev/null ;  exit" 0 1 2 3 15

for ticker in `cat ./.BancoDados/RelatoriosContabeis | cut -d';' -f1 | sed "s/ //" | sort | uniq  | tr "\n" " "`

do
lynx --dump -reload http://www.fundamentus.com.br/detalhes.php?papel=$ticker > /tmp/$$_dump_fundamentus 2>> .erros.txt


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
LastData=`cat /tmp/$$_dump_fundamentus | grep "?Últ balanço processado" | sed "s/.*processado //" | sed "s/ //"`
ultCot=`cat /tmp/$$_dump_fundamentus | grep "?Data últ cot" | sed "s/.*últ cot //" | sed "s/ //"`

echo "$ticker"

echo "$ticker;$Papel;$Cotacao;$NroAcoes;$Ativo;$PatrLiq;$LucroTrimestral;$LucroAnual;$Roic;$Setor;$SubSetor;$LastData" | sed "s/ //g" | sed "s/\.//g" >> ./.BancoDados/Bc1

echo "$ultCot;$Cotacao;$NroAcoes;$Ativo;$PatrLiq;$LucroTrimestral;$LucroAnual;$Roic;$Setor;$SubSetor;$LastData" | sed "s/ //g" | sed "s/\.//g" >> ./.BancoDados/historicas/$ticker

sleep 1
#read

done

mv ./.BancoDados/Bc1 ./.BancoDados/RelatoriosContabeis

exit 0
