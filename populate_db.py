import json
import sys

from data.scripts.add_office_codes import add_office_codes
from data.scripts.add_users import add_users_for_offices, add_users_from_json
from data.scripts.add_statuses import add_statuses
from data.scripts.add_sample_orders import add_sample_orders
from models import UserModel

# users: [UserModel] = db.session.UserModel.query.all()
#
# if (not users or len(users)==0):
#     sys.exit()

# imports are inside, otherwise we get circular import during testing
with open("./data/office_codes.json") as office_codes_json:
    office_codes_list = json.load(office_codes_json)

with open("./data/users.json") as users_json:
    users_list = json.load(users_json)

with open("./data/statuses.json") as statuses_json:
    statuses_list = json.load(statuses_json)

def populate_db(db):
    add_office_codes(office_codes_list, db)
    add_users_for_offices(office_codes_list, db)
    add_users_from_json(users_list, db)
    add_statuses(statuses_list, db)
    add_sample_orders(office_codes_list, db)

db.session.commit()

