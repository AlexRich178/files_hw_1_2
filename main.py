RECIPES = 'recipes.txt'


def making_cook_book():
    with open(RECIPES, 'r', encoding='utf-8') as f:
        cook_book = {}
        lines = f.readlines()
        for index, line in enumerate(lines):
            # логика для первого блюда
            if index == 0:  # отправная точка первая строка
                amount_ingredients = int(lines[index + 1])  # определяем кол-во ингридиентов (строк)
                start_ingredients = index + 2  # начало строк с ингридиентами
                stop_ingredients = index + 2 + amount_ingredients  # конец строк с ингридиентами
                temp_list = []  # временный список
                for ingredients in range(start_ingredients, stop_ingredients):
                    split_line = lines[index + ingredients].strip().split(
                        ' | ')  # разбиваем строку на отдельные элементы
                    temp_list.append(
                        dict(zip(['ingredient_name', 'quantity', 'measure'], split_line)))  # заполняем временный список
                cook_book[lines[index].strip()] = temp_list  # добавляем получившуюся конструкцию в конечный словарь
            # логика для последующих блюд аналогична первому, только за отправную точку берем пустые строки между блюдами
            elif line == '\n':
                amount_ingredients = int(lines[index + 2])
                start_ingredients = index + 3
                stop_ingredients = index + 3 + amount_ingredients
                temp_list = []
                for ingredients in range(start_ingredients, stop_ingredients):
                    split_line = lines[ingredients].strip().split(' | ')
                    temp_list.append(dict(zip(['ingredient_name', 'quantity', 'measure'], split_line)))
                cook_book[lines[index + 1].strip()] = temp_list

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = making_cook_book()
    shopping_list = {}
    for dish in set(dishes):
        if dish in cook_book.keys():
            for i in cook_book[dish]:
                ingredient_name = i['ingredient_name']
                tmp_dict = dict(zip(['measure', 'quantity'], [i['measure'], int(i['quantity']) * person_count]))
                if ingredient_name in shopping_list:
                    shopping_list[ingredient_name]['quantity'] += tmp_dict['quantity']
                else:
                    shopping_list[ingredient_name] = tmp_dict

    print(shopping_list)


get_shop_list_by_dishes(['Фахитос', 'Омлет'], person_count=2)
