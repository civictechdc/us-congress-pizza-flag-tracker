
Database Tests
Orders (operations on Orders)
Orders.create (order: Order)
 - Create a new order
Confirm key is created
Orders.getByOrderNum() => Order object
Orders.getAll() => Order[]
 - Get all orders
Orders.getFrst() Order
Orders.update(status, key)
 - updates record corresponding to key
Routes
Mocking? check that function calls
  create (post) => calls Orders.create
  get/id/<id>
  get/all
  get/first 
Update status based on key