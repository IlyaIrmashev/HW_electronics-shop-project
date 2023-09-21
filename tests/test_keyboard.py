import pytest
from src.keyboard import Keyboard


def test_init():
    keyboard1 = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(keyboard1) == "Dark Project KD87A"
    assert str(keyboard1.language) == "EN"



def test_change_lang():
    keyboard1 = Keyboard('Dark Project KD87A', 9600, 5)
    keyboard1.change_lang()
    assert str(keyboard1.language) == "RU"
    keyboard1.change_lang().change_lang()
    assert str(keyboard1.language) == "RU"
    with pytest.raises(AttributeError):
        keyboard1.language = "CH"
