#위에서 아래로 (chapter6-02)

n = int(input())
array =[]
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

for i in range(len(array)):
    print(array[i], end= " ")

#for i in array:
#    print(i, end=" ")
