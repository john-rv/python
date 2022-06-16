# список
# упорядоченная последовательность
# получить элемент можно по индексу
# обновить элемент можно по индексу
auto_list = [
    ["A6", ["год выпуска", [2013]],
     ["объем двигателя", [2.0]],
     ["мощность л.с", [180]],
     ["привод", ["передний"]]
     ],
    ["A7", ["год выпуска", [2014]],
     ["объем двигателя", [2.0]],
     ["мощность л.с", [245]],
     ["привод", ["передний"]]
     ]

]

print(auto_list[0])

# множество
# элементы не упорядочены, при выводе могут выводтся в любом порядке
# элементы без индекса
# элементы можно получить только используя цикл
# проверить есть ли элемент, можно с помощью in
# нельзя изменять элемент, можно только добавить новый или удалить
# выводит долько уникальные значения
auto_set = {
    ("ауди A6", "год выпуска: 2013", "объем двигателя: 2.0", "мощность л.с: 180", "привод: передний"),
    ("ауди A7", "год выпуска: 2014", "объем двигателя: 2.0", "мощность л.с: 245", "привод: передний")
}

print(("ауди A6", "год выпуска: 2013", "объем двигателя: 2.0", "мощность л.с: 180", "привод: передний") in auto_set)

# словарь
# можно получить доступ к элементу по ключу
# можно изменить значение зная его ключ
# исплользуя items можно получить ключ - значение
# добавление элементов выполняется с помощью нового ключа
# проверить наличие ключа можно спомощью in
auto_dict = {
    "ауди A6": {"год выпуска": 2013, "объем двигателя": 2.0, "мощность л.с": 180, "привод": "передний"},
    "ауди A7": {"год выпуска": 2014, "объем двигателя": 2.0, "мощность л.с": 245, "привод": "передний"}
}
print(auto_dict["ауди A6"])

# Если необходимо хранить уникальные значения, то необходимо использовать set,
# если требуется упорядоченная последовательность то - list,
# если необходимо связать значение с ключом то dict
