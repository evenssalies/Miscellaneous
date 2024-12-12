# Cette routine obtient le nombre de lignes d'un gros fichier .csv sans le charger complètement.
#   Nous l'appliquons au fichier de 8,3 Go de recensement des établissements localisés en France
#       StockEtablissementHistorique_utf8.csv, disponible sur data.gouv.fr :
#       Pour le télécharger directement :
#       https://www.data.gouv.fr/en/datasets/base-sirene-des-entreprises-et-de-leurs-etablissements-siren-siret/
#
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

line_count = count_lines_in_csv('... StockEtablissementHistorique_utf8.csv')
print(f"The CSV file contains {line_count} lines.")