# Cette commande obtient le nombre de lignes d'un gros fichier .csv sans le charger complètement
# Auteur: Evens SALIES

import pandas as pd

# Pareil, mais avec la fonction read_csv de pandas et en utilisant des chunks
def count_lines_in_csv(file_path):
    line_count = 0
    chunk_size = 1000000
    for chunk in pd.read_csv(file_path, chunksize=chunk_size, dtype=str):
        line_count += len(chunk)
        print(f"We reached", line_count)
    return line_count

line_count = count_lines_in_csv('C:/Users/evens/Documents/Evens/DATA/Firm/Demography/StockEtablissementHistorique_utf8.csv')
print(f"The CSV file contains {line_count} lines.")