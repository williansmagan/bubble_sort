lista = []
lista = [2, 5, 0, 30, 12, 6, 99, 123, 10, 33] #Lista de itens. Pode ser configurada para puxar dados de uma inserção do usuário
lista_original = lista.copy() # Cria uma cópia da lista original


#Função de ordenação
def BubbleSort(lista):
    tamanho = len(lista) #Conta quantos itens existem na lista
    for i in range(tamanho): #inicia uma sequência de verificações, repetindo o número de itens contados na lista
        for j in range(0, tamanho - i - 1): #Inicia a verificação dos valores da lista, percorrendo todos os elementos. O (i - 1) faz com que os elementos que já estão em ordem sejam pulados da reetição da verificação
            if lista[j] > lista[j+1]: #Compaação dos dois elementos adjacentes da lista.
                lista[j], lista[j+1] = lista[j+1], lista[j] #Se o maior elemento estivar a esquerda da comparação, os elementos são alterados de posição.
    return lista #Retorna a lista ordenada para exibição ao usuário



lista_ordenada = BubbleSort(lista) #Executa a função de ordenação BubbleSort
print('Lista original: ', lista_original) #Exibe a lista original para ordenação
print('Lista ordenada em ordem crescente: ', lista_ordenada) #Exibe a lista ordenada em ordem crescente