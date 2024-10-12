a = int(input())
b = int(input())
if b == 0:
    print('На 0 делить нельзя')
elif a%b == 0:
    print('Делится',a,' / ',b,' = ',a//b)
else:
    print('Не делится',a,' / ',b,' = ',a//b, ' остаток = ', a%b)
