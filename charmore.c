#include <stdio.h>
int main(void) {
    char    c='a';
    printf("c is the character %c\n", c);
    printf("c in ASCII is %d.\n", c);
    printf("Three consecutive chars are: %c%c%c.\n", c, c+1, c+2);
    printf("Three bell rings char ... %c %c %c", 7, 7, 7);
    return 0;
}