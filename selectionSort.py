array = [12,66,52,8,2,2,3,4,90]
size = len(array)
def selection_sort(array):
    for i in range(size):
        min_index = i
        for j in range(i+1, size):
            if array[j] < array[min_index]:
                min_index = j
            array[i], array[min_index] = array[min_index], array[i]
    return array
print(selection_sort(array))
print(f"The Smallest element in an array is {array[0]}.")
print(f"The Largest element in an array is {array[-1]}.")
