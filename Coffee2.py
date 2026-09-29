orders = []
menu = {
    "американо": 150,
    "капучино": 220,
    "латте": 240,
    "раф": 280,
    "чай зелёный": 120
}
while True:
    name = str(input("введите название напитка: "))
    name = name.lower()
    if name == "готово":
        break
    if name not in menu:
        print("Такого напитка нет в меню")
    else:
        count = int(input("Введите количество стаканов: "))
        if count < 0:
            print("Количество должно быть положительным числом")
price = menu[name]
total = price * count
order = {
    "drink": name.title(),
    "count": count,
    "price": price,
    "total": total
}
orders.append(order)
