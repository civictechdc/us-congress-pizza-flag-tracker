import pytest
from flag.orders import Orders 

class TestBasic():
    def test_basic(self):
        assert 1 == 1

class TestOrders():
    def test_create(self):
        x = Orders.create(self)
