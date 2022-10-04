import json
from src.constituent.constituent_actions import ConstituentActions
from src.constituent.constituent_model import ConstituentModel
from src.status.status_model import StatusModel
from src.status.status_actions import StatusActions
from src.order.order_model import OrderModel
from src.order_log.order_log_actions import LogActions
from config import db
import uuid

from src.util import table_record_to_json, table_to_json


class OrderQueryParams:
    statuses = ""
    usa_state = ""
    office_code = ""
    keyword = ""
    order_number = ""

    def isEmpty(self):
        return not (self.status_code or self.usa_state or self.office_code)


class OrderActions:
    @classmethod
    def create(
        cls,
        usa_state: str,
        order_number: int,
        home_office_code: str,
        order_status_id: int = None,
        order_status: OrderModel = None,
        uuid_param: str = None,
        constituent_id: str = None,
    ):
        if not constituent_id:
            constituent_id = cls.select_mock_constituent()
        theUuid = uuid_param or str(uuid.uuid4())
        new_order = OrderModel(
            theUuid,
            usa_state,
            order_number,
            home_office_code,
            order_status_id,
            order_status,
            constituent_id,
        )
        db.session.add(new_order)
        db.session.commit()
        LogActions.create_order_log(
            theUuid, usa_state, order_number, home_office_code, order_status_id
        )
        return new_order

    @classmethod
    def get_orders(cls, query_params: OrderQueryParams = OrderQueryParams()):
        query = (OrderModel.home_office_code == OrderModel.home_office_code) & (OrderModel.archived == 0)

        if query_params.order_number:
            query = query & (OrderModel.order_number ==
                             query_params.order_number)
        if query_params.office_code:
            query = query & (OrderModel.home_office_code ==
                             query_params.office_code)
        if query_params.usa_state:
            query = query & (OrderModel.usa_state == query_params.usa_state)
        if query_params.statuses:
            status_query = query_params.statuses.split(',')
            statuses = StatusActions.get_sorted_statuses()
            sub_query = OrderModel.home_office_code != OrderModel.home_office_code
            for status in statuses:
                if status.status_code in status_query:
                    sub_query = sub_query | (
                        OrderModel.order_status_id == status.id)

            query = query & sub_query

        orders = OrderModel.query.filter(query)
        order_array = [order for order in orders]
        if query_params.keyword:
            filter_obj = filter(
                lambda order: query_params.keyword.upper()
                in json.dumps(table_record_to_json(order)).upper(),
                order_array,
            )
            order_filtered_array = list(filter_obj)
        else:
            order_filtered_array = order_array
        return order_filtered_array

    @classmethod
    def get_order_by_order_number(cls, order_number):
        order = OrderModel.query.filter(
            OrderModel.order_number == order_number).first()
        return order

    @classmethod
    def get_order_by_uuid(cls, uuid):
        order = OrderModel.query.filter(OrderModel.uuid == uuid).first()
        return order

    # Do we need this classmethod?
    @classmethod
    def get_by_home_office_code(cls, home_office_code):
        return OrderModel.query.filter(
            OrderActions.home_office_code == home_office_code
        )

    @classmethod
    def get_orders_by_usa_state(cls, usa_state):
        return OrderModel.query.filter(OrderActions.usa_state == usa_state)

    @classmethod
    def get_orders_by_order_status_id(cls, order_status_id):
        return OrderModel.query.filter(OrderActions.order_status_id == order_status_id)

    @classmethod
    def select_mock_constituent(cls):
        len_order = OrderModel.query.count()
        constituents = ConstituentActions.get_constituents()
        len_constituent = len(constituents)
        constituent_index = len_order % len_constituent
        constituent_id = constituents[constituent_index].uuid
        return constituent_id

    @classmethod
    def update_order_by_uuid(
        cls,
        uuid,
        usa_state=None,
        order_number=None,
        home_office_code=None,
        order_status_id=None,
        archived=0,
    ):
        order = cls.get_order_by_uuid(uuid)
        order.order_number = order_number or order.order_number
        order.usa_state = usa_state or order.usa_state
        order.home_office_code = home_office_code or order.home_office_code
        order.order_status_id = order_status_id or order.order_status_id
        order.archived = archived
        LogActions.create_order_log(
            order_uuid = uuid,
            usa_state = order.usa_state,
            order_number = order.order_number,
            home_office_code = order.home_office_code,
            order_status_id = order.order_status_id,
            order_archived = 0,
        )
        db.session.commit()
        return order

    @classmethod
    def delete_order_by_uuid(cls, uuid):
        order = cls.get_order_by_uuid(uuid)
        order.archived = 1
        LogActions.create_order_log(
            order_uuid = uuid,
            usa_state = order.usa_state,
            order_number = order.order_number,
            home_office_code = order.home_office_code,
            order_status_id = order.order_status_id,
            order_archived = 1,
        )
        db.session.commit()

    @classmethod
    def commit_status_update(cls):
        db.session.commit()
        return
