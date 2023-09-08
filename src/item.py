import csv


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
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

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
        with open(path, 'r', encoding="windows-1251") as csv_file:
            csv_data: csv.DictReader = csv.DictReader(csv_file)
            for line in csv_data:
                cls(line['name'], float(line['price']), int(line['quantity']))

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
