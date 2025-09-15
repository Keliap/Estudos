#include<stdlib.h>

int main(){

    int n;

    printf("Digite um numero: ");
    scanf("%d",&n);

    if (n % 2 != 0)
    {
        printf("Esse numero e impar %d\n", n);
    }else{
        printf("Numero e par %d\n", n);
    }if (n < 0)
    {
        printf("Este numero e negativo: %d\n", n);
    }else{
        printf(" Esse numero e positivo %d\n", n);
    }
    
    
    
    
    
}