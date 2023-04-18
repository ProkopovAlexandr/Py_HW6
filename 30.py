arr = []
arr.append(int(input("Введите первое число: ")))
step = int(input("Введите шаг прогрессии: "))
d = int(input("Введите кол-во элементов: "))

while len(arr) < d:
    arr.append(arr[len(arr) - 1] + step)

print(*arr)