num = int(input("input:"))
result = []

for ii in range(1, num+1):
    if ii % 5 == 0 and ii % 3 == 0:
        result.append(ii)
    elif ii % 5 != 0 and ii % 3 != 0:
        result.append(ii)
print(len(result))