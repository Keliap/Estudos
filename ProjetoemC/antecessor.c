#include<stdio.h>

int main(){

    int n, c, b;

    printf("Digite um numero: ");
    scanf("%d", &n);

    if (n != 0)
    {
        c = n - 1;
        b = n + 1;

        printf("Seu antecessor e: %d\n", c);
        printf("Seu sucessor e: %d\n", b);
    }
    
}