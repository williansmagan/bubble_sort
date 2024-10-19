# Bubble Sort

## Algoritmo de Ordenação Bubble Sort

O Bubble Sort é um algoritmo de ordenação simples que funciona comparando elementos adjacentes em uma lista e trocando-os de posição se estiverem na ordem errada. O processo é repetido iterativamente até que a lista esteja completamente ordenada.

**Como funciona:**

1. **Comparação:** O algoritmo percorre a lista, comparando cada elemento com seu vizinho seguinte.
2. **Troca:** Se os elementos estiverem na ordem errada (o elemento esquerdo maior que o direito), eles são trocados de posição.
3. **Repetição:** O processo de comparação e troca é repetido para a lista inteira até que nenhuma troca seja necessária, indicando que a lista está ordenada.

**Exemplo:**

Considere a lista não ordenada: `[5, 1, 4, 2, 8]`.

**Passos do Bubble Sort:**

1. **Iteração 1:**
    - Comparar `5` e `1`. Trocar, resultando em `[1, 5, 4, 2, 8]`.
    - Comparar `5` e `4`. Trocar, resultando em `[1, 4, 5, 2, 8]`.
    - Comparar `5` e `2`. Trocar, resultando em `[1, 4, 2, 5, 8]`.
    - Comparar `5` e `8`. Não trocar, resultando em `[1, 4, 2, 5, 8]`.
2. **Iteração 2:**
    - Comparar `1` e `4`. Não trocar.
    - Comparar `4` e `2`. Trocar, resultando em `[1, 2, 4, 5, 8]`.
    - Comparar `4` e `5`. Não trocar.
    - Comparar `5` e `8`. Não trocar.
3. **Iteração 3:**
    - Comparar `1` e `2`. Não trocar.
    - Comparar `2` e `4`. Não trocar.
    - Comparar `4` e `5`. Não trocar.
    - Comparar `5` e `8`. Não trocar.

A lista agora está ordenada: `[1, 2, 4, 5, 8]`.

**Complexidade:**

- **Tempo:**
    - Melhor Caso: O(n), onde n é o número de elementos na lista.
    - Médio Caso: O(n^2).
    - Pior Caso: O(n^2).
- **Espaço:** O(1).

**Vantagens:**

- Fácil de entender e implementar.

**Desvantagens:**

- Lento para listas grandes.
- Ineficiente para listas quase ordenadas.

**Aplicações:**

O Bubble Sort é frequentemente usado para fins educacionais.


**Conclusão:**

O Bubble Sort é um algoritmo de ordenação simples, mas ineficiente para listas grandes. Embora seja útil para fins educacionais, ele raramente é usado em aplicações práticas devido à sua baixa eficiência.