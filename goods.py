# Вывести на экран таблицу из 4 строк:
# три товара и сумма без использования цикла

goods = {
    'гречка': 78,
    'лук': 15,
    'морковка': 40
}

left_col = 15

# Двойная подстановка!

print('+' + '-' * left_col + '+' + '-' * left_col + '+')

print('|%(name)15s' % {'name': 'лук'} + '|', end='')
print('%(price)15i' % {
    'price': goods['лук']
    } + '|')

print('+' + '-' * left_col + '+' + '-' * left_col + '+')
print('|' + 'морковка' + '|')
print('+' + '-' * left_col + '+' + '-' * left_col + '+')
print('|' + 'гречка' + '|')
print('+' + '-' * left_col + '+' + '-' * left_col + '+')
print('| Итог     |' + str(
     goods['лук'] +  goods['гречка'] +  goods['морковка']
    ) + '|')
print('+' + '-' * left_col + '+' + '-' * left_col + '+')
