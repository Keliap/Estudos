#include<stdio.h>
#include<math.h>

int main(){
    int a, b ,c;
    int menor;

    printf("Primeiro valor: ");
    scanf("%d",&a);
    printf("Segundo valor: ");
    scanf("%d",&b);
    printf("Terceiro valor: ");
    scanf("%d",&c);

    if( a< b && a>c){
        menor = a;
    }else if(b<c){
        menor = b;
    } else{
        menor = c;
    }
    printf("Menor = %d\n", menor);
}