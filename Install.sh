#!/bin/bash

trap "rm /tmp/$$_* 2> /dev/null ;  exit" 0 1 2 3 15


git init
git remote add origin https://github.com/CassioMaciel/AnaliseFundamentalista.git
git config --global credential.helper cache
git config --global user.name "Cássio Maciel Lemos"
git config --global user.email "cassio.mac.eng@gmail.com"
git pull origin master
#git pull https://github.com/CassioMaciel/AnaliseFundamentalista.git/AtualizarDados.sh
#git pull https://github.com/CassioMaciel/AnaliseFundamentalista/blob/master/AtualizarDados.sh


#git add README.md
#git commit -m "first commit"
#git remote add origin https://github.com/CassioMaciel/Scripts-Python.git
#git push -u origin master
#git status
#git config -l
#git config --global user.email "cassio.mac.eng@gmail.com"
#git config --global user.name "Cássio Maciel Lemos"
#git config --global credential.helper cache
#git clone
#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





#git add AtualizarDados.sh 
#git add Relatorio.sh
#git add ./.BancoDados/historica
#git commit -m "atualização 20210901"


