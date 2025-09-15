#include<stdio.h>

int main(){

    char nome1 [50], nome2[50];
    int idade1, idade2;
    double media;

    printf("Dados da primeira pessoa: ");
    printf("Nome: ");
    gets(nome1);
    printf("Idade: ");
    scanf("%d",&idade1);

    printf("Dados da segunda pessoa: ");
    printf("Nome: ");
    fseek(stdin, 0, SEEK_END);
    gets(nome2);
    printf("Idade: ");
    scanf("%d", &idade2);

    media = (idade1 + idade2) /2.0;

    printf("A media da idade de %s e %s eh de %.1lf anos", nome1, nome2, media);

        
}