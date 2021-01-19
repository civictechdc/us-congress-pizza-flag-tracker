from config import app
from controllers import *

# add routes below
app.add_url_rule('/', view_func=index)