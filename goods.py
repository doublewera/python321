# Вывести на экран таблицу из 4 строк:
# три товара и сумма без использования цикла

goods = {
    'гречка': 78,
    'лук': 15,
    'морковка': 40
}

left_col = 15

# Двойная подстановка!

summa = 0
print('+' + '-' * left_col + '+' + '-' * left_col + '+')
for tovar in goods:  # Питон перебирает словарь по ключу
    print('|%(name)15s' % {'name': tovar} + '|', end='')
    print('%(price)15i' % {'price': goods[tovar]} + '|')
    print('+' + '-' * left_col + '+' + '-' * left_col + '+')
    summa += goods[tovar]




print('| Итог     |' + str(
     summa
    ) + '|')
print('+' + '-' * left_col + '+' + '-' * left_col + '+')
