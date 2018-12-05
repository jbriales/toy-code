# coding=utf-8


class Foo:
    def __init__(self, *kwargs):
        # List of fields
        # This automates, but does not provide autocompletion
        for attr in ['title']:
            setattr(self, attr, 'abc')
        # self.title = None


# Try autocompletion in Pycharm
foo = Foo()
foo.title