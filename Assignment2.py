# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    num_1 = max(numbers)

    while num_1 in numbers:
        numbers.remove(num_1)

    if numbers == []:
        return(num_1, None)
    else:
        num_2 = max(numbers)

    return (num_1, num_2)

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    i = min(numbers)

    while i <= max(numbers):
        if numbers.count(i) > 1:
            numbers.remove(i)
        else:
            i += 1
            continue

    numbers.sort()    

    return numbers
# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    list = [min(arr)]
    i = arr[0]

    while i < max(arr):
        if i in arr:
            list.append(i + min(list) + max(list))
            i += 1
        else:
            i += 1
            continue

    return list

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    return [[]]
# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    i = 0
    list = []
    n = 1

    while i < len(lst):
        if i == 0:
            list.append(lst[i])
            i += 1
        elif i == step * n:
            list.append(lst[i])
            i += 1
            n += 1
        else:
            i += 1

    return list

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    product = sum([a * b for a, b in zip(list1, list2)])
    return product

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    return [[0, 0], [0, 0]]
