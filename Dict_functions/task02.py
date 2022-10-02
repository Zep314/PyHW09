# Задание:
# Иван решил создать самый большой словарь в мире.
# Для этого он придумал функцию biggest_dict(**kwargs),
# которая принимает неограниченное количество параметров «ключ: значение»
# и обновляет созданный им словарь my_dict, состоящий всего из одного
# элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.

my_dict = {'first_one': 'we can do it'}

def biggest_dict(**kwargs):
    global my_dict
    for (key,value) in kwargs.items():
        my_dict[key]=value

print(my_dict)
biggest_dict(one='1', two='2', three='3', four=4, five=5)
print(my_dict)
