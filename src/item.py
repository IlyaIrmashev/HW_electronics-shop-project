import csv


class InstantiateCSVError(Exception):
    def __int__(self, message):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        """Отображает информацию об объекте класса в режиме отладки"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Отображает информацию об объекте класса для пользователей"""
        return f"{self.__name}"

    def __add__(self, other):
        """
        Складывает экземпляры класса `Phone` и `Item` (сложение по количеству товара в магазине)
        Проверяет, чтобы нельзя было сложить `Phone` или `Item` с экземплярами не `Phone` или `Item` классов.
        """
        if not issubclass(other.__class__, self.__class__):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path):
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv
        """
        Item.all = []
        try:
            with open(path, 'r', encoding="windows-1251") as csv_file:
                csv_data: csv.DictReader = csv.DictReader(csv_file)
                for line in csv_data:
                    if len(line['name']) == 0 or int(line['price']) < 1 or int(line['quantity']) < 0:
                        raise InstantiateCSVError("Файл item.csv поврежден")
                    cls(line['name'], float(line['price']), int(line['quantity']))
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")



    @staticmethod
    def string_to_number(number):
        """
        Возвращает число из числа-строки
        """
        try:
            return int(float(number))
        except ValueError:
            raise ValueError('Эта строка не содержит число.')

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_new):
        if len(name_new) > 10:
            self.__name = name_new[:10]
        else:
            self.__name = name_new
