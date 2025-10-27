students=int(input('введите количество школьников '))
mandarins=int(input('введите количество мандаринов '))
mandarins_student= mandarins//students
mandarins_basket=mandarins%students
print('Каждому школьнику достанется ', mandarins_student)
print('Вкорзине останется ', mandarins_basket)