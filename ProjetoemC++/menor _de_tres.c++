#include<iostream>

using namespace std;

int main(){

    int a, b , c, menor;

    cout<< "Primeiro numero: ";
    cin>> a;
    cout<< "Segundo numero: ";
    cin>> b;
    cout<< "Terceiro numero: ";
    cin>> c;

    if (a < b && a < c)
    {
        menor = a;
    } 
    else if (b < c)
    {
        menor = b;
    }else{
        menor = c;
    }
    cout<< "Menor = " << menor << endl;
    }
    
    
