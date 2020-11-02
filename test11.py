#冒泡排序
lista=[0,1,2,888,5,1,2,54,4,5,7,8,9,6,3,2,1,4,11,55,88,77,987,2,23,54,87,98]
listput=[]
print(len(lista))
for i in range(len(lista)-12):
    for j in range(len(lista)-1):
        if lista[j]>lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
        else:
            pass
print(lista)


def bubbleSort(array):
    sort = True
    while sort:
        sort = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                temp = array[i + 1]
                array[i + 1] = array[i]
                array[i] = temp
                sort = True


bubbleSort(lista)
print(lista)
