################################ imports necessarios ##################################

import pandas as pd

from IPython.display import display
import random
from pandas import ExcelWriter
from random import seed

#######################################################################################


################################## vendas janeiro #####################################



Produtos = ['Teclado', 'Mouse', 'Monitor', 'Placa Mãe', 'Processador', 'Headset', 'Cadeira gamer', 'Fonte de alimentação', 'Fan', 'Joystick', 'Notebook', 'Calculadora']
Precos = [89.90, 49.90, 599.90, 799.0, 2990.90, 250, 999.90, 500, 80, 250, 4000, 1500]

Size = 105


produtos_df = []
quantidade_df = []
valor_df = []
valor_final_df = []
lucro_df = []
Id_unico = []



for i in range(Size):
    posicao = random.randint(0, 11)

    quantidade = random.randint(1, 10)

    produtos_df.append(Produtos[posicao])
    quantidade_df.append(quantidade)
    valor_df.append(Precos[posicao])
    lucro_df.append(quantidade*Precos[posicao]*0.25)
    valor_final_df.append(quantidade*Precos[posicao])
    Id_unico.append(i)

vendas_df_jan = {

    'Id Compra':Id_unico,
    'Produto':produtos_df,
    'Quantidade':quantidade_df,
    'Valor':valor_df,
    'Valor Final':valor_final_df,
    'Lucro':lucro_df
}

vendas_df_jan = pd.DataFrame(vendas_df_jan)
   
    
    #######################################################################################

    ################################## vendas fevereiro ###################################

Produtos = ['Teclado', 'Mouse', 'Monitor', 'Placa Mãe', 'Processador', 'Headset', 'Cadeira gamer', 'Fonte de alimentação', 'Fan', 'Joystick', 'Notebook', 'Calculadora']
Precos = [89.90, 49.90, 599.90, 799.0, 2990.90, 250, 999.90, 500, 80, 250, 4000, 1500]

Size = 130



produtos_df = []
quantidade_df = []
valor_df = []
valor_final_df = []
lucro_df = []
Id_unico = []



for i in range(Size):
    posicao = random.randint(0, 11)

    quantidade = random.randint(1, 10)

    produtos_df.append(Produtos[posicao])
    quantidade_df.append(quantidade)
    valor_df.append(Precos[posicao])
    lucro_df.append(quantidade*Precos[posicao]*0.25)
    valor_final_df.append(quantidade*Precos[posicao])
    Id_unico.append(i)

vendas_df_fev = {

    'Id Compra':Id_unico,
    'Produto':produtos_df,
    'Quantidade':quantidade_df,
    'Valor':valor_df,
    'Valor Final':valor_final_df,
    'Lucro':lucro_df
}

vendas_df_fev = pd.DataFrame(vendas_df_fev)

#######################################################################################

################################## vendas março #######################################

Produtos = ['Teclado', 'Mouse', 'Monitor', 'Placa Mãe', 'Processador', 'Headset', 'Cadeira gamer', 'Fonte de alimentação', 'Fan', 'Joystick', 'Notebook', 'Calculadora']
Precos = [89.90, 49.90, 599.90, 799.0, 2990.90, 250, 999.90, 500, 80, 250, 4000, 1500]

Size = 130



produtos_df = []
quantidade_df = []
valor_df = []
valor_final_df = []
lucro_df = []
Id_unico = []



for i in range(Size):
    posicao = random.randint(0, 11)

    quantidade = random.randint(1, 10)

    produtos_df.append(Produtos[posicao])
    quantidade_df.append(quantidade)
    valor_df.append(Precos[posicao])
    lucro_df.append(quantidade*Precos[posicao]*0.25)
    valor_final_df.append(quantidade*Precos[posicao])
    Id_unico.append(i)

vendas_df_mar = {

    'Id Compra':Id_unico,
    'Produto':produtos_df,
    'Quantidade':quantidade_df,
    'Valor':valor_df,
    'Valor Final':valor_final_df,
    'Lucro':lucro_df
}

vendas_df_mar = pd.DataFrame(vendas_df_mar)

#######################################################################################

##################################### vendas abril ####################################

Produtos = ['Teclado', 'Mouse', 'Monitor', 'Placa Mãe', 'Processador', 'Headset', 'Cadeira gamer', 'Fonte de alimentação', 'Fan', 'Joystick', 'Notebook', 'Calculadora']
Precos = [89.90, 49.90, 599.90, 799.0, 2990.90, 250, 999.90, 500, 80, 250, 4000, 1500]

Size = 130


produtos_df = []
quantidade_df = []
valor_df = []
valor_final_df = []
lucro_df = []
Id_unico = []



for i in range(Size):
    posicao = random.randint(0, 11)

    quantidade = random.randint(1, 10)

    produtos_df.append(Produtos[posicao])
    quantidade_df.append(quantidade)
    valor_df.append(Precos[posicao])
    lucro_df.append(quantidade*Precos[posicao]*0.25)
    valor_final_df.append(quantidade*Precos[posicao])
    Id_unico.append(i)

vendas_df_abr = {

    'Id Compra':Id_unico,
    'Produto':produtos_df,
    'Quantidade':quantidade_df,
    'Valor':valor_df,
    'Valor Final':valor_final_df,
    'Lucro':lucro_df
}

vendas_df_abr = pd.DataFrame(vendas_df_abr)
    

#######################################################################################

#################################### vendas maio ######################################

Produtos = ['Teclado', 'Mouse', 'Monitor', 'Placa Mãe', 'Processador', 'Headset', 'Cadeira gamer', 'Fonte de alimentação', 'Fan', 'Joystick', 'Notebook', 'Calculadora']
Precos = [89.90, 49.90, 599.90, 799.0, 2990.90, 250, 999.90, 500, 80, 250, 4000, 1500]

Size = 90


produtos_df = []
quantidade_df = []
valor_df = []
valor_final_df = []
lucro_df = []
Id_unico = []



for i in range(Size):
    posicao = random.randint(0, 11)

    quantidade = random.randint(1, 10)

    produtos_df.append(Produtos[posicao])
    quantidade_df.append(quantidade)
    valor_df.append(Precos[posicao])
    lucro_df.append(quantidade*Precos[posicao]*0.25)
    valor_final_df.append(quantidade*Precos[posicao])
    Id_unico.append(i)

vendas_df_mai = {

    'Id Compra':Id_unico,
    'Produto':produtos_df,
    'Quantidade':quantidade_df,
    'Valor':valor_df,
    'Valor Final':valor_final_df,
    'Lucro':lucro_df
}

vendas_df_mai = pd.DataFrame(vendas_df_mai)
    
#######################################################################################

#################################### vendas junho #####################################

Produtos = ['Teclado', 'Mouse', 'Monitor', 'Placa Mãe', 'Processador', 'Headset', 'Cadeira gamer', 'Fonte de alimentação', 'Fan', 'Joystick', 'Notebook', 'Calculadora']
Precos = [89.90, 49.90, 599.90, 799.0, 2990.90, 250, 999.90, 500, 80, 250, 4000, 1500]

Size = 92

produtos_df = []
quantidade_df = []
valor_df = []
valor_final_df = []
lucro_df = []
Id_unico = []



for i in range(Size):
    posicao = random.randint(0, 11)

    quantidade = random.randint(1, 10)

    produtos_df.append(Produtos[posicao])
    quantidade_df.append(quantidade)
    valor_df.append(Precos[posicao])
    lucro_df.append(quantidade*Precos[posicao]*0.25)
    valor_final_df.append(quantidade*Precos[posicao])
    Id_unico.append(i)

vendas_df_jun = {

    'Id Compra':Id_unico,
    'Produto':produtos_df,
    'Quantidade':quantidade_df,
    'Valor':valor_df,
    'Valor Final':valor_final_df,
    'Lucro':lucro_df
}

vendas_df_jun = pd.DataFrame(vendas_df_jun)

#######################################################################################

#################################### vendas julho #####################################

Produtos = ['Teclado', 'Mouse', 'Monitor', 'Placa Mãe', 'Processador', 'Headset', 'Cadeira gamer', 'Fonte de alimentação', 'Fan', 'Joystick', 'Notebook', 'Calculadora']
Precos = [89.90, 49.90, 599.90, 799.0, 2990.90, 250, 999.90, 500, 80, 250, 4000, 1500]

Size = 68

produtos_df = []
quantidade_df = []
valor_df = []
valor_final_df = []
lucro_df = []
Id_unico = []



for i in range(Size):
    posicao = random.randint(0, 11)

    quantidade = random.randint(1, 10)

    produtos_df.append(Produtos[posicao])
    quantidade_df.append(quantidade)
    valor_df.append(Precos[posicao])
    lucro_df.append(quantidade*Precos[posicao]*0.25)
    valor_final_df.append(quantidade*Precos[posicao])
    Id_unico.append(i)

vendas_df_jul = {

    'Id Compra':Id_unico,
    'Produto':produtos_df,
    'Quantidade':quantidade_df,
    'Valor':valor_df,
    'Valor Final':valor_final_df,
    'Lucro':lucro_df
}

vendas_df_jul = pd.DataFrame(vendas_df_jul)

#######################################################################################

#################################### vendas agosto ####################################

Produtos = ['Teclado', 'Mouse', 'Monitor', 'Placa Mãe', 'Processador', 'Headset', 'Cadeira gamer', 'Fonte de alimentação', 'Fan', 'Joystick', 'Notebook', 'Calculadora']
Precos = [89.90, 49.90, 599.90, 799.0, 2990.90, 250, 999.90, 500, 80, 250, 4000, 1500]

Size = 86

produtos_df = []
quantidade_df = []
valor_df = []
valor_final_df = []
lucro_df = []
Id_unico = []



for i in range(Size):
    posicao = random.randint(0, 11)

    quantidade = random.randint(1, 10)

    produtos_df.append(Produtos[posicao])
    quantidade_df.append(quantidade)
    valor_df.append(Precos[posicao])
    lucro_df.append(quantidade*Precos[posicao]*0.25)
    valor_final_df.append(quantidade*Precos[posicao])
    Id_unico.append(i)

vendas_df_ago = {

    'Id Compra':Id_unico,
    'Produto':produtos_df,
    'Quantidade':quantidade_df,
    'Valor':valor_df,
    'Valor Final':valor_final_df,
    'Lucro':lucro_df
}

vendas_df_ago = pd.DataFrame(vendas_df_ago)

#######################################################################################

#################################### vendas setembro ##################################

Produtos = ['Teclado', 'Mouse', 'Monitor', 'Placa Mãe', 'Processador', 'Headset', 'Cadeira gamer', 'Fonte de alimentação', 'Fan', 'Joystick', 'Notebook', 'Calculadora']
Precos = [89.90, 49.90, 599.90, 799.0, 2990.90, 250, 999.90, 500, 80, 250, 4000, 1500]

Size = 93

produtos_df = []
quantidade_df = []
valor_df = []
valor_final_df = []
lucro_df = []
Id_unico = []



for i in range(Size):
    posicao = random.randint(0, 11)

    quantidade = random.randint(1, 10)

    produtos_df.append(Produtos[posicao])
    quantidade_df.append(quantidade)
    valor_df.append(Precos[posicao])
    lucro_df.append(quantidade*Precos[posicao]*0.25)
    valor_final_df.append(quantidade*Precos[posicao])
    Id_unico.append(i)

vendas_df_set = {

    'Id Compra':Id_unico,
    'Produto':produtos_df,
    'Quantidade':quantidade_df,
    'Valor':valor_df,
    'Valor Final':valor_final_df,
    'Lucro':lucro_df
}

vendas_df_set = pd.DataFrame(vendas_df_set)

#######################################################################################

#################################### vendas outubro ###################################

Produtos = ['Teclado', 'Mouse', 'Monitor', 'Placa Mãe', 'Processador', 'Headset', 'Cadeira gamer', 'Fonte de alimentação', 'Fan', 'Joystick', 'Notebook', 'Calculadora']
Precos = [89.90, 49.90, 599.90, 799.0, 2990.90, 250, 999.90, 500, 80, 250, 4000, 1500]

Size = 72

produtos_df = []
quantidade_df = []
valor_df = []
valor_final_df = []
lucro_df = []
Id_unico = []



for i in range(Size):
    posicao = random.randint(0, 11)

    quantidade = random.randint(1, 10)

    produtos_df.append(Produtos[posicao])
    quantidade_df.append(quantidade)
    valor_df.append(Precos[posicao])
    lucro_df.append(quantidade*Precos[posicao]*0.25)
    valor_final_df.append(quantidade*Precos[posicao])
    Id_unico.append(i)

vendas_df_out = {

    'Id Compra':Id_unico,
    'Produto':produtos_df,
    'Quantidade':quantidade_df,
    'Valor':valor_df,
    'Valor Final':valor_final_df,
    'Lucro':lucro_df
}

vendas_df_out = pd.DataFrame(vendas_df_out)

#######################################################################################

#################################### vendas novembro ##################################

Produtos = ['Teclado', 'Mouse', 'Monitor', 'Placa Mãe', 'Processador', 'Headset', 'Cadeira gamer', 'Fonte de alimentação', 'Fan', 'Joystick', 'Notebook', 'Calculadora']
Precos = [89.90, 49.90, 599.90, 799.0, 2990.90, 250, 999.90, 500, 80, 250, 4000, 1500]

Size = 52

produtos_df = []
quantidade_df = []
valor_df = []
valor_final_df = []
lucro_df = []
Id_unico = []



for i in range(Size):
    posicao = random.randint(0, 11)

    quantidade = random.randint(1, 10)

    produtos_df.append(Produtos[posicao])
    quantidade_df.append(quantidade)
    valor_df.append(Precos[posicao])
    lucro_df.append(quantidade*Precos[posicao]*0.25)
    valor_final_df.append(quantidade*Precos[posicao])
    Id_unico.append(i)

vendas_df_nov = {

    'Id Compra':Id_unico,
    'Produto':produtos_df,
    'Quantidade':quantidade_df,
    'Valor':valor_df,
    'Valor Final':valor_final_df,
    'Lucro':lucro_df
}

vendas_df_nov = pd.DataFrame(vendas_df_nov)

#######################################################################################

#################################### vendas dezembro ##################################

Produtos = ['Teclado', 'Mouse', 'Monitor', 'Placa Mãe', 'Processador', 'Headset', 'Cadeira gamer', 'Fonte de alimentação', 'Fan', 'Joystick', 'Notebook', 'Calculadora']
Precos = [89.90, 49.90, 599.90, 799.0, 2990.90, 250, 999.90, 500, 80, 250, 4000, 1500]

Size = 145

produtos_df = []
quantidade_df = []
valor_df = []
valor_final_df = []
lucro_df = []
Id_unico = []



for i in range(Size):
    posicao = random.randint(0, 11)

    quantidade = random.randint(1, 10)

    produtos_df.append(Produtos[posicao])
    quantidade_df.append(quantidade)
    valor_df.append(Precos[posicao])
    lucro_df.append(quantidade*Precos[posicao]*0.25)
    valor_final_df.append(quantidade*Precos[posicao])
    Id_unico.append(i)

vendas_df_dez = {

    'Id Compra':Id_unico,
    'Produto':produtos_df,
    'Quantidade':quantidade_df,
    'Valor':valor_df,
    'Valor Final':valor_final_df,
    'Lucro':lucro_df
}

vendas_df_dez = pd.DataFrame(vendas_df_dez)

#######################################################################################

################################## exportando os dados ################################



with pd.ExcelWriter('C:/Users/thall/Desktop/exports/tabela_apoio.xlsx') as writer:
    vendas_df_jan.to_excel(writer, sheet_name='vendas janeiro')
    vendas_df_fev.to_excel(writer, sheet_name='vendas fevereiro')
    vendas_df_mar.to_excel(writer, sheet_name='vendas março')
    vendas_df_abr.to_excel(writer, sheet_name='vendas abril')
    vendas_df_mai.to_excel(writer, sheet_name='vendas maio')
    vendas_df_jun.to_excel(writer, sheet_name='vendas junho')
    vendas_df_jul.to_excel(writer, sheet_name='vendas julho')
    vendas_df_ago.to_excel(writer, sheet_name='vendas agosto')
    vendas_df_set.to_excel(writer, sheet_name='vendas setembro')
    vendas_df_out.to_excel(writer, sheet_name='vendas outubro')
    vendas_df_nov.to_excel(writer, sheet_name='vendas novembro')
    vendas_df_dez.to_excel(writer, sheet_name='vendas dezembro')



