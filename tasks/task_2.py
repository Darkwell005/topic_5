days: list = ["Понедельник", "Вторник", "Среда",
              "Четверг", "Пятница", "Суббота", "Воскресенье"
              ]

num_week = int(input('Введите номер дня недели от 1 до 7: '))
day_weeks = days[num_week - 1]
print(day_weeks)
