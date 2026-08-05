/* Addition des carrés de 1 à 100 millions et
    calcul du temps machine en C, Stata, Mata
    https://en.cppreference.com/w/c/chrono/clock_t
    https://en.wikipedia.org/wiki/C_data_types
    Voir le programme Stata matastataspeed.do  
    
    Je n'arrive pas à calculer correctement la somme
    au-delà de n = 4-5 millions. Charger la librairie
    d'arithmétique de précision https://gmplib.org/ */

#include    <stdio.h>
#include    <time.h>

unsigned long long dotproduct(long);
int main(void)
{    
    clock_t start = clock();
     unsigned long long product = dotproduct(1000000);
     printf("%llu\n", product);
    clock_t end = clock();
    double cpu_time = ((double)(end - start))/CLOCKS_PER_SEC;
    printf("%f\n", cpu_time);
    return 0;
}

unsigned long long dotproduct(long n)
{
    unsigned long long p = 0;
    for (unsigned long long i = 1; i <= n; ++i)
    {
        p += i * i;
    }
    return p;
}