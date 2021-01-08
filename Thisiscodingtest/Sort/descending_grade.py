#성적이 낮은 순서로 학생 출력하기(chapter6-03)

n = int(input())
array = []
for i in range(n):
    x = input().split()
    array.append((x[0],x[1]))

def setting(data):
    return data[1]

array.sort(key=setting)
#array = sorted(array, key=lambda student:student[1])

for i in array:
    print(i[0], end=" ")
