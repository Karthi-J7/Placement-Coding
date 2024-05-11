
# Method 1
# Getting input and split it into an array 

l = [int(i) for i in input().split()]
n = len(l)      #Finding length of an Array
l.sort()        #Sorting the Array

# The Repeated Elements are arranged in next to next manner
# We printed the first element mannually.
# While iterating, checking the current and previous element if it is different print the number

print(l[0])
for i in range(1, len(l)):
    if not (l[i] == l[i - 1]):
        print(l[i])

# Method 2
# Converting the list to set inorder to remove the duplicate elements
print(set(l))