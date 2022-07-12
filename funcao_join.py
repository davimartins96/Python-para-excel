############################# fazendo imports ####################################

import pandas as pd

from IPython.display import display

##################################################################################

############################ importando tabelas ##################################

clientes_df = pd.read_excel('join.xlsx')
vendas_df = pd.read_excel('tabela_vendas.xlsx')
vendas_df_join = pd.read_excel('vendas_join.xlsx')

##################################################################################

display(clientes_df)
display(vendas_df)

############################### left join ########################################

#por default a função join usa o inner

leftjoin_df = clientes_df.merge(vendas_df, how='left', left_on='Id Compra', right_on='Id Compra')

display(leftjoin_df)

##################################################################################

############################### right join #######################################

rightjoin_df = clientes_df.merge(vendas_df, how='right', left_on='Id Compra', right_on='Id Compra')

display(rightjoin_df)

##################################################################################

################################ inner join ######################################

innerjoin_df = clientes_df.merge(vendas_df_join, how='inner', left_on='Id Compra', right_on='Id Compra')

display(innerjoin_df)

##################################################################################

################################ cross join ######################################

crossjoin_df = clientes_df.merge(vendas_df_join, how='cross')

##################################################################################



outerjoin_df = clientes_df.merge(vendas_df_join, how='outer', left_on='Id Compra', right_on='Id Compra')








