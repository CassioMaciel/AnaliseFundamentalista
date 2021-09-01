#!/bin/bash

trap "rm /tmp/$$_* 2> /dev/null ;  exit" 0 1 2 3 15


git init
git remote add origin https://github.com/CassioMaciel/AnaliseFundamentalista.git
#git config --global user.name "Cássio Maciel Lemos"
#git config --global user.email "cassio.mac.eng@gmail.com"
#git config --global credential.helper cache
#git config --global credential.helper store
git pull origin master




