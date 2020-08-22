my_rating = []
pop_num = int(input('Введите свой элемент рейтинга: '))
p = 0 # не понимаю с логической точки зрения для чего это условие, если поставить : 1,2,3... ничего не меняется О_о
# Но без этого ничего не работает О_о
for r in my_rating:

    if pop_num <= r:
        r += 1
my_rating.insert(p, pop_num)
print(my_rating)







