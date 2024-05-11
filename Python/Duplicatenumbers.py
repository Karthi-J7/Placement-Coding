# Getting input and split it into an array 

l = [int(i) for i in input().split()]
n = len(l)      #Finding length of an Array
l.sort()        #Sorting the Array

# The Repeated Elements are arranged in next to next manner
# here, Checking the current and next elements are equal but it doesn't equal to temp
# if it is equals, Assign it to temp variable and print it 

t = 0
for i in range(n - 1):
    if l[i] == l[i + 1] and t != l[i]:
        t = l[i]
        print(t)
