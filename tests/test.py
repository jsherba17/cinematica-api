def func(x, y):
    return x * y


def test_answer():
    assert func(3, 5) == 15

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert  "hello" in x

class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        self.value = 2
        assert self.value != 1