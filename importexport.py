# Importer
#
#   .dta
import pandas as pd
DATA = pd.read_stata('myfile.dta')

#   .raw (do later)

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
