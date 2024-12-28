import os

"""# classe: Phrase
class Phrase:
    # attribut: ma-phrase, qui référence une chaîne de caractères
    ma_phrase = "Je fais un MOOC sur python"

print(f"{Phrase.ma_phrase}\n")

# Phrase est aussi un objet, à partir duquel on peut créer des instances
# instance: p, qui est une instance de la classe Phrase
p = Phrase()

# p est aussi un objet
print(f"{p}\n")

# Accéder à l'espace de nommage de p, idem avec la fonction vars()
Phrase.__dict__
print(f"{vars(Phrase)}\n")

# En revanche, p n'a pas d'attribut ma_phrase !
#  C'est une instance avec un espace de nommage vide (sans attributs) !
print(f"{vars(p)}\n")

# Or, on a une relation d'héritage entre l'instance p et la classe Phrase,
#  p hérite néansmoins des attributs de la classe Phrase
print(f"{p.ma_phrase}\n")

# attribut: mots, ajouté à Phrase, qui référence une liste de mots en découpant ma_phrase
Phrase.mots = Phrase.ma_phrase.split()
print(f"{Phrase.mots}\n")
print(f"{p.mots}\n")
print(f"Espace de nommage de :\n Phrase : {vars(Phrase)},\n p : {vars(p)}\n")

# Implémentation d'une méthode (on parle aussi de comportement) dans la classe Phrase.
#  Une méthode est une fonction que l'on définit dans la classe. Les méthodes sont
#  capables de travailler sur les attributs de l'instance p. Dans l'exemple suivant,
#  la méthode mymethod() a permis de créer un attribut ma_phrase dans l'instance, qui
#  référence l'argument que j'ai passé à la méthode  
s = "Je fais un MOOC sur python"
class Phrase:
    def mymethod(self, ma_phrase):
        self.ma_phrase = ma_phrase

p = Phrase()
p.mymethod(s)
print(f"{vars(p)}\n")

# Sont équivalents
p.mymethod(s)
Phrase.mymethod(p, s)

# Comparaison avec le constructeur __init__()
class Phrase:
    def __init__(self, ma_phrase):
        self.ma_phrase = ma_phrase

p = Phrase(s)
print(f"{vars(p)}\n")

# Sont équivalents
p = Phrase(s)
Phrase.__init__(p, s)"""

# Application 1
class Famille:
    def __init__(self, fore_name, sur_name):
        self.forename = fore_name
        self.surname = sur_name

    def display_info(self):
        print(f"Forename: {self.forename:<10} Surname: {self.surname}")

s = "Salies"
family_members = [("Karine", "Chakir"), ("Evens", s), ("Zoë", s), ("Niña", s)]
os.system('cls')
for forename, surname in family_members:
    member = Famille(forename, surname)
    member.display_info()