#include    <stdio.h>
int         main(void) {
    int     miles, yards;
    double  kilometers;
    printf("Please enter miles and yards:");
    scanf("%d %d", &miles, &yards);
    kilometers = 1.609*(miles + yards / 1760.0);
    printf("\n %d miles and %d yards is %lf kilometers.\n", miles,
    yards, kilometers);
    return  0;
}