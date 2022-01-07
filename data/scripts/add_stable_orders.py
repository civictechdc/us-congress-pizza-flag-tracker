import uuid
import random

fakeUUIDs = [
    "268bf202-5da5-44be-9709-017a0833c661",
    "652f6df6-a320-4316-a758-103e10421866",
    "605f5f4c-5110-418a-9b1a-1213ebe2c4ea",
    "961feb08-9ea7-4bab-9e18-bd28153e34c1",
    "7c99905f-2465-4af8-93ef-3f8f7c9037e9",
    "940ce5a5-5104-489b-8dbe-ae1e5489aee6",
    "9aecc08b-da42-443e-a6ff-afb03e199d38",
    "75c54e18-d516-4162-b065-3159f5ac8337",
    "efe605ad-6429-4e02-8501-35156186fca3",
    "adede23c-e1b1-4c1f-b76b-94eef91d4331",
]


def add_stable_orders(office_codes_list, db):

    print("Adding sample orders (stable)");

    from src.order.order_model import OrderModel

    for x in range(10):
        order_number = x + 1

        # To come back to this. Desired behavior is to create randomized orders if the app is being tested, but non-randomized orders if the app is being developed.
        #     theUuid = str(uuid.uuid4())
        #     usa_state_object = random.choice(office_codes_list)
        #     usa_state = usa_state_object.get("usa_state")
        #     order_status = random.randint(1, 10)
        #     home_office_code = random.choice(usa_state_object.get("office_code"))

        theUuid = fakeUUIDs[x]
        usa_state_object = office_codes_list[x + x + 2]
        usa_state = usa_state_object.get("usa_state")

        if x > 0 and x <= 9:
            order_status_id = x
        else:
            order_status_id = 1
        home_office_code = usa_state_object.get("office_code")[0]

        order_ = OrderModel(
            theUuid, usa_state, order_number, home_office_code, order_status_id
        )
        db.session.add(order_)
    
    db.session.commit()