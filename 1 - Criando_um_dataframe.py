######################################### importando bibliotecas ###########################################

import pandas as pd
from IPython.display import display

#py -m pip ipython

############################################################################################################

######################################### criando um dataFrame #############################################

vendas = {
    'Id Compra':['1', '2', '3', '4', '5', '6'],
    'Produto':['a', 'b', 'c', 'd', 'e', 'f'],
    'Valor':[100, 200, 300, 400, 500, 600],
    'Lucro':[20, 40, 60, 80, 100, 120]
}

vendas_df = pd.DataFrame(vendas)

display(vendas_df)