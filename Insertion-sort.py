
numbers = [5,2,4,6,1,3,9,12,3,10,11,14,3,1]


for i in range(0,len(numbers)):
    for j in range(0,i):
        if(numbers[i] < numbers[j]):
            numbers.insert(j,numbers[i])
            numbers.pop(i+1)
            break
print(numbers)    