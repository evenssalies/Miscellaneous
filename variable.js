// https://openclassrooms.com/fr/courses/7696886-apprenez-a-programmer-avec-javascript/8204834-structurez-des-donnees-grace-aux-objets

// La valeur peut changer au cours du code
let y = 1;
let x1 = "oui : ";

// La valeur reste constante tout au long du code
const x2 = ", non : ";
const x3 = 1;
const x4 = 0;
const x5 = true;

// Modifier y n'a pas besoin de refaire un let
y += 1;
x1 += x3;          // Concatenation de chaîne de caractères
x1 += x2; 
x1 += x4;

console.log(y);
console.log(x1);
console.log(x5);