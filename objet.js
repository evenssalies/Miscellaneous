// Déclarer l'objet matrice
let matrice = {
    ligne_nb: 3,
    colonne_nb: 4,
    nulle: true
};

// Mettre à jour l'objet : ajouter une propriété
if (matrice.nulle == false) {
    matrice.valeur = 0;
} else {
    matrice.valeur = 1;
}

// Afficher les valeurs et remplir deux tableaux :
// - un tableau des valeurs (tableau_valeur)
// - un tableau ligne_nb x colonne_nb (tableau_matrice)
const valeur = matrice.valeur;
let tableau_valeur = [];
let tableau_matrice = []; // Faut-il dimensionner une matrice vide ici ?
for (let i = 0; i < matrice.ligne_nb; i++) {
    for (let j = 0; j < matrice.colonne_nb; j++) {
        let cellule = "(" + i + "," + j + ") :";
        let valeur = cellule + matrice.valeur;
        
        // Afficher les valeurs
        console.log(valeur);

        // Remplir tableau_valeur avec la méthode push()
        tableau_valeur.push(matrice.valeur);
        // Remplir la matrice
    }
}

console.log(matrice);
console.log(tableau_valeur);
console.log(tableau_matrice);