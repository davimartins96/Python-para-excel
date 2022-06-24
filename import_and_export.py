####################################### importando bibliotecas #####################################

import pandas as pd

from IPython.display import display

####################################################################################################

###################################### lendo um excel ##############################################

vendas_df = pd.read_csv('https://raw.githubusercontent.com/Thallysson-br/Python-para-excel/main/tabela_vendas.csv?token=GHSAT0AAAAAABV56W3S7EWGNRAGGTDXSCVGYVVXIWA', sep=';')

display(vendas_df)

##vendas_df.to_excel('C:/Users/thall/Desktop/exports/Tabela Vendas.xlsx',sheet_name='Tabela Vendas')

####################################################################################################