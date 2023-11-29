import mathematics


class TestMathMethods():

    def test_add(self):
        assert 3 == mathematics.add(1, 2)
        assert 10 == mathematics.add(3, 7)

    def test_multiply(self):
        assert 50 == mathematics.multiply(5, 10)

    def test_power(self):
        assert 256 == mathematics.power(2, 8)

