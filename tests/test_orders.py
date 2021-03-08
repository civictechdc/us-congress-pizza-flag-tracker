import pytest
from OrderTransactions import OrderTransactions 
from models import OrderModel
class TestOrderTransactions():
    def test_create(self):
        # TODO: Make a random id number
        success = OrderTransactions.create( "MD",  567238, "MD06")
        assert(success)
        orderTransaction = OrderTransactions.getorder(567238)
        assert(orderTransaction)
