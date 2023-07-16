line = input('Введите строку: ')

tuple_line = tuple(set(line))

print('Уникальные символы:', tuple_line)
print('Количество уникальных символов:', len(tuple_line))
