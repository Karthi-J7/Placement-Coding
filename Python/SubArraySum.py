arr = [5, 6, -3, 7, -13, 8, -2, 5, -6, 7, -11, 3, 10, -10,-6, -10, 7, 2]
n = len(arr)
sub_array = []
sub_array_sum = []

for i in range(n):
    for j in range(i + 1, n):
        sub_array.append(arr[i : j])
        sub_array_sum.append(sum(arr[i : j]))

max_index = sub_array_sum.index(max(sub_array_sum))
print(sub_array[max_index])
