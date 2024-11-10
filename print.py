# Importer
#
#   .dta
import pandas as pd
DATA = pd.read_stata('http://www.evens-salies.com/rd_e_gerdfund.dta')

#       Les variables du fichier, missing et type
DATA.info()

#       Première valeur de la variable RD_COU_TOTAL_TOTAL
VAR = DATA.at[0, 'RD_COU_TOTAL_TOTAL']
print(VAR)

#       Deux colonnes d'un tableau .csv side by side
#       (country et i)
DATA = pd.read_csv('http://www.evens-salies.com/country_code_baci92.csv')
DATA.info()
for j in range(len(DATA)):
    print(DATA.at[j, 'country'], DATA.at[j, 'i'])