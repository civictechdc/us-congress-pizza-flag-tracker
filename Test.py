# from AuthController
from importlib import reload

import os
os.environ["DATABASE_URL"] = ""
os.environ["FRONTEND_URI"] = ""
os.environ["SECRET_KEY"] = ""
