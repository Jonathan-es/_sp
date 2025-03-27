#include<stdio.h>
int sum(int x){
	int a, b;
    a = 0;
    b = 0;
	do{
		b = a + b;
		a++;
	}while(a <= x);
	return b;
}

int main() {
    printf("sum(10)=%d\n", sum(10));
    return 0;
  }