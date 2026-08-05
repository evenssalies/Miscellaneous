#include <stdio.h>
int main() {
    int     a;
    double  b, c, average;
    printf("Enter an integer and two floats:");
    scanf("%d %f %f", &a, &b, &c);
    average = (a+b+c)/3;
    printf("The average is %f.\n", average);
    return 0;
}