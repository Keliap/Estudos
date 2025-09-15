#include<stdio.h>

int main(){

    int a, b;

    printf("Digite a primeiro numero: ");
    scanf("%d",&a);
    printf("Digite o segundo numero: ");
    scanf("%d",&b);

    while (a != b)
    {
        if ( a < b){
            printf("Crescente\n");
        } else{
            printf("Descrescente\n");
        }

        printf("Digite outros dois numeros:\n");
        scanf("%d",&a);
        scanf("%d",&b);
    }
return 0;
}