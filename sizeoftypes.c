#include <stdio.h>
int main(void) {
    char    ch = 'e';
    printf("On my system\n");
    printf("int is %lu bytes.\n", sizeof(int));
    printf("long int is %lu bytes.\n", sizeof(long int));
    printf("char is %lu bytes.\n", sizeof(ch));
    printf("float is %lu bytes.\n", sizeof(float));
    printf("double is %lu bytes.\n", sizeof(double));
    printf("long double is %lu bytes.\n", sizeof(long double));
    return 0;
}