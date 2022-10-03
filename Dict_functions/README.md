# Работа со словарями в Python #

* **task01.py** - Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в 
  котором каждый элемент списка является и ключом и значением. Предполагается, что элементы списка будут 
  соответствовать правилам задания ключей в словарях. 
* **task022.py** - Иван решил создать самый большой словарь в мире. Для этого он придумал функцию 
  _biggest_dict(**kwargs)_, которая принимает неограниченное количество параметров «ключ: значение» и обновляет 
  созданный им словарь my_dict, состоящий всего из одного элемента «first_one» со значением «we can do it». 
  Воссоздайте эту функцию. 
* **task03.py** - Дана строка в виде случайной последовательности чисел от 0 до 9. Требуется создать словарь, который 
  в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве значений – количество 
  этих чисел в имеющейся последовательности. Для построения словаря создайте функцию count_it(sequence), 
  принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.