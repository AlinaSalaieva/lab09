elements = {
    ("H",): "Водень",
    ("He",): "Гелій",
    ("Li",): "Літій",
    ("Be",): "Берилій",
    ("B",): "Бор",
    ("C",): "Вуглець",
    ("N",): "Азот",
    ("O",): "Кисень",
    ("F",): "Фтор",
    ("Ne",): "Неон"
}

while True:
    symbol = input("Введіть символ елемента (або 'stop' для завершення): ")
    if symbol == "stop":
        break
    name = input(f"Введіть назву елемента для символу {symbol}: ")
    elements[(symbol,)] = name

sorted_elements = dict(sorted(elements.items(), key=lambda item: item[1]))

print("\nСловник елементів в алфавітному порядку:")
for symbol, name in sorted_elements.items():
    print(f"{symbol[0]}: {name}")
