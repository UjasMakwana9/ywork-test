# Input
child_array = [1,2,2]

sum = 0

if child_array[0] > child_array[1]:
    sum += 2
else:
    sum+=1

if child_array[1] > child_array[2] or child_array[1]>child_array[0]:
    sum+=2
else:
    sum+=1

if child_array[1] < child_array[2] :
    sum+=2
else:
    sum+=1



print("Sum of candies:", sum)
