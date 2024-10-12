n = int(input())
finabuchi = [1,1]
for i in range(n-2):
    a = finabuchi[i] + finabuchi[i+1]
    finabuchi.append(a)
print(finabuchi)