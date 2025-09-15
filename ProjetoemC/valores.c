#include<stdio.h>

int main(){

    int a, b, c, soma;

    printf("Digite o primeiro numero: ");
    scanf("%d",&a);

    printf("Digite o segundo numero: ");
    scanf("%d",&b);

    if(a == b){
        soma = a + b;
        printf("O resultado e: %d", soma);
    }else{
        c = a * b;
        printf("O resultado da multiplicação e: %d", c);
    }
}