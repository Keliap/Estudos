#include<stdio.h>

int main(){

    int x, y, soma, cont, i;

    printf("Digite dois numero: ");
    scanf("%d", &x);
    scanf("%d", &y);

    if (x > y)
    {
        cont = x;
        x = y;  
        y = cont;
    }
    soma = 0;

    for (i = x+1; i< y; i++)
    {
        if( i % 2 !=0 ){
            soma = soma + i;
        }
    }
     printf("Soma dos impares e = %d\n",soma);
    
    

        

}