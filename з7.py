import math
mesto = int(input('введите номер места'))
if mesto<37:
    kupe=math.ceil(mesto / 4)
    print('номер вашего купе:', kupe)
else:
    print('ошибка! такого места не существует')
