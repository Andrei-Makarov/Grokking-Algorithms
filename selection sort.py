'''Сортировка выбором из книги "Грокаем алгоритмы второе издание"'''
#Функция для поиска наименьшего элемента массива
def findSmallest (arr):
    smallest = arr[0]    #Для хранения наименьшего значения
    smallest_index = 0   #Для хранения индекса наименьшего значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

#Функция сортировки выбором
def selectionSort(arr):  #Сортируем массив
    newArr = []
    copiedArr = list(arr) #Копируем сортируемый массив перед изменением
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr) #Находим наименьший элемент
        newArr.append(copiedArr.pop(smallest)) #Добавляем его в новый массив
    return newArr

print(selectionSort([99,1,6,8,45,12,11]))
