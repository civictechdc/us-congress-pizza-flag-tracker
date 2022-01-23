import json
import sys
from dotenv import load_dotenv
load_dotenv()


from config import db
from src.user.user_model import UserModel
from data.scripts.add_offices import add_offices
from data.scripts.add_stable_orders import add_stable_orders
from data.scripts.add_statuses import add_statuses
from data.scripts.add_users import add_fed_users, add_state_office_users



users = db.session.query(UserModel).all()
users_exist = users and len(users) > 0
if users_exist:
    print("Seed data has already been populated.")
    sys.exit()
with open(
        "data/office_codes.json",
) as office_codes_json:
    office_codes_list = json.load(office_codes_json)

with open("data/users.json") as users_json:
    users_list = json.load(users_json)

with open("data/statuses.json") as statuses_json:
    statuses_list: object = json.load(statuses_json)

add_offices(office_codes_list=office_codes_list, db=db)
add_state_office_users(office_codes_list, db)
add_fed_users(users_list, db)
add_statuses(statuses_list, db)
add_stable_orders(office_codes_list, db)