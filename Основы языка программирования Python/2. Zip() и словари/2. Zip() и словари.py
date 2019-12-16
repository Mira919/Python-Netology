# 1. Надо отсортировать имена по алфавиту и познакомить людей с одинаковыми индексами после сортировки.
# Если кол-во людей в списках будет не совпадать, то выведем пользователю предупреждение, что кто-то может остаться без пары!

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys = sorted(boys)
girls = sorted(girls)

boys_girls = zip(boys, girls)
boys_girls = list(boys_girls)

if len(boys) != len(girls):
  print('Кто - то может остаться без пары!')
else:
  for couple in boys_girls:
    print(couple[0],' и ', couple[1])

# Идеальные пары:
# Alex и Emma
# Arthur и Kate
# John и Kira
# Peter и Liza
# Richard и Trisha

# 2. Необходимо вывести пользователю список покупок необходимого количества ингредиентов для приготовления блюд на определенное число персон.

person = 5
cook_book = [
  ['салат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ]
]
for dish in cook_book:
    print(dish[0]+':')
    for ingredient_all in dish[1]:
        print(ingredient_all[0] + ',' , str(person * ingredient_all[1]) + ingredient_all[2])
    print('')

# Салат:
# картофель, 500гр.
# морковь, 250гр.
# огурцы, 250гр.
# горошек, 150гр.
# майонез, 350мл.

# Пицца:
# сыр, 250гр.
# томаты, 250гр.
# тесто, 500гр.
# бекон, 150гр.
# колбаса, 150гр.
# грибы, 100гр.

# Фруктовый десерт:
# хурма, 300гр.
# киви, 300гр.
# творог, 300гр.
# сахар, 50гр.
# мед, 250мл.
