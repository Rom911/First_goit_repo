my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict["name"])  # Виведе 'Alice'

my_dict["age"] = 26  # Змінює вік на 26
my_dict["email"] = "alice@example.com"  # Додає нову пару ключ-значення
print(my_dict)

del my_dict["age"] # удаление пары ключ значение
print(my_dict)

print("name" in my_dict) # проверка есть ли ключ
print("age" in my_dict)
