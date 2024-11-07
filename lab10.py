students = ["Діма", "Женя", "Льошка", "Миколка"]
cities = ["Дніпро", "Київ", "Одеса", "Харків"]
grades = [4.5, 4.8, 4.2, 4.7]
student_data = [(students[i], cities[i], grades[i]) for i in range(len(students))]
for data in student_data:
    print(f"Ім'я: {data[0]}, Місто: {data[1]}, Середній бал: {data[2]}")
print("\n" + "="*50 + "\n")
x = int(input("Введіть число x: "))
y = int(input("Введіть число y: "))
def get_divisors(n):
    return {i for i in range(1, n + 1) if n % i == 0}
divisors_x = get_divisors(x)
divisors_y = get_divisors(y)
common_divisors = divisors_x & divisors_y
max_common_divisor = max(common_divisors)
print("Спільні дільники чисел:", common_divisors)
print("Найбільший спільний дільник:", max_common_divisor)
print("\n" + "="*50 + "\n")
print("Завдання 3: Сортування континентів за площею\n")
file_name = "continents.txt"
continents_area = {}
try:
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            try:
                name, area = line.strip().split(", ")
                continents_area[name] = int(area)
            except ValueError:
                print(f"Помилка в рядку: {line}. Перевірте формат.")
except FileNotFoundError:
    print(f"Файл {file_name} не знайдено. Перевірте його наявність і шлях до нього.")
if continents_area:
    sorted_continents = sorted(continents_area.items(), key=lambda x: x[1], reverse=True)
    for continent, area in sorted_continents:
        print(f"{continent}: {area} кв. км")