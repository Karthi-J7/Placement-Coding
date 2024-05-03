arr = [[1, 2, 3], 
       [4, 5, 6]]

transpose_array = [[arr[j][i] for j in range(len(arr))]for i in range(len(arr[0]))]

print(transpose_array)