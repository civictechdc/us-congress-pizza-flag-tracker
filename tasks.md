To Do:
- discuss: rename state to status?
- review create test and code
- check code coverage
- remove any untested code
- test adding an order: 
  - model
    - When create an order with required attributes, then it gets saved to the database and auto generates an id
  - controller
    - when call controller with required attributes the posted values get sent to create order
  - router: confirm a route calls the correct controller
  - Manually build and test UI for creating an order
- test getting qr code 
  - Util.getQRCode(order_number) returns qr code in format root_url:/update/<order.id>
  - model: verify model includes qrCode
    - when call controller with required attributes the posted values get sent to create order
    - router: confirm route calls the correc controller
  - Manually build and test UI for viewing a specific order and seeing the qr code and scanning the qr code
- create status codes and descriptions and get all
  - model
    - when create an order with required attributes, then StatusCodes.getDescription(statusCode) returns the description
  - controller
  - route for creating and getting
  - UI: when call get root_url:/update/<order.id> you see a drop down for statusses and order id is displayed 
- update status
  - OrderTransactions.updateStatus (orderNumber, statusCode) updates status code of specified order number
  - controller: when update status of specified order with a specific status code, the order is updated with the order id of that status code.  Order id can be passed in URL, status code will be posted
  - route: confirm root_url:/update/<order.id> passes the order id and posted parameters to the controller
  - UI: after selecting status, user can click Submit and it will do a post to update the status
- test and UI for creating and getting all attributes for an order
- test and UI for creating with invalid attributes
- test and UI for updating order
- test filtering order by multiple parameters
- test create order with invalid state
  
  
  

Done: