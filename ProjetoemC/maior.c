#include<stdio.h>

int main(){

    int a, b, c, soma;

    printf("Digite o primeiro numero: ");
    scanf("%d",&a);
    printf("Digite o segundo numero: ");
    scanf("%d",&b);
    printf("Digite o terceiro numero: ");
    scanf("%d",&c);

    soma = a + b;
     if (soma < c){
        printf("O resultado e: %d", soma);
    } else{
        printf ("O resultado e: %d", c);
    }
}