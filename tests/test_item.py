"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone


@pytest.fixture()
def test_class():
    return Item("Смартфон", 12000, 2)


def test_calculate_total_price(test_class):
    """
    Тестирует функцию подсчета общей стоимости конкретного товара
    """

    assert test_class.calculate_total_price() == 24000


def test_apply_discount(test_class):
    """
    Тестирует функцию применения скидки на определенный товар
    """
    test_class.apply_discount()
    assert test_class.price == test_class.price * Item.pay_rate


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("")

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("../src/items.csv")


def test_string_to_number():
    assert Item.string_to_number('6') == 6
    assert Item.string_to_number('7.0') == 7
    assert Item.string_to_number('8.7') == 8


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    with pytest.raises(ValueError):
        item1 + 10
