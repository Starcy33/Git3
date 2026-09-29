order = []
menu = {
    "Американо": 150,
    "Капучино": 220,
    "Латте": 240,
    "Раф": 280,
    "Чай зелёный": 120
}
while True:
    name = str(input("введите название напитка: "))
    name = name.lower()
    if name not in menu:
        print("Такого напитка нет в меню")
    elif name.lower() == "готово":
        break
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
