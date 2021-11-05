def find_smallest(arr):
    '''упорядочить массив по возрастанию'''
    smallest = arr[0] # для хранения наименьшего значения
    smallest_index = 0  #index наименьшего значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

#arr = [9,7,0,12,4,26,8,1,3]
#print(find_smallest(arr))

def selection_sort(arr):
    '''сортирует массив'''
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr) #ищет миним.элемент в массиве
        newArr.append(arr.pop(smallest)) #и добавляет его в нов.массив
    return newArr

print(selection_sort([5,12, 3, 6, 2, 10]))
print()
print(selection_sort([9,7,12,4,26,8,1,3]))
