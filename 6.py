print('*' * 120)
fun = []
product = {'Наименование товара': '', 'стоимость': '', 'количество': ''}
analytics_1 = {'наименование товара': [], 'стоимость': [], 'количество': []}
num = 0
while True:
    if input('Для выхода из программы нажмите "Q", для продолжения "Enter": ').upper() == 'Q':
        break
    num += 1
    for p in product.keys():
        _ = input(f'Введите значение " {p} ": ')
        product[p] = int(_) if (p == 'стоимость' or p == 'количество') else _
    analytics_1[p].append(product[p])
    fun.append((num, product))
    print(f'Аналитика по товарам:')
    for key, val in analytics_1.items():
        print(f'{key[:25]:>30} : {val}')
    print('*' * 120)






