## To Do nearterm:
- discuss: rename state to status?
- review create test and code
- refactor
  - move getOrder and any other order transaction code to OrderTransactions
  - check code coverage
  - comment out any untested code
  - look at naming
  - use named parameters instead of positional
- test adding an order: 
  - model
    - When create an order with required attributes, then it gets saved to the database and auto generates an id
  - controller
  - router: confirm a route calls the correct controller
  - Manually build and test UI for creating an order
- test getting qr code 
  - Util.getQRCode(get_secure_id(order_number)) returns qr code in format root_url:/update/<order.id>
  - Test when you add a order there is a QR code attribute on the order.
  - Change model
  - change controller
  - change router
  - Manually build and test UI for viewing a specific order and seeing the qr code and scanning the qr code
- create status codes and descriptions + getAllStatusCodes()
  - model actions (create, read, update, delete)
    - test wen create several statusses (StatusCodeActions.create), then StatusCodeActions.getAll() returns those statusses
    - test when create several statusses, then StatusCodes.getDescription(statusCode) returns the description
  - controller f
  - route for creating and getting 
  - UI: when call get root_url:/update/<order.id> you see a drop down for statusses and order id is displayed 

### Later / authorization tests
- update status
  - test OrderActions.updateStatus (orderNumber, statusCode) updates status code of specified order number
  - controller
  - route: confirm root_url:/update/<order.id> passes the order id and posted parameters to the controller
  - UI: (scanning code) after selecting status, user can click Submit and it will do a post to update the status
- test and UI for creating and getting all attributes for an order
- test and UI for creating with invalid attributes
- test and UI for updating order
- test filtering order by multiple parameters
- test create order with invalid state
  

### Tests That Are Done:
