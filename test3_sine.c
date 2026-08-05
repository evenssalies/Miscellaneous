/* Demande à l'utilisateur d'entrer un nombre entre 0 et 1.
    J'utilise x comme identifier et non sinValue, clair,
    certes, mais long !
 */

#include <stdio.h>

#define _USE_MATH_DEFINES   // Use the value of Pi already defined in math.h
#include <math.h>

int main(void)
{ 
    float sinValue;
        printf("Enter a number x between 0 and 1: ");
        scanf("%f", &sinValue);
        printf("The sinus of %.3f is %.3f.\n\n", 
            sinValue, sin(sinValue)); // Rounded tp 3rd decimal place

    double h = 0.1; /*step size*/
    double i;
    for(i = 0.0; i < M_PI; i += h)
    printf("%5.1f: %.15e\n", i, sin(i)*sin(i)+cos(i)*cos(i));
    return 0;
}