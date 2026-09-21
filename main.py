with open('data.csv', 'r', encoding='utf-8') as f:
    line = f.readlines()
data = line[1:]

age = []
surname = []
favorite_color = []
for line in data:
    value = line.strip().split(',')
    age.append(int(value[1]))
    surname.append(value[2])
    favorite_color.append(value[3])
#Средний возраст, вручную
sumElements = 0 
for i in range(len(age)):
    sumElements += age[i]
average_value = sumElements /len(age)
#самый часто встречаемый цвет с подсчетом
counts = {}
for color in favorite_color:
    counts[color] = counts.get(color,0) + 1
best_color = max(counts,key=counts.get)
#поиск минимума с помощью min
youngest = min(age)
with open('result.csv', 'w',encoding='utf-8') as f:
    f.write("Резутальт и статистика чтения из файла\n\n")
    f.write(f"Все возроста:{age}\n")
    f.write(f"Все фамилии:{surname}\n")
    f.write(f"Любимые цвета:{favorite_color}\n")
    f.write(f"Средний возраст:{average_value}\n")
    f.write(f"Самый популярный цвет:{best_color} встертился {counts[best_color]} раз\n")
    f.write(f"Самый молодой участник:{youngest}\n")
