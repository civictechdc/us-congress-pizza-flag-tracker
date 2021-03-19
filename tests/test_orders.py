import pytest
import random
from OrderActions import OrderActions 
from models import OrderModel
from config import *

class TestOrderActions():
    
    def test_create(self):
        unique_order_number = random.randint(1,1000000)
        order = OrderActions.create( "MD",  unique_order_number , "MD06")
        retrievedOrder = OrderActions.get_order_by_order_number(unique_order_number)
        assert(retrievedOrder.order_number == unique_order_number)
        # assert(retrievedOrder.status_id == 1)

    def test_unique_uuid(self):
        unique_order_number1 = random.randint(1,1000000)
        unique_order_number2 = random.randint(1,1000000)
        OrderActions.create("MD", unique_order_number1, "MD06")
        order1 = OrderActions.get_order_by_order_number(unique_order_number1)
        OrderActions.create("MA", unique_order_number2, "MA08")
        order2 = OrderActions.get_order_by_order_number(unique_order_number2)
        assert(order1.uuid != order2.uuid)
       