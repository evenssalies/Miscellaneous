# Variation sur la commande print
# Auteur: Evens SALIES
#   Source of 1590 OpenML dataset: Ron Kohavi, "Scaling Up the Accuracy of Naive-Bayes Classifiers:
#       a Decision-Tree Hybrid", Proceedings of the Second International Conference on Knowledge
#       Discovery and Data Mining, 1996
#   Adaptation of code source: https://www.fun-mooc.fr/fr/cours/machine-learning-python-scikit-learn/

import pandas as pd

#   Première valeur de la variable RD_COU_TOTAL_TOTAL
DATA = pd.read_stata('http://www.evens-salies.com/rd_e_gerdfund.dta')
DATA.info()
VAR = DATA.at[0, 'RD_COU_TOTAL_TOTAL']
print(VAR)

#   Deux colonnes d'un tableau .csv side by side (country, i)
DATA = pd.read_csv('http://www.evens-salies.com/country_code_baci92.csv')
DATA.info()
for j in range(len(DATA)):
    print(DATA.at[j, 'country'], DATA.at[j, 'i'])

#   Va chercher la prochaine base dans openml
import openml
DATASET = openml.datasets.get_dataset(1590)

#       Les données sont organisées en X|y|categorical_indicator|attribute_names (we ignore the last two):
# _: categorical_indicator is a boolean array that indicates which columns are categorical.
# _: attribute_names is a list of strings representing the names of the columns in the dataset.
X, y, _, _ = DATASET.get_data(target=DATASET.default_target_attribute)

#       Concaténation des deux tableaux
DATA = pd.concat([X, y], axis=1)

#       Informations sur le tableau avec la méthode info()
DATA.info()

#       Les 5 premières lignes avec la fonction print()
print(DATA.head())

#       Les valeurs uniques de la feature "class"
print(DATA['class'].value_counts())

#       Sélectionne y et un sous-ensemble X de features en séparant les variables numériques des catégorielles
#       (il s'agit de listes).
TARGET = 'class'
FEAT_CON = ['age', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
FEAT_CAT = ['workclass', 'education', 'marital-status', 'occupation',
            'relationship', 'race', 'sex', 'native-country']

#      Concaténation des colonnes
Xy = FEAT_CON + FEAT_CAT + [TARGET]

#       Remplace DATA par les variables du sous-ensemble
DATA = DATA[Xy]

#       Affiche le nombre d'observations et de variables (X, y)
print(f"The dataset contains {DATA.shape[0]} observations and {DATA.shape[1]} variables")

#       Nombre de features (#variables - 1) et de classes (#elements dans TARGET)
print(f"Parmi les variables, il y a {DATA.shape[1] - 1} features et {len([TARGET])} classe(s).")

#       Tableau de fréquences
print(DATA['workclass'].value_counts(), end='\n\n')
print(DATA['sex'].value_counts())