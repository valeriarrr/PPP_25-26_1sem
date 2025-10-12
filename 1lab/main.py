#1.Анализ текста (частота сов и букв)
import copy, re
stroka = input()  # Вводим длинную строку
 
if stroka == ' ' or stroka == '':
    print('Ваедите непустую строку!')
else:
    words = re.sub('[.|?|,|!|@|#|$|%|^|&|*|(|)|-|_|+|=|/|>|<|;|:|~|`|"|№|{|}|[|]||1|2|3|4|5|6|7|8|9|0]', '', str(stroka.lower())).split()  # Преобразуем строку в список со словами, убираем из него небуквеные выражения, все слова начинаются со строчной буквы
    symbol = list(filter(str.isalpha, stroka.lower()))  # Преобразуем строку в список с символами, убираем из него небуквеные выражения, все символы являются строчными буквами
    
    copy_words = list(set(copy.deepcopy(words)))  # Копируем список со словами для удаления повторяющихся элементов
    copy_symbol = list(set(copy.deepcopy(symbol)))  # Копируем список с символами для удаления повторяющихся элементов
    
    count_words = len(copy_words)
    count_symbol = len(copy_symbol)
                    
    if count_words < 5:
        print('Введите строку, которая будет состоять из 5 и более разных слов!')
    else:
        if count_symbol < 5:
            print('Введите строку, в которой будет 5 и более разных символов!')
        else:
            print(f'Массив слов: {words}')  # Выводим массив слов
            print(f'Массив символов: {symbol}')  # Выводим массив символов
 
            print('')
 
            score_of_words = dict()
            for i in set(words):
                score_words = words.count(i)  # Подсчитываем сколько и какие слова повторяются в списке
                score_of_words.update({i : score_words})  # Создаем словарь, состоящий из слов и их повторений
 
            print('Сколько встречаются слова в списке:')
 
            top_words = []
            for key, value in sorted(score_of_words.items(), key = lambda item: item[1], reverse=True):  # Сортируем словарь по убыванию количества повторений слов в строке
                print(f'{key} : {value}')
                top_words.append(f'{key}')  # Добавляем в список слова и их повторения
    
            score_of_symbol = dict() 
            for j in set(symbol): 
                score_symbol = symbol.count(j)  # Подсчитываем сколько и какие символы повторяются в списке
                score_of_symbol.update({j : score_symbol})  # Создаем словарь, состоящий из символов и их повторений
 
            print('')
 
            print('Сколко встречаются символы в списке:')
 
            top_symbol = []
            for key, value in sorted(score_of_symbol.items(), key = lambda item: item[1], reverse=True):  # Сортируем словарь по убыванию количества повторений символов в строке
                print(f'{key} : {value}') 
                top_symbol.append(f'{key}')  # Добавляем в список символы и их повторения
 
            print('')
 
            top_words = top_words[:5]  # Оставляем в списке топ 5 самых популярных слов
            print(f'Топ 5 самых популярных слов: {top_words}') 
 
            top_symbol = top_symbol[:5]
            print(f'Топ 5 самых популярных символов: {top_symbol}')  # Оставляем в списке топ 5 самых популярных символов
