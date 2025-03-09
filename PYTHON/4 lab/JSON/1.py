import json
with open("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/4 lab/JSON/sample-data.json", "r") as f:
    data = json.load(f)
print("Inherit status")
print("="*84)
DN="DN"
Description="Description"
Speed="Speed"
MTU="MTU"
print(f"{DN:50} {Description:20} {Speed:7} {MTU:10}") 
print("-"*84)
for item in data["imdata"]:  #imdata is key which contain list of elements
    attr = item["l1PhysIf"]["attributes"]  #attr == attributes     attributes is dictionary
    dn = attr.get("dn")
    descr = attr.get("descr")
    speed = attr.get("speed")
    mtu = attr.get("mtu")
    print(f"{dn:50} {descr:20} {speed:7} {mtu:10}")       #{variable:width} -->  определяют ширину столбцов при выводе данных















# #     Метод	  |         Описание	       |         Входной аргумент |	       Пример использования       |
# # --------------|----------------------------|--------------------------|-----------------------------------|
# #  json.load(f) | Загружает JSON из файла	   |    Файловый объект	      |       json.load(f)                |
# # json.loads(s) |	Загружает JSON из строки   |       Строка JSON	      | json.loads('{"name": "Alice"}')   |



                                                # отличия между load and dump
#          Метод	  |                            Что делает?	                             |     Аргументы	 |          Пример
# ------------------|----------------------------------------------------------------------|-------------------|--------------------------
# json.load(f)	  |         Читает JSON из файла и превращает его в Python-объект	     |   Файловый объект |  (f)	data = json.load(f)
# json.dump(obj, f) |	Записывает Python-объект в файл в формате JSON	Объект Python (obj), |   файловый объект |  (f)	json.dump(data, f)





















# import json
# with open ("/Usersdiastursynbek/Downloads/KBTU/PP2/PYTHON/4 lab/JSON/sample-data.json", "r") as file:
#     data = json.load(file)


# for item in data["imdata"]:
#     attr= item["l1PhysIf"]["attributes"]
#     dn= attr.get("dn")
#     descr= attr.get("descr")
#     speed= attr.get("speed")
#     mtu= attr.get("mtu")
#     print(f"{dn:50}{descr:3}{speed:7}{mtu}")
    

























#     Этот код на Python выполняет следующие действия:

# 1. Открывает и загружает JSON-файл

# import json
# with open("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/4 lab/JSON/sample-data.json", "r") as f:
#     data = json.load(f)

# 	•	Открывает файл sample-data.json (если путь указан правильно).
# 	•	Загружает содержимое JSON-файла в переменную data как словарь (dict).

# 2. Выводит заголовки

# print("Inherit status")
# print("="*50)
# print("DN")
# print("-"*50)

# 	•	Выводит заголовок “Inherit status”.
# 	•	Рисует разделительные линии.

# 3. Проходит по каждому интерфейсу в JSON

# for item in data["imdata"]:
#     attr = item["l1PhysIf"]["attributes"]

# 	•	data["imdata"] – это список объектов, каждый из которых представляет собой информацию о сетевом интерфейсе.
# 	•	attr = item["l1PhysIf"]["attributes"] – извлекает атрибуты интерфейса.

# 4. Извлекает и форматирует данные

# dn = attr.get("dn")
# descr = attr.get("descr")
# speed = attr.get("speed")
# mtu = attr.get("mtu")
# print(f"{dn:50} {descr:11} {speed:7} {mtu}")

# 	•	dn (Distinguished Name) – путь к интерфейсу в сети.
# 	•	descr (Description) – описание (может быть пустым).
# 	•	speed – скорость интерфейса.
# 	•	mtu – Maximum Transmission Unit (максимальный размер пакета).

# 📌 Форматирование f"{dn:50} {descr:11} {speed:7} {mtu}":
# 	•	dn:50 – ширина 50 символов (для выравнивания).
# 	•	descr:11 – ширина 11 символов.
# 	•	speed:7 – ширина 7 символов.

# 🔹 Что будет в выводе?

# Допустим, в JSON есть такие данные:

# {
#     "imdata": [
#         {
#             "l1PhysIf": {
#                 "attributes": {
#                     "dn": "topology/pod-1/node-201/sys/phys-[eth1/1]",
#                     "descr": "Uplink",
#                     "speed": "10G",
#                     "mtu": "9000"
#                 }
#             }
#         },
#         {
#             "l1PhysIf": {
#                 "attributes": {
#                     "dn": "topology/pod-1/node-201/sys/phys-[eth1/2]",
#                     "descr": "",
#                     "speed": "inherit",
#                     "mtu": "9150"
#                 }
#             }
#         }
#     ]
# }

# 📌 Вывод в терминале:

# Inherit status
# ==================================================
# DN
# --------------------------------------------------
# topology/pod-1/node-201/sys/phys-[eth1/1]       Uplink       10G   9000
# topology/pod-1/node-201/sys/phys-[eth1/2]                   inherit   9150

# 📌 Итог

# Этот код читает JSON-файл с данными о сетевых интерфейсах и выводит информацию о каждом интерфейсе в формате таблицы.

# ✅ Если файл не найден, будет ошибка FileNotFoundError.
# ✅ Если descr пустое, просто оставит пробел.
# ✅ Используется get(), чтобы избежать KeyError, если ключа нет.

# 🔹 Если нужно что-то исправить или добавить (например, фильтрацию интерфейсов), скажите! 🚀