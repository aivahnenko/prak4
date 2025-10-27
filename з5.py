minutes = int(input("Введите количество минут: "))
hours = minutes // 60
remaining_minutes = minutes % 60
print(f"{minutes} мин - это {hours} час {remaining_minutes} минут")