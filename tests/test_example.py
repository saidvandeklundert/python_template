from example import Human
from example import Beast


def test_something():
    assert True


def test_human():

    said = Human("Said")
    assert said.say_something() == "I made a template repo"


def test_beast():
    beast = Beast("Leviathan")
    assert beast.say_something() == "I am a beast"
