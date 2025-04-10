#include <stdio.h>

int power(int a, int b) {
    int c = 1;
    for (int i = 0; i < b; i++) {
        c = c * a;
    }
    return c;
}

int main() {
    printf("result = %d\n", power(2, 3));
    return 0;
}
