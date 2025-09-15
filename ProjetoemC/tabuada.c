#include<stdio.h>

int main(){

    int i, n, produto; 

    printf("Deseja a tabuada para qual valor: ");
    scanf("%d", &n);

    for (i = 0; i <= 10 ; i++) {
        produto = n * i;
        printf("%d x %d = %d\n", n, i, produto);

    }
        
    


}