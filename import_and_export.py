####################################### importando bibliotecas #####################################

import pandas as pd

from IPython.display import display

####################################################################################################

###################################### lendo um excel ##############################################

vendas_df = pd.read_excel('C:/Users/thall/Desktop/Aulas/Python para excel/Python-para-excel/tabela_vendas')

display(vendas_df)

vendas_df.to_excel('C:/Users/thall/Desktop/exports', 'Tabela Vendas')