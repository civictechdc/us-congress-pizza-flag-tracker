from models import OrderModel

class Orders:
    def create(self, mystate: str, order_number: int, coffice:str ):
        x = OrderModel.new(mystate, 1234, "MD01") 
        #x.state = state
        #Ethan proposal: class calls things in the model,
        #  we call the class rather than the model direclty
        return x