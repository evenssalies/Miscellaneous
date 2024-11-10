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
DATA = pd.read_csv('myfile.csv')

#   .xlsx
DATA = pd.read_excel('myfile.xlsx',
        sheet_name='sheetname',
        header=0)

#   .RData
import pyreadr as r
FRAME = r.read_r('myfile.RData')
DATA = FRAME['mydata.data']

# Exporter
#
#   .dta
DATA.to_stata('filename.dta', write_index=False)
