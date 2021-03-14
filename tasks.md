## To Do nearterm:
- [ ] rename state to status
- [ ] review create test and code
- [ ] refactor options
  - check code coverage
  - comment out any untested code
  - look at naming
  - use named parameters instead of positional
- [ ] adding an order: 
  - [x] test the model
    - When create an order with required attributes, auto generates an id
  - [] (just write the) controller & router : confirm a route calls the correct controller
  - [ ] Manually build React UI for creating an order
    - define API_ROOT env variable to coordinate the backend and frontend.
    - add the javascript files and setup root element for React
- [ ] Getting the QR code:
  - Create test that `Util.getQRCode('any_string')` returns PNG for the qr code from `?root_url:/show/any_string` route (we can build on early Feb experiment)
  - Create test for OrderTransactions: when you add a order there is a QR code attribute on the order.
  - Create a test that `OrderTransactions.getOrderByID(ordernumber).qrCode` returns the PNG of the QR code including the order's corresponding UUID.
  - Manually build and test UI for specifying an order number and displaying the qr code so that you can print it.
- [ ] getting list of orders
  - create test for OrderTransactions.getAll()
  - create controller and router
  - create UI to list orders, all attributes except QR code
  - when click on an order, see the QR code 
- create status codes and descriptions + getAllStatusCodes()
  - model actions (create, read, update, delete)
    - test when create several statusses (StatusCodeActions.create), then StatusCodeActions.getAll() returns those statusses
    - test when create several statusses, then StatusCodes.getDescription(statusCode) returns the description
  - controller and router for creating and getting statusses
  - UI for listing and creatng statusses
- update status
  - create test for OrderTransactions.updateStatus(order_number, status)
  - create controller and router
  - review UI for scanning and updating status
  - consider status being a drop down - only a few, scanning two codes is cumbersome
  - UI: 
    - when call get ??root_url:/show/<order.id> you see a drop down for statusses and order id is displayed
    - when submit, update status
### Later / authorization tests
- tests for admin authorization
- tests for update status authorization
- tests and UI for creating and getting all attributes for an order
- tests and UI for creating with invalid attributes
- tests and UI for updating order
- tests filtering order by multiple parameters
- tests create order with invalid US state
  

### Tests That Are Done:

### Low Priority Tasks
- consider passing an object rather than positional for create