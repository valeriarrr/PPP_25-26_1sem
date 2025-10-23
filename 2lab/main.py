#5 Соотношение букв по частоте
line = input()  # Вводим строку
if line == ' ' or line == '':  # Проверяем ввод 
    print('Введите непустую строку!')
else:
    line = list(filter(str.isalpha, line.lower()))  # Преобразуем строку в список с символами, убираем из него небуквенные выражения, все символы являются строчными буквами

    score_of_line = dict()
    for j in line:
        score_line = line.count(j)  # Подсчитываем сколько и какие символы повторяются в списке
        score_of_line.update({j: score_line})  # Создаем словарь, состоящий из символов и их повторений

    matching_keys = {}  # Создадим словарь с ключами, состоящих из значений, и значениями, состоящих из букв с одинаковым повтором
       
    for key, value in score_of_line.items():
        if value in matching_keys:  # Если значение ключа в словаре score_of_symbol совпадает с значением другого ключа, то это значение добавляется в список 
            matching_keys[value].append(key)
        else:  # В другом случае значение, которого нет в словаре становится в нем ключом
            matching_keys[value] = [key]
            
    for value_2, keys_2 in matching_keys.items():  # Выводим ключи с одинаковыми значениями
        if len(keys_2) > 1:  # Если значение встречается более чем у одного ключа
            for i in range(len(keys_2) - 1):
                for j in range(i + 1, len(keys_2)):
                    print(f"{keys_2[i]}={keys_2[j]}")
