import sys
sys.stdout.reconfigure(encoding='utf-8')

# ─────────────────────────────
# Mémoire partagée (blackboard)
# ─────────────────────────────
etat = {}   # Tous les noeuds du behavior tree peuvent lire et
            # écrire dans ce dictionnaire

# ─────────────────────────────
# ACTION : entrer deux nombres
# ─────────────────────────────
def entrer_nombres():
    etat["x"] = int(input("Entrez x ∈ ℕ* : "))
    etat["y"] = int(input("Entrez y ∈ ℕ* : "))
    return True

# ─────────────────────────────
# CONDITION : nombres valides
# ─────────────────────────────
def nombres_valides():
    return etat["x"] > 0 and etat["y"] > 0

# ─────────────────────────────
# ACTION : calculer max et min
# ─────────────────────────────
def calculer_max_min():
    x = etat["x"]
    y = etat["y"]
    etat["m"] = max(x, y)
    etat["n"] = min(x, y)
    print("Le maximum de", x, "et", y, "est", etat["m"])
    print("Le minimum de", x, "et", y, "est", etat["n"])
    return True

# ─────────────────────────────
# CONDITION : m est multiple de n
# ─────────────────────────────
def est_multiple():
    return etat["m"] % etat["n"] == 0

# ─────────────────────────────
# ACTION : afficher gagné
# ─────────────────────────────
def afficher_gagne():
    print(etat["m"], "est un multiple de", etat["n"], "→ gagné !")
    return True

# ─────────────────────────────
# ACTION : afficher perdu
# ─────────────────────────────
def afficher_perdu():
    print(etat["m"], "n'est pas un multiple de", etat["n"], "→ perdu !")
    return True

# ─────────────────────────────
# SÉQUENCE et SÉLECTEUR
# ─────────────────────────────

def sequence(*noeuds):      # La fonction peut prendre > 1 noeuds
    for noeud in noeuds:
        if not noeud():
            return False
    return True

def selecteur(*noeuds):  
    for noeud in noeuds:
        if noeud():
            return True
    return False

# ─────────────────────────────
# ARBRE PRINCIPAL
# ─────────────────────────────
def arbre_principal():
    return sequence(
        entrer_nombres,      # ACTION
        nombres_valides,     # CONDITION
        calculer_max_min,    # ACTION
        lambda: selecteur(   # SÉLECTEUR
            lambda: sequence(
                est_multiple,     # CONDITION
                afficher_gagne    # ACTION
            ),
            afficher_perdu        # ACTION (fallback)
        )
    )

# Exécution
arbre_principal()