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

#   .raw

#   .csv
DATA = pd.read_csv("http://www.evens-salies.com/country_code_baci92.csv")
DATA.info()
for j in range(len(DATA)):
    print(DATA.at[j, 'country'], DATA.at[j, 'i'])

#   .xlsx
DATA = pd.read_excel('C:/Users/evens/Documents/cardkrueger1994_short.xlsx',
        sheet_name='Feuil2',
        header=0)
DATA.info()

#   .RData
import pyreadr as r
FRAME = r.read_r('C:/Users/evens/Documents/Synth/data/synth.data.RData')
DATA = FRAME['synth.data']
DATA.info()

# Exporter
#
#   .dta
DATA.to_stata('C:/Users/evens/Documents/synth.data.dta', write_index=False)