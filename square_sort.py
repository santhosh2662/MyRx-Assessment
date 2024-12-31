# square_sort.py
def square_and_sort(arr):
    return sorted([x ** 2 for x in arr])

input_array = [-12, -8, -7, -5, 2, 4, 5, 11, 15]
print(square_and_sort(input_array))
