################################ import necessários ##################################

import pandas as pd
from IPython.display import display

######################################################################################

############################## lendo o arquivo csv ###################################

clientes_df = pd.read_excel('tabela_clientes.xlsx')
vendas_df = pd.read_excel('tabela_vendas.xlsx')

######################################################################################

########################### buscando dados no dataframe ##############################

clientes = clientes_df[['Nome Cliente', 'Email', 'CPF']]

uma_linha = vendas_df.loc[1] #pega a linha com indice 1

varias_linhas = vendas_df.loc[1:3] # pega da linha 1 até a linha 3

condicao = vendas_df.loc[vendas_df['Id Compra']== 10,] ## usa uma condicao para encontrar a informação necessária

formatando_a_tabela = vendas_df.loc[vendas_df['Id Compra'] == 10, ['Id Compra','Produto', 'Quantidade', 'Valor final']]

display(formatando_a_tabela)

######################################################################################

#metodo .head(número de linhas iniciais que você pretende ver no terminal)
#metodo .shape mostra quantas linhas e colunas possui o seu banco de dados
#metodo .describe() mostra vários parametros da tabela como contar os valores numericos
#mostrar os máximos e minimos e a média dos valores na tabela e descio padrão std



