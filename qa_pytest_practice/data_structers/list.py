
#Копирование по ссылке
list_1 = [1,2,3]
list_2 = list_1
list_2.extend(["+", "alex"])
print(list_1)

#Правильное копирование последдовательности списка
list_3 = list_1.copy()
print(list_3)