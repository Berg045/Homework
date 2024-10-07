# создается в фигурных скобках и обязательно должна быть пара - {'ключ':значение}.
from lib2to3.pygram import python_grammar_no_print_statement

phone_book = {'Vlad' : 79765434543, 'Boris': 87468273477}
print(phone_book)

# методы работы со словарями:
# например, чтобы обратиться к определенному элементу ( ключу Boris) делаем как и при работе со списками
print(phone_book['Boris'])

# ключ является неизменным типом, а значение переменным, те его можно менять, например
phone_book['Vlad'] = 19587349988
print(phone_book)
# видим что произошла замена значения 79765434543 на 19587349988

# если ввести несуществующий ключ, например
phone_book['Alex'] = 23438884400
# и запустим, то увидим что произошло добавление в нашу тлф книгу, а в случае со списками получили
# бы ошибку
print(phone_book)
# для удаления можно воспользоваться функцией del
del phone_book['Boris']
print(phone_book)

# если нужно внести сразу несколько имен используем метод update
phone_book.update({'Nik': 32547771288, 'Boris': 87468273477 })
# и получим
print(phone_book)

# метод get возвращает данные по ключу
print(phone_book.get('Boris'))
# а если обратится к несуществующему ключу, то получим NONE

print(phone_book.get('Anna'))
# и можно указать значение по умолчанию, если такого ключа нет, например 'Такого ключа нет' и получим вместо NONE
print(phone_book.get('Anna','Такого ключа нет'))

# метод pop применяется для того чтобы вытащить пару(ключ:значение) из словаря, например Boris
print(phone_book)
phone_book.pop('Boris')
print(phone_book)

# метод keys используется для вытаскивания всех ключей в словаре
print(phone_book.keys())
# а если применить метод values, то вытащим все значения(номера тлф)
print(phone_book.values())
# а если нужна пара то используем items
print(phone_book.items())


# SET - МНОЖЕСТВА не содержат повторяющихся элементов
set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'String', (1,2,3) }
print(set_)
# для того чтобы перевести во множества например список используем команду SET
list_ = [1, 1, 1, 1, 2, 2, 2, 3, 3, 1, 4, 4,5]
print(set(list_))
# а если хотим заменить сразу весь список на множества, то пишем
list_ = set(list_)
print(list_)

# для того чтобы удалить элемент из множества пользуемся DISCARD ИЛИ REMOVE
# результат будет одинаков, за исключением того что DISCARD не выдает ошибку если элемент отсутствует
print(list_.discard(1))
print(list_.remove(2))
print(list_)
# чтобы добавить элемент используем команду add
print(list_.add(6))
print(list_)