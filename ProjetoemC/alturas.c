#include<stdio.h>

int main(){

    int n, contM;
    double soma, percentualM;

    printf("Quantas pessoas serão digitadas: ");
    scanf("%d",&n);

    char nome [n] [50];
    int idades [n];
    double alturas [n];

    for (int i=0; i < n; i++){
        printf("Dados da %da pessoa:\n", i + 1);
        printf("Nome: ");
        fseek(stdin, 0, SEEK_END);
        gets(nome[i]);
        printf("Idade: ");
        scanf("%d", &idades[i]);
        printf("Altura: ");
        scanf("%lf",&alturas[i]);
    }

        soma = 0;
        for (int i=0; i<n; i++){
            soma = soma + alturas[i];
        }
        contM = 0;

        for(int i = 0; i < n ; i++){
            if (idades[i] < 16)
            {
                contM ++;
            }
        }
        
        percentualM = contM * 100.0 / n;
        printf("Pessoas com menos de 16 anos: %.1lf %%\n", percentualM);

        for (int i = 0; i < n; i++){
            if (idades[i] < 16)
            {
                printf("%s\n", nome[i]);
            }
            
        }




    }


