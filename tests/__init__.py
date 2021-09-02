from dotenv import load_dotenv
import os

load_dotenv()

database_url=os.environ["DATABASE_URL"]
sqlite_string = "sqlite:///"
if sqlite_string in database_url:
    start_pos = len(sqlite_string)
    file_name: str = database_url[start_pos:]
    if not os.path.exists(file_name):
       raise Exception("Error:"+file_name+" does not exist")


