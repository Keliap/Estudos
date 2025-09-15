#include<iostream>

using namespace std;

int main(){

    int x, y, aux, soma;

    cout<< "Digite dois numeros: "<< endl;
    cin >> x >>y;

    if (x>y)
    {
        aux = x;
        x = y;
        y = aux;
    }
    soma = 0;
    for (int i = x; i < y; i++)
    {
        if (i % 2 !=0)
        {
            soma = soma + i;
        }
        
    }
    cout << "Soma dos Impares = " << soma << endl;
}