# cost_bit = int(input('cost bitcoin = '))
# per = int(input('percent = '))
# total_cost = cost_bit * (per / 100) + cost_bit
# print(total_cost)
# print(cost_bit * (per / 100))


# geo = int(input('Geo '))
# alg = int(input('Alg '))
# phy = int(input('Phy '))
# Aver = (geo + alg + phy) / 3
# if Aver < 4:
#     print('Вам действительно нужно работать больше')
# if 4 <= Aver <= 6:
#     print('Тебе нужно больше работать')
# if Aver >= 7:
#     print('Хорошая работа!')




# geo = int(input('Geo = '))
# alg = int(input('Alg = '))
# phy = int(input('Phy = '))

# print('Average =', int(geo + alg + phy) / 3)



# width = int(input('width = '))
# height = int(input('height = '))
# total_area = width * height
# print(total_area)


# cost_lt = int(input('Enter the cost: '))
# percent = int(input('Enter the percent: '))
# total_cost = cost_lt * (percent / 100) + cost_lt
# print('Total cost LT =', total_cost)




people = input('Являетесь ли вы участником? Y or N: ')
if people != 'Y' or people != 'N':
    print('неверное значение')
else:
    total_hours = int(input('Кол-во часов: '))
    if people == 'Y': 
        total_cost = (2 * total_hours) * 1.1
        print('Пользователь-участник пробыл', total_hours, 'часа за 2$/час плюс 10%, общая сумма составляет', total_cost)
    elif people == 'N':
        total_cost = (5 * total_hours) * 1.2
        print('Пользователь-посетитель пробыл', total_hours, 'часа за 5$/час плюс 20%, общая сумма составляет', total_cost)







