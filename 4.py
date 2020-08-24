user_pop = input('Напишите предложение из 3 слов: ') .split()

for p, pop in enumerate(user_pop, 1):
    print(p, pop)

    #print(p, pop) if len(pop) <= 10 else print(p, (pop[:10]))
