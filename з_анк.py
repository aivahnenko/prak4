name = input("Ваше имя: ")
age_str = input("Ваш возраст: ")
subjects_str = input("Любимые предметы (через запятую): ")
# --- ВАШ КОД ЗДЕСЬ ---
age = int(age_str)  # Преобразуем возраст в целое число
subjects = subjects_str.split(",")  # Разбиваем строку предметов на список

student = {
    "name": name,
    "age": age,
    "subjects": subjects
}

print("=" * 30)
print("АНКЕТА СТУДЕНТА")
print("=" * 30)

print(f"Имя: {student['name']}")
print(f"Возраст: {student['age']}")
print(f"Любимые предметы: {', '.join(student['subjects'])}")

print("=" * 30)