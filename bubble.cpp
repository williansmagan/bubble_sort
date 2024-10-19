#include <iostream>
using namespace std;

void BubbleSort(int lista[], int x) {
    for(int i = 0; i < x; i++) {
        for(int j = 0; j < (x - 1 - i); j++) {
            if(lista[j] > lista[j + 1]) {
                int aux = lista[j];
                lista[j] = lista[j + 1];
                lista[j + 1] = aux;
            }
        }
    }
}

void imprimir(int lista[], int x) {
    for(int i = 0; i < x; i++) {
        cout << lista[i] << " ";
    }

    cout << endl;
}


int main() {
    int lista[] = {2, 5, 0, 30, 12, 6, 99, 123, 10, 33};
    int lista1[] = {2, 5, 0, 30, 12, 6, 99, 123, 10, 33};
    
    int x = sizeof(lista) / sizeof(lista[0]);

    BubbleSort(lista, x);

    cout << "Lista original: ";
    imprimir(lista1, x);

    cout << "Lista ordenada: ";
    imprimir(lista, x);

    return 0;
}