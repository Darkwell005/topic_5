line: str = input('Введите строку: ')

unique_chars: tuple = tuple(set(line))

print('Уникальные символы:', unique_chars)
print('Количество уникальных символов:', len(unique_chars))
