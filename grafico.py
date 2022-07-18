################################ imports necessários ##################################

from matplotlib.ft2font import VERTICAL
from numpy import linspace
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

#######################################################################################

################################ lendo as tabelas #####################################

vendas_df_jan = pd.read_excel('tabela_apoio.xlsx', 'vendas janeiro')
vendas_df_fev = pd.read_excel('tabela_apoio.xlsx', 'vendas fevereiro')
vendas_df_mar = pd.read_excel('tabela_apoio.xlsx', 'vendas março')
vendas_df_abr = pd.read_excel('tabela_apoio.xlsx', 'vendas abril')
vendas_df_mai = pd.read_excel('tabela_apoio.xlsx', 'vendas maio')
vendas_df_jun = pd.read_excel('tabela_apoio.xlsx', 'vendas junho')
vendas_df_jul = pd.read_excel('tabela_apoio.xlsx', 'vendas julho')
vendas_df_ago = pd.read_excel('tabela_apoio.xlsx', 'vendas agosto')
vendas_df_set = pd.read_excel('tabela_apoio.xlsx', 'vendas setembro')
vendas_df_out = pd.read_excel('tabela_apoio.xlsx', 'vendas outubro')
vendas_df_nov = pd.read_excel('tabela_apoio.xlsx', 'vendas novembro')
vendas_df_dez = pd.read_excel('tabela_apoio.xlsx', 'vendas dezembro')



display(vendas_df_jul)


#######################################################################################

################################ iniciando graficos ###################################

#plt.plot(vendas_df_jul['Lucro'])
#plt.ylabel('Lucro')
#plt.show()

#######################################################################################

################################ grafico x e y ########################################


#plt.plot(vendas_df_jul['Id Compra'],vendas_df_jul['Lucro'])
#plt.ylabel('Lucro(R$)')
#plt.xlabel('Id Compra')

#plt.show()

#######################################################################################

###################### grafico x e y delimitando minimos e maximos ####################

#plt.plot(vendas_df_jul['Id Compra'], vendas_df_jul['Lucro'])
#plt.axis([10, 60, 100, 10000])
#plt.ylabel('Lucro(R$)')
#plt.xlabel('Id Compra')

#plt.show()

#######################################################################################

######################## mudando estilo de ponteiro ###################################

#plt.plot(vendas_df_jul['Id Compra'], vendas_df_jul['Lucro'], '--g')

#plt.plot(vendas_df_jul['Id Compra'], vendas_df_jul['Lucro']+500, '^b')

#plt.plot(vendas_df_jul['Id Compra'], vendas_df_jul['Lucro']-500, 'sk')

#plt.show()

######################################################################################

######################### colocando varios plots um ao lado do outro #################

jan_Lucro = vendas_df_jan['Lucro'].sum()
fev_Lucro = vendas_df_fev['Lucro'].sum()
mar_Lucro = vendas_df_mar['Lucro'].sum()
abr_Lucro = vendas_df_abr['Lucro'].sum()
mai_Lucro = vendas_df_mai['Lucro'].sum()
jun_Lucro = vendas_df_jun['Lucro'].sum()
jul_Lucro = vendas_df_jul['Lucro'].sum()
ago_Lucro = vendas_df_ago['Lucro'].sum()
set_Lucro = vendas_df_set['Lucro'].sum()
out_Lucro = vendas_df_out['Lucro'].sum()
nov_Lucro = vendas_df_nov['Lucro'].sum()
dez_Lucro = vendas_df_dez['Lucro'].sum()

valores = [jan_Lucro, fev_Lucro, mar_Lucro, abr_Lucro, mai_Lucro, jun_Lucro, jul_Lucro, ago_Lucro, set_Lucro, out_Lucro, nov_Lucro, dez_Lucro]
nomes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

plt.figure(figsize=(18,6))

x = [1, 2, 3 , 4 , 5 , 6, 7, 8, 9, 10, 11, 12]
plt.subplot(131)

plt.bar(x, valores)
plt.xticks(x, nomes, rotation=90)
plt.xlabel('Meses')
plt.ylabel('Lucro(R$)')
plt.legend('Lucro anual')




plt.subplot(132)

plt.scatter(nomes, valores, c= 'k')
plt.xticks(x, nomes, rotation=90)
plt.legend('Lucro anual')


plt.subplot(133)

plt.plot(nomes, valores, 'm-.')
plt.xticks(x, nomes, rotation=90)
plt.legend('Lucro anual')

plt.suptitle('Diferentes gráficos')

plt.show()