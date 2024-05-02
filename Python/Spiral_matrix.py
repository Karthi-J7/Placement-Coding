
arr = [[1, 2, 3, 4], 
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

row_min = 0
row_max = len(arr) - 1

col_min = 0
col_max = len(arr[0]) - 1
steps = 0

while (steps < len(arr) * len(arr[0])):
    for j in range(col_min, col_max + 1):
        print(arr[row_min][j])
        steps += 1

    row_min += 1

    for j in range(row_min, row_max + 1):
        print(arr[j][col_max])
        steps += 1

    col_max -= 1

    for j in range(col_max, col_min - 1, -1):
        print(arr[row_max][j])
        steps += 1
    
    row_max -= 1
    
    for j in range(row_max, row_min - 1, -1):
        print(arr[j][col_min])
        steps += 1

    col_min += 1
    