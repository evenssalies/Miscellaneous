#include <stdio.h>
#include <math.h>

int main() {
    printf("x\t\tSin(x)\n");
    printf("-------------------\n");

    for (double x = 0.0; x <= 1.0; x += 0.001) {
        double sinValue = sin(x);
        printf("%.2f\t\t%.4f\n", x, sinValue);
    }

    return 0;
}