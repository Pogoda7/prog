import tkinter as tk
from tkinter import *
from tkinter import ttk


# Создание графического интерфейса
window = tk.Tk()

window.title("Калькулятор для магазина")
window.geometry("600x650+450+100")
window.iconbitmap(default="icon.ico")
window.configure(bg="#F3E8DC")
window.update_idletasks()
window.resizable(False, False) # Выключает растяжку окна по вертикали и горизонтали
#window.attributes("-toolwindow", True) # Выключает верхний хаб, оставляя закрытие и title
window.attributes("-alpha", 0.9) # Делает прозрачность окна


# Словарь с категориями и их ценами
categories = {
    "-": {"-": 0, "S": 0, "M": 0, "L": 0},
    'Футболка': {'-': 0, 'S': 500, 'M': 550, 'L': 600},
    'Шорты': {'-': 0, 'S': 400, 'M': 450, 'L': 500},
    'Джинсы': {'-': 0, 'S': 800, 'M': 850, 'L': 900},
    'Платье': {'-': 0, 'S': 700, 'M': 750, 'L': 800},
    'Рубашка': {'-': 0, 'S': 600, 'M': 650, 'L': 700},
    'Кофта': {'-': 0, 'S': 550, 'M': 600, 'L': 650},
    'Юбка': {'-': 0, 'S': 600, 'M': 650, 'L': 700},
    'Брюки': {'-': 0, 'S': 700, 'M': 750, 'L': 800},
    'Куртка': {'-': 0, 'S': 1000, 'M': 1050, 'L': 1100},
    'Свитер': {'-': 0, 'S': 550, 'M': 600, 'L': 650},
    'Пальто': {'-': 0, 'S': 1200, 'M': 1250, 'L': 1300},
    'Жакет': {'-': 0, 'S': 800, 'M': 850, 'L': 900},
    'Водолазка': {'-': 0, 'S': 500, 'M': 550, 'L': 600},
    'Блузка': {'-': 0, 'S': 450, 'M': 500, 'L': 550},
    'Толстовка': {'-': 0, 'S': 600,'M': 650,'L': 700},
    'Пиджак': {'-': 0, 'S': 900, 'M': 950, 'L': 1000},
    'Жилет': {'-': 0, 'S': 400, 'M': 450, 'L': 500},
    'Костюм': {'-': 0, 'S': 1500, 'M': 1550, 'L': 1600},
    'Блейзер': {'-': 0, 'S': 800, 'M': 850, 'L': 900},
    'Сарафан': {'-': 0, 'S': 600, 'M': 650, 'L': 700}
}

# Словарь с городами доставки и стоимостью доставки
delivery_cities = {
    '-': 0,
    'Без доставки': 0,
    'Москва': 500,
    'Санкт-Петербург': 700,
    'Новосибирск': 1000,
    'Екатеринбург': 900,
    'Казань': 800,
    'Нижний Новгород': 750,
    'Челябинск': 950,
    'Омск': 1100,
    'Самара': 850,
    'Ростов-на-Дону': 950,
    'Уфа': 800,
    'Красноярск': 1050,
    'Пермь': 900,
    'Воронеж': 750,
    'Волгоград': 900,
    'Краснодар': 950,
    'Саратов': 800,
    'Тюмень': 1000,
    'Тольятти': 850,
    'Ижевск': 900,
    'Барнаул': 1100,
    'Ульяновск': 750,
    'Иркутск': 1050,
    'Хабаровск': 950,
    'Ярославль': 800,
    'Владивосток': 1000,
    'Махачкала': 900,
    'Оренбург': 750,
    'Новокузнецк': 950,
    'Кемерово': 1100,
    'Рязань': 850,
    'Томск': 800,
    'Астрахань': 1050,
    'Пенза': 900,
    'Набережные Челны': 750,
    'Липецк': 950,
    'Тула': 1000,
    'Киров': 850,
    'Чебоксары': 800,
    'Калининград': 1050
}

def calculate_price():
    # Получение выбранной категории, размера и города доставки
    selected_category = category_var.get()
    selected_size = size_var.get()
    selected_delivery_city = delivery_city_var.get()

    # Получение цены товара из словаря
    price = categories[selected_category][selected_size]

    # Получение стоимости доставки из словаря
    delivery_cost = delivery_cities[selected_delivery_city]

    # Вычисление общей стоимости
    total_price = price + delivery_cost

    # Вывод цены на экран
    price_label.config(text=f"Цена: {total_price} рублей")

# Создание выпадающего списка для выбора категории
category_label = tk.Label(window, text="Выберите категорию:", font='Times 20', bg="#CBBEB5", fg="black")
category_label.pack(fill=X, padx=[160, 160], pady=10)

category_var = tk.StringVar(window)
category_var.set(list(categories.keys())[0])

category_dropdown = ttk.OptionMenu(window, category_var, *categories.keys())
category_dropdown.pack(fill=X, padx=[180, 180], pady=5)

# Создание выпадающего списка для выбора размера
size_label = tk.Label(window, text="Выберите размер:", font='Times 20', bg="#CBBEB5", fg="black")
size_label.pack(fill=X, padx=[160, 160], pady=20)

size_var = tk.StringVar(window)
size_var.set("S")

size_dropdown = ttk.OptionMenu(window, size_var, *categories[list(categories.keys())[0]].keys())
size_dropdown.pack(fill=X, padx=[180, 180], pady=5)

# Создание выпадающего списка для выбора города доставки
delivery_city_label = tk.Label(window, text="Выберите город доставки:", font='Times 20', bg="#CBBEB5", fg="black")
delivery_city_label.pack(fill=X, padx=[130, 130], pady=20)

delivery_city_var = tk.StringVar(window)
delivery_city_var.set(list(delivery_cities.keys())[0])

delivery_city_dropdown = ttk.OptionMenu(window, delivery_city_var, *delivery_cities.keys())
delivery_city_dropdown.pack(fill=X, padx=[180, 180], pady=5)

# Создание кнопки для расчета цены
calculate_button = ttk.Button(window, text="Рассчитать", command=calculate_price)
calculate_button.pack(fill=X, padx=[180, 180], pady=20)

# Создание метки для вывода цены
price_label = tk.Label(window, text="Цена: ", font='Times 20', bg="#CBBEB5", fg="black")
price_label.pack(fill=X, padx=[180, 180], pady=1)

window.mainloop()