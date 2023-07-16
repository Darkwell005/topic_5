numbers: list = [12, 45, 0.34711, 67, 89, 34, 55.632781, 78.9395]

avg_num: float = sum(numbers) / len(numbers)
round_num: float = round(avg_num, 1)

print('Среднее значение:', round_num)
