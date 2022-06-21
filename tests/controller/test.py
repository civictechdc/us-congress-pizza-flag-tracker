def test_get_orders_by_multiple_status_code(self):
    statuses = StatusActions.get_sorted_statuses()
    status_to_query = statuses[1].status_code + \
        ", " + statuses[2].status_code
    unique_order_number = random.randint(1, 1000000)
    usa_state = "MD"
    home_office_code = "MD-06"

    order = OrderActions.create(
        usa_state=usa_state, order_number=unique_order_number, home_office_code=home_office_code)
    order = OrderActions.update_order_by_uuid(
        order.uuid, order_status_id=statuses[1].id)

    order = OrderActions.create(
        usa_state=usa_state, order_number=unique_order_number, home_office_code=home_office_code)
    order = OrderActions.update_order_by_uuid(
        order.uuid, order_status_id=statuses[2].id)

    unique_order_number2 = random.randint(1, 1000000)
    order = OrderActions.create(
        usa_state="CA", order_number=unique_order_number2, home_office_code="CA-03")
    query_params = OrderQueryParams()
    query_params.statuses = status_to_query
    found_orders = OrderActions.get_orders(query_params)

    assert len(found_orders) > 0
    count_status1 = 0
    count_status2 = 0
    count_wrong_status = 0

    for order in found_orders:
        if statuses[1].id == order.order_status_id:
            count_status1 += 1
        elif statuses[2].id == order.order_status_id:
            count_status2 += 1
        else:
            count_wrong_status += 1

    assert count_status1 > 0 and count_status2 > 0 and count_wrong_status == 0
    #assert order.order_status_id == statuses[1].id
