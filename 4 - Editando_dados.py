################################### Importando bibliotecas ########################################

import pandas as pd
from IPython.display import display

###################################################################################################


################################### Lendo os arquivos #############################################


vendas_df = pd.read_excel('tabela_vendas.xlsx')
clientes_df = pd.read_excel('tabela_clientes.xlsx')
clientes_df_2 = pd.read_excel('tabela_clientes_2.xlsx')


###################################################################################################

################################### criando novas colunas #########################################

display(vendas_df)



vendas_df['Comissão'] = vendas_df['Lucro']*0.3

vendas_df.loc[:, 'Modelo'] = 0

display(vendas_df)



###################################################################################################

################################### alterando um ou mais dados ####################################

vendas_df.loc[vendas_df['Quantidade'] == 2, 'Modelo'] = 5

display(vendas_df)

###################################################################################################
############################ adicionando linhas ###################################################

clientes_df = clientes_df.append(clientes_df_2)

display(clientes_df)