numder=int(input('введите четырехзначное число '))
thousand=numder//1000
hundred=(numder%1000) // 100
ten=(numder%100) // 10
one=(numder%10)
print('цифра в позиции тысяч: ',thousand)
print('цифра в позиции сотен: ',hundred)
print('цифра в позиции десятков: ',ten)
print('цифра в позиции едениц: ',one)