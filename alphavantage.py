#BASEADO EM CURSO HASHTAG COMO USAR API ALPHAVANTAGE
import requests
import pandas as pd
from io import StringIO

acoes = ['BRCO11', 'BTCI11', 'TGAR11', 'KFOF11', 'HFOF11', 'BTLG11', 'GARE11', 'XPLG11', 'KNCA11', 'GTWR11', 'RZTR11', 'vghf11', 'VISC11', 'XPML11']

compilada = pd.DataFrame()

for acao in acoes:
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={acao}.SAO&apikey=W8ZF3XX8VJNT7SYB&datatype=csv'
    r = requests.get(url)
    tabela = pd.read_csv(StringIO(r.text))
    lista_tabelas = [compilada, tabela]
    compilada = pd.concat(lista_tabelas)
    
print(compilada)
