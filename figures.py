# Graphiques
# Auteur: Evens SALIES
#   Voir print.py pour les comentaires sur l'étape d'importation et préparation des données
#       Source of 1590 OpenML dataset: Ron Kohavi, "Scaling Up the Accuracy of Naive-Bayes Classifiers: a Decision-Tree Hybrid",
#           Proceedings of the Second International Conference on Knowledge Discovery and Data Mining, 1996

# Importation des librairies
import pandas as pd

# Importation et préparation des données d'OpenML
import openml
DATASET = openml.datasets.get_dataset(1590)
X, y, _, _ = DATASET.get_data(target=DATASET.default_target_attribute)
DATA = pd.concat([X, y], axis=1)
TARGET = 'class'
FEAT_CON = ['age', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
FEAT_CAT = ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']
Xy = FEAT_CON + FEAT_CAT + [TARGET]
DATA = DATA[Xy]

# Importation de matplotlib pour afficher les graphiques
import matplotlib.pyplot as plt

"""# Histogramme (placé dans un garbage objet)
DATA.hist(figsize=(10, 7))
plt.show()

# Pour les variables catégorielles, je peux utiliser la méthode value_counts() pour afficher les fréquences
print(DATA['workclass'].value_counts(), end='\n\n')
print(DATA['education'].value_counts(), end='\n\n')
print(DATA['marital-status'].value_counts(), end='\n\n')
print(DATA['occupation'].value_counts(), end='\n\n')
print(DATA['relationship'].value_counts(), end='\n\n')
print(DATA['sex'].value_counts(), end='\n\n')
print(DATA['native-country'].value_counts(), end='\n\n')"""

# Tableau croisé
print()
print(pd.crosstab(index=DATA['education'], columns=DATA['education-num']))

#
import seaborn as sns

# We plot a subset of the data to keep the plot readable and make the plotting
# faster
n_samples_to_plot = 5000
columns = ['age', 'education-num', 'hours-per-week']
_ = sns.pairplot(
    data=DATA[:n_samples_to_plot],
    vars=columns,
    hue=TARGET,
    plot_kws={'alpha': 0.2},
    height=3,
    diag_kind='hist',
    diag_kws={'bins': 30},
)
plt.show()