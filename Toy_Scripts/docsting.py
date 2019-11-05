def test(house):
    """
    To test this docstring run the command 'python -m doctest -v ./docstring.py'
    this is my doc test

    >>> test("stark")
    'good choice'

    >>> test('lanister')
    'aww... sorry'
    """
    if (house == "stark"):
        return('good choice')
    else:
        return('aww... sorry')


class Parent():
    """this is my parent """
    def ___init___(self):
        pass

class Child(parent):
    def ___init___(self):
        pass
