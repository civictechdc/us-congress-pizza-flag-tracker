import pytest
import random
from OrderTransactions import OrderTransactions 
from models import OrderModel

class TestOrderTransactions():
    def test_create(self):
        # TODO: Make a random id number
        unique_order_number = random.randint(1,1000000)
        success = OrderTransactions.create( "MD",  unique_order_number , "MD06")
        assert(success)
        orderTransaction = OrderTransactions.getorder(unique_order_number)
        assert(orderTransaction)


    def test_unique_uuid(self):
        unique_order_number1 = random.randint(1,1000000)
        unique_order_number2 = random.randint(1,1000000)
        OrderTransactions.create("MD", unique_order_number1, "MD06")
        order1 = OrderTransactions.getorder(unique_order_number1)
        OrderTransactions.create("MA", unique_order_number2, "MA08")
        order2 = OrderTransactions.getorder(unique_order_number2)
        # db.ForeignKey('order_number.uuid')

        assert(order1.uuid != order2.uuid)
       

    